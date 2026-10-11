#!/usr/bin/env python3
"""
Bộ công cụ thao tác DOCX chuẩn PTIT (Tích hợp tài nguyên /docx-official):
- LUÔN LUÔN chỉnh sửa trên file có sẵn (nếu chưa có thì sao chép từ assets/template_ptit.docx).
- LUÔN LUÔN tự động sao lưu bản cũ vào thư mục `back-up-docx` trước mỗi lần thay đổi.
- Tái sử dụng trực tiếp các script chuẩn OOXML từ references/docx-official.
"""

import os
import sys
import shutil
from datetime import datetime
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Định vị đường dẫn tương đối động (Phi hardcode)
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_ASSETS_DIR = BASE_DIR / "assets"
DEFAULT_TEMPLATE_PATH = DEFAULT_ASSETS_DIR / "template_ptit.docx"
DOCX_OFFICIAL_SCRIPTS = BASE_DIR / "references" / "docx-official" / "ooxml" / "scripts"

def backup_docx(docx_path: str | Path) -> Path | None:
    """Tự động đưa bản cũ vào thư mục `back-up-docx` trước khi chỉnh sửa."""
    target_file = Path(docx_path).resolve()
    if not target_file.exists():
        return None

    backup_dir = target_file.parent / "back-up-docx"
    backup_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{target_file.stem}_{timestamp}{target_file.suffix}"
    backup_path = backup_dir / backup_filename

    shutil.copy2(target_file, backup_path)
    print(f"[BACKUP] Sao luu ban cu vao: {backup_path.name}")
    return backup_path

def ensure_existing_docx(docx_path: str | Path, template_path: str | Path = None) -> Path:
    """
    Đảm bảo luôn có file DOCX để chỉnh sửa:
    Nếu file chưa tồn tại -> Tự động sao chép từ khung có sẵn `assets/template_ptit.docx`.
    Tuyệt đối không tạo file trắng từ đầu.
    """
    target = Path(docx_path).resolve()
    if not target.exists():
        tpl = Path(template_path or DEFAULT_TEMPLATE_PATH).resolve()
        if not tpl.exists():
            raise FileNotFoundError(f"Khong tim thay khung mau tai: {tpl}")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(tpl, target)
        print(f"[INIT] Khoi tao tu khung co san: {tpl.name} -> {target.name}")
    return target

def replace_in_docx(docx_path: str | Path, replacements: dict, output_path: str | Path = None) -> Path:
    """
    Chỉnh sửa trực tiếp file DOCX:
    1. Sao lưu bản cũ vào `back-up-docx/`
    2. Thay thế văn bản giữ nguyên toàn bộ định dạng, bảng biểu, ảnh bìa hoa văn
    """
    target = ensure_existing_docx(docx_path)
    output = Path(output_path or target).resolve()

    # Luôn sao lưu file hiện tại trước khi ghi đè
    backup_docx(target)

    doc = Document(str(target))

    def _replace_text_in_paragraph(p):
        full_text = "".join(r.text for r in p.runs)
        for old_txt, new_txt in replacements.items():
            if old_txt in full_text:
                full_text = full_text.replace(old_txt, new_txt)
                if p.runs:
                    p.runs[0].text = full_text
                    for r in p.runs[1:]:
                        r.text = ""
                else:
                    p.text = full_text

    for p in doc.paragraphs:
        _replace_text_in_paragraph(p)

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    _replace_text_in_paragraph(p)

    for section in doc.sections:
        for p in section.header.paragraphs:
            _replace_text_in_paragraph(p)
        for p in section.footer.paragraphs:
            _replace_text_in_paragraph(p)

    doc.save(str(output))
    print(f"[OK] Cap nhat thanh cong vao: {output.name}")
    return output

def append_to_existing_docx(docx_path: str | Path, new_content: list, output_path: str | Path = None) -> Path:
    """
    Nối thêm nội dung vào file DOCX có sẵn:
    1. Sao lưu bản cũ vào `back-up-docx/`
    2. Thêm đoạn văn bản/tiêu đề chuẩn font Times New Roman 13pt
    """
    target = ensure_existing_docx(docx_path)
    output = Path(output_path or target).resolve()

    backup_docx(target)

    doc = Document(str(target))

    for item in new_content:
        heading_level = item.get("heading")
        text = item.get("text", "")
        if heading_level:
            p = doc.add_heading(text, level=heading_level)
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(6)
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.color.rgb = RGBColor(0, 0, 0)
        else:
            p = doc.add_paragraph(text)
            p.paragraph_format.first_line_indent = Cm(1.0)
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.line_spacing = 1.3
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(13)
                r.font.color.rgb = RGBColor(0, 0, 0)

    doc.save(str(output))
    print(f"[OK] Noi them noi dung thanh cong vao: {output.name}")
    return output

def unpack_docx(docx_path: str | Path, output_dir: str | Path):
    """Ủy quyền thao tác unpack tới script unpack.py của references/docx-official."""
    unpack_script = DOCX_OFFICIAL_SCRIPTS / "unpack.py"
    if unpack_script.exists():
        sys.path.insert(0, str(DOCX_OFFICIAL_SCRIPTS))
        import unpack
        unpack.extract_archive_safely(docx_path, output_dir)
        unpack.pretty_print_xml(Path(output_dir))
        print(f"[OK] Da unpack bang docx-official unpack.py vao: {output_dir}")
    else:
        raise FileNotFoundError(f"Khong tim thay unpack.py tai: {unpack_script}")

def pack_docx(input_dir: str | Path, output_docx: str | Path) -> Path:
    """Ủy quyền thao tác pack tới script pack.py của references/docx-official (Kèm tự động backup)."""
    out_file = Path(output_docx).resolve()
    if out_file.exists():
        backup_docx(out_file)

    pack_script = DOCX_OFFICIAL_SCRIPTS / "pack.py"
    if pack_script.exists():
        sys.path.insert(0, str(DOCX_OFFICIAL_SCRIPTS))
        import pack
        pack.pack_archive_cleanly(input_dir, out_file)
        print(f"[OK] Da pack bang docx-official pack.py vao: {out_file.name}")
        return out_file
    else:
        raise FileNotFoundError(f"Khong tim thay pack.py tai: {pack_script}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Su dung:")
        print("  python docx_tools.py unpack <file.docx> <output_dir>")
        print("  python docx_tools.py pack <input_dir> <output.docx>")
        sys.exit(1)

    cmd = sys.argv[1].lower()
    if cmd == "unpack":
        unpack_docx(sys.argv[2], sys.argv[3])
    elif cmd == "pack":
        pack_docx(sys.argv[2], sys.argv[3])
