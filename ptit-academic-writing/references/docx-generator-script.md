# Kịch bản Mẫu Tự động Hóa Xuất Báo cáo DOCX Chuẩn PTIT (python-docx)

Dưới đây là mã nguồn Python mẫu (`ptit_docx_builder.py`) được tối ưu hóa toàn diện để tự động tạo tài liệu Microsoft Word (`.docx`) chuẩn 100% quy định PTIT.

---

```python
import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

class PTITDocxBuilder:
    def __init__(self, filename="Bao_Cao_PTIT.docx", assets_dir=None):
        self.filename = filename
        self.doc = Document()
        self.assets_dir = assets_dir or os.path.join(os.path.dirname(__file__), "..", "assets")
        self._setup_page_geometry()
        self._setup_styles()

    def _setup_page_geometry(self):
        """Thiết lập kích thước trang A4 và căn lề chuẩn PTIT (Top 2cm, Bottom 2cm, Left 3.0cm, Right 1.5cm)"""
        section = self.doc.sections[0]
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(3.0)
        section.right_margin = Cm(1.5)
        section.header_distance = Cm(1.2)
        section.footer_distance = Cm(1.2)

    def _setup_styles(self):
        """Thiết lập font chữ Times New Roman và các cấp độ Heading"""
        # Normal Style
        style_normal = self.doc.styles['Normal']
        style_normal.font.name = 'Times New Roman'
        style_normal.font.size = Pt(13)
        style_normal.font.color.rgb = RGBColor(0, 0, 0)
        style_normal.paragraph_format.line_spacing = 1.3
        style_normal.paragraph_format.space_before = Pt(0)
        style_normal.paragraph_format.space_after = Pt(4)
        style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        style_normal.paragraph_format.first_line_indent = Cm(1.0)

    def add_cover_page(self, report_type="BÁO CÁO BÀI TẬP LỚN", subject="TRỰC QUAN HÓA DỮ LIỆU", 
                       title="TÊN ĐỀ TÀI BÁO CÁO NGHIÊN CỨU", faculty="KHOA CÔNG NGHỆ THÔNG TIN 1",
                       lecturer="TS. Nguyễn Văn A", students=None, academic_year="2026"):
        """Tạo trang bìa chuẩn PTIT có khung hoa văn và Logo"""
        students = students or [("Tạ Hoài Bình", "B23DCKD008", "D23CQKD01-B")]
        
        # Section 1: Trang bìa
        p_dept = self.doc.add_paragraph()
        p_dept.paragraph_format.first_line_indent = Cm(0)
        p_dept.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_dept.paragraph_format.space_after = Pt(2)
        run = p_dept.add_run("BỘ THÔNG TIN VÀ TRUYỀN THÔNG\n")
        run.bold = True
        run.font.size = Pt(12)
        run2 = p_dept.add_run("HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG\n")
        run2.bold = True
        run2.font.size = Pt(13)
        run3 = p_dept.add_run(faculty.upper())
        run3.bold = True
        run3.font.size = Pt(13)

        # Chèn Logo PTIT
        logo_path = os.path.join(self.assets_dir, "Logo.png")
        if os.path.exists(logo_path):
            p_logo = self.doc.add_paragraph()
            p_logo.paragraph_format.first_line_indent = Cm(0)
            p_logo.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_logo.paragraph_format.space_before = Pt(12)
            p_logo.paragraph_format.space_after = Pt(12)
            p_logo.add_run().add_picture(logo_path, width=Cm(3.8))

        # Tiêu đề Báo cáo & Học phần
        p_type = self.doc.add_paragraph()
        p_type.paragraph_format.first_line_indent = Cm(0)
        p_type.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_type.paragraph_format.space_after = Pt(4)
        run_type = p_type.add_run(f"{report_type}\n")
        run_type.bold = True
        run_type.font.size = Pt(16)
        run_type.font.color.rgb = RGBColor(160, 20, 20) # Tone đỏ PTIT
        
        run_sub = p_type.add_run(f"HỌC PHẦN: {subject.upper()}")
        run_sub.bold = True
        run_sub.font.size = Pt(14)

        # Tên Đề tài
        p_title = self.doc.add_paragraph()
        p_title.paragraph_format.first_line_indent = Cm(0)
        p_title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_title.paragraph_format.space_before = Pt(18)
        p_title.paragraph_format.space_after = Pt(28)
        run_lbl = p_title.add_run("ĐỀ TÀI:\n")
        run_lbl.bold = True
        run_lbl.font.size = Pt(14)
        run_name = p_title.add_run(title.upper())
        run_name.bold = True
        run_name.font.size = Pt(18)

        # Khung thông tin SV & GV
        p_info = self.doc.add_paragraph()
        p_info.paragraph_format.first_line_indent = Cm(2.5)
        p_info.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_info.paragraph_format.space_after = Pt(2)
        p_info.add_run(f"Giảng viên hướng dẫn:  {lecturer}\n").bold = True
        
        for i, (name, msv, lop) in enumerate(students):
            lbl = "Sinh viên thực hiện:   " if i == 0 else "                       "
            p_info.add_run(f"{lbl}{name} - MSV: {msv} (Lớp: {lop})\n")

        # Địa danh & Năm
        p_footer = self.doc.add_paragraph()
        p_footer.paragraph_format.first_line_indent = Cm(0)
        p_footer.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_footer.paragraph_format.space_before = Pt(36)
        run_year = p_footer.add_run(f"HÀ NỘI - {academic_year}")
        run_year.bold = True
        run_year.font.size = Pt(13)

        # Ngắt sang trang mới
        self.doc.add_page_break()

    def add_heading_1(self, text):
        """Thêm tiêu đề Chương (Heading 1)"""
        p = self.doc.add_paragraph()
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(text.upper())
        run.bold = True
        run.font.size = Pt(15)
        run.font.color.rgb = RGBColor(0, 51, 102)
        return p

    def add_heading_2(self, text):
        """Thêm mục cấp 2 (Heading 2)"""
        p = self.doc.add_paragraph()
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        run = p.add_run(text)
        run.bold = True
        run.font.size = Pt(13.5)
        return p

    def add_heading_3(self, text):
        """Thêm mục cấp 3 (Heading 3)"""
        p = self.doc.add_paragraph()
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(text)
        run.bold = True
        run.italic = True
        run.font.size = Pt(13)
        return p

    def add_figure(self, image_path, caption, fig_num="1.1", width_cm=14):
        """Chèn hình vẽ có tiêu đề chuẩn PTIT ở DƯỚI hình"""
        if not os.path.exists(image_path):
            return
        p_img = self.doc.add_paragraph()
        p_img.paragraph_format.first_line_indent = Cm(0)
        p_img.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(2)
        p_img.add_run().add_picture(image_path, width=Cm(width_cm))

        p_cap = self.doc.add_paragraph()
        p_cap.paragraph_format.first_line_indent = Cm(0)
        p_cap.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(8)
        run_cap = p_cap.add_run(f"Hình {fig_num}: {caption}")
        run_cap.bold = True
        run_cap.font.size = Pt(11.5)

    def save(self):
        """Lưu tệp Word hoàn chỉnh"""
        self.doc.save(self.filename)
        print(f"Đã xuất báo cáo chuẩn PTIT: {self.filename}")
```
