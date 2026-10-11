---
name: "vietnam-childhood-memories"
description: "AI studio sản xuất video Ký Ức Tuổi Thơ Nông Thôn Việt Nam (Góc Quê Xưa) 100% người thật điện ảnh hoài niệm (1980s-1990s-2000s). Hỗ trợ trọn vẹn 2 chế độ: Video Ngắn Hoài Niệm (Shorts 9:16 có Voice-over Nam Bộ 10s/cảnh) và Phim Ngắn Điện Ảnh (Cinematic 16:9 Không Lời Thoại thuần Foley & Match-Cut). Hệ thống Token tham chiếu nhất quán, chống AI nhựa sáp, prompt 1 đoạn văn liên tục cho tool chạy hàng loạt, và tự động xuất 5 file Word (.docx) sạch không bảng."
---

# Vietnam Childhood Memories Pipeline (Góc Quê Tuổi Thơ V10)

**Tác giả:** Xuanlv  
**Đặc trưng:** 100% Người Thật Điện Ảnh Hoài Niệm (1980s - 1990s - 2000s) • Da rám nắng chân thật • Bối cảnh làng quê mộc mạc • 2 Chế độ độc lập (Shorts 9:16 có Voice & Phim Ngắn 16:9 Không Lời Thoại) • Thủ pháp Match-Cut điện ảnh • Không búp bê/nhựa sáp AI • Prompt 1 đoạn văn liên tục cho Tool chạy hàng loạt • Trọn bộ 5 file Word (.docx) Zero-Table.

---

## 1. NGUYÊN TẮC CỐT LÕI HỆ THỐNG V10

### 1.1. Hai Chế Độ Sản Xuất Độc Lập (Dual Operating Modes)

Hệ thống hỗ trợ 2 phong cách sản xuất linh hoạt theo nhu cầu phân phối:

- **CHẾ ĐỘ 1: VIDEO NGẮN HOÀI NIỆM (Nostalgic Voice Shorts 9:16 — 30s đến 50s):**
  - **Mục tiêu:** Kéo traffic viral, subscribers trên YouTube Shorts, TikTok, Facebook Reels.
  - **Quy chuẩn thời lượng:** Chuẩn hóa **10.0 giây cố định cho mỗi phân cảnh** (30s = 3 cảnh, 40s = 4 cảnh, 50s = 5 cảnh).
  - **Âm thanh:** Thuyết minh Voice-over hoài niệm lắng đọng, khóa cứng **100% Giọng Miền Nam / Nam Bộ** (22 - 26 từ/cảnh).
  - **Dựng phim:** Ghép nối bằng chuyển cảnh hòa tan chéo **Cross-Dissolve 0.5s** êm ái.

