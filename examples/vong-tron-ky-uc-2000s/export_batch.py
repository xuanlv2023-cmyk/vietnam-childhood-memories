#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script tự động kết xuất trọn bộ 5 File Word (.docx) chuyên dụng cho sản xuất hàng loạt
Dự án: Vòng Tròn Ký Ức Tuổi Thơ (22 Phân Cảnh 16:9 Chuẩn Điện Ảnh 4K)
Skill: vietnam-childhood-memories (Mode 2: Phim Ngắn Không Lời Thoại)
1. 00_HO_SO_THAM_CHIEU_GOC.docx
2. 01_PROMPTS_ANH_HANG_LOAT.docx
3. 02_PROMPTS_VIDEO_HANG_LOAT.docx
4. 03_PROMPTS_VOICE_HANG_LOAT.docx
5. 04_METADATA_SEO.docx

Quy chuẩn Tool Batch:
- 100% văn bản thuần túy (Plain Text Paragraphs), KHÔNG sử dụng Table ở bất kỳ file nào.
- 01_PROMPTS_ANH: Mỗi cảnh là đúng 1 đoạn văn liên tục (22 cảnh = đúng 22 đoạn văn).
- 02_PROMPTS_VIDEO: Mỗi cảnh là đúng 1 đoạn văn liên tục không ngắt dòng bên trong (22 cảnh = đúng 22 đoạn văn).
- 03_PROMPTS_VOICE: Bản đặc tả Foley & Audio Timeline (22 cảnh = đúng 22 đoạn văn).
"""

import os
import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def add_styled_title(doc, title_text, subtitle_text, note_text=None):
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_title = p_title.add_run(title_text)
    run_title.font.name = 'Segoe UI'
    run_title.font.size = Pt(17)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(180, 83, 9) # Amber Brown
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run_sub = p_sub.add_run(subtitle_text)
    run_sub.font.name = 'Segoe UI'
    run_sub.font.size = Pt(10)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(100, 116, 139)

    if note_text:
        p_sub.paragraph_format.space_after = Pt(4)
        p_note = doc.add_paragraph()
        p_note.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run_note = p_note.add_run(note_text)
        run_note.font.name = 'Segoe UI'
        run_note.font.size = Pt(9.5)
        run_note.font.color.rgb = RGBColor(194, 65, 12)
        p_note.paragraph_format.space_after = Pt(16)
    else:
        p_sub.paragraph_format.space_after = Pt(14)

def add_clean_paragraph(doc, text_content, font_name='Consolas', font_size=10, is_bold=False):
    """Thêm đúng 1 đoạn văn liên tục không nhãn thừa cho tool batch"""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(14)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text_content)
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = is_bold
    run.font.color.rgb = RGBColor(30, 41, 59)

def export_file_00(output_dir):
    doc = Document()
    add_styled_title(doc, "HỒ SƠ THAM CHIẾU GỐC (MASTER REFERENCE ASSETS)",
                     "Dự án: Vòng Tròn Ký Ức Tuổi Thơ • Phim Ngắn 16:9 Chuẩn 4K",
                     "⚠️ BƯỚC 0 BẮT BUỘC: Nạp ảnh Model Sheet của các nhân vật và bối cảnh làm Character Reference cho Tool AI.")

    p_h1 = doc.add_heading(level=2)
    p_h1.add_run("1. Master Character Model Sheet [BOY_TEEN] (14 tuổi) & [MAN_ADULT] (25 tuổi)")
    p_c1 = doc.add_paragraph()
    p_c1.add_run("• Cậu bé thiếu niên [BOY_TEEN]: ").bold = True
    p_c1.add_run("14 tuổi, da ngăm nắng, áo sơ mi trắng học sinh, đi dép tổ ong, xe đạp Phượng Hoàng cũ.\n")
    p_c1.add_run("• Người lớn [MAN_ADULT]: ").bold = True
    p_c1.add_run("25 tuổi, dáng cao gầy, áo khoác gió nâu, ba lô sẫm màu, ánh mắt ấm áp kiên định.")
    p_c1.paragraph_format.space_after = Pt(4)

    prompt_char = "A professional cinematic character turnaround model sheet of a Vietnamese male character across two eras, arranged on a wide 16:9 seamless warm studio canvas. On the left side: three views of [BOY_TEEN] as a 14-year-old rural schoolboy, sun-tanned skin with natural pores, wearing a white school shirt and dark trousers, standing beside a vintage green bicycle. On the right side: three views of [MAN_ADULT] as a 25-year-old grown man sharing the exact same distinct facial bone structure, nose shape, and warm eyes, wearing a brown jacket with backpack. 100% real human photography, raw 8k DSLR on Sony A7R V with 85mm f/1.4 lens, natural skin textures, zero CGI, zero 3D render --ar 16:9 --style raw"
    add_clean_paragraph(doc, prompt_char)

    p_h2 = doc.add_heading(level=2)
    p_h2.add_run("2. Master Character Sheet [MOTHER] & [FATHER] (Hai Thời Kỳ)")
    p_c2 = doc.add_paragraph()
    p_c2.add_run("• Mẹ quê [MOTHER]: ").bold = True
    p_c2.add_run("42 tuổi đến 55 tuổi, áo bà ba hoa nhã nhặn, tóc búi sau gáy, đôi bàn tay gầy chai sạn.\n")
    p_c2.add_run("• Cha quê [FATHER]: ").bold = True
    p_c2.add_run("45 tuổi đến 58 tuổi, áo cộc tay sờn cổ, tóc hoa râm, ánh mắt nghiêm nghị giàu tình cảm.")
    p_c2.paragraph_format.space_after = Pt(4)

    p_h3 = doc.add_heading(level=2)
    p_h3.add_run("3. Master Location Sheets")
    p_c3 = doc.add_paragraph()
    p_c3.add_run("• Cổng trường làng đầu 2000s, quán net cỏ màn CRT, đường đê làng rợp bóng tre, nhà quê với niêu cá kho và bát sứ trắng viền xanh.")
    p_c3.paragraph_format.space_after = Pt(4)

    doc.save(os.path.join(output_dir, "00_HO_SO_THAM_CHIEU_GOC.docx"))

# 22 image prompts (1 đoạn văn liên tục / cảnh)
image_prompts = [
    "Cinematic 16:9 4K establishing photograph of an early 2000s rural Vietnamese village school gate under massive ancient shade trees, golden midday sunlight filtering through leaves casting warm dappled light patterns across dirt courtyard, students in white shirts flooding out, [BOY_TEEN] pushing a vintage green bicycle alongside his best friend walking through rustic iron gate, authentic period detail, raw 8k DSLR on Sony A7R V, zero AI plastic smoothing --ar 16:9 --style raw",
    "Cinematic 16:9 4K side tracking photograph along a scenic rural Vietnamese dyke road shaded by bamboo groves, [BOY_TEEN] and his best friend riding vintage bicycles side by side, white school shirts fluttering softly in the breeze, turning heads to laugh naturally while watching road, medium shot framing facial warmth before opening to green rice paddy fields in soft warm afternoon haze, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K interior photograph of an early 2000s Vietnamese village LAN gaming internet cafe, weathered lime-washed walls, narrow wooden desks, red plastic stools, slow ceiling fan, glowing blue CRT computer monitors with authentic glass bulb thickness, [BOY_TEEN] and friend sitting shoulder to shoulder totally engrossed playing a retro video game, phosphor glow mixed with golden outdoor light, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K dramatic close-up photograph of [BOY_TEEN] inside rustic internet cafe, analog wall clock showing 13:15 PM in background, his eyes shifting from playful excitement to sudden shock and panic, wide dark eyes and parted lips, standing up grabbing weathered fabric backpack, nuanced natural reaction without exaggeration, natural teen skin pores, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K slow following photograph in rustic Vietnamese country house, [MOTHER] placing a steaming clay pot of caramelized braised fish onto plain wooden dining table beside prepared rice bowls, [FATHER] sitting silently glancing at empty chair, mother walking to wooden threshold leaning gently against door frame gazing down village lane with deep longing, soft indoor shade, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K low-angle tracking photograph positioned tightly beside spinning bicycle wheel moving rapidly along dirt dyke road between expansive rice fields, realistic motion blur on metal spokes, fine road dust kicking up gently, camera tilting up to [BOY_TEEN] pedaling urgently with full effort, schoolbag strapped to rear rack, face showing worry and determination, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K romantic nostalgic medium photograph on an afternoon, [BOY_TEEN] gently pedaling vintage bicycle carrying [GIRL_NEIGHBOR] in traditional white student ao dai sitting sideways on padded rear rack, riding slowly beside willow-shaded village canal, white silk fabric draped neatly fluttering gently in river breeze, girl smiling shyly, boy glancing back tenderly, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K wide panoramic sunset photograph, [BOY_TEEN] riding vintage bicycle carrying [GIRL_NEIGHBOR] across an ancient low stone bridge with stone railings after study class, deep violet and golden sunset hues reflecting over tranquil village river, elongated bicycle shadow cast on stone bridge deck, girl holding notebooks on lap, boy pedaling steadily, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K split-match photographic study: white student school shirt hanging on rustic wooden peg in country house match-cutting identically in framing to brown adult jacket of [MAN_ADULT] hanging on wall peg in cramped urban rental room; tight close-up of teen hand gripping bicycle handlebar match-cutting to adult weathered hand gripping dark backpack strap, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K interior passenger bus photograph, [MAN_ADULT] resting forehead against bus window looking out through glass reflection where aging [MOTHER] and [FATHER] stand waving goodbye beside rural country road, sharp focus on young man's melancholy reflective eyes with faint double reflection on window, parents growing smaller as bus begins rolling forward, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K photograph of [MAN_ADULT] standing still on safe city sidewalk edge beside bustling urban intersection at twilight, towering modern high-rise office towers with glowing windows behind him, continuous streams of cars and motorbikes creating subtle motion blur streaks in background, cool slate-cyan lighting with golden street reflections, wearing dark backpack, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K high-angle cinematic aerial vista photograph of a coastal highway and railway line stretching along Central Vietnam coastline at dawn, green rugged mountain slopes on one side, tranquil pale-blue ocean on the other, delicate morning mist hovering between landscape layers, small passenger bus travels steadily, pink-cyan sunrise sky, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K night interior photograph in cramped urban rental room, [MAN_ADULT] working diligently at wooden desk under warm focused desk lamp, laptop, paper notebook and glass of water arranged neatly, three-quarter angle revealing tired yet determined eyes, gently rubbing bridge of nose taking a deep breath, cool night blue moonlight from small window, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K horizontal tracking close-up photograph of aging [MOTHER]'s slender weathered hands using chopsticks to place a tender piece of braised fish into a nostalgic white porcelain bowl with blue rim, placed lovingly at her absent son's wooden chair, camera shifting focus slowly from bowl to the empty wooden stool beside it, mother's hand pausing before pulling back, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K static medium interior photograph of aging [MOTHER] and [FATHER] eating quiet dinner in rustic country kitchen at dusk, same wooden dining table and blue-rimmed porcelain bowls, open wooden doorway framing dark tropical garden in background, mother resting chopsticks gazing out into dark yard, father looking tenderly at her placing gentle weathered hand over hers, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K mirror reflection photograph in urban rental room, [MAN_ADULT] standing before bathroom mirror looking deeply into his own reflection after long exhausting workday, camera over his shoulder showing both real face and optically correct reflection, slowly resting hand on mirror frame, his intense gaze softening as childhood memories wash over him, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K master match-cut photograph: close-up of [MAN_ADULT] placing nostalgic white porcelain bowl with blue rim onto modest rental room table; exactly matching position and angle to the identical blue-rimmed porcelain bowl on rustic family dining table in the past, revealing [BOY_TEEN] smiling beside loving parents as mother's hand serves fish, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K dynamic backward tracking photograph of [MAN_ADULT] carrying backpack striding purposefully through sunlit train station platform in crisp morning light, his face glowing with radiant anticipation and joyful relief, footsteps determined and resolute, subtle passengers walking naturally in background, strong architectural lines, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K side tracking photograph pulling back slowly, [MAN_ADULT] walking along familiar village dyke road amidst golden ripe rice paddies in warm late afternoon glow, backpack on shoulder, gentle breeze swaying golden rice stalks, slowing his pace to look at whispering bamboo grove with joyful recognition, golden sunset light illuminating his smiling face, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K emotional homecoming photograph looking outward from courtyard toward rustic wooden gate as [MAN_ADULT] pushes open gate and steps inside, aging [MOTHER] recognizing him and rushing forward from veranda, aging [FATHER] standing up quickly, young man drops backpack embracing mother tightly then pulling father into a collective loving embrace, tearful eyes and radiant choked smiles, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K gentle arc photograph around round wooden dining table, complete family reunited under warm golden ceiling light, enjoying traditional home-cooked meal with clay pot braised fish, boiled vegetables, and nostalgic blue-rimmed porcelain bowls, [MOTHER] placing fish into [MAN_ADULT]'s bowl as he looks at her with tender gratitude, [FATHER] smiling broadly beside them, raw 8k DSLR --ar 16:9 --style raw",
    "Cinematic 16:9 4K circular narrative closing match-cut photograph: looking through open wooden window into dark night yard with glowing warm window centered in frame; match-cutting seamlessly to rustic village school gate bathed in bright morning golden sunlight under ancient trees, [BOY_TEEN] pedaling vintage bicycle out from gate smiling brilliantly, complete eternal circle, raw 8k DSLR --ar 16:9 --style raw"
]

def export_file_01(output_dir):
    doc = Document()
    add_styled_title(doc, "PROMPTS TẠO ẢNH HÀNG LOẠT (BATCH IMAGE PROMPTS)",
                     "Dự án: Vòng Tròn Ký Ức Tuổi Thơ • Chuẩn 16:9 4K Real Human Photography",
                     "Định dạng Tool Batch: 100% văn bản thuần túy không nhãn thừa. Mỗi cảnh là đúng 1 đoạn văn liên tục xuống dòng (22 cảnh = đúng 22 đoạn văn sạch).")
    for p in image_prompts:
        add_clean_paragraph(doc, p)
    doc.save(os.path.join(output_dir, "01_PROMPTS_ANH_HANG_LOAT.docx"))

# 22 video prompts (1 đoạn văn liên tục / cảnh)
video_prompts = [
    "Cinematic 16:9 4K establishing wide shot of an early 2000s rural Vietnamese village school gate under massive ancient shade trees, golden midday sunlight filtering through leaves casting warm dappled light patterns across dirt courtyard, students in white shirts flooding out cheerfully, [BOY_TEEN] (14-year-old Vietnamese boy with sun-tanned skin and authentic skin pores) pushing a vintage green bicycle alongside his best friend walking through rustic iron gate, slow smooth dolly forward from village road toward the boys, gentle rustling leaves and dust motes glowing in warm air, authentic period detail, zero AI plastic smoothing, pristine sensor clarity, ending smoothly as boys mount bicycles --ar 16:9 --style raw",
    "Cinematic 16:9 4K side tracking shot moving at bicycle speed along a scenic rural Vietnamese dyke road shaded by towering bamboo groves, [BOY_TEEN] and his best friend riding vintage bicycles side by side, light white school shirts fluttering softly in the breeze, turning heads to laugh naturally while watching road, medium shot framing facial warmth before opening to reveal endless green rice paddy fields in soft warm afternoon haze, natural spoke motion blur on wheels, authentic dirt road texture, zero CGI cartoon look, ending as they look ahead toward village entrance --ar 16:9 --style raw",
    "Cinematic 16:9 4K interior shot of an early 2000s Vietnamese village LAN gaming internet cafe, weathered lime-washed walls, narrow wooden desks, red plastic stools, slow ceiling fan, glowing blue CRT computer monitors with authentic glass bulb thickness, [BOY_TEEN] and friend sitting shoulder to shoulder totally engrossed playing a retro video game without brand logos, smooth camera glide along desk row settling on boy's fascinated face bathed in CRT phosphor glow mixed with golden outdoor light from open door, authentic nostalgic atmosphere, ending as he suddenly glances up at wall clock --ar 16:9 --style raw",
    "Cinematic 16:9 4K dramatic close-up of [BOY_TEEN] inside rustic internet cafe, smooth rack focus from retro analog wall clock showing 13:15 PM directly to boy's face, his eyes shifting from playful excitement to sudden shock and panic, camera gently pushing into his wide dark eyes and parted lips, immediately standing up grabbing weathered fabric backpack and pivoting toward door, nuanced natural reaction without exaggeration, natural teen skin pores and realistic lighting, soft ambient background blur, zero plastic wax doll effect --ar 16:9 --style raw",
    "Cinematic 16:9 4K slow following camera in rustic Vietnamese country house, [MOTHER] (loving 42-year-old rural Vietnamese mother in floral cotton shirt) placing a steaming clay pot of caramelized braised fish onto plain wooden dining table beside prepared rice bowls, [FATHER] sitting silently glancing at empty chair, camera tracking mother as she walks to wooden threshold leaning gently against door frame gazing down village lane with deep patient longing, soft indoor shade contrasting with bright warm midday yard, natural dust motes, rich poignant domestic atmosphere --ar 16:9 --style raw",
    "Cinematic 16:9 4K low-angle tracking shot positioned tightly beside spinning bicycle wheel moving rapidly along dirt dyke road between expansive rice fields, realistic motion blur on metal spokes, fine road dust kicking up gently, camera smoothly tilting up from spinning wheel to [BOY_TEEN] pedaling urgently with full effort, both hands gripping handlebars firmly, schoolbag strapped to rear rack, face showing authentic mix of worry and determination, bright sunny sky, golden field reflections, ending as he turns into home path --ar 16:9 --style raw",
    "Cinematic 16:9 4K romantic nostalgic medium tracking shot on another afternoon, [BOY_TEEN] gently pedaling vintage bicycle carrying [GIRL_NEIGHBOR] (cute 14-year-old girl in traditional white student ao dai) sitting sideways on padded rear rack, riding slowly beside willow-shaded village canal, white silk fabric draped neatly fluttering gently in river breeze, girl smiling shyly, boy glancing back tenderly before facing road with modest smile, soft golden afternoon water reflections, pure innocent rural romance, zero artificial CGI --ar 16:9 --style raw",
    "Cinematic 16:9 4K wide panoramic sunset shot, [BOY_TEEN] riding vintage bicycle carrying [GIRL_NEIGHBOR] across an ancient low stone bridge with stone railings after extra study class, deep violet and golden sunset hues reflecting over tranquil village river, elongated bicycle shadow cast on stone bridge deck, camera slowly panning from riverbank following them, girl holding notebooks on lap, boy pedaling steadily, peaceful timeless Vietnamese pastoral beauty, leading toward soft evening glow at bridge end --ar 16:9 --style raw",
    "Cinematic 16:9 4K precise match-cut montage representing passage of years: white student school shirt hanging on rustic wooden peg in country house match-cuts identically in framing and position to brown adult jacket of [MAN_ADULT] hanging on wall peg in cramped urban rental room; then tight close-up of teen hand gripping bicycle handlebar match-cuts seamlessly in motion and position to adult weathered hand gripping dark backpack strap, golden nostalgic amber grade transitioning smoothly to muted slate-cyan urban tone, pristine optical alignment, zero morphing glitch --ar 16:9 --style raw",
    "Cinematic 16:9 4K interior passenger bus shot, [MAN_ADULT] (25-year-old Vietnamese man) resting forehead against bus window, looking out through glass reflection where aging [MOTHER] and [FATHER] stand waving goodbye beside rural country road, sharp focus on young man's melancholy reflective eyes with faint double reflection on bus window, parents growing smaller as bus begins rolling forward, soft daylight, steady vehicular motion, silent poignant farewell, cinematic realism, zero distortion --ar 16:9 --style raw",
    "Cinematic 16:9 4K slow dolly forward on [MAN_ADULT] standing still on safe city sidewalk edge beside bustling urban intersection at twilight, towering modern high-rise office towers with glowing windows behind him, continuous streams of cars and motorbikes creating subtle motion blur streaks in background, cool slate-cyan lighting with golden street reflections, wearing dark backpack, gaze filled with quiet longing and solitude amidst dense metropolitan rush --ar 16:9 --style raw",
    "Cinematic 16:9 4K high-angle cinematic aerial vista of a coastal highway and railway line stretching along Central Vietnam coastline at dawn, green rugged mountain slopes on one side, tranquil pale-blue ocean on the other, delicate morning mist hovering between landscape layers, camera floating forward along road direction toward horizon as small passenger bus travels steadily, pristine perspective, pink-cyan sunrise sky, vast melancholic journey of livelihood --ar 16:9 --style raw",
    "Cinematic 16:9 4K night interior shot in cramped urban rental room, [MAN_ADULT] working diligently at wooden desk under warm focused desk lamp, laptop, paper notebook and glass of water arranged neatly, camera starting over-the-shoulder then smoothly sliding to three-quarter angle revealing tired yet determined eyes, gently rubbing bridge of nose taking a deep breath then continuing typing, cool night blue moonlight from small window contrasting warm desk glow, authentic solitude --ar 16:9 --style raw",
    "Cinematic 16:9 4K slow horizontal tracking close-up of aging [MOTHER]'s slender weathered hands using chopsticks to place a tender piece of braised fish into a nostalgic white porcelain bowl with blue rim, placed lovingly at her absent son's wooden chair, camera shifting focus slowly from bowl to the empty wooden stool beside it, mother's hand pausing for a heartfelt moment before slowly pulling back, warm kitchen lantern glow, delicate rising steam, palpable unspoken motherly longing --ar 16:9 --style raw",
    "Cinematic 16:9 4K static medium interior shot of aging [MOTHER] and [FATHER] eating quiet dinner in rustic country kitchen at dusk, same wooden dining table and blue-rimmed porcelain bowls, open wooden doorway framing dark tropical garden in background, mother resting chopsticks gazing out into dark yard, father looking tenderly at her placing gentle weathered hand over hers, warm golden indoor illumination surrounded by cool twilight blue, deep enduring parental love --ar 16:9 --style raw",
    "Cinematic 16:9 4K mirror reflection shot in urban rental room, [MAN_ADULT] standing before bathroom mirror looking deeply into his own reflection after long exhausting workday, camera over his shoulder showing both real face and optically correct reflection, slowly resting hand on mirror frame, his intense gaze softening as childhood memories wash over him, dim warm light mingling with cool night blue, camera slowly creeping in on his eyes filled with nostalgic emotion --ar 16:9 --style raw",
    "Cinematic 16:9 4K master match-cut shot: close-up of [MAN_ADULT] placing nostalgic white porcelain bowl with blue rim onto modest rental room table; the exact instant bottom of bowl touches wooden surface, match-cuts seamlessly in exact position and angle to the identical blue-rimmed porcelain bowl on rustic family dining table in the past, camera widening gently to reveal [BOY_TEEN] smiling beside loving parents as mother's hand serves fish, cool cyan grading warming instantly into golden amber --ar 16:9 --style raw",
    "Cinematic 16:9 4K dynamic backward tracking medium shot of [MAN_ADULT] carrying backpack striding purposefully through sunlit train station platform in crisp morning light, his face glowing with radiant anticipation and joyful relief, footsteps determined and resolute, subtle passengers walking naturally in background, strong architectural lines leading toward departing passenger train, golden sunrise beams, uplifting emotional cinematic tempo --ar 16:9 --style raw",
    "Cinematic 16:9 4K side tracking shot pulling back slowly, [MAN_ADULT] walking along familiar village dyke road amidst golden ripe rice paddies in warm late afternoon glow, backpack on shoulder, gentle breeze swaying golden rice stalks, slowing his pace to look at whispering bamboo grove with joyful recognition, golden sunset light illuminating his smiling face echoing opening youth scenes, familiar ancestral roof visible ahead --ar 16:9 --style raw",
    "Cinematic 16:9 4K emotional homecoming shot looking outward from courtyard toward rustic wooden gate as [MAN_ADULT] pushes open gate and steps inside, aging [MOTHER] recognizing him and rushing forward from veranda, aging [FATHER] standing up quickly, young man drops backpack embracing mother tightly then pulling father into a collective loving embrace, camera gliding in from medium to medium-close capturing tearful eyes and radiant choked smiles, warm golden hour rays, genuine family reunion --ar 16:9 --style raw",
    "Cinematic 16:9 4K gentle arc tracking shot moving slowly around round wooden dining table, complete family reunited under warm golden ceiling light, enjoying traditional home-cooked meal with clay pot braised fish, boiled vegetables, and nostalgic blue-rimmed porcelain bowls, [MOTHER] placing fish into [MAN_ADULT]'s bowl as he looks at her with tender gratitude, [FATHER] smiling broadly beside them, rising food steam, profound peaceful contentment --ar 16:9 --style raw",
    "Cinematic 16:9 4K circular narrative closing match-cut: camera slowly dollying backward from laughing family dinner through open wooden window into dark night yard, holding glowing warm window centered in frame; at exact window frame position, match-cuts seamlessly to rustic village school gate bathed in bright morning golden sunlight under ancient trees, [BOY_TEEN] pedaling vintage bicycle out from gate smiling brilliantly, camera continuing backward glide as morning sun and nostalgia complete eternal circle --ar 16:9 --style raw"
]

def export_file_02(output_dir):
    doc = Document()
    add_styled_title(doc, "PROMPTS TẠO VIDEO HÀNG LOẠT (BATCH MEGA PROMPTS)",
                     "Dự án: Vòng Tròn Ký Ức Tuổi Thơ • Chuẩn Điện Ảnh 16:9 4K",
                     "Định dạng Tool Batch: 100% văn bản thuần túy không nhãn thừa. Mỗi cảnh là đúng 1 đoạn văn liên tục không ngắt dòng bên trong (22 cảnh = đúng 22 đoạn văn sạch).")
    for vp in video_prompts:
        add_clean_paragraph(doc, vp)
    doc.save(os.path.join(output_dir, "02_PROMPTS_VIDEO_HANG_LOAT.docx"))

# 22 foley lines (1 đoạn văn liên tục / cảnh)
foley_lines = [
    "Tiếng trống trường làng vang tùng tùng, tiếng học sinh ùa ra cười nói xôn xao, tiếng chim hót trên vòm xà cừ, tiếng xích xe đạp cũ lách cách.",
    "Tiếng gió lùa qua rặng tre xào xạc, tiếng xích líp xe đạp quay đều trên đường cát đê làng, tiếng cười đùa tự nhiên của hai cậu học trò.",
    "Tiếng lách cách gõ bàn phím cơ và chuột máy tính, tiếng quạt trần quay chậm vù vù, tiếng rè nhẹ của dàn màn hình CRT cổ điển.",
    "Tiếng ghế nhựa kéo lê ngắn trên nền gạch, tiếng cặp sách vải dù va chạm vội vã, tiếng bước chân gấp gáp của cậu bé giật mình trễ giờ cơm.",
    "Tiếng đũa bát chạm mặt bàn gỗ lách cách, tiếng niêu đất kho cá sôi lăn tăn bốc khói, tiếng ve sầu trưa hè râm ran ngoài vườn cây.",
    "Tiếng xích líp xe đạp quay tít gấp gáp, tiếng gió rít qua tai, tiếng thở dốc hối hả và tiếng bánh xe lăn nhanh trên đường đê đất bụi.",
    "Tiếng tà áo dài lụa bay phần phật nhẹ trong gió chiều, tiếng nước gợn sóng êm ả dưới bờ kênh, tiếng cười khúc khích thẹn thùng của cô bé.",
    "Tiếng bánh xe đạp lăn chậm qua mặt cầu đá cổ, tiếng nước sông chảy lững lờ, giai điệu guitar mộc acoustic rải nốt êm dịu lúc hoàng hôn.",
    "Tiếng xích xe đạp nhỏ dần rồi hòa tan nhịp nhàng sang tiếng động cơ xe khách đường dài rì rầm, tiếng gió lùa qua cửa kính chuyển mùa.",
    "Tiếng động cơ xe khách lăn bánh trên đường nhựa xa xa, tiếng thở dài lưu luyến của người con tựa trán vào kính nhìn cha mẹ vẫy tay.",
    "Tiếng còi xe và dòng xe cộ đô thị gầm rú dày đặc ở ngã tư giờ tan tầm, tiếng bước chân vội vã của dòng người xa lạ trên vỉa hè.",
    "Tiếng gió biển thổi lồng lộng qua đèo dốc miền Trung, tiếng động cơ xe khách đều đều hòa cùng tiếng sóng biển vỗ rì rào lúc rạng đông.",
    "Tiếng gõ bàn phím laptop trong đêm vắng, tiếng quạt máy nhỏ quay rù rù trong phòng trọ chật hẹp, tiếng thở hắt nhọc nhằn của người tăng ca.",
    "Tiếng đũa tre chạm vào thành bát sứ trắng viền xanh lách cách, tiếng hơi nóng mỏng bốc lên từ niêu cá kho, khoảng lặng thở dài của mẹ già.",
    "Tiếng côn trùng đêm rả rích ngoài vườn cây tối, tiếng bát đũa nhẹ của cha mẹ già, tiếng bàn tay cha đặt lên bàn tay mẹ vỗ về ấm áp.",
    "Tiếng nước nhỏ giọt trong phòng tắm, tiếng ngón tay chạm nhẹ lên mặt kính gương, tiếng chuông xe đạp năm xưa vang vọng mờ ảo trong tâm tưởng.",
    "Tiếng đáy bát sứ chạm xuống mặt bàn phòng trọ lách cách nối liền sang tiếng bát chạm mâm cơm quê nhà, giai điệu piano dâng trào cảm xúc.",
    "Tiếng bước chân giày rảo bước dứt khoát trên sân ga ngập nắng mai, tiếng còi tàu xa xa, tiếng loa ga dịu dàng, nhịp piano tươi sáng rộn rã.",
    "Tiếng gió thổi qua đồng lúa chín vàng xào xạc, tiếng chim chiền chiện hót trên đồng quê, tiếng bước chân thân thuộc chậm rãi bước về nhà.",
    "Tiếng đẩy cánh cổng gỗ kêu kẽo kẹt, tiếng ba lô rơi xuống đất, tiếng ôm nghẹn ngào vỡ òa, tiếng nấc rưng rưng xúc động của cha mẹ đón con.",
    "Tiếng bát đũa sum họp reo vui lách cách quanh mâm cơm tròn, tiếng cười ấm áp của cha mẹ, tiếng hơi nóng niêu cá kho bốc lên thơm phức.",
    "Tiếng cười gia đình vọng qua khung cửa sổ đêm rồi hòa tan sang tiếng chuông xe đạp leng keng rộn rã dưới cổng trường làng nắng mai khép lại."
]

def export_file_03(output_dir):
    doc = Document()
    add_styled_title(doc, "BẢN ĐẶC TẢ FOLEY & AUDIO TIMELINE HÀNG LOẠT",
                     "Dự án: Vòng Tròn Ký Ức Tuổi Thơ • Phim Ngắn Không Lời Thoại",
                     "Định dạng Tool Batch: Danh sách đặc tả hiệu ứng âm thanh Foley và tiếng động đời thực cho 22 phân cảnh (22 đoạn văn sạch).")
    for fl in foley_lines:
        add_clean_paragraph(doc, fl, font_name='Segoe UI', font_size=11)
    doc.save(os.path.join(output_dir, "03_PROMPTS_VOICE_HANG_LOAT.docx"))

def export_file_04(output_dir):
    doc = Document()
    add_styled_title(doc, "GÓI TỐI ƯU SEO & ĐĂNG TẢI VIRAL ĐIỆN ẢNH 16:9",
                     "Dự án: Vòng Tròn Ký Ức Tuổi Thơ • Chuẩn Đăng Tải YouTube 4K")

    p_h1 = doc.add_heading(level=2)
    p_h1.add_run("1. Prompt Tạo Ảnh Bìa Thumbnail (16:9 4K)")
    thumb_prompt = "A deeply emotional cinematic 16:9 4K master thumbnail photograph, split composition or golden ratio focus. In the center, a 25-year-old Vietnamese man [MAN_ADULT] with misty, emotional eyes holding an iconic white porcelain rice bowl with blue rim at a rustic country dinner table, loving aging mother [MOTHER] smiling warmly beside him as warm golden lantern light illuminates their faces. In the upper soft background, faint nostalgic double exposure of a 14-year-old rural schoolboy [BOY_TEEN] pedaling a vintage bicycle along a sunny village dyke road under bamboo trees. Authentic weathered skin textures with visible pores, rich golden amber lighting, pristine 8k DSLR quality on Sony A7R V with 85mm f/1.4 lens, clean negative space on left side for bold typography, zero AI plastic wax smoothing, zero 3D CGI rendering --ar 16:9 --style raw"
    add_clean_paragraph(doc, thumb_prompt)

    p_h2 = doc.add_heading(level=2)
    p_h2.add_run("2. Chữ Dán Thumbnail (Overlay Text)")
    add_clean_paragraph(doc, "ĐI THẬT XA ĐỂ TRỞ VỀ 🌾❤️\nVÒNG TRÒN KÝ ỨC TUỔI THƠ 🚲✨\nBỮA CƠM CỦA MẸ NĂM ẤY 😭🍲", font_name='Segoe UI', font_size=11)

    p_h3 = doc.add_heading(level=2)
    p_h3.add_run("3. Tiêu Đề Đa Nền Tảng (A/B Testing Headlines)")
    add_clean_paragraph(doc, "A: Phim Ngắn: VÒNG TRÒN KÝ ỨC — Đi nửa đời người mới hiểu bữa cơm quê ấm đến nhường nào (Phim Điện Ảnh 4K)\nB: Tuổi thơ đầu những năm 2000: Quán net trốn học, chuyến xe rời quê và chiếc ghế trống của mẹ... 🌾🥺\nC: Dù đi bao xa, vòng tròn ký ức tuổi thơ vẫn luôn chờ ta trở về | Ký Ức Đồng Quê Việt Nam", font_name='Segoe UI', font_size=11)

    p_h4 = doc.add_heading(level=2)
    p_h4.add_run("4. Caption & Hashtag 3 Tầng")
    add_clean_paragraph(doc, "Có những buổi trưa trốn học chơi game ở quán net cỏ đầu làng, nghe tiếng trống trường tan học rộn rã mà giật mình đạp xe cuống cuồng về nhà vì sợ mẹ la... Rồi thời gian trôi, đứa trẻ năm xưa bước lên chuyến xe khách rời quê mưu sinh, để lại căn nhà nhỏ với đôi mắt mẹ cha ngóng cửa và chiếc ghế trống bên niêu cá kho bốc khói. Đi qua bao thăng trầm phố thị, thứ duy nhất cứu rỗi tâm hồn ta chính là con đường đê quen thuộc và mâm cơm gia đình ấm áp ngày trở về.\n\n#KyUcTuoiTho #GocQueXua #PhimNganDienAnh #TuoiThoDau2000s #NhungNam2000 #LangQueVietNam #NhoQue #TinhMe #NguoiConXaXu #DienAnhVietNam #KýỨcTuổiThơ #GócQuê", font_name='Segoe UI', font_size=10.5)

    doc.save(os.path.join(output_dir, "04_METADATA_SEO.docx"))

def export_all():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "export_batch")
    os.makedirs(output_dir, exist_ok=True)
    export_file_00(output_dir)
    export_file_01(output_dir)
    export_file_02(output_dir)
    export_file_03(output_dir)
    export_file_04(output_dir)
    print(f"[OK] Đã xuất thành công trọn bộ 5 file .docx chuẩn Tool Batch tại: {output_dir}")

if __name__ == '__main__':
    export_all()
