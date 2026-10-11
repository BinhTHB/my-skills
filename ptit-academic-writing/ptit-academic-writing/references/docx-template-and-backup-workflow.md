# Quy trình Thao tác DOCX PTIT, Khung mẫu Linh hoạt & Sao lưu Tự động

Mọi kỹ thuật thao tác với file DOCX (đọc nội dung, trích xuất text, sửa văn bản, can thiệp OOXML, bảng biểu, redlining / tracked changes) **tham chiếu trực tiếp kỹ năng `/docx-official`** và tài liệu đính kèm tại `references/docx-official/`. Kỹ năng này không lặp lại các hướng dẫn kỹ thuật đó.

---

## 1. Hai Nguyên tắc Bắt buộc của PTIT

1. **LUÔN LUÔN CHỈNH SỬA CÁI CÓ SẴN (KHÔNG TẠO MỚI TỪ CON SỐ 0):**
   - **Đã có file báo cáo:** Thao tác trực tiếp trên file Word `.docx` của người dùng theo quy trình của kỹ năng `/docx-official`.
   - **Làm bài mới:** Sao chép nguyên vẹn khung mẫu có sẵn từ `assets/template_ptit.docx` ra thư mục làm việc, sau đó dùng kỹ năng `/docx-official` hoặc script tiện ích để thay thế nội dung. Tuyệt đối không tạo file Word trắng từ đầu.

2. **LUÔN TỰ ĐỘNG ĐƯA BẢN CŨ VÀO THƯ MỤC `back-up-docx`:**
   - Trước khi lưu đè bất kỳ thay đổi nào, file hiện tại phải được nhân bản vào thư mục `back-up-docx/` nằm cùng cấp:
     ```
     [thư_mục_chứa_file]/back-up-docx/[tên_file]_[YYYYMMDD_HHMMSS].docx
     ```
   - Đảm bảo 100% dữ liệu gốc được bảo toàn, sinh viên có thể đối chiếu hoặc quay lui bất kỳ lúc nào.

---

## 2. Khung Mẫu DOCX Chuẩn Học viện (`assets/template_ptit.docx`)

Khung mẫu có sẵn đã được thiết kế chuẩn mực nhưng **hoàn toàn phi hardcode (không gò bó một đề tài hay số chương cố định)**:
- **Trang bìa (Section 1):** Khung hoa văn viền chìm (`assets/Khung.png`), `Logo.png` 3.5cm, lề Trái 2.5cm, Phải 2.0cm, Trên 2.0cm, Dưới 2.0cm.
- **Thân bài (Section 2):** Bỏ viền hoa văn, header ngắt liên kết, footer canh giữa có trường mã Word `PAGE` tự động, lề Trái 3.0cm (đóng gáy), Phải 1.5cm, Trên 2.0cm, Dưới 2.0cm.
- **Hệ thống đề mục & Mục lục:**
  - Mục lục tích hợp trường mã Word TOC tự động (`TOC \o "1-3" \h \z \u`), tự động cập nhật số trang khi người dùng thêm/bớt mục.
  - Các khối mô-đun mẫu: Lời cảm ơn/cam đoan, Danh mục từ viết tắt, Mở đầu, Các chương nội dung, Kết luận, Tài liệu tham khảo IEEE.

### Bảng Placeholder Động trong Khung mẫu:
| Placeholder | Ý nghĩa thay thế (Linh hoạt theo loại bài) |
| :--- | :--- |
| `[KHOA CHUYÊN NGÀNH]` | Khoa Viễn thông 1, Khoa CNTT 1, Khoa ATTT, v.v. |
| `[BÁO CÁO BÀI TẬP LỚN / TIỂU LUẬN / ĐỒ ÁN / KHÓA LUẬN]` | Loại hình văn bản học thuật |
| `[TÊN HỌC PHẦN]` | Tên môn học (VD: Trực quan hóa dữ liệu, Kỹ thuật lập trình...) |
| `[TÊN ĐỀ TÀI BÁO CÁO HOẶC ĐỒ ÁN NGHIÊN CỨU]` | Tên đề tài nghiên cứu chính |
| `[HỌ VÀ TÊN GIẢNG VIÊN]` | Giảng viên hướng dẫn |
| `[HỌ VÀ TÊN SINH VIÊN]` | Họ tên sinh viên thực hiện |
| `[MÃ SINH VIÊN]` | Mã số sinh viên (VD: B23DCKD008) |
| `[LỚP SINH VIÊN]` | Lớp chuyên ngành (VD: D23CQKD02-B) |
| `[NHÓM MÔN HỌC]` | Nhóm môn học tín chỉ |
| `[NĂM]` | Năm bảo vệ / nộp bài (VD: 2026) |

---

## 3. Bản đồ Tham chiếu Kỹ thuật với Kỹ năng `/docx-official`

Mọi tài liệu và công cụ chuyên sâu của `/docx-official` đã được tích hợp sẵn tại thư mục nội bộ `references/docx-official/`:

| Nhu cầu kỹ thuật | Tài liệu / Script tham chiếu nội bộ |
| :--- | :--- |
| **Quy trình tổng quan DOCX** | `references/docx-official/SKILL.md` |
| **Thao tác chuyên sâu OOXML, thẻ XML, DOM** | `references/docx-official/ooxml.md` |
| **Soạn thảo DOCX theo JavaScript/TypeScript** | `references/docx-official/docx-js.md` |
| **Giải nén & Định dạng đẹp XML an toàn** | `references/docx-official/ooxml/scripts/unpack.py` |
| **Đóng gói lại file DOCX chuẩn nén** | `references/docx-official/ooxml/scripts/pack.py` |
| **Thư viện Python thao tác Document DOM** | `references/docx-official/scripts/document.py` |
| **Redlining (Tracked Changes) có kiểm soát** | Xem phần Redlining Workflow trong `references/docx-official/SKILL.md` |

---

## 4. Công cụ Tiện ích Nội bộ (`scripts/docx_tools.py`)

Cung cấp các hàm tự động hóa bảo vệ an toàn dữ liệu:
- `ensure_existing_docx(docx_path)`: Tự động khởi tạo từ `assets/template_ptit.docx` nếu file đích chưa tồn tại (tuyệt đối không tạo file trắng).
- `backup_docx(docx_path)`: Tự động nhân bản file cũ vào thư mục `back-up-docx/` kèm dấu thời gian `_YYYYMMDD_HHMMSS`.
- `replace_in_docx(docx_path, replacements)`: Thay thế placeholder giữ nguyên 100% định dạng phông chữ, bảng biểu và hoa văn trang bìa.
- `append_to_existing_docx(docx_path, new_content)`: Bổ sung chương/tiểu mục mới chuẩn phông Times New Roman 13pt.
