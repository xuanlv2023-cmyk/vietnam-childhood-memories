#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script tự động kết xuất trọn bộ 5 File Word (.docx) chuyên dụng cho sản xuất hàng loạt (Batch Production):
1. 00_HO_SO_THAM_CHIEU_GOC.docx
2. 01_PROMPTS_ANH_HANG_LOAT.docx
3. 02_PROMPTS_VIDEO_HANG_LOAT.docx
4. 03_PROMPTS_VOICE_HANG_LOAT.docx
5. 04_METADATA_SEO.docx

Quy chuẩn hệ thống V10:
- 100% văn bản thuần túy (Plain Text Paragraphs), TUYỆT ĐỐI KHÔNG DÙNG TABLE/BẢNG BIỂU.
- Chuẩn Thẻ Phân Rã (Tagged Blocks) chuẩn hóa: [SPECIFICATION], [CAMERA CONTROL], [CHARACTER ANCHOR], [DYNAMIC ENVIRONMENT], [INITIAL STATE], [MICRO-ACTING TIMELINE], [AUDIO BGM & FOLEY], [FINAL STATE], [NEGATIVE CONSTRAINTS].
- Mỗi phân cảnh là MỘT ĐOẠN VĂN DUY NHẤT LIÊN TỤC (Single Continuous Line), không ngắt dòng giữa chừng.
- Phân cách giữa các cảnh bằng 1 lần xuống dòng, cực kỳ thuận tiện cho copy-paste vào các Tool chạy hàng loạt.
"""

import os
import sys

# Đảm bảo UTF-8 trên Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

try:
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
except ImportError:
    print("Thư viện 'python-docx' chưa được cài đặt. Hãy chạy: pip install python-docx")
    sys.exit(1)

def add_styled_title(doc, title_text, subtitle_text, note_text=None):
    """Thêm tiêu đề chuẩn trang nhã cho file Word"""
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_title = p_title.add_run(title_text)
    run_title.font.name = 'Segoe UI'
    run_title.font.size = Pt(17)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(139, 69, 19) # Rustic warm brown
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_sub = p_sub.add_run(subtitle_text)
    run_sub.font.name = 'Segoe UI'
    run_sub.font.size = Pt(10)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(113, 128, 150) # Slate gray

    if note_text:
        p_sub.paragraph_format.space_after = Pt(4)
        p_note = doc.add_paragraph()
        p_note.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run_note = p_note.add_run(note_text)
        run_note.font.name = 'Segoe UI'
        run_note.font.size = Pt(9.5)
        run_note.font.color.rgb = RGBColor(194, 65, 12) # Rust orange accent
        p_note.paragraph_format.space_after = Pt(16)
    else:
        p_sub.paragraph_format.space_after = Pt(14)

def add_prompt_paragraph(doc, text_content, label=None, font_name='Consolas', font_size=9.5, is_bold=False):
    """Thêm đoạn văn prompt thuần túy (hoàn toàn không dùng table), có nhãn nhẹ bên trên"""
    if label:
        p_label = doc.add_paragraph()
        run_lbl = p_label.add_run(label)
        run_lbl.font.name = 'Segoe UI'
        run_lbl.font.size = Pt(10.5)
        run_lbl.font.bold = True
        run_lbl.font.color.rgb = RGBColor(139, 69, 19) # Rustic brown
        p_label.paragraph_format.space_before = Pt(8)
        p_label.paragraph_format.space_after = Pt(2)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(14)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text_content)
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = is_bold
    run.font.color.rgb = RGBColor(33, 37, 41)

def safe_save_doc(doc, filepath):
    """Lưu file Word an toàn, xử lý tình huống file đang mở trên máy người dùng"""
    try:
        doc.save(filepath)
        print(f" -> Đã xuất: {os.path.basename(filepath)}")
    except PermissionError:
        base, ext = os.path.splitext(filepath)
        fallback = f"{base}_updated{ext}"
        try:
            doc.save(fallback)
            print(f" ⚠️ File {os.path.basename(filepath)} đang được mở trong Word! Đã lưu bản mới nhất vào: {os.path.basename(fallback)}")
        except Exception as e:
            print(f" ❌ Không thể lưu file {os.path.basename(filepath)}: {e}")
    except Exception as e:
        print(f" ❌ Lỗi lưu file {os.path.basename(filepath)}: {e}")

# DỮ LIỆU DỰ ÁN MẪU: CHIỀU NƯỚNG BẮP RƠM RẠ
PROJECT_DATA = {
    "project_name": "Chiều Nướng Bắp Rơm Rạ Bên Bờ Ruộng",
    "lead_char": "Cậu bé Tâm @_Char_Rural_Boy_Tam (9 tuổi, da rám nắng bánh mật, lấm lem tro trấu, áo cộc bạc màu)",
    "support_char": "Bé Mai @_Char_Rural_Girl_Mai (8 tuổi, tóc thắt bím hai bên, áo hoa nhí bạc màu)",
    "environment": "Cánh đồng lúa sau mùa gặt và đống rơm rạ chiều hoàng hôn @_Location_Straw_Paddy_Field",
    "scenes": [
        {
            "id": "Scene 01 [00:00 - 00:10]",
            "image_prompt": "Cinematic medium wide shot, two 9-year-old Vietnamese rural children @_Char_Rural_Boy_Tam and @_Char_Rural_Girl_Mai squatting together beside a rustic straw haystack on harvested golden rice paddy field @_Location_Straw_Paddy_Field during warm sunset golden hour, Tâm carefully blowing air into dry straw to light a small campfire with glowing embers, authentic sun-tanned weathered skin with natural visible pores, light dried mud and ash smudges on cheeks, wearing faded 1990s vintage frayed cotton tank tops and dark shorts, barefoot on dry soil, curls of white aromatic smoke rising, low-angle golden sunbeams, shot on 35mm vintage anamorphic lens, realistic photographic texture, no CGI --ar 9:16 --v 6.1",
            "video_prompt": "[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 24/30 FPS, unretouched real human photography, authentic 1990s Vietnamese rural documentary capture, warm golden hour 3800K, raw skin texture with visible pores, zero AI plastic smoothing. [CAMERA CONTROL]: Slow smooth horizontal camera pan from left to right at eye-level, tracking the children squatting beside the straw haystack with subtle organic handheld breathing motion. [CHARACTER ANCHOR]: @_Char_Rural_Boy_Tam, 9-year-old Vietnamese village boy with lean build, sun-tanned honey skin, unruly buzz-cut hair, and light soot smudges on cheeks, accompanied by @_Char_Rural_Girl_Mai. [DYNAMIC ENVIRONMENT]: @_Location_Straw_Paddy_Field, vast golden harvested rice field, dry straw haystack, gentle curls of aromatic white woodsmoke rising in the evening air. [INITIAL STATE]: Inherits Keyframe 1: Tâm and Mai squatting beside dry straw, Tâm holding a handful of straw above glowing embers. [MICRO-ACTING TIMELINE]: - [0.0s - 3.0s]: Tâm gently feeds handfuls of dry yellow straw into glowing red embers on the ground, his face concentrated with playful determination. - [3.0s - 7.0s]: He leans forward, puffing his cheeks to blow a gentle breath of air into the tinder, sparks drifting softly as white smoke billows upwards, squinting his eyes affectionately against the smoke. - [7.0s - 10.0s]: A flame crackles into life, illuminating their sun-tanned faces with warm flickering firelight, as Mai claps her hands in innocent delight. [AUDIO BGM & FOLEY]: Dry straw crackling softly in growing fire, gentle blowing breath sound, distant afternoon breeze rustling through dry rice stalks, cheerful acoustic bamboo flute melody ducked at -22dB. [FINAL STATE]: Warm firelight dancing on children's laughing faces, settling posture for Scene 2. [NEGATIVE CONSTRAINTS]: Strictly NO CGI 3D animation, NO airbrushed doll skin, NO jump cuts, NO morphing, NO modern items, raw authentic film grain.",
            "voice_over": "Hồi nhỏ, cứ mỗi mùa gặt xong, bờ ruộng rơm khô lại trở thành thiên đường tuyệt vời nhất của lũ trẻ con xóm nghèo chúng mình.",
            "sound_design": "Dry straw crackling softly in growing fire, gentle blowing breath sound, distant afternoon breeze rustling through dry rice stalks, cheerful acoustic bamboo flute melody."
        },
        {
            "id": "Scene 02 [00:10 - 00:20]",
            "image_prompt": "Cinematic medium close-up, 9-year-old Vietnamese village boy @_Char_Rural_Boy_Tam squatting close to the glowing straw bonfire in @_Location_Straw_Paddy_Field, holding a rustic fresh corn cob on a wooden skewer directly over hot red embers, yellow corn kernels sizzling and slightly charred with roasted golden edges, white smoke curling around his sun-tanned face, his eyes teary and squinting from the pungent sweet woodsmoke, genuine mischievous grin on his face with visible soot marks on nose, authentic weathered skin texture, glowing amber sunset light, 35mm film grain, 8k resolution --ar 9:16 --v 6.1",
            "video_prompt": "[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 24/30 FPS, unretouched real human photography, authentic Vietnamese rural nostalgia, seamless continuation from Scene 1 end frame. [CAMERA CONTROL]: Locked-off eye-level medium close-up (MCU), fixed 50mm vintage lens at f/2.2, zero camera panning, zero zooming, unwavering stability. [CHARACTER ANCHOR]: @_Char_Rural_Boy_Tam, identical 9-year-old Vietnamese village boy, sun-tanned skin, faded blue tank top, authentic soot marks on cheeks. [DYNAMIC ENVIRONMENT]: Beside the glowing straw embers in @_Location_Straw_Paddy_Field, warm ambient sunset light, thin aromatic smoke wafting across frame. [INITIAL STATE]: Inherits Keyframe 2: Tâm holding a wooden skewer with fresh corn cob over glowing embers, excited gaze. [MICRO-ACTING TIMELINE]: - [0.0s - 3.0s]: Tâm carefully rotates the rustic wooden skewer with both hands, watching the golden corn kernels roast and char slightly with intense excitement. - [3.0s - 7.0s]: A sudden gust of wind blows a puff of white woodsmoke directly toward his face; he squints hard, blinking teary eyes playfully while puffing air from lips to clear smoke, revealing realistic soot smudges. - [7.0s - 10.0s]: The corn sizzles delicately, and Tâm grins widely in anticipation, his chest rising with natural breathing and throat swallowing in pure delight. [AUDIO BGM & FOLEY]: Corn kernels softly sizzling on hot coals, puffing breath blowing away smoke, crickets chirping softly in dusk, warm acoustic nylon guitar notes ducked at -22dB. [FINAL STATE]: Roasted golden corn held up with proud mischievous grin, settling into Keyframe 3 posture. [NEGATIVE CONSTRAINTS]: Strictly NO facial distortion, NO morphed fingers, NO waxy plastic skin, NO sudden camera jerks, raw lifelike footage.",
            "voice_over": "Bắp non bẻ trộm đem vùi tro nóng, khói rơm cay xè khóe mắt nhưng mùi bắp nướng thơm lừng khiến đứa nào đứa nấy háo hức nuốt nước miếng.",
            "sound_design": "Corn kernels softly sizzling on hot coals, puffing breath blowing away smoke, crickets chirping softly in dusk, warm acoustic nylon guitar notes."
        },
        {
            "id": "Scene 03 [00:20 - 00:30]",
            "image_prompt": "Cinematic candid medium shot, two Vietnamese rural children @_Char_Rural_Boy_Tam and @_Char_Rural_Girl_Mai sitting side by side on dry straw mat on the edge of harvested paddy field @_Location_Straw_Paddy_Field, breaking a steaming hot roasted golden corn cob in half to share, both faces covered in black soot and charcoal smudges, laughing joyfully with bright sparkling eyes, bite marks on the steaming corn, radiant low-angle deep orange sunset casting long shadows and ethereal rim light on their hair, authentic sun-tanned skin, raw 1990s nostalgia documentary style, 35mm film aesthetic --ar 9:16 --v 6.1",
            "video_prompt": "[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 24/30 FPS, unretouched real human photography, authentic Vietnamese documentary realism, golden hour finale. [CAMERA CONTROL]: Slow gentle dolly-out shot capturing the two children sitting together beside the straw haystack with deep emotional warmth. [CHARACTER ANCHOR]: @_Char_Rural_Boy_Tam and @_Char_Rural_Girl_Mai, identical facial geometry and authentic weathered sun-tanned skin, faces comically smudged with black charcoal soot. [DYNAMIC ENVIRONMENT]: Edge of harvested paddy field @_Location_Straw_Paddy_Field, deep orange and violet twilight sky, ethereal rim lighting on their hair. [INITIAL STATE]: Inherits Keyframe 3: Tâm and Mai sitting side by side holding the steaming roasted corn cob. [MICRO-ACTING TIMELINE]: - [0.0s - 3.0s]: Tâm snaps the steaming freshly roasted corn cob in two pieces with a delicate cracking sound, steam rising gracefully into the cool evening breeze. - [3.0s - 7.0s]: He hands the larger half to Mai; both eagerly take a savory bite, blowing gently on the hot corn before chewing with pure blissful happiness. - [7.0s - 10.0s]: They look at each other's dirty soot-stained faces and burst into innocent, heartwarming laughter, leaning their shoulders together as sunset fades to twilight. [AUDIO BGM & FOLEY]: Delicate snap of corn cob breaking, happy laughter of children, gentle evening twilight insects, nostalgic bamboo flute and acoustic strings ending warmly. [FINAL STATE]: Heartwarming laughter frozen in tender dusk light, perfectly closing the 30s video narrative. [NEGATIVE CONSTRAINTS]: Strictly NO jump cuts, NO morphing, NO uncanny CGI smile, NO modern artifacts, pure nostalgic cinematic perfection.",
            "voice_over": "Giờ lớn lên giữa phố xá rực rỡ, tìm đâu lại được nụ cười lấm lem bùn đất và vị ngọt của những buổi chiều quê năm ấy.",
            "sound_design": "Delicate snap of corn cob breaking, happy laughter of children, gentle evening twilight insects, nostalgic bamboo flute and acoustic strings ending warmly."
        }
    ],
    "seo": {
        "titles": [
            "Chiều Nướng Bắp Rơm Rạ: Vị Ngọt Tuổi Thơ Mà Tiền Bạc Không Thể Mua Lại",
            "Hồi Nhỏ Có Ai Từng Cay Xè Mắt Vì Nướng Bắp Bờ Ruộng Giống Tụi Mình Không?",
            "Góc Quê: Mùi Rơm Rạ Chiều Hoàng Hôn Và Nụ Cười Lấm Lem Năm Ấy"
        ],
        "thumbnail_prompt": "Cinematic eye-level emotional thumbnail, 9-year-old Vietnamese rural boy @_Char_Rural_Boy_Tam grinning broadly with face smudged in black charcoal soot, holding up a golden charred roasted corn cob with steam rising, next to rustic straw haystack on harvested rice paddy field @_Location_Straw_Paddy_Field during breathtaking golden hour sunset, rich amber sunbeams illuminating dust particles, authentic sun-tanned weathered skin texture, candid human expression of pure innocent joy, shot on 35mm vintage Leica lens, masterpiece realism, viral youtube shorts cover --ar 9:16 --v 6.1",
        "thumbnail_text": "VỊ NGỌT TUỔI THƠ",
        "caption": "Có những hương vị mà dù sau này đi khắp bốn bể, ăn trăm món ngon vật lạ, ta vẫn không tài nào tìm lại được... Đó là vị bắp non nướng vùi trong tro rơm rạ, là vị cay nồng của khói làm cay xè khóe mắt, và là nụ cười giòn tan lấm lem than củi của lũ bạn năm nào. Bạn còn nhớ buổi chiều quê ấy không? ❤️🌾",
        "hashtags": "#kyuctuoitho #tuoithotoi #gocque #quehuong #hoainiem #nuongbap #romra #langquevietnam #dongque #mientay #shorts #viralshorts #reelsvn #xuhuong #fyp"
    }
}

def export_file_00(output_dir):
    """Xuất 00_HO_SO_THAM_CHIEU_GOC.docx - 100% văn bản thuần, không table"""
    doc = Document()
    add_styled_title(doc, "HỒ SƠ THAM CHIẾU GỐC (MASTER REFERENCE ASSETS)", 
                     f"Dự án: {PROJECT_DATA['project_name']} • Tác giả: Xuanlv",
                     "⚠️ BƯỚC 0 BẮT BUỘC: Nạp ảnh nhân vật và bối cảnh chuẩn làm Face/Style Reference trước khi render phân cảnh hàng loạt:")

    p_h1 = doc.add_heading(level=2)
    p_h1.add_run("1. Master Character Model Sheets (@_Char_...)")
    
    p_desc = doc.add_paragraph()
    p_desc.add_run("• Nhân vật chính: ").bold = True
    p_desc.add_run(f"{PROJECT_DATA['lead_char']}\n")
    p_desc.add_run("• Nhân vật phụ: ").bold = True
    p_desc.add_run(f"{PROJECT_DATA['support_char']}\n")

    add_prompt_paragraph(doc, 
        "Cinematic 4-angle character turnaround model sheet of a 9-year-old Vietnamese rural boy @_Char_Rural_Boy_Tam: front view, 45-degree angle, side profile, and back view. Lean athletic build, authentic deeply sun-tanned weathered skin with natural honey undertones, visible skin pores and light perspiration, short unruly black buzz-cut hair, lively expressive dark brown eyes with playful sparkle, wearing a faded sun-bleached vintage blue cotton tank top with frayed hem and dark grey cotton shorts, bare feet with dirt smudges, neutral warm outdoor lighting, candid documentary realism, highly consistent facial features across all 4 angles, masterpiece 8k resolution --ar 16:9 --v 6.1",
        label="Prompt tạo Sheet 4 góc nhìn Nhân vật chính (@_Char_Rural_Boy_Tam):")

    p_h2 = doc.add_heading(level=2)
    p_h2.add_run("2. Master Environment Sheet (@_Location_...)")
    
    p_env_desc = doc.add_paragraph()
    p_env_desc.add_run("• Bối cảnh: ").bold = True
    p_env_desc.add_run(f"{PROJECT_DATA['environment']}\n")

    add_prompt_paragraph(doc,
        "Cinematic wide establishing shot of a vast harvested Vietnamese rice paddy field during golden hour sunset @_Location_Straw_Paddy_Field, endless golden yellow rice stubble, a colossal rustic straw haystack, thin gentle curls of white aromatic woodsmoke rising from glowing embers on the ground, silhouette of lush green bamboo grove in distant background, low-angle warm amber sunlight 3800K, authentic 1990s Vietnamese countryside atmosphere, 35mm film grain, 8k --ar 16:9 --v 6.1",
        label="Prompt tạo Bối cảnh chuẩn Master (@_Location_Straw_Paddy_Field):")

    filepath = os.path.join(output_dir, "00_HO_SO_THAM_CHIEU_GOC.docx")
    safe_save_doc(doc, filepath)

def export_file_01(output_dir):
    """Xuất 01_PROMPTS_ANH_HANG_LOAT.docx - 100% văn bản thuần, không table, 1 đoạn văn liên tục/cảnh"""
    doc = Document()
    add_styled_title(doc, "PROMPTS TẠO ẢNH HÀNG LOẠT (BATCH IMAGE PROMPTS)", 
                     f"Dự án: {PROJECT_DATA['project_name']} • Tỷ lệ: 9:16",
                     "💡 HƯỚNG DẪN: Mỗi phân cảnh bên dưới là MỘT ĐOẠN VĂN LIÊN TỤC DUY NHẤT. Copy nguyên khối dán thẳng vào Tool hàng loạt (Midjourney / Flux):")

    for sc in PROJECT_DATA["scenes"]:
        add_prompt_paragraph(doc, sc["image_prompt"])

    filepath = os.path.join(output_dir, "01_PROMPTS_ANH_HANG_LOAT.docx")
    safe_save_doc(doc, filepath)

def export_file_02(output_dir):
    """Xuất 02_PROMPTS_VIDEO_HANG_LOAT.docx - 100% văn bản thuần, không table, chuẩn Tagged Blocks, 1 đoạn văn liên tục/cảnh"""
    doc = Document()
    add_styled_title(doc, "PROMPTS TẠO VIDEO 10S HÀNG LOẠT (BATCH VIDEO PROMPTS - TAGGED BLOCKS)", 
                     f"Dự án: {PROJECT_DATA['project_name']} • Chuẩn: 10.0s/cảnh • Chuẩn Thẻ Phân Rã",
                     "💡 HƯỚNG DẪN: Mỗi phân cảnh là MỘT ĐOẠN VĂN LIÊN TỤC chứa đầy đủ Thẻ Phân Rã và Timeline vi mô [0-3s], [3-7s], [7-10s]. Nạp Keyframe tương ứng làm First Frame rồi copy dán vào Kling AI / Hailuo / Veo 3.1:")

    for sc in PROJECT_DATA["scenes"]:
        add_prompt_paragraph(doc, sc["video_prompt"])

    filepath = os.path.join(output_dir, "02_PROMPTS_VIDEO_HANG_LOAT.docx")
    safe_save_doc(doc, filepath)

def export_file_03(output_dir):
    """Xuất 03_PROMPTS_VOICE_HANG_LOAT.docx - 100% văn bản thuần, không table, 1 đoạn văn liên tục/cảnh"""
    doc = Document()
    add_styled_title(doc, "LỜI THOẠI VOICE-OVER HÀNG LOẠT (CLEAN TTS SCRIPTS)", 
                     f"Dự án: {PROJECT_DATA['project_name']} • Voice: @Voice_Viet_Nostalgic_Narrator",
                     "💡 HƯỚNG DẪN: Văn bản tiếng Việt sạch 100%. Copy dán vào ElevenLabs / Vbee / FPT.AI để tạo file voice cho từng phân cảnh:")

    for sc in PROJECT_DATA["scenes"]:
        add_prompt_paragraph(doc, sc["voice_over"], font_name='Segoe UI', font_size=11, is_bold=False)

    filepath = os.path.join(output_dir, "03_PROMPTS_VOICE_HANG_LOAT.docx")
    safe_save_doc(doc, filepath)

def export_file_04(output_dir):
    """Xuất 04_METADATA_SEO.docx - 100% văn bản thuần, không table"""
    doc = Document()
    add_styled_title(doc, "GÓI METADATA & SEO VIRAL ĐỀ XUẤT", 
                     f"Dự án: {PROJECT_DATA['project_name']} • Nền tảng: Shorts / TikTok / Reels",
                     "💡 HƯỚNG DẪN: Bộ tiêu đề A/B, prompt tạo Thumbnail, Caption và Hashtag chuẩn tối ưu hóa thuật toán đề xuất:")

    p_h1 = doc.add_heading(level=2)
    p_h1.add_run("1. Tiêu Đề Video (A/B Testing)")
    for idx, title in enumerate(PROJECT_DATA["seo"]["titles"], 1):
        p_t = doc.add_paragraph()
        p_t.add_run(f"• Phương án {idx}: ").bold = True
        p_t.add_run(title)

    p_h2 = doc.add_heading(level=2)
    p_h2.add_run("2. Prompt Tạo Ảnh Thumbnail (Tỉ lệ 9:16)")
    add_prompt_paragraph(doc, PROJECT_DATA["seo"]["thumbnail_prompt"], label="Prompt Midjourney / Flux:")

    p_th_text = doc.add_paragraph()
    p_th_text.add_run("• Chữ dán trên Thumbnail: ").bold = True
    p_th_text.add_run(f"\"{PROJECT_DATA['seo']['thumbnail_text']}\" (Font Sans-Serif đậm màu vàng viền đen, đặt ở 1/3 phía trên khung hình).")

    p_h3 = doc.add_heading(level=2)
    p_h3.add_run("3. Caption Bài Viết")
    add_prompt_paragraph(doc, PROJECT_DATA["seo"]["caption"], font_name='Segoe UI', font_size=10.5)

    p_h4 = doc.add_heading(level=2)
    p_h4.add_run("4. Cây Hashtag 3 Tầng")
    add_prompt_paragraph(doc, PROJECT_DATA["seo"]["hashtags"], font_name='Consolas', font_size=10)

    filepath = os.path.join(output_dir, "04_METADATA_SEO.docx")
    safe_save_doc(doc, filepath)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_root = os.path.abspath(os.path.join(script_dir, ".."))
    default_output_dir = os.path.join(skill_root, "examples", "chieu-nuong-bap-rom-ra", "export_batch")

    output_dir = sys.argv[1] if len(sys.argv) > 1 else default_output_dir
    os.makedirs(output_dir, exist_ok=True)

    print("=" * 60)
    print("XUẤT TRỌN BỘ 5 FILE WORD CHUYÊN DỤNG CHO TOOL HÀNG LOẠT (ZERO-TABLE)")
    print(f"Thư mục xuất file: {output_dir}")
    print("=" * 60)

    export_file_00(output_dir)
    export_file_01(output_dir)
    export_file_02(output_dir)
    export_file_03(output_dir)
    export_file_04(output_dir)

    print("=" * 60)
    print("HOÀN TẤT 100%! Trọn bộ 5 file Word đã sẵn sàng nạp Tool chạy hàng loạt.")
    print("=" * 60)

if __name__ == "__main__":
    main()
