---
name: ptit-academic-writing
description: Soan thao bao cao Bai tap lon (BTL), Tieu luan, Do an chuyen nganh va Khoa luan tot nghiep theo chuan Hoc vien Cong nghe Buu chinh Vien thong (PTIT). Cau truc mo-dun phi hardcode linh hoat theo de tai. Tich hop toan dien ky nang /docx-official trong references/docx-official de thao tac DOCX. Luon luon chinh sua tren file co san (assets/template_ptit.docx hoac file cua nguoi dung), khong tao moi tu dau. Tu dong sao luu ban cu vao thu muc back-up-docx moi khi thay doi. Van phong dung tam sinh vien dai hoc thuc te, chap nhan san tu nhien, trich dan IEEE.
user-invocable: true
argument-hint: "btl | do-an | tieu-luan | edit-docx | outline"
license: MIT
metadata:
  category: "academic-writing"
  tags: "PTIT, Academic Writing, BTL, Report, Thesis, Student Level, IEEE, Word DOCX, Template Edit, Auto Backup, Non-hardcoded, docx-official"
---

# Kỹ năng Soạn thảo Báo cáo Học thuật PTIT (Tầm Sinh viên Thực tế)

Kỹ năng này chuyên sâu về lập đề cương, soạn thảo nội dung kỹ thuật, trích dẫn học thuật IEEE và định dạng/chỉnh sửa tài liệu báo cáo đúng 100% quy chuẩn của **Học viện Công nghệ Bưu chính Viễn thông (PTIT)** với cấu trúc mô-đun linh hoạt, hoàn toàn phi hardcode.

---

## 1. Bản đồ Tham chiếu (Reference Index)

| Nghiệp vụ / Nhu cầu | Nguồn tham chiếu (Nội bộ & Hệ thống) |
| :--- | :--- |
| **Kỹ thuật Thao tác DOCX Chuyên sâu** (Đọc, trích xuất text, sửa OOXML DOM, unpack/pack, redlining) | **Tích hợp trọn bộ `/docx-official` nội bộ:** `references/docx-official/SKILL.md`, `references/docx-official/ooxml.md`, `references/docx-official/docx-js.md` |
| **Quy trình Khung mẫu PTIT & Tự động sao lưu** (Khung mẫu linh hoạt `assets/template_ptit.docx`, tự động lưu `back-up-docx`) | `references/docx-template-and-backup-workflow.md` & `scripts/docx_tools.py` |
| **Cấu trúc Mô-đun Báo cáo Phi Hardcode** (BTL 3-4 chương, Tiểu luận 3 phần, Đồ án/Khóa luận 4-5 chương) | `references/report-types-structure.md` |
| **Quy chuẩn Thể thức PTIT** (Căn lề, Font 13pt, Bìa hoa văn + Logo, Quy cách Bảng/Hình) | `references/ptit-standards.md` |
| **Văn phong Sinh viên & Sạn Tự nhiên** (Cách viết chân thực, tránh văn phong AI giáo sư) | `references/anti-ai-academic-tone.md` |
| **Cẩm nang Trích dẫn Chuẩn IEEE** (Quy tắc đánh số [1], [2]... khớp nội văn) | `references/ieee-citation-guide.md` |

---

## 2. Hai Quy tắc Bất Di Bất Dịch khi Thao tác DOCX

Mọi kỹ thuật đọc, sửa đổi, phân tích file DOCX được thực hiện theo tiêu chuẩn của **`/docx-official`**, kết hợp 2 quy tắc bắt buộc của PTIT:

1. **LUÔN LUÔN CHỈNH SỬA CÁI CÓ SẴN (KHÔNG TẠO MỚI TỪ CON SỐ 0):**
   - **Đã có file báo cáo:** Thao tác trực tiếp trên file Word `.docx` của người dùng.
   - **Làm bài mới:** Bắt buộc sao chép khung mẫu linh hoạt từ `assets/template_ptit.docx` ra làm file đích rồi sửa nội dung. Tuyệt đối không tạo file trắng từ con số 0.
