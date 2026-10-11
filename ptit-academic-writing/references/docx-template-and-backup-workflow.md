# Khung mẫu DOCX và quy trình sao lưu

Tài liệu này mô tả các khung mẫu, placeholder và công cụ Python. Thông số trình bày nằm trong `ptit-standards.md`. Thao tác OOXML chuyên sâu nằm trong `docx-official/`.

---

## 1. Khung mẫu theo loại báo cáo

| File | Loại | Thành phần đặc trưng |
| :--- | :--- | :--- |
| `assets/template_btl.docx` | BTL, 3 chương | Lời cảm ơn, Danh mục viết tắt (bảng 0.1), Mục lục, Phần mở đầu, 3 chương, Kết luận, Tài liệu tham khảo |
| `assets/template_do_an.docx` | Đồ án, khóa luận, 4 chương | Phiếu giao nhiệm vụ, Lời cam đoan, Lời cảm ơn, Nhận xét GVHD, Nhận xét phản biện, Tóm tắt VN, Abstract, Mục lục, Danh mục viết tắt, Danh mục bảng, Danh mục hình, Phần mở đầu, 4 chương, Kết luận, Tài liệu tham khảo, Phụ lục |
| `assets/template_tieu_luan.docx` | Tiểu luận, 3 phần lớn | Mục lục, Phần 1 (mở đầu), Phần 2 (nội dung), Phần 3 (kết luận), Tài liệu tham khảo |

Cấu trúc chung của cả ba file:

- **Section 1 (bìa):** không có số trang. Khung hoa văn và logo nằm trong header.
- **Section 2 (phần đầu):** số La Mã (i, ii, iii...), bắt đầu từ 1.
- **Section 3 (thân bài):** số Ả Rập, bắt đầu từ 1.
- Tiêu đề dùng style Heading 1, 2, 3. Mục lục là trường TOC đã được điền sẵn số trang.
- Trang đầu của mỗi chương, mỗi mục lớn bắt đầu trang mới.

Các mục trong khung mẫu có chứa ghi chú "xóa mục này nếu..." (danh mục bảng, danh mục hình). Hãy xóa khi không cần.

---

## 2. Placeholder

| Placeholder | Ý nghĩa |
| :--- | :--- |
| `[KHOA CHUYÊN NGÀNH]` | Khoa, ví dụ Khoa Công nghệ thông tin 1 |
| `[TÊN HỌC PHẦN]` | Tên học phần, ví dụ Trực quan hóa dữ liệu |
| `[TÊN ĐỀ TÀI BÁO CÁO HOẶC ĐỒ ÁN NGHIÊN CỨU]` | Tên đề tài |
| `[HỌ VÀ TÊN GIẢNG VIÊN]` | Giảng viên hướng dẫn |
| `[HỌ VÀ TÊN SINH VIÊN]` | Họ và tên sinh viên |
| `[MÃ SINH VIÊN]` | Mã sinh viên, ví dụ B23DCKD008 |
| `[LỚP SINH VIÊN]` | Lớp, ví dụ D23CQKD01-B |
| `[NHÓM MÔN HỌC]` | Nhóm môn học, ví dụ Nhóm 05 |
| `[NĂM]` | Năm nộp bài, ví dụ 2026 |

Đồ án có thêm `[TÊN NGÀNH]` (dòng "NGÀNH:" trên bìa). Tiểu luận dùng chung placeholder với BTL.

---

## 3. Công cụ Python (`scripts/docx_tools.py`)

- `template_path_for(kind)`: trả về file khung mẫu theo loại (`btl`, `do-an`, `tieu-luan`).
- `ensure_existing_docx(docx_path, kind)`: nếu file đích chưa có, sao chép từ khung mẫu tương ứng. Không tạo file trắng.
- `backup_docx(docx_path)`: sao lưu vào `back-up-docx/` kèm dấu thời gian. Nếu trùng giây, thêm `_2`, `_3`.
- `replace_in_docx(docx_path, replacements, output_path=None)`: thay placeholder ở cấp run. Quét thân bài, bảng lồng nhau, header và footer. Giữ định dạng của từng run.
- `append_to_existing_docx(docx_path, new_content, before=None, output_path=None)`: chèn nội dung trước một tiêu đề. Định dạng heading và thân bài theo quy chuẩn PTIT, heading có style Heading để mục lục nhận diện.
- `check_document(docx_path)`: kiểm tra tiêu đề thiếu style, trường mục lục, placeholder còn sót, đoạn trống, số section.
- `unpack_docx` và `pack_docx`: ủy quyền cho `docx-official/ooxml/scripts/unpack.py` và `pack.py`.

---

## 4. Dựng lại khung mẫu

`scripts/build_templates.py` dựng ba file khung mẫu từ đặc tả nội dung, lấy bìa và logo từ `assets/src/base_cover.docx`. Quy trình:

1. Dựng tài liệu với mục lục có số trang giả.
2. Render bằng LibreOffice, tìm trang thật của từng tiêu đề bằng `pdftotext`.
3. Dựng lại với số trang đã đo. Số dòng mục lục không đổi nên bố cục giữ nguyên.
4. Kiểm tra lại: số trang đo lần hai phải khớp.
5. Bỏ thumbnail cũ và đặt metadata sạch.

Để sửa nội dung khung mẫu, chỉnh đặc tả trong `build_templates.py` rồi chạy lại. Không sửa tay file `.docx` rồi quên cập nhật đặc tả.
