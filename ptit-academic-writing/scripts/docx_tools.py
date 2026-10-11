#!/usr/bin/env python3
"""
Bộ công cụ thao tác DOCX chuẩn PTIT (tích hợp tài nguyên /docx-official).

Nguyên tắc:
- Luôn chỉnh sửa trên file có sẵn. Nếu chưa có thì sao chép từ khung mẫu đúng loại báo cáo.
- Luôn sao lưu bản cũ vào `back-up-docx/` trước khi ghi.
- Thay thế ở cấp run: giữ định dạng của từng run.
- Tiêu đề dùng style Heading 1-3 (để mục lục cập nhật được bằng F9).
- Chèn nội dung đúng vị trí (trước một tiêu đề), không mặc định nối cuối file.

Khung mẫu theo loại báo cáo (assets/):
  btl        -> template_btl.docx        (BTL, 3 chương)
  do-an      -> template_do_an.docx      (đồ án / khóa luận, 4 chương, đủ trang thủ tục)
  tieu-luan  -> template_tieu_luan.docx  (tiểu luận, 3 phần lớn)

Cách dùng (CLI):
  python docx_tools.py init     <kind> <out.docx>
  python docx_tools.py replace  <file.docx> <replacements.json> [--out out.docx]
  python docx_tools.py append   <file.docx> <content.json> [--before "TIÊU ĐỀ"] [--out out.docx]
  python docx_tools.py check    <file.docx>
  python docx_tools.py backup   <file.docx>
  python docx_tools.py unpack   <file.docx> <output_dir>
  python docx_tools.py pack     <input_dir> <output.docx>

Định dạng JSON:
  replacements.json : {"[HỌ VÀ TÊN SINH VIÊN]": "Tạ Hoài Bình", "[NĂM]": "2026"}
  content.json      : [{"heading": 1, "text": "CHƯƠNG 2: ..."}, {"text": "Nội dung đoạn..."}]
"""

import argparse
import json
import shutil
import re
import sys
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS = BASE_DIR / "assets"
TEMPLATES = {
    "btl": ASSETS / "template_btl.docx",
    "do-an": ASSETS / "template_do_an.docx",
    "tieu-luan": ASSETS / "template_tieu_luan.docx",
}
DEFAULT_KIND = "btl"
DOCX_OFFICIAL_SCRIPTS = BASE_DIR / "references" / "docx-official" / "ooxml" / "scripts"
BACKUP_DIR_NAME = "back-up-docx"
FONT_NAME = "Times New Roman"


# ---------------------------------------------------------------------------
# Sao lưu, khởi tạo
# ---------------------------------------------------------------------------

def backup_docx(docx_path):
    """Sao lưu file hiện tại vào back-up-docx/ với dấu thời gian. None nếu file chưa có."""
    target = Path(docx_path).resolve()
    if not target.exists():
        return None

    backup_dir = target.parent / BACKUP_DIR_NAME
    backup_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = backup_dir / f"{target.stem}_{stamp}{target.suffix}"
    n = 2
    while dest.exists():  # tránh ghi đè khi sửa hai lần trong cùng một giây
        dest = backup_dir / f"{target.stem}_{stamp}_{n}{target.suffix}"
        n += 1

    shutil.copy2(target, dest)
    print(f"[BACKUP] {dest}")
    return dest


def template_path_for(kind):
    key = kind or DEFAULT_KIND
    if key not in TEMPLATES:
        raise ValueError(f"Loại báo cáo không hợp lệ: {key}. Chọn: {', '.join(TEMPLATES)}")
    path = TEMPLATES[key]
    if not path.exists():
        raise FileNotFoundError(f"Chưa có khung mẫu: {path}")
    return path


def ensure_existing_docx(docx_path, kind=None):
    """Nếu file đích chưa có thì sao chép từ khung mẫu đúng loại. Không tạo file trắng."""
    target = Path(docx_path).resolve()
    if not target.exists():
        tpl = template_path_for(kind)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(tpl, target)
        print(f"[INIT] Khởi tạo từ khung mẫu {tpl.name} -> {target.name}")
    return target


# ---------------------------------------------------------------------------
# Định dạng dùng chung
# ---------------------------------------------------------------------------

def set_run_format(run, size, bold=False, italic=False):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(0, 0, 0)
    rpr = run._r.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rfonts.set(qn(attr), FONT_NAME)


