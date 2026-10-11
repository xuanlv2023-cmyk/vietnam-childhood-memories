# Skill: Vietnam Childhood Memories (Góc Quê Tuổi Thơ V10)

Hệ thống AI studio chuyên biệt sản xuất video ngắn & phim ngắn điện ảnh về **Ký Ức Tuổi Thơ Làng Quê Việt Nam** (1980s - 1990s - 2000s) theo chuẩn kênh đối thủ triệu view "Góc quê".

---

## 🌟 TÍNH NĂNG NỔI BẬT

1. **Hỗ Trợ Trọn Vẹn 2 Chế Độ Sản Xuất Độc Lập:**
   * **Chế độ 1 (Mode 1) — Video Ngắn Hoài Niệm (Shorts 9:16 có Voice-Over):** Chuẩn hóa 10.0s cố định mỗi cảnh (30s = 3 cảnh, 40s = 4 cảnh), lồng tiếng thuyết minh Nam Bộ lắng đọng, chuyển cảnh Cross-Dissolve 0.5s.
   * **Chế độ 2 (Mode 2) — Phim Ngắn Điện Ảnh (Cinematic 16:9 Không Lời Thoại):** Độ dài 1.5 - 3 phút, nhịp cảnh 5.5s - 8.5s hữu cơ, ứng dụng thủ pháp Match-Cut điện ảnh kết nối không-thời gian, thuần Foley đời thực & nhạc mộc.
2. **Khắc Phục Hoàn Toàn Vấn Đề "Mặt Búp Bê & Nhựa Sáp AI" (Anti-AI Slop):**
   * Bộ từ khóa Da Thật (`authentic weathered sun-tanned skin, visible real pores, light perspiration, mud and ash smudges`).
   * Trang phục bạc màu sờn chỉ thập niên 80-90-2000 (`sun-bleached vintage cotton, frayed hem, honeycomb sandals`).
   * Ánh sáng giờ vàng và ráng chiều hoài niệm (`Golden Hour 3800K, volumetric sunbeams, warm 35mm film grain`).
3. **Hệ Thống Tham Chiếu Token Nhất Quán:**
   * Nhân vật: `@_Char_Rural_Boy_Tam`, `[BOY_TEEN]` lớn lên thành `[MAN_ADULT]`, `[MOTHER]`, `[FATHER]`.
   * Bối cảnh & Đạo cụ: Cổng trường làng xà cừ, quán net cỏ màn CRT, đường đê tre, niêu cá kho, bát sứ trắng viền xanh.
4. **Chuẩn Prompt Hàng Loạt (Batch Copy Blocks):**
   * **Một phân cảnh = Một đoạn văn duy nhất liên tục (Single Continuous Line)**, tuyệt đối không xuống dòng nội bộ.
   * Copy-paste 1 chạm vào các tool tự động hóa render hàng loạt.
5. **Trọn Bộ 5 File Word (.docx) Không Bảng Biểu (Zero-Table Policy):**
   * 100% định dạng đoạn văn bản thuần túy, sạch sẽ, không dùng bảng biểu để tool tự động hóa đọc mượt mà không lỗi.

---

## 📁 CẤU TRÚC THƯ MỤC

```text
vietnam-childhood-memories/
├── SKILL.md                          # Bộ quy tắc cốt lõi, DNA hình ảnh & 8 giai đoạn sản xuất (2 chế độ)
├── README.md                         # Hướng dẫn tổng quan & tra cứu nhanh
├── references/                       # Tài liệu tham khảo chuyên sâu
│   ├── 01-visual-dna-cinematics.md   # Ngôn ngữ thị giác điện ảnh, ánh sáng, chất liệu người thật
│   ├── 02-character-and-setting-tokens.md # Thư viện Token tham chiếu nhân vật & bối cảnh
│   ├── 03-scriptwriting-and-emotional-hooks.md # Nghệ thuật biên kịch chạm cảm xúc 8X-9X
│   ├── 04-prompt-engineering-batch-rules.md    # Quy chuẩn viết prompt 1 đoạn văn liên tục
│   ├── 05-audio-foley-and-vo-dna.md  # Thiết kế âm thanh: Voice DNA, Foley đồng quê & BGM
│   ├── 06-assembly-ffmpeg-workflow.md# Quy trình nối video xfade 0.5s & hòa âm bằng FFmpeg
│   └── 07-cinematic-matchcuts-and-visual-storytelling.md # Nghệ thuật Match-Cut & Phim không lời thoại
├── examples/                         # Dự án mẫu thực chiến hoàn chỉnh
│   ├── chieu-nuong-bap-rom-ra/       # Benchmark Mode 1: Shorts 9:16 có Voice-Over (30s)
│   └── vong-tron-ky-uc-2000s/        # Benchmark Mode 2: Phim Ngắn Điện Ảnh 16:9 Không Lời Thoại (22 cảnh)
└── scripts/
    └── export_batch_docx.py          # Script Python tự động xuất 5 file Word sạch không table
```
