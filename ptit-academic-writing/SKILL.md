---
name: ptit-academic-writing
description: "Soạn thảo và chỉnh sửa báo cáo học thuật theo chuẩn Học viện Công nghệ Bưu chính Viễn thông (PTIT): bài tập lớn (BTL), tiểu luận môn học, đồ án chuyên ngành, khóa luận tốt nghiệp. Dùng khi người dùng muốn lập đề cương, viết chương, trích dẫn IEEE, hoặc tạo và sửa file Word (.docx) theo mẫu PTIT. Từ khóa: BTL, bài tập lớn, tiểu luận, đồ án, khóa luận, luận văn, báo cáo PTIT, đề cương, tài liệu tham khảo, trích dẫn IEEE, sửa file Word. Soan thao bao cao BTL, tieu luan, do an, khoa luan PTIT, trich dan IEEE, sua file docx. Luôn chỉnh sửa trên file có sẵn, không tạo từ con số 0. Văn phong sinh viên thực tế, không bịa số liệu."
user-invocable: true
argument-hint: "btl | do-an | tieu-luan | edit-docx | outline"
license: MIT
metadata:
  category: "academic-writing"
  tags: "PTIT, Academic Writing, BTL, Report, Thesis, Student Level, IEEE, Word DOCX, Template Edit, Auto Backup, docx-official"
---

# Kỹ năng Soạn thảo Báo cáo Học thuật PTIT

Hỗ trợ lập đề cương, soạn nội dung, trích dẫn IEEE và chỉnh sửa báo cáo theo quy chuẩn của **Học viện Công nghệ Bưu chính Viễn thông (PTIT)**.

---

## 1. Bản đồ tham chiếu

| Nhu cầu | Nguồn |
| :--- | :--- |
| Thể thức trang, font, bảng, hình, bìa | `references/ptit-standards.md` (nguồn duy nhất cho thông số) |
| Cấu trúc từng loại báo cáo | `references/report-types-structure.md` |
| Khung mẫu, placeholder, công cụ Python | `references/docx-template-and-backup-workflow.md` |
| Văn phong sinh viên thực tế | `references/anti-ai-academic-tone.md` |
| Trích dẫn IEEE | `references/ieee-citation-guide.md` |
| Thao tác DOCX chuyên sâu (OOXML, redlining) | `references/docx-official/` (không sửa) |

---

## 2. Chọn khung mẫu theo loại báo cáo

| Loại | Đối số | File khung mẫu | Nội dung chính |
| :--- | :--- | :--- | :--- |
| Bài tập lớn | `btl` | `assets/template_btl.docx` | 3 chương; có Lời cảm ơn, Danh mục viết tắt, Mục lục |
| Đồ án chuyên ngành / Khóa luận | `do-an` | `assets/template_do_an.docx` | 4 chương; có Phiếu giao nhiệm vụ, Lời cam đoan, Nhận xét GVHD và phản biện, Tóm tắt VN/EN, danh mục bảng và hình, Phụ lục |
| Tiểu luận môn học | `tieu-luan` | `assets/template_tieu_luan.docx` | 3 phần lớn, không chia chương |
| Sửa file có sẵn | `edit-docx` | file của người dùng | Không viết lại toàn bộ |
| Chỉ lập đề cương | `outline` | không tạo file | Trả về đề cương trong khung chat |

Nếu không có đối số, suy ra từ yêu cầu. Nếu vẫn chưa rõ, hỏi một lần.

Khi bài làm mới, tạo file từ khung mẫu đúng loại:

```bash
python scripts/docx_tools.py init btl bao_cao.docx
```

Không tạo file trắng từ đầu.

---

## 3. Quy trình làm việc

1. **Thu thập thông tin trước khi viết.** Cần: loại báo cáo, học phần, tên đề tài, số chương (với BTL), tên giảng viên hướng dẫn, họ tên sinh viên, mã sinh viên, lớp, nhóm môn học, năm. Hỏi gộp một lần.
2. **Xác định file đích.**
   - Đã có file của người dùng: sửa trực tiếp file đó, sau khi sao lưu.
   - Làm bài mới: `init` từ khung mẫu đúng loại.