def fill_paragraph(doc, paragraph, item):
    """
    Điền một đoạn theo quy chuẩn PTIT.
    item: {"heading": 1|2|3, "text": ...} hoặc {"text": ...} (thân bài).
    Heading dùng style Heading N để mục lục nhận diện được.
    """
    text = item.get("text", "")
    level = item.get("heading")
    pf = paragraph.paragraph_format

    if level in (1, 2, 3):
        paragraph.style = doc.styles[f"Heading {level}"]
        pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
        pf.first_line_indent = Cm(0)
        pf.space_before = Pt({1: 12, 2: 8, 3: 3}[level])
        pf.space_after = Pt({1: 6, 2: 4, 3: 3}[level])
        pf.keep_with_next = True
        run = paragraph.add_run(text)
        set_run_format(run, {1: 15, 2: 13.5, 3: 13}[level], bold=True, italic=(level == 3))
    else:
        pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        pf.first_line_indent = Cm(1.0)
        pf.space_before = Pt(6)
        pf.space_after = Pt(6)
        pf.line_spacing = 1.3
        run = paragraph.add_run(text)
        set_run_format(run, 13)


def _iter_all_paragraphs(doc):
    """Đoạn ở thân, bảng lồng nhau, header và footer (bỏ trùng)."""
    def from_table(table):
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    yield p
                for nested in cell.tables:
                    yield from from_table(nested)

    for p in doc.paragraphs:
        yield p
    for table in doc.tables:
        yield from from_table(table)
    for section in doc.sections:
        for part in (section.header, section.footer):
            for p in part.paragraphs:
                yield p
            for table in part.tables:
                yield from from_table(table)


def _replace_in_paragraph(paragraph, replacements):
    """
    Thay chuỗi trong đoạn, kể cả khi chuỗi nằm trên nhiều run.
    Phần đầu của chuỗi cũ nằm ở run nào thì nội dung mới nằm ở run đó.
    Các run khác chỉ bị cắt phần thuộc chuỗi cũ, định dạng riêng không đổi.
    """
    count = 0
    for old, new in replacements.items():
        if not old:
            continue
        start = 0
        while True:
            runs = paragraph.runs
            full = "".join(r.text for r in runs)
            idx = full.find(old, start)
            if idx < 0:
                break
            end = idx + len(old)
            pos = 0
            wrote = False
            for r in runs:
                text = r.text
                rs, re_ = pos, pos + len(text)
                pos = re_
                if re_ <= idx or rs >= end:
                    continue
                s = max(idx, rs) - rs
                e = min(end, re_) - rs
                if not wrote:
                    r.text = text[:s] + new + text[e:]
                    wrote = True
                else:
                    r.text = text[:s] + text[e:]
            count += 1
            start = idx + len(new)
    return count


def replace_in_document(doc, replacements):
    """Thay placeholder trong một Document đã mở. Trả về số vị trí đã thay."""
    seen, total = set(), 0
    for p in _iter_all_paragraphs(doc):
        if id(p._p) in seen:
            continue
        seen.add(id(p._p))
        total += _replace_in_paragraph(p, replacements)
    return total


# ---------------------------------------------------------------------------
# Thao tác trên file
# ---------------------------------------------------------------------------

def replace_in_docx(docx_path, replacements, output_path=None):
    target = ensure_existing_docx(docx_path)
    output = Path(output_path or target).resolve()
    backup_docx(target)
    doc = Document(str(target))
    total = replace_in_document(doc, replacements)
    doc.save(str(output))
    print(f"[OK] {output.name}: đã thay {total} vị trí")
    return output


def _norm(text):
    return " ".join(text.split()).upper()


def append_to_existing_docx(docx_path, new_content, before=None, output_path=None):
    """
    Chèn nội dung vào file có sẵn.
    before: tiêu đề có sẵn để chèn ngay trước (không phân biệt hoa thường).
    Không truyền before thì thêm cuối file.
    """
    target = ensure_existing_docx(docx_path)
    output = Path(output_path or target).resolve()
    backup_docx(target)
    doc = Document(str(target))

    anchor = None
    if before:
        key = _norm(before)
        for p in doc.paragraphs:
            if _norm(p.text) == key:
                anchor = p
                break
        if anchor is None:
            raise ValueError(f"Không tìm thấy tiêu đề '{before}' để chèn trước")

    for item in new_content:
        paragraph = doc.add_paragraph()
        fill_paragraph(doc, paragraph, item)
        if anchor is not None:
            anchor._p.addprevious(paragraph._p)

    doc.save(str(output))
    where = f"trước '{before}'" if anchor is not None else "cuối file"
    print(f"[OK] Đã chèn {len(new_content)} mục {where}: {output.name}")
    return output


HEADING_LIKE = re.compile(
    r"^(CHƯƠNG\s+\d+|PHẦN\s+|KẾT LUẬN|TÀI LIỆU THAM KHẢO|LỜI CẢM ƠN|LỜI CAM ĐOAN|"
    r"DANH MỤC|TÓM TẮT|ABSTRACT|PHỤ LỤC|PHIẾU GIAO|NHẬN XÉT|MỤC LỤC)"
)


