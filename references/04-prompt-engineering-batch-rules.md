# Prompt Engineering & Batch Rules (Quy Chuẩn Viết Prompt Hàng Loạt)

Tài liệu này quy định cấu trúc kỹ thuật của prompt để đảm bảo chất lượng hình ảnh/video đạt chuẩn điện ảnh và tương thích 100% với các công cụ tạo ảnh, video, âm thanh hàng loạt (Batch Tools).

---

## 1. NGUYÊN TẮC VÀNG CHO KHỐI BATCH COPY

### Quy Tắc 1: Một Phân Cảnh = Một Đoạn Văn Duy Nhất Liên Tục (Single Continuous Paragraph)
* Trong khối dành cho tool hàng loạt, nội dung prompt của mỗi phân cảnh phải là **MỘT ĐOẠN VĂN LIÊN TỤC TRÊN MỘT DÒNG**.
* **TUYỆT ĐỐI KHÔNG**:
  * Không thêm bất kỳ tiền tố nào như `"Phân cảnh 1:"`, `"Phân cảnh 2:"`, `"Scene 1:"` hay tiêu đề con vào khối batch copy.
  * Không nhấn Enter xuống dòng giữa chừng trong prompt của một cảnh.
  * Không dùng bullet point (`-`, `*`) ngắt dòng trong nội dung prompt.
  * Không chèn ký tự lạ hay thẻ XML làm gián đoạn dòng văn bản.
* **Mục đích**: Các tool tự động hóa đọc danh sách prompt dựa vào dấu ngắt dòng `\n`. Nếu có tiền tố thừa, tool sẽ render chữ thừa đó vào ảnh/video, hoặc nếu một prompt bị xuống dòng nội bộ, tool sẽ hiểu lầm là có 2 hoặc nhiều prompt khác nhau, gây lỗi render toàn bộ hệ thống.

### Quy Tắc 2: Xuống Dòng Phân Tách Giữa Các Phân Cảnh
* Giữa các phân cảnh khác nhau (Cảnh 1, Cảnh 2, Cảnh 3), xuống dòng bằng 1 lần Enter (tạo khoảng cách 1 dòng trống).
* Định dạng chuẩn:
  ```text
  [Toàn bộ nội dung prompt của cảnh 1 là một đoạn văn liên tục không xuống dòng]

  [Toàn bộ nội dung prompt của cảnh 2 là một đoạn văn liên tục không xuống dòng]

  [Toàn bộ nội dung prompt của cảnh 3 là một đoạn văn liên tục không xuống dòng]
  ```

---

## 2. CẤU TRÚC PROMPT ẢNH ĐIỆN ẢNH (IMAGE PROMPT BLUEPRINT)

Một câu prompt ảnh hoàn chỉnh phải gom đủ 6 thành phần sau thành 1 đoạn văn liên tục:
1. **Chủ thể & Token**: Định danh nhân vật bằng Token (`@_Char_...`) kèm độ tuổi, biểu cảm chân thực.
2. **Hành động vi mô**: Chi tiết động tác đang thực hiện (thổi lửa, bẻ bắp, trèo rào, lội bùn).
3. **Bối cảnh & Token**: Không gian đồng quê bằng Token (`@_Location_...`).
4. **Chất liệu & Độ thật (Anti-AI Engine)**: `authentic weathered sun-tanned skin, visible natural skin pores, sweat beads, dry mud smudges on cheeks, frayed vintage cotton clothing`.
5. **Ánh sáng & Màu sắc**: `warm golden hour sunset 3800K, low-angle volumetric sunlight, rising aromatic white smoke, nostalgic 35mm Kodak film color palette`.
6. **Thông số máy ảnh**: `Cinematic medium wide shot, shot on 35mm vintage anamorphic lens, f/2.2, soft natural bokeh, subtle film grain, masterpiece realism, 8k resolution --ar 9:16 --v 6.1`.

---

## 3. CẤU TRÚC PROMPT VIDEO 10S (VIDEO PROMPT BLUEPRINT)

Prompt video 10s cho các mô hình AI Video Engine (Kling AI, Google Veo 3.1, Hailuo, Runway Gen-3) gồm đủ 5 lớp chuyển động gom trong 1 đoạn văn liên tục:
1. **Trạng thái khởi đầu (Initial State)**: Mô tả ngắn gọn khớp với Keyframe đầu vào.
2. **Chuyển động Camera (Camera Movement)**: `Slow subtle horizontal camera pan left-to-right at eye-level, maintaining stable framing with organic handheld breathing motion`.
3. **Diễn xuất nhân vật 10 giây (Micro-Acting Progression)**:
   * [0s - 3s]: Hành động chuẩn bị, ánh mắt tập trung nhìn vào đối tượng.
   * [3s - 7s]: Hành vi cao trào (thổi phì phò vào than hồng, khói bay cay mắt, nheo mắt cười toe toét).
   * [7s - 10s]: Quay sang bạn bên cạnh chia sẻ nụ cười hạnh phúc, ngực phập phồng nhịp thở tự nhiên.
4. **Vật lý môi trường (Environmental Physics)**: `Thin curls of white smoke drifting gently in the evening breeze, golden rice stalks swaying softly in background, gentle heat haze shimmering above glowing red embers`.
5. **Chất lượng điện ảnh & Giữ vững nhân dạng**: `Strict character consistency, continuous authentic sun-tanned skin texture, natural 24fps motion blur, zero morphed artifacts, cinematic nostalgic atmosphere`.

---

## 4. QUY CHUẨN PROMPT VOICE-OVER & SOUND FOLEY

* **Voice-over**: Bản text tiếng Việt sạch 100%, không để ký hiệu âm nhạc `♪` hay ghi chú `[Tiếng cười]` trong câu thoại đọc.
* **Sound Foley**: Liệt kê chi tiết âm thanh tự nhiên tương ứng để sound designer hoặc AI SFX generator tạo âm thanh chân thực nhất:
  * Foley: Tiếng củi nổ lách tách, tiếng lá rơm xào xạc, tiếng gió thổi rặng tre rì rào, tiếng ếch nhái râm ran lúc chạng vạng.
  * BGM: Tiếng sáo trúc quê hương nhẹ nhàng, đàn tranh hoặc guitar mộc acoustic sâu lắng, du dương.