3. **Điền bìa và thông tin chung** bằng `replace`.
4. **Viết nội dung** bằng `append` (có `--before` để chèn trước một tiêu đề có sẵn, ví dụ "KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN"). Tiêu đề phải dùng style Heading để mục lục nhận diện.
5. **Kiểm tra trước khi giao** bằng `check` và đối chiếu thủ công:
   - Không còn placeholder ngoài những mục người dùng cần tự điền (liệt kê rõ cho họ).
   - Mọi `[n]` trong văn có trong danh mục tài liệu tham khảo, đánh số theo thứ tự xuất hiện.
   - Bảng `Bảng x.y` có tiêu đề phía trên; hình `Hình x.y` có tiêu đề phía dưới.
   - Mục lục đã cập nhật (xem mục 5).

---

## 4. Quy tắc bất di bất dịch khi thao tác DOCX

1. **Luôn chỉnh sửa trên file có sẵn.** Không tạo file trắng.
2. **Luôn sao lưu bản cũ** vào `back-up-docx/` cùng cấp trước mỗi lần ghi. Tên file: `[tên]_[YYYYMMDD_HHMMSS].docx`, thêm `_2`, `_3` nếu trùng giây.

---

## 5. Mục lục

Mục lục là trường Word TOC, lấy các tiêu đề có style Heading 1-3. Các khung mẫu đã gắn style Heading và đã đo sẵn số trang, nên người dùng có thể mở Word và nhấn **Ctrl+A rồi F9**, chọn "Update entire table", để cập nhật sau khi thêm hoặc bớt mục.

Nếu tiêu đề được viết mới bằng cách gõ tay (không dùng style Heading), nó sẽ không xuất hiện trong mục lục. Lệnh `check` sẽ báo lỗi này.

---

## 6. Số liệu và liêm chính học thuật

1. **Chỉ dùng số liệu thật của người dùng.** Số trong các ví dụ của `references/` chỉ là minh họa cách viết.
2. **Thiếu số liệu thì dùng placeholder** như `[KẾT QUẢ ĐO]` và hỏi người dùng. Không tự điền số cho đẹp.
3. **Không bịa nguồn.** Chỉ trích dẫn tài liệu người dùng cung cấp hoặc đã kiểm chứng. Không tự tạo tác giả, DOI, đường dẫn hay ngày truy cập.
4. **Nhắc người dùng kiểm tra quy định của khoa và giảng viên** về việc dùng công cụ AI trong bài làm.

---

## 7. Công cụ (`scripts/docx_tools.py`)

Cài phụ thuộc một lần: `pip install python-docx --break-system-packages`.

```bash
python scripts/docx_tools.py init     btl bao_cao.docx                       # tạo từ khung mẫu
python scripts/docx_tools.py replace  bao_cao.docx thay_the.json             # thay placeholder, giữ định dạng
python scripts/docx_tools.py append   bao_cao.docx noi_dung.json --before "KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN"
python scripts/docx_tools.py check    bao_cao.docx                           # kiểm tra cấu trúc
python scripts/docx_tools.py backup   bao_cao.docx                           # sao lưu thủ công
python scripts/docx_tools.py unpack   bao_cao.docx thu_muc_xml               # ủy quyền docx-official
python scripts/docx_tools.py pack     thu_muc_xml bao_cao_moi.docx
```

Định dạng JSON:

- `thay_the.json`: `{"[HỌ VÀ TÊN SINH VIÊN]": "Tạ Hoài Bình", "[NĂM]": "2026"}`
- `noi_dung.json`: `[{"heading": 1, "text": "CHƯƠNG 4: ..."}, {"heading": 2, "text": "4.1 ..."}, {"text": "Đoạn nội dung..."}]`

Khi thay placeholder nằm trên nhiều run, phần thay thế nhận định dạng của run đầu tiên chứa chuỗi cũ.

---

## 8. Dựng lại khung mẫu

Khung mẫu được dựng từ `scripts/build_templates.py` (đặc tả nội dung, bìa lấy từ `assets/src/base_cover.docx`). Script đo số trang thật bằng LibreOffice để điền mục lục. Chạy lại khi cần đổi cấu trúc chung: `python scripts/build_templates.py`. Cần LibreOffice và `pdftotext`.