def check_document(docx_path):
    """Kiểm tra nhanh một file báo cáo: heading, placeholder còn sót, đoạn trống, section, mục lục."""
    path = Path(docx_path).resolve()
    doc = Document(str(path))
    problems, notes = [], []

    for p in doc.paragraphs:
        text = p.text.strip()
        if not text or "\t" in text:
            continue
        style = p.style.name if p.style is not None else ""
        if HEADING_LIKE.match(_norm(text)) and not style.lower().startswith(("heading", "toc")):
            if style.lower() != "toc heading":
                problems.append(f"Tiêu đề chưa có style Heading (mục lục sẽ bỏ sót): '{text[:60]}'")

    placeholders = set()
    for p in _iter_all_paragraphs(doc):
        for m in re.findall(r"\[[^\[\]]{2,}\]", p.text):
            placeholders.add(m)
    if placeholders:
        short = sorted(x if len(x) <= 40 else x[:37] + "...]" for x in placeholders)
        notes.append(f"Placeholder cần điền ({len(placeholders)}): " + "; ".join(short))

    empties = sum(1 for p in doc.paragraphs if not p.text.strip()
                  and p._p.find(".//" + qn("w:drawing")) is None
                  and p._p.find(".//" + qn("w:sectPr")) is None
                  and p._p.find(".//" + qn("w:fldChar")) is None)
    if empties:
        notes.append(f"Đoạn trống không chức năng: {empties} (nên dùng khoảng cách đoạn thay vì Enter)")

    body_xml = doc.element.body.xml
    if "TOC \\o" not in body_xml:
        problems.append("Không thấy trường mục lục (TOC)")
    notes.append(f"Số section: {len(doc.sections)}")

    print(f"== Kiểm tra: {path.name} ==")
    for m in problems:
        print("[LỖI]", m)
    for m in notes:
        print("[GHI CHÚ]", m)
    if not problems:
        print("[OK] Không có lỗi cấu trúc.")
    return problems


# ---------------------------------------------------------------------------
# Unpack / pack (ủy quyền cho docx-official, không sửa)
# ---------------------------------------------------------------------------

def _load_official(module_name):
    script = DOCX_OFFICIAL_SCRIPTS / f"{module_name}.py"
    if not script.exists():
        raise FileNotFoundError(f"Không tìm thấy {module_name}.py tại: {script}")
    sys.path.insert(0, str(DOCX_OFFICIAL_SCRIPTS))
    return __import__(module_name)


def unpack_docx(docx_path, output_dir):
    unpack = _load_official("unpack")
    unpack.extract_archive_safely(docx_path, output_dir)
    unpack.pretty_print_xml(Path(output_dir))
    print(f"[OK] Đã unpack vào: {output_dir}")


def pack_docx(input_dir, output_docx):
    out_file = Path(output_docx).resolve()
    backup_docx(out_file)
    pack = _load_official("pack")
    ok = pack.pack_document(input_dir, out_file)
    if ok is False:
        raise RuntimeError("Pack không vượt qua kiểm tra; xem thông báo ở trên")
    print(f"[OK] Đã pack: {out_file.name}")
    return out_file


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Công cụ DOCX chuẩn PTIT")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="Tạo file mới từ khung mẫu")
    p.add_argument("kind", choices=list(TEMPLATES))
    p.add_argument("out")

    p = sub.add_parser("replace", help="Thay placeholder")
    p.add_argument("docx")
    p.add_argument("json_file")
    p.add_argument("--out")

    p = sub.add_parser("append", help="Chèn nội dung")
    p.add_argument("docx")
    p.add_argument("json_file")
    p.add_argument("--before")
    p.add_argument("--out")

    p = sub.add_parser("check", help="Kiểm tra cấu trúc file")
    p.add_argument("docx")

    p = sub.add_parser("backup", help="Sao lưu file")
    p.add_argument("docx")

    p = sub.add_parser("unpack", help="Giải nén DOCX")
    p.add_argument("docx")
    p.add_argument("output_dir")

    p = sub.add_parser("pack", help="Đóng gói DOCX")
    p.add_argument("input_dir")
    p.add_argument("output_docx")

    args = parser.parse_args(argv)

    if args.cmd == "init":
        tpl = template_path_for(args.kind)
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(tpl, args.out)
        print(f"[INIT] {tpl.name} -> {args.out}")
    elif args.cmd == "replace":
        replace_in_docx(args.docx, _load_json(args.json_file), args.out)
    elif args.cmd == "append":
        append_to_existing_docx(args.docx, _load_json(args.json_file), args.before, args.out)
    elif args.cmd == "check":
        check_document(args.docx)
    elif args.cmd == "backup":
        backup_docx(args.docx)
    elif args.cmd == "unpack":
        unpack_docx(args.docx, args.output_dir)
    elif args.cmd == "pack":
        pack_docx(args.input_dir, args.output_docx)


if __name__ == "__main__":
    main()