2. **LUÔN TỰ ĐỘNG ĐƯA BẢN CŨ VÀO THƯ MỤC `back-up-docx`:**
   - Mỗi lần có lệnh sửa văn bản, thay thế nội dung hoặc nối chương mới, hệ thống tự động nhân bản file hiện tại vào thư mục `back-up-docx/` nằm cùng cấp:
     `[thư_mục_chứa_file]/back-up-docx/[tên_file]_[YYYYMMDD_HHMMSS].docx`
   - Đảm bảo an toàn 100% cho dữ liệu của người dùng, không bao giờ bị mất bài cũ.

---

## 3. Cấu trúc Báo cáo Phi Hardcode (Dynamic Academic Modular Structure)

Cấu trúc tài liệu không bị gò bó trong một số lượng chương cố định mà thích ứng linh hoạt theo loại bài và yêu cầu của giảng viên:
- **Bài tập lớn môn học (BTL):** 3 chương (môn lập trình, ứng dụng, mạng) hoặc 4 chương (môn dữ liệu, AI, hệ thống phức hợp).
- **Tiểu luận môn học:** 3 Phần lớn (Mở đầu – Nội dung – Kết luận) hoặc các mục La Mã (I, II, III).
- **Đồ án chuyên ngành / Khóa luận tốt nghiệp:** 4 đến 5 chương, bổ sung Lời cam đoan, Phiếu giao nhiệm vụ, Nhận xét GVHD và Cán bộ phản biện.
- **Danh mục Bảng biểu & Hình vẽ:** Chỉ thêm khi bài viết có từ 2 bảng biểu hoặc 2 hình vẽ trở lên. Nếu bài viết không có bảng/hình thì không để danh mục rỗng.
- **Mục lục:** Tích hợp trường mã Word TOC tự động (`TOC \o "1-3" \h \z \u`), tự động cập nhật số trang khi người dùng thêm/bớt đề mục.

---

## 4. Các Nguyên tắc Soạn thảo Cốt lõi

### A. Thể thức & Trang in Chuẩn 100% PTIT
1. **Trang bìa chính:** Khung viền hoa văn (`assets/Khung.png`) chìm sau văn bản (`behindDoc="1"`), Logo PTIT (`assets/Logo.png`), cơ quan chủ quản `BỘ THÔNG TIN VÀ TRUYỀN THÔNG` -> `HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG`.
2. **Căn lề trang A4:** Lề trên: 2.0cm, Lề dưới: 2.0cm, Lề trái: 2.5-3.0cm (đóng gáy), Lề phải: 1.5-2.0cm.
3. **Phông chữ & Đoạn văn:** `Times New Roman` 13pt, màu thuần đen (`RGBColor(0, 0, 0)`), Before 6pt, After 6pt, giãn dòng 1.3, First Line Indent 1.0cm.
4. **Tiêu đề Bảng biểu & Hình vẽ:** Bảng đặt tiêu đề ở **TRÊN**; Hình vẽ/Sơ đồ đặt tiêu đề ở **DƯỚI**.

### B. Nội dung & Văn phong Sinh viên Thực tế (Anti-AI)
1. **Đúng tầm sinh viên:** Trình bày trực diện vào việc code, thư viện thực tế (Pandas, Streamlit, PyTorch, Express...), dữ liệu thật và các bước giải quyết lỗi.
2. **Chấp nhận sạn tự nhiên & hạn chế:** Mô tả đúng môi trường máy cá nhân Core i5/16GB RAM, tập dữ liệu vài chục nghìn dòng, thời gian xử lý thực tế.
3. **Trích dẫn IEEE đầy đủ:** Gắn mã số `[1]`, `[2]`... khớp 1-1 với danh mục tham khảo.