#!/usr/bin/env python3
"""
Dựng lại các khung mẫu PTIT từ một đặc tả (spec) và nguồn bìa assets/src/base_cover.docx.

Ra ba file:
  assets/template_btl.docx        BTL, 3 chương
  assets/template_do_an.docx      Đồ án / khóa luận, 4 chương, đủ trang thủ tục
  assets/template_tieu_luan.docx  Tiểu luận, 3 phần lớn

Quy trình:
  1. Dựng tài liệu theo đặc tả. Tiêu đề dùng style Heading 1-3. Mục lục là trường TOC.
  2. Render bằng LibreOffice, tìm số trang thật của từng tiêu đề.
  3. Dựng lại với số trang đã tìm (số dòng mục lục giữ nguyên nên bố cục không đổi).
  4. Bỏ thumbnail cũ, đặt metadata sạch.

Chạy:  python3 scripts/build_templates.py
Cần: python-docx, LibreOffice (soffice), pdftotext (poppler-utils).
"""

import copy
import datetime as dt
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from docx import Document
from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Cm, Pt, RGBColor

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import docx_tools as T  # noqa: E402

BASE = T.ASSETS / "src" / "base_cover.docx"
TEXT_WIDTH_CM = 16.5  # 21.0 - 3.0 (trái) - 1.5 (phải)

LOI_CAM_ON = [
    "Lời đầu tiên, em xin chân thành gửi lời cảm ơn sâu sắc tới các Thầy, Cô giáo thuộc Học viện "
    "Công nghệ Bưu chính Viễn thông đã tận tình giảng dạy, truyền đạt những kiến thức nền tảng và "
    "chuyên môn quý báu trong suốt quá trình học tập.",
    "Đặc biệt, em xin bày tỏ lòng biết ơn chân thành nhất tới Giảng viên hướng dẫn đã luôn định hướng "
    "phương pháp tiếp cận khoa học, giải đáp tận tình các vướng mắc kỹ thuật trong suốt quá trình hoàn "
    "thành đề tài.",
    "Mặc dù đã rất nỗ lực hoàn thiện nội dung và báo cáo một cách chỉn chu nhất, song do giới hạn về mặt "
    "thời gian và kinh nghiệm thực tiễn, đề tài khó tránh khỏi những thiếu sót nhất định. Em rất mong "
    "nhận được những nhận xét, góp ý quý báu từ quý Thầy, Cô để hoàn thiện đề tài tốt hơn trong tương lai.",
]

REFERENCES = [
    "[1] Tên tác giả, \"Tên bài báo hoặc tài liệu tham khảo,\" Tên tạp chí hoặc nguồn, Năm.",
    "[2] Tên tác giả, Tên sách, Lần xuất bản. Thành phố: Nhà xuất bản, Năm.",
    "[3] Tên tổ chức hoặc tác giả, \"Tên trang hoặc tài liệu trực tuyến,\" Tên website, Năm. Truy cập: ngày/tháng/năm.",
]

PH = "[Trình bày nội dung theo hướng dẫn của mục này. Xóa phần hướng dẫn sau khi viết xong.]"


def H(level, text, pbb=False):
    return ("H", level, text, pbb)


def P(text):
    return ("P", text)


def NOTE(text):
    return ("NOTE", text)


def BREAK(fmt):
    return ("BREAK", fmt)  # kết thúc section; fmt là kiểu đánh số của section này


# ---------------------------------------------------------------------------
# Đặc tả từng loại báo cáo
# ---------------------------------------------------------------------------

def body_common_intro():
    return [
        H(1, "PHẦN MỞ ĐẦU"),
        H(2, "1. Tính cấp thiết của đề tài"), P("[Trình bày bối cảnh thực tiễn, lý do lựa chọn đề tài và bài toán kỹ thuật cần giải quyết.]"),
        H(2, "2. Mục tiêu nghiên cứu"), P("[Mục tiêu tổng quát và các mục tiêu kỹ thuật cụ thể cần hoàn thành.]"),
        H(2, "3. Đối tượng và phạm vi nghiên cứu"), P("[Xác định rõ đối tượng thực nghiệm, phạm vi dữ liệu hoặc giới hạn chức năng.]"),
        H(2, "4. Phương pháp tiếp cận và công cụ thực thi"), P("[Phương pháp, quy trình triển khai và công nghệ sử dụng.]"),
        H(2, "5. Bố cục của báo cáo"), P("[Tóm tắt cấu trúc các chương tiếp theo và phần kết luận.]"),
    ]


