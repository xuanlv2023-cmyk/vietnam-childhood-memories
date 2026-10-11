# Assembly & FFmpeg Workflow (Quy Trình Dựng Phim & Nối Video Bằng FFmpeg)

Tài liệu này cung cấp các lệnh và quy trình tự động hóa ghép các phân cảnh 10.0s thành video hoàn chỉnh chất lượng điện ảnh bằng FFmpeg, đảm bảo chuyển cảnh mượt mà và hòa âm chuẩn xác.

---

## 1. QUY CHUẨN KỸ THUẬT VIDEO ĐẦU RA

* **Độ phân giải**: `1080x1920` (Chuẩn dọc 9:16 cho Shorts/TikTok/Reels) hoặc `1920x1080` (Chuẩn ngang 16:9).
* **Tốc độ khung hình (Frame Rate)**: `30 FPS` cố định (`cfr` mode, không dùng `vfr`).
* **Video Codec**: `libx264`, Pixel Format `yuv420p`, Profile `high`, Preset `slow`, CR `18` (độ sắc nét cao nhất).
* **Audio Codec**: `aac`, Sample Rate `48000 Hz`, Bitrate `192k`.

---

## 2. HIỆU ỨNG HÒA TAN CHÉO (CROSS-DISSOLVE 0.5S)

Để giữ đúng phong cách hoài niệm êm dịu của kênh đối thủ "Góc quê", giữa các phân cảnh 10.0s ta áp dụng hiệu ứng chuyển cảnh `xfade=transition=fade:duration=0.5`.

### Lệnh Nối 3 Phân Cảnh (Video 30 Giây):
Giả sử có 3 video render: `scene_01.mp4`, `scene_02.mp4`, `scene_03.mp4` (mỗi file dài 10.0 giây):

```powershell
ffmpeg -y `
  -i scene_01.mp4 -i scene_02.mp4 -i scene_03.mp4 `
  -filter_complex "`
    [0:v][1:v]xfade=transition=fade:duration=0.5:offset=9.5[v01]; `
    [v01][2:v]xfade=transition=fade:duration=0.5:offset=19.0[v_out]" `
  -map "[v_out]" -c:v libx264 -pix_fmt yuv420p -r 30 video_seamless.mp4
```

---

## 3. HÒA ÂM (AUDIO MIXING & DUCKING) VÀ XUẤT MASTER

Lệnh ghép video liền mạch cùng 3 kênh âm thanh:
1. `video_seamless.mp4`: Video hình ảnh đã nối chuyển cảnh.
2. `voice_over.mp3`: Giọng đọc thuyết minh thu âm/TTS.
3. `foley_ambience.mp3`: Tiếng lửa rơm nổ, tiếng gió đồng, tiếng ve hè.
4. `bgm_acoustic.mp3`: Nhạc nền sáo trúc/guitar nhẹ nhàng.

```powershell
ffmpeg -y `
  -i video_seamless.mp4 `
  -i voice_over.mp3 `
  -i foley_ambience.mp3 `
  -i bgm_acoustic.mp3 `
  -filter_complex "`
    [1:a]volume=1.0[vo]; `
    [2:a]volume=0.35[foley]; `
    [3:a]volume=0.25[bgm]; `
    [vo][foley][bgm]amix=inputs=3:duration=first:dropout_transition=2[a_out]" `
  -map 0:v -map "[a_out]" `
  -c:v copy -c:a aac -b:a 192k -ar 48000 `
  final_master.mp4
```

---

## 4. TẠO THUMBNAIL CHUẨN ĐIỆN ẢNH TỪ VIDEO HOÀN THIỆN

Để trích xuất khung hình đắt giá nhất làm thumbnail ở giây thứ 5.0 và gắn viền hoặc tỷ lệ nét căng:

```powershell
ffmpeg -y -ss 00:00:05.000 -i final_master.mp4 -vframes 1 -q:v 2 thumbnail_raw.jpg
```
