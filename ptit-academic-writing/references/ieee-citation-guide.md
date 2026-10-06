# Hướng dẫn Chuẩn Trích dẫn Học thuật IEEE (IEEE Citation Guide)

Quy định chuẩn mực về trích dẫn tài liệu tham khảo theo định dạng IEEE bắt buộc áp dụng trong toàn bộ các báo cáo học thuật, đồ án và khóa luận tại PTIT.

---

## 1. Nguyên tắc Trích dẫn Nội văn (In-text Citations)

1. **Đánh số thứ tự tăng dần theo thứ tự xuất hiện trong văn bản:**
   - Nguồn tham khảo đầu tiên xuất hiện trong báo cáo được gán nhãn `[1]`, nguồn tiếp theo được gán nhãn `[2]`, `[3]`...
   - **Tuyệt đối không xếp danh mục cuối bài theo bảng chữ cái A-Z** (khác với chuẩn APA hay Harvard). Thứ tự trong danh mục Tài liệu tham khảo phải khớp hoàn toàn 1-1 với thứ tự `[1]`, `[2]`, `[3]`... trong thân bài.
2. **Quy tắc trích dẫn bắt buộc:**
   - Mọi khái niệm lý thuyết, thuật toán, công thức toán học, tập dữ liệu hoặc kết quả nghiên cứu kế thừa từ bên ngoài **bắt buộc phải gắn mã trích dẫn** ngay tại mệnh đề hoặc câu văn tương ứng.
   - Vị trí đặt mã: Đặt trước dấu chấm câu hoặc ngay sau tên tác giả/thuật toán được nhắc tới.
     - *Đúng:* "...theo kiến trúc mạng nơ-ron Transformer được Vaswani và các cộng sự đề xuất [1]."
     - *Đúng:* "...sử dụng định dạng lưu trữ cột nén Snappy để giảm thiểu dung lượng đĩa [2], [3]."
     - *Trích dẫn nhiều nguồn liên tiếp:* `[1]–[3]` hoặc `[1], [4], [7]`.

---

## 2. Quy chuẩn Định dạng Danh mục Tài liệu Tham khảo (Reference List)

### 1. Bài báo Tạp chí Khoa học (Journal Article)
- **Cấu trúc:** `[STT] Tên_Tác_Giả, "Tên bài báo," *Tên tạp chí in nghiêng*, vol. X, no. Y, pp. trang_đầu-trang_cuối, Tháng Năm.`
- **Ví dụ:**
  `[1] M. Zaharia et al., "Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing," *IEEE Transactions on Parallel and Distributed Systems*, vol. 24, no. 6, pp. 1100–1112, Jun. 2013.`

### 2. Kỷ yếu Hội thảo Khoa học (Conference Proceedings)
- **Cấu trúc:** `[STT] Tên_Tác_Giả, "Tên bài báo," in *Tên kỷ yếu hội thảo*, Địa điểm tổ chức, Năm, pp. trang_đầu-trang_cuối.`
- **Ví dụ:**
  `[2] A. Vaswani et al., "Attention is All you Need," in *Advances in Neural Information Processing Systems (NeurIPS 2017)*, Long Beach, CA, USA, 2017, pp. 5998–6008.`

### 3. Sách Chuyên khảo / Giáo trình (Book)
- **Cấu trúc:** `[STT] Tên_Tác_Giả, *Tên sách in nghiêng*, lần tái bản (nếu có). Nơi xuất bản: Nhà xuất bản, Năm.`
- **Ví dụ:**
  `[3] M. Kleppmann, *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems*, 1st ed. Sebastopol, CA: O'Reilly Media, 2017.`

### 4. Tài liệu Kỹ thuật Trực tuyến / Whitepaper / Documentation
- **Cấu trúc:** `[STT] Tên_Tổ_chức/Tác_giả, "Tên tài liệu kỹ thuật," Tên nền tảng/Website, Năm phát hành. [Online]. Available: URL. (Truy cập: Ngày Tháng Năm).`
- **Ví dụ:**
  `[4] Apache Software Foundation, "Apache Parquet Documentation," Apache Parquet, 2025. [Online]. Available: https://parquet.apache.org/docs/. (Truy cập: 15/02/2026).`

### 5. Báo cáo Nghiên cứu / Bản thảo lưu trữ (Preprint / arXiv)
- **Cấu trúc:** `[STT] Tên_Tác_Giả, "Tên báo cáo," arXiv preprint arXiv:XXXX.XXXXX, Năm.`
- **Ví dụ:**
  `[5] J. Devlin, M. W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding," arXiv:1810.04805, 2018.`

---

## 3. Các Lỗi Sai Nghiêm Trọng Cần Tuyệt Đối Tránh

1. ❌ **Đưa danh sách môn học đã học vào tài liệu tham khảo:** Ví dụ: "1. Môn Học Máy, 2. Môn Cơ sở dữ liệu". (Đây là lỗi sai học thuật nghiêm trọng, bị trừ điểm trực tiếp).
2. ❌ **Liệt kê nguồn ở mục cuối bài nhưng không có mã `[x]` tương ứng trong thân bài.** (Mọi nguồn đều phải được in-text citation).
3. ❌ **Chỉ dán mỗi đường link URL thô:** Ví dụ: `[1] https://wikipedia.org/wiki/Python`. Bắt buộc phải có tên tác giả/tổ chức, tên tài liệu, năm và ngày truy cập.
4. ❌ **Trích dẫn nguồn không đáng tin cậy:** Tránh trích dẫn các blog cá nhân không rõ tác giả, bài viết diễn đàn hỏi đáp (trừ trường hợp trích dẫn tài liệu chính thức từ GitHub repository hoặc trang chủ công nghệ).