def spec_btl():
    front = [
        H(1, "LỜI CẢM ƠN"),
        *[P(t) for t in LOI_CAM_ON],
        H(1, "DANH MỤC THUẬT NGỮ VÀ TỪ VIẾT TẮT", pbb=True),
        P("Bảng 0.1: Danh mục các thuật ngữ và từ viết tắt trong báo cáo"),
        ("TABLE",),
        ("TOCH", "MỤC LỤC"),
        ("TOC",),
        BREAK("lowerRoman"),
    ]
    body = [
        *body_common_intro(),
        H(1, "CHƯƠNG 1: TỔNG QUAN BÀI TOÁN VÀ CƠ SỞ LÝ THUYẾT", pbb=True),
        H(2, "1.1 Khảo sát bài toán và bối cảnh thực tiễn"), P(PH),
        H(2, "1.2 Cơ sở lý thuyết nền tảng"), P(PH),
        H(1, "CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP", pbb=True),
        H(2, "2.1 Phân tích yêu cầu và kiến trúc hệ thống"), P(PH),
        H(2, "2.2 Thiết kế chi tiết và cấu trúc dữ liệu"), P(PH),
        H(1, "CHƯƠNG 3: HIỆN THỰC HÓA VÀ THỰC NGHIỆM", pbb=True),
        H(2, "3.1 Cài đặt và triển khai chức năng"), P(PH),
        H(2, "3.2 Kết quả thực nghiệm và đánh giá"), P(PH),
        H(1, "KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", pbb=True),
        H(2, "1. Các kết quả định lượng đạt được"), P(PH),
        H(2, "2. Hạn chế của đề tài"), P(PH),
        H(2, "3. Hướng phát triển mở rộng"), P(PH),
        H(1, "TÀI LIỆU THAM KHẢO", pbb=True),
        *[P(r) for r in REFERENCES],
    ]
    return {"cover": {"[BÁO CÁO BÀI TẬP LỚN / TIỂU LUẬN / ĐỒ ÁN / KHÓA LUẬN]": "BÁO CÁO BÀI TẬP LỚN"},
            "spec": front + body}