- **CHẾ ĐỘ 2: PHIM NGẮN ĐIỆN ẢNH (Cinematic Visual Poem 16:9 — 1.5 đến 3 phút):**
  - **Mục tiêu:** Video ngang YouTube chuẩn 4K, giữ chân khán giả trung thành, trải nghiệm điện ảnh sâu sắc.
  - **Phong cách kể chuyện:** Thuần thị giác (**Show, Don't Tell**) — **100% KHÔNG LỜI THOẠI, KHÔNG VOICE-OVER**.
  - **Nhịp cảnh điện ảnh hữu cơ:** Thời lượng cảnh biến thiên tự nhiên **5.5s - 8.5s/cảnh** theo nhịp thở cảm xúc (hành động nhanh 5.5-6.5s, tĩnh lặng 7.0-9.0s).
  - **Thủ pháp dựng:** Ứng dụng **Bộ từ điển Match-Cut điện ảnh** ([`references/07-cinematic-matchcuts-and-visual-storytelling.md`](references/07-cinematic-matchcuts-and-visual-storytelling.md)) kết nối không - thời gian (Áo học sinh $\to$ Áo người lớn; Chiếc bát sứ ở phố $\to$ Chiếc bát sứ ở quê; Vòng tròn ký ức qua khung cửa).
  - **Âm thanh:** Lớp Foley đời thực mộc mạc (tiếng ve, tiếng xích líp xe đạp, tiếng bát đũa, tiếng niêu cá) hòa cùng độc tấu Piano & Guitar mộc.

---

### 1.2. Hệ Thống Token Tham Chiếu Nhất Quán (@_Char_ & @_Location_)
* **Triệt tiêu hoàn toàn hiện tượng "mặt búp bê AI, da sáp bóng nhẫy, nhân vật biến đổi qua từng cảnh"**:
  * Mỗi nhân vật được gán một Token nhận dạng cố định (ví dụ: `@_Char_Rural_Boy_Tam`, `@_Char_Mother_Ba`, `@_Char_Father_Sau`, hoặc `[BOY_TEEN]` lớn lên thành `[MAN_ADULT]`).
  * Mỗi bối cảnh được gán một Token cố định (ví dụ: `@_Location_School_Gate_2000s`, `@_Location_Internet_Cafe_CRT`, `@_Location_Straw_Paddy_Field`).
* **Quy chuẩn chất liệu người thật 100% (Anti-AI Slop)**:
  * Da rám nắng bánh mật có lỗ chân lông thật (`authentic weathered sun-tanned skin texture, real visible pores`).
  * Vết lấm lem bùn đất, mồ hôi nhễ nhại tự nhiên (`smudges of dried mud and dust on cheeks and forearms`).
  * Quần áo vải thô bạc màu sờn chỉ, áo thun 3 lỗ chắp vá, dép tổ ong mòn gót hoặc chân trần.
  * Cấm filter làm mịn da, cấm phong cách hoạt hình 3D CGI hoạt họa Disney/Pixar.

---

### 1.3. Quy Chuẩn Prompt Hàng Loạt (Batch Copy Blocks)
* **Quy tắc Vàng**: Mỗi phân cảnh là **MỘT ĐOẠN VĂN DUY NHẤT LIÊN TỤC (Single Continuous Paragraph)**.
* **CẤM TUYỆT ĐỐI**: Không xuống dòng hay dùng gạch đầu dòng giữa chừng trong prompt của một phân cảnh.
* **Mục đích**: Người dùng có thể copy nguyên khối prompt dán thẳng vào các Tool tự động hóa (Automation Tools) mà tool nhận diện trọn vẹn mỗi dòng là 1 prompt của 1 cảnh.
* Phân tách giữa các cảnh: **Xuống dòng 1 lần**.

---

### 1.4. Hệ Thống Xuất Bản 5 File Word (.docx) Thuần Văn Bản (Zero Table Export)
* Toàn bộ 5 file Word kết xuất được format dạng văn bản thuần có tiêu đề trang nhã, **100% KHÔNG DÙNG BẢNG BIỂU (NO TABLES)**:
  1. `00_HO_SO_THAM_CHIEU_GOC.docx`: Sheet tạo ảnh nhân vật 4 góc nhìn & bối cảnh chuẩn.
  2. `01_PROMPTS_ANH_HANG_LOAT.docx`: Prompts tạo ảnh độc lập từng cảnh (1 đoạn văn/cảnh).
  3. `02_PROMPTS_VIDEO_HANG_LOAT.docx`: Prompts tạo video chuẩn điện ảnh (1 đoạn văn/cảnh).
  4. `03_PROMPTS_VOICE_HANG_LOAT.docx`: Lời bình voice-over sạch (nếu Chế độ 1) hoặc Ghi chú Audio Foley & Timeline (nếu Chế độ 2).
  5. `04_METADATA_SEO.docx`: Prompt Thumbnail, Tiêu đề A/B test, Caption & Hashtag.

---

## 2. WORKFLOW 8 GIAI ĐOẠN CHUẨN HÓA

### Giai đoạn 0 — Thu Thập Yêu Cầu Đầu Vào & Chọn Chế Độ
1. **Chế độ sản xuất mong muốn**:
   - **Chế độ 1:** Video Ngắn Hoài Niệm (Shorts 9:16 có Voice-over Nam Bộ, 3-5 cảnh x 10.0s).
   - **Chế độ 2:** Phim Ngắn Điện Ảnh (Cinematic 16:9 Không Lời Thoại, nhịp 6-8s, thuần Foley & Match-Cut).
2. **Khung thời gian & Bối cảnh**: Làng quê Bắc Bộ, Trung Bộ hay Nam Bộ? Thập niên 1980s, 1990s hay đầu 2000s?
3. **Phương thức sản xuất**: Sáng tạo kịch bản mới hay Clone bóc tách từ video đối thủ?

### Giai đoạn 1 — Định Danh Token Nhân Vật & Bối Cảnh
* Tra cứu và khởi tạo Token theo [`references/02-character-and-setting-tokens.md`](references/02-character-and-setting-tokens.md).
* Tạo Model Sheet tham chiếu 4 góc nhìn cho nhân vật chính và ảnh toàn cảnh bối cảnh.

### Giai đoạn 2 — Biên Kịch Cảm Xúc & Phân Rã Kịch Bản
* **Nếu Chế độ 1:** Áp dụng công thức 3-4 cảnh chuẩn 10.0s kèm lời bình voice 22-26 từ ([`references/03-scriptwriting-and-emotional-hooks.md`](references/03-scriptwriting-and-emotional-hooks.md)).
* **Nếu Chế độ 2:** Áp dụng nghệ thuật kể chuyện thuần thị giác và từ điển Match-Cut ([`references/07-cinematic-matchcuts-and-visual-storytelling.md`](references/07-cinematic-matchcuts-and-visual-storytelling.md)).

### Giai đoạn 3 — Viết Mega Prompts Chuẩn 1 Đoạn Văn Liên Tục
* Soạn thảo chi tiết theo [`references/04-prompt-engineering-batch-rules.md`](references/04-prompt-engineering-batch-rules.md).
* Mỗi phân cảnh là 1 đoạn văn liên tục không ngắt dòng.

### Giai đoạn 4 — Tạo Ảnh Keyframe Khởi Đầu & Tham Chiếu Nhất Quán
* Nạp Prompt ảnh Keyframe vào Midjourney v6 / Flux.1 Schnell/Dev để khóa diện mạo và ánh sáng.

### Giai đoạn 5 — Tạo Video Bằng AI Video Engine
* Nạp Keyframe làm First Frame trên Kling AI / Hailuo / Veo 3.1 / Runway Gen-3.
* Chuyển động máy quay mượt mà theo đúng đặc tả: dolly in/out, tracking ngang, pan chậm.

### Giai đoạn 6 — Sản Xuất Âm Thanh & Âm Nhạc
* **Chế độ 1:** Thu âm Voice thuyết minh Nam Bộ trầm ấm hoài niệm (`@Voice_Viet_Nostalgic_Narrator`) + Foley nền nhẹ ([`references/05-audio-foley-and-vo-dna.md`](references/05-audio-foley-and-vo-dna.md)).
* **Chế độ 2:** Mix Foley đời thực đa tầng (tiếng xích xe, ve sầu, tiếng bát đũa, quạt máy) + Nhạc nền Piano/Guitar mộc mạc, không lời thoại.

### Giai đoạn 7 — Dựng Phim & Nối Video Bằng FFmpeg
* Nối các clip mượt mà bằng Cross-Dissolve hoặc Match-Cut chính xác, xuất video Master chuẩn ([`references/06-assembly-ffmpeg-workflow.md`](references/06-assembly-ffmpeg-workflow.md)).

### Giai đoạn 8 — Kết Xuất Trọn Bộ 5 File Word Hàng Loạt
* Chạy script `scripts/export_batch_docx.py` để tạo thư mục `export_batch/` sẵn sàng nạp tool.

---

## 3. OUTPUT CONTRACT (SẢN PHẨM BẮT BUỘC)

Mỗi dự án hoàn thành bắt buộc phải chứa đầy đủ 6 hạng mục trong thư mục `examples/<ten-du-an>/`:
1. `STORY.md`: Kịch bản tổng, phân tích nhịp cảm xúc, ghi rõ Chế độ 1 hay Chế độ 2.
2. `CHARACTER_SHEETS.md`: Khai báo chi tiết các token `@_Char_...` và `@_Location_...`.
3. `FLOW.md`: Sơ đồ dòng chảy cảm xúc, các điểm chuyển cảnh hoặc match-cut.
4. `MEGA_PROMPTS.md`: Toàn bộ prompts phân cảnh kèm khối Batch Copy Blocks 1 đoạn văn liên tục.
5. `VO_SCRIPT.md`: Lời bình voice-over (Chế độ 1) hoặc Bảng phân rã Foley & Music Timeline (Chế độ 2).
6. `METADATA_SEO.md`: Prompt Thumbnail, Tiêu đề A/B test, Caption và Hashtag 3 tầng.
7. `export_batch/`: Trọn bộ 5 file Word (.docx) sạch 100% không dùng bảng biểu.