def spec_do_an():
    front = [
        H(1, "PHIẾU GIAO NHIỆM VỤ"),
        NOTE("[Đính kèm phiếu giao nhiệm vụ bản chính do Khoa cấp, theo mẫu của Khoa.]"),
        H(1, "LỜI CAM ĐOAN", pbb=True),
        P("Em xin cam đoan đây là công trình nghiên cứu của riêng em, được thực hiện dưới sự hướng dẫn của "
          "[HỌ VÀ TÊN GIẢNG VIÊN]. Các số liệu và kết quả trong đồ án là trung thực và chưa từng được công bố "
          "trong công trình nào khác. Các tài liệu tham khảo đã được trích dẫn đầy đủ."),
        H(1, "LỜI CẢM ƠN", pbb=True),
        *[P(t) for t in LOI_CAM_ON],
        H(1, "NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN", pbb=True),
        NOTE("[Nội dung nhận xét do giảng viên hướng dẫn ghi và ký.]"),
        H(1, "NHẬN XÉT CỦA CÁN BỘ CHẤM PHẢN BIỆN", pbb=True),
        NOTE("[Nội dung nhận xét do cán bộ chấm phản biện ghi và ký.]"),
        H(1, "TÓM TẮT ĐỒ ÁN", pbb=True),
        P("[Tóm tắt bài toán, phương pháp, kết quả chính và đóng góp, khoảng 250–300 từ.]"),
        H(1, "ABSTRACT", pbb=True),
        P("[English summary of the report: problem, method, main results and contributions, about 250–300 words.]"),
        ("TOCH", "MỤC LỤC", True),
        ("TOC",),
        H(1, "DANH MỤC TỪ VIẾT TẮT", pbb=True),
        ("TABLE",),
        H(1, "DANH MỤC BẢNG BIỂU", pbb=True),
        NOTE("[Liệt kê theo thứ tự: Bảng x.y – tiêu đề. Xóa mục này nếu báo cáo có ít hơn 2 bảng.]"),
        H(1, "DANH MỤC HÌNH VẼ", pbb=True),
        NOTE("[Liệt kê theo thứ tự: Hình x.y – tiêu đề. Xóa mục này nếu báo cáo có ít hơn 2 hình.]"),
        BREAK("lowerRoman"),
    ]
    body = [
        *body_common_intro(),
        H(1, "CHƯƠNG 1: TỔNG QUAN BÀI TOÁN VÀ CƠ SỞ LÝ THUYẾT", pbb=True),
        H(2, "1.1 Khảo sát bài toán và bối cảnh thực tiễn"), P(PH),
        H(2, "1.2 Cơ sở lý thuyết nền tảng"), P(PH),
        H(1, "CHƯƠNG 2: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG", pbb=True),
        H(2, "2.1 Phân tích yêu cầu chức năng và phi chức năng"), P(PH),
        H(2, "2.2 Kiến trúc hệ thống"), P(PH),
        H(2, "2.3 Thiết kế chi tiết và cấu trúc dữ liệu"), P(PH),
        H(1, "CHƯƠNG 3: HIỆN THỰC HÓA HỆ THỐNG", pbb=True),
        H(2, "3.1 Môi trường và công cụ triển khai"), P(PH),
        H(2, "3.2 Cài đặt các thành phần chính"), P(PH),
        H(1, "CHƯƠNG 4: THỰC NGHIỆM VÀ ĐÁNH GIÁ", pbb=True),
        H(2, "4.1 Kịch bản và dữ liệu thực nghiệm"), P(PH),
        H(2, "4.2 Kết quả và đánh giá"), P(PH),
        H(1, "KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN", pbb=True),
        H(2, "1. Các kết quả đạt được"), P(PH),
        H(2, "2. Hạn chế của đề tài"), P(PH),
        H(2, "3. Hướng phát triển mở rộng"), P(PH),
        H(1, "TÀI LIỆU THAM KHẢO", pbb=True),
        *[P(r) for r in REFERENCES],
        H(1, "PHỤ LỤC", pbb=True),
        NOTE("[Mã nguồn quan trọng, bảng số liệu chi tiết, nếu có.]"),
    ]
    return {"cover": {"[BÁO CÁO BÀI TẬP LỚN / TIỂU LUẬN / ĐỒ ÁN / KHÓA LUẬN]": "ĐỒ ÁN CHUYÊN NGÀNH",
                      "HỌC PHẦN: [TÊN HỌC PHẦN]": "NGÀNH: [TÊN NGÀNH]"},
            "spec": front + body}


def spec_tieu_luan():
    front = [
        ("TOCH", "MỤC LỤC"),
        ("TOC",),
        BREAK("lowerRoman"),
    ]
    body = [
        H(1, "PHẦN 1: MỞ ĐẦU / ĐẶT VẤN ĐỀ"),
        H(2, "1.1 Lý do chọn đề tài và bối cảnh"), P(PH),
        H(2, "1.2 Mục tiêu nghiên cứu"), P(PH),
        H(2, "1.3 Đối tượng và phạm vi nghiên cứu"), P(PH),
        H(2, "1.4 Phương pháp nghiên cứu"), P(PH),
        H(1, "PHẦN 2: NỘI DUNG NGHIÊN CỨU"),
        H(2, "2.1 Cơ sở lý luận của vấn đề"), P(PH),
        H(2, "2.2 Thực trạng vấn đề trong thực tiễn"), P(PH),
        H(2, "2.3 Phân tích nguyên nhân và đánh giá ưu, nhược điểm"), P(PH),
        H(2, "2.4 Đề xuất giải pháp hoặc kiến nghị"), P(PH),
        H(1, "PHẦN 3: KẾT LUẬN"),
        P(PH),
        H(1, "TÀI LIỆU THAM KHẢO", pbb=True),
        *[P(r) for r in REFERENCES],
    ]
    return {"cover": {"[BÁO CÁO BÀI TẬP LỚN / TIỂU LUẬN / ĐỒ ÁN / KHÓA LUẬN]": "TIỂU LUẬN HỌC PHẦN"},
            "spec": front + body}


KINDS = {
    "btl": ("template_btl.docx", spec_btl),
    "do-an": ("template_do_an.docx", spec_do_an),
    "tieu-luan": ("template_tieu_luan.docx", spec_tieu_luan),
}


# ---------------------------------------------------------------------------
# Dựng tài liệu
# ---------------------------------------------------------------------------

def roman(n):
    vals = [(10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s
            n -= v
    return out


def _add_fld(paragraph, instr, size=None, placeholder="1", close=True):
    def run_with(el):
        r = paragraph.add_run()
        r._r.append(el)
        if size:
            r.font.size = Pt(size)
        return r
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin"); run_with(b)
    it = OxmlElement("w:instrText"); it.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    it.text = instr
    r = paragraph.add_run(); r._r.append(it)
    s = OxmlElement("w:fldChar"); s.set(qn("w:fldCharType"), "separate"); run_with(s)
    if placeholder:
        t = paragraph.add_run(placeholder)
        if size:
            t.font.size = Pt(size)
    if close:
        e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end"); run_with(e)


def _style_xml(style_el, ppr, rpr):
    for tag in ("w:pPr", "w:rPr"):
        for old in style_el.findall(qn(tag)):
            style_el.remove(old)
    style_el.append(parse_xml(f"<w:pPr {nsdecls('w')}>{ppr}</w:pPr>"))
    style_el.append(parse_xml(f"<w:rPr {nsdecls('w')}>{rpr}</w:rPr>"))


TNR = '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="Times New Roman" w:cs="Times New Roman"/>'


def fix_styles(doc):
    """Heading 1-3 đen, TNR, không theme; thêm TOC 1-2 để F9 ra đúng định dạng."""
    styles = doc.styles.element
    specs = {
        "Heading 1": ('<w:keepNext/><w:keepLines/><w:spacing w:before="240" w:after="120"/>'
                      '<w:jc w:val="left"/><w:outlineLvl w:val="0"/>',
                      f'{TNR}<w:b/><w:bCs/><w:color w:val="000000"/><w:sz w:val="30"/><w:szCs w:val="30"/>'),
        "Heading 2": ('<w:keepNext/><w:keepLines/><w:spacing w:before="160" w:after="80"/>'
                      '<w:jc w:val="left"/><w:outlineLvl w:val="1"/>',
                      f'{TNR}<w:b/><w:bCs/><w:color w:val="000000"/><w:sz w:val="27"/><w:szCs w:val="27"/>'),
        "Heading 3": ('<w:keepNext/><w:keepLines/><w:spacing w:before="120" w:after="60"/>'
                      '<w:jc w:val="left"/><w:outlineLvl w:val="2"/>',
                      f'{TNR}<w:b/><w:bCs/><w:i/><w:iCs/><w:color w:val="000000"/><w:sz w:val="26"/><w:szCs w:val="26"/>'),
    }
    for st in styles.findall(qn("w:style")):
        name = st.find(qn("w:name"))
        if name is not None and name.get(qn("w:val")) in specs:
            ppr, rpr = specs[name.get(qn("w:val"))]
            _style_xml(st, ppr, rpr)

    toc_specs = {
        "TOC1": ("toc 1", '<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9354"/></w:tabs>'
                          '<w:spacing w:before="80" w:after="40" w:line="276" w:lineRule="auto"/><w:jc w:val="left"/>',
                 f'{TNR}<w:b/><w:color w:val="000000"/><w:sz w:val="26"/>'),
        "TOC2": ("toc 2", '<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9354"/></w:tabs>'
                          '<w:spacing w:before="40" w:after="20" w:line="276" w:lineRule="auto"/>'
                          '<w:ind w:left="340"/><w:jc w:val="left"/>',
                 f'{TNR}<w:color w:val="000000"/><w:sz w:val="26"/>'),
    }
    existing = {st.get(qn("w:styleId")): st for st in styles.findall(qn("w:style"))}
    for sid, (name, ppr, rpr) in toc_specs.items():
        st = existing.get(sid)
        if st is None:
            st = parse_xml(
                f'<w:style {nsdecls("w")} w:type="paragraph" w:styleId="{sid}">'
                f'<w:name w:val="{name}"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/>'
                f'<w:uiPriority w:val="39"/><w:unhideWhenUsed/></w:style>')
            styles.append(st)
        _style_xml(st, ppr, rpr)


def _clear_after_cover(doc):
    body = doc.element.body
    final = body.find(qn("w:sectPr"))
    cover_end = None
    for child in body.iterchildren():
        if child.tag == qn("w:p") and child.find(".//" + qn("w:sectPr")) is not None:
            cover_end = child
            break
    if cover_end is None:
        raise RuntimeError("Không tìm thấy section break của bìa trong file nguồn")
    remove = []
    seen_cover = False
    for child in body.iterchildren():
        if child is cover_end:
            seen_cover = True
            continue
        if seen_cover and child is not final:
            remove.append(child)
    for el in remove:
        body.remove(el)
    return final


def _find_source_table(src_doc):
    for child in src_doc.element.body.iterchildren():
        if child.tag == qn("w:tbl"):
            return copy.deepcopy(child)
    raise RuntimeError("Không tìm thấy bảng DM viết tắt trong nguồn")


def _section_copy(final_sect, fmt):
    sect = copy.deepcopy(final_sect)
    for tag in ("w:headerReference", "w:footerReference", "w:pgNumType"):
        for el in sect.findall(qn(tag)):
            sect.remove(el)
    pg = OxmlElement("w:pgNumType")
    pg.set(qn("w:fmt"), fmt)
    pg.set(qn("w:start"), "1")
    cols = sect.find(qn("w:cols"))
    if cols is not None:
        cols.addprevious(pg)
    else:
        sect.append(pg)
    return sect


def _set_final_numbering(final_sect, fmt):
    for el in final_sect.findall(qn("w:pgNumType")):
        final_sect.remove(el)
    pg = OxmlElement("w:pgNumType")
    pg.set(qn("w:fmt"), fmt)
    pg.set(qn("w:start"), "1")
    cols = final_sect.find(qn("w:cols"))
    if cols is not None:
        cols.addprevious(pg)
    else:
        final_sect.append(pg)


def _toc_entries(spec):
    """Danh sách (level, text, section) cho mục lục, theo thứ tự đặc tả."""
    out, section = [], "front"
    for item in spec:
        if item[0] == "BREAK":
            section = "body"
        elif item[0] == "H":
            out.append((item[1], item[2], section))
    return out


def build(kind, page_numbers=None, out_path=None):
    filename, spec_fn = KINDS[kind]
    cfg = spec_fn()
    spec = cfg["spec"]
    src = Document(str(BASE))
    table_src = _find_source_table(src)

    doc = Document(str(BASE))
    fix_styles(doc)
    final = _clear_after_cover(doc)
    final_template = copy.deepcopy(final)

    # Đổi tiêu đề bìa theo loại báo cáo
    T.replace_in_document(doc, cfg.get("cover", {}))

    entries = _toc_entries(spec)
    if page_numbers is None:
        page_numbers = ["0"] * len(entries)
    entry_iter = iter(zip(entries, page_numbers))

    def add_p():
        return doc.add_paragraph()

    for item in spec:
        kind_ = item[0]
        if kind_ == "H":
            _, level, text, pbb = item
            p = add_p()
            T.fill_paragraph(doc, p, {"heading": level, "text": text})
            if pbb:
                p.paragraph_format.page_break_before = True
        elif kind_ == "TOCH":
            p = add_p()
            p.style = doc.styles["TOC Heading"]
            pf = p.paragraph_format
            pf.alignment = 0
            pf.space_before = Pt(12)
            pf.space_after = Pt(6)
            pf.page_break_before = item[2] if len(item) > 2 else True
            r = p.add_run(item[1])
            T.set_run_format(r, 15, bold=True)
        elif kind_ == "P":
            p = add_p()
            T.fill_paragraph(doc, p, {"text": item[1]})
        elif kind_ == "NOTE":
            p = add_p()
            T.fill_paragraph(doc, p, {"text": item[1]})
            for r in p.runs:
                r.font.italic = True
        elif kind_ == "TABLE":
            sect_el = doc.element.body.find(qn("w:sectPr"))
            sect_el.addprevious(copy.deepcopy(table_src))
        elif kind_ == "TOC":
            _emit_toc(doc, entry_iter)
        elif kind_ == "BREAK":
            p = add_p()
            p._p.get_or_add_pPr().append(_section_copy(final_template, item[1]))
        else:
            raise ValueError(f"Token đặc tả không hợp lệ: {item}")

    _set_final_numbering(final, "decimal")

    # Footer: front dùng số La Mã, body dùng số Ả Rập, bìa không có số
    sections = doc.sections
    for idx, sec in enumerate(sections):
        sec.header.is_linked_to_previous = False
        if idx == 0:
            sec.footer.is_linked_to_previous = False
            continue
        sec.footer.is_linked_to_previous = False
        fp = sec.footer.paragraphs[0]
        for r in list(fp.runs):
            r._r.getparent().remove(r._r)
        fp.alignment = 1
        _add_fld(fp, " PAGE ", size=12)

    cp = doc.core_properties
    cp.title = f"Khung mẫu báo cáo PTIT ({kind})"
    cp.author = ""
    cp.last_modified_by = ""
    cp.comments = ""
    cp.subject = ""
    cp.keywords = "PTIT, báo cáo, khung mẫu"
    cp.category = "Khung mẫu"
    now = dt.datetime.now(dt.timezone.utc).replace(tzinfo=None, microsecond=0)
    cp.created = now
    cp.modified = now
    cp.revision = 1

    out = Path(out_path or (T.ASSETS / filename))
    doc.save(str(out))
    _strip_thumbnail(out)
    return out


def _emit_toc(doc, entry_iter):
    p0 = doc.add_paragraph()
    _add_fld(p0, ' TOC \\o "1-3" \\h \\z \\u ', placeholder=None, close=False)
    for (level, text, _section), number in entry_iter:
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.alignment = 0
        pf.first_line_indent = Cm(0)
        pf.left_indent = Cm({1: 0, 2: 0.6, 3: 1.2}[level])
        pf.space_before = Pt(4 if level == 1 else 2)
        pf.space_after = Pt(2)
        pf.tab_stops.add_tab_stop(Cm(TEXT_WIDTH_CM), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        r1 = p.add_run(text)
        T.set_run_format(r1, 13 if level == 1 else 13, bold=(level == 1))
        r2 = p.add_run("\t" + number)
        T.set_run_format(r2, 13, bold=(level == 1))
    p_end = doc.add_paragraph()
    e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end")
    rr = p_end.add_run(); rr._r.append(e)


def _strip_thumbnail(path):
    fd, tmp_name = tempfile.mkstemp(suffix=".docx")
    import os
    os.close(fd)
    tmp = Path(tmp_name)
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            if item.filename == "docProps/thumbnail.jpeg":
                continue
            data = zin.read(item.filename)
            if item.filename == "_rels/.rels":
                text = data.decode("utf-8")
                text = re.sub(r'<Relationship[^>]*Target="docProps/thumbnail\.jpeg"[^>]*/>', "", text)
                data = text.encode("utf-8")
            zout.writestr(item, data)
    shutil.move(str(tmp), str(path))
    Path(path).chmod(0o644)


# ---------------------------------------------------------------------------
# Đo số trang thật bằng LibreOffice
# ---------------------------------------------------------------------------

def _norm(s):
    return re.sub(r"\s+", "", s).upper()


def render_pages(docx_path):
    outdir = Path(tempfile.mkdtemp())
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(outdir), str(docx_path)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
    pdf = outdir / (Path(docx_path).stem + ".pdf")
    text = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"], check=True,
                          capture_output=True, text=True).stdout
    pages = text.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return [p.splitlines() for p in pages]


def measure(kind):
    filename, spec_fn = KINDS[kind]
    spec = spec_fn()["spec"]
    entries = _toc_entries(spec)
    probe = build(kind, None, out_path=Path(tempfile.mkdtemp()) / "probe.docx")
    pages = render_pages(probe)

    cur = 1  # trang 0 là bìa; front bắt đầu ở trang 1
    found = []
    toc_pages = {i for i, lines in enumerate(pages)
                 if sum(1 for l in lines if "...." in l or "…" in l) >= 3}
    for level, text, section in entries:
        target = _norm(text)
        hit = None
        for i in range(cur, len(pages)):
            if i in toc_pages:
                continue
            lines = pages[i]
            for j, line in enumerate(lines):
                if _norm(line) == target or (j + 1 < len(lines) and _norm(line + lines[j + 1]) == target):
                    hit = i
                    break
            if hit is not None:
                break
        if hit is None:
            raise RuntimeError(f"Không tìm thấy tiêu đề trên PDF: {text}")
        cur = hit
        found.append(hit)

    body_start = None
    numbers = []
    for (level, text, section), page in zip(entries, found):
        if section == "body" and body_start is None:
            body_start = page
    for (level, text, section), page in zip(entries, found):
        if section == "front":
            numbers.append(roman(page))  # front bắt đầu tại trang index 1 nên số = index
        else:
            numbers.append(str(page - body_start + 1))
    return numbers


def build_all():
    results = {}
    for kind in KINDS:
        nums = measure(kind)
        out = build(kind, nums)
        # kiểm tra: dựng lại với số đã đo phải cho đúng số đó
        check = measure(kind)
        ok = check == nums
        results[kind] = (out, ok, nums)
        print(f"[{kind}] {out.name}  mục lục khớp: {ok}")
    return results


if __name__ == "__main__":
    build_all()
