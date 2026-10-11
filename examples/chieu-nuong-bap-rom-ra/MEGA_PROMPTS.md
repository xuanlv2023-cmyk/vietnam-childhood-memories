# Mega Prompts Điện Ảnh & Khối Batch Copy (MEGA_PROMPTS.md)

Dự án: **Chiều Nướng Bắp Rơm Rạ Bên Bờ Ruộng** (30.0 Giây • 3 Phân Cảnh x 10.0s)  
Hệ thống Token: `@_Char_Rural_Boy_Tam`, `@_Char_Rural_Girl_Mai`, `@_Location_Straw_Paddy_Field`

> **Quy chuẩn kỹ thuật:** Chuẩn Thẻ Phân Rã (Tagged Blocks Architecture), Khóa cứng 10.0s/cảnh (`Exactly 10.0 seconds`), Single Continuous Unbroken Take 10.0s, Timeline diễn xuất vi mô 3 chặng `[0.0s - 3.0s], [3.0s - 7.0s], [7.0s - 10.0s]`, triệt tiêu hoàn toàn morphing và mặt búp bê/nhựa AI.

---

## 📋 BỘ PROMPTS CHẠY HÀNG LOẠT (BATCH COPY BLOCK — 1 ĐOẠN VĂN / CẢNH)
> **💡 HƯỚNG DẪN DÙNG TOOL BATCH:** Copy toàn bộ ô code block bên dưới dán thẳng vào tool chạy hàng loạt. Mỗi phân cảnh là **đúng 1 đoạn văn liên tục** (không có ngắt dòng bên trong, không có tiền tố thừa). Các phân cảnh phân cách nhau bằng **1 lần xuống dòng**.

### 1. PROMPTS TẠO ẢNH HÀNG LOẠT (BATCH IMAGE PROMPTS - 9:16)
```text
Cinematic medium wide shot, two 9-year-old Vietnamese rural children @_Char_Rural_Boy_Tam and @_Char_Rural_Girl_Mai squatting together beside a rustic straw haystack on harvested golden rice paddy field @_Location_Straw_Paddy_Field during warm sunset golden hour, Tâm carefully blowing air into dry straw to light a small campfire with glowing embers, authentic sun-tanned weathered skin with natural visible pores, light dried mud and ash smudges on cheeks, wearing faded 1990s vintage frayed cotton tank tops and dark shorts, barefoot on dry soil, curls of white aromatic smoke rising, low-angle golden sunbeams, shot on 35mm vintage anamorphic lens, realistic photographic texture, no CGI --ar 9:16 --v 6.1

Cinematic medium close-up, 9-year-old Vietnamese village boy @_Char_Rural_Boy_Tam squatting close to the glowing straw bonfire in @_Location_Straw_Paddy_Field, holding a rustic fresh corn cob on a wooden skewer directly over hot red embers, yellow corn kernels sizzling and slightly charred with roasted golden edges, white smoke curling around his sun-tanned face, his eyes teary and squinting from the pungent sweet woodsmoke, genuine mischievous grin on his face with visible soot marks on nose, authentic weathered skin texture, glowing amber sunset light, 35mm film grain, 8k resolution --ar 9:16 --v 6.1

Cinematic candid medium shot, two Vietnamese rural children @_Char_Rural_Boy_Tam and @_Char_Rural_Girl_Mai sitting side by side on dry straw mat on the edge of harvested paddy field @_Location_Straw_Paddy_Field, breaking a steaming hot roasted golden corn cob in half to share, both faces covered in black soot and charcoal smudges, laughing joyfully with bright sparkling eyes, bite marks on the steaming corn, radiant low-angle deep orange sunset casting long shadows and ethereal rim light on their hair, authentic sun-tanned skin, raw 1990s nostalgia documentary style, 35mm film aesthetic --ar 9:16 --v 6.1
```

### 2. PROMPTS TẠO VIDEO 10S HÀNG LOẠT (BATCH VIDEO PROMPTS - EXACTLY 10.0S)
```text
[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 24/30 FPS, unretouched real human photography, authentic 1990s Vietnamese rural documentary capture, warm golden hour 3800K, raw skin texture with visible pores, zero AI plastic smoothing. [CAMERA CONTROL]: Slow smooth horizontal camera pan from left to right at eye-level, tracking the children squatting beside the straw haystack with subtle organic handheld breathing motion. [CHARACTER ANCHOR]: @_Char_Rural_Boy_Tam, 9-year-old Vietnamese village boy with lean build, sun-tanned honey skin, unruly buzz-cut hair, and light soot smudges on cheeks, accompanied by @_Char_Rural_Girl_Mai. [DYNAMIC ENVIRONMENT]: @_Location_Straw_Paddy_Field, vast golden harvested rice field, dry straw haystack, gentle curls of aromatic white woodsmoke rising in the evening air. [INITIAL STATE]: Inherits Keyframe 1: Tâm and Mai squatting beside dry straw, Tâm holding a handful of straw above glowing embers. [MICRO-ACTING TIMELINE]: - [0.0s - 3.0s]: Tâm gently feeds handfuls of dry yellow straw into glowing red embers on the ground, his face concentrated with playful determination. - [3.0s - 7.0s]: He leans forward, puffing his cheeks to blow a gentle breath of air into the tinder, sparks drifting softly as white smoke billows upwards, squinting his eyes affectionately against the smoke. - [7.0s - 10.0s]: A flame crackles into life, illuminating their sun-tanned faces with warm flickering firelight, as Mai claps her hands in innocent delight. [AUDIO BGM & FOLEY]: Dry straw crackling softly in growing fire, gentle blowing breath sound, distant afternoon breeze rustling through dry rice stalks, cheerful acoustic bamboo flute melody ducked at -22dB. [FINAL STATE]: Warm firelight dancing on children's laughing faces, settling posture for Scene 2. [NEGATIVE CONSTRAINTS]: Strictly NO CGI 3D animation, NO airbrushed doll skin, NO jump cuts, NO morphing, NO modern items, raw authentic film grain.

[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 24/30 FPS, unretouched real human photography, authentic Vietnamese rural nostalgia, seamless continuation from Scene 1 end frame. [CAMERA CONTROL]: Locked-off eye-level medium close-up (MCU), fixed 50mm vintage lens at f/2.2, zero camera panning, zero zooming, unwavering stability. [CHARACTER ANCHOR]: @_Char_Rural_Boy_Tam, identical 9-year-old Vietnamese village boy, sun-tanned skin, faded blue tank top, authentic soot marks on cheeks. [DYNAMIC ENVIRONMENT]: Beside the glowing straw embers in @_Location_Straw_Paddy_Field, warm ambient sunset light, thin aromatic smoke wafting across frame. [INITIAL STATE]: Inherits Keyframe 2: Tâm holding a wooden skewer with fresh corn cob over glowing embers, excited gaze. [MICRO-ACTING TIMELINE]: - [0.0s - 3.0s]: Tâm carefully rotates the rustic wooden skewer with both hands, watching the golden corn kernels roast and char slightly with intense excitement. - [3.0s - 7.0s]: A sudden gust of wind blows a puff of white woodsmoke directly toward his face; he squints hard, blinking teary eyes playfully while puffing air from lips to clear smoke, revealing realistic soot smudges. - [7.0s - 10.0s]: The corn sizzles delicately, and Tâm grins widely in anticipation, his chest rising with natural breathing and throat swallowing in pure delight. [AUDIO BGM & FOLEY]: Corn kernels softly sizzling on hot coals, puffing breath blowing away smoke, crickets chirping softly in dusk, warm acoustic nylon guitar notes ducked at -22dB. [FINAL STATE]: Roasted golden corn held up with proud mischievous grin, settling into Keyframe 3 posture. [NEGATIVE CONSTRAINTS]: Strictly NO facial distortion, NO morphed fingers, NO waxy plastic skin, NO sudden camera jerks, raw lifelike footage.

[SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 24/30 FPS, unretouched real human photography, authentic Vietnamese documentary realism, golden hour finale. [CAMERA CONTROL]: Slow gentle dolly-out shot capturing the two children sitting together beside the straw haystack with deep emotional warmth. [CHARACTER ANCHOR]: @_Char_Rural_Boy_Tam and @_Char_Rural_Girl_Mai, identical facial geometry and authentic weathered sun-tanned skin, faces comically smudged with black charcoal soot. [DYNAMIC ENVIRONMENT]: Edge of harvested paddy field @_Location_Straw_Paddy_Field, deep orange and violet twilight sky, ethereal rim lighting on their hair. [INITIAL STATE]: Inherits Keyframe 3: Tâm and Mai sitting side by side holding the steaming roasted corn cob. [MICRO-ACTING TIMELINE]: - [0.0s - 3.0s]: Tâm snaps the steaming freshly roasted corn cob in two pieces with a delicate cracking sound, steam rising gracefully into the cool evening breeze. - [3.0s - 7.0s]: He hands the larger half to Mai; both eagerly take a savory bite, blowing gently on the hot corn before chewing with pure blissful happiness. - [7.0s - 10.0s]: They look at each other's dirty soot-stained faces and burst into innocent, heartwarming laughter, leaning their shoulders together as sunset fades to twilight. [AUDIO BGM & FOLEY]: Delicate snap of corn cob breaking, happy laughter of children, gentle evening twilight insects, nostalgic bamboo flute and acoustic strings ending warmly. [FINAL STATE]: Heartwarming laughter frozen in tender dusk light, perfectly closing the 30s video narrative. [NEGATIVE CONSTRAINTS]: Strictly NO jump cuts, NO morphing, NO uncanny CGI smile, NO modern artifacts, pure nostalgic cinematic perfection.
```

### 3. KỊCH BẢN LỜI THOẠI THU ÂM HÀNG LOẠT (BATCH TTS SCRIPTS)
```text
Hồi nhỏ, cứ mỗi mùa gặt xong, bờ ruộng rơm khô lại trở thành thiên đường tuyệt vời nhất của lũ trẻ con xóm nghèo chúng mình.

Bắp non bẻ trộm đem vùi tro nóng, khói rơm cay xè khóe mắt nhưng mùi bắp nướng thơm lừng khiến đứa nào đứa nấy háo hức nuốt nước miếng.

Giờ lớn lên giữa phố xá rực rỡ, tìm đâu lại được nụ cười lấm lem bùn đất và vị ngọt của những buổi chiều quê năm ấy.
```

---

## 🔎 CHI TIẾT TỪNG PHÂN CẢNH (ĐỂ SOÁT LỖI & KIỂM TRA)

### CẢNH 1: NHÓM LỬA RƠM — KHƠI GỢI KÝ ỨC (0.0s - 10.0s)
* **Prompt Tạo Ảnh Keyframe K1**:
  `Cinematic medium wide shot, two 9-year-old Vietnamese rural children @_Char_Rural_Boy_Tam and @_Char_Rural_Girl_Mai squatting together beside a rustic straw haystack on harvested golden rice paddy field @_Location_Straw_Paddy_Field during warm sunset golden hour, Tâm carefully blowing air into dry straw to light a small campfire with glowing embers, authentic sun-tanned weathered skin with natural visible pores, light dried mud and ash smudges on cheeks, wearing faded 1990s vintage frayed cotton tank tops and dark shorts, barefoot on dry soil, curls of white aromatic smoke rising, low-angle golden sunbeams, shot on 35mm vintage anamorphic lens, realistic photographic texture, no CGI --ar 9:16 --v 6.1`
* **Prompt Video 10s**:
  ```text
  [SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 24/30 FPS, unretouched real human photography, authentic 1990s Vietnamese rural documentary capture, warm golden hour 3800K, raw skin texture with visible pores, zero AI plastic smoothing.
  [CAMERA CONTROL]: Slow smooth horizontal camera pan from left to right at eye-level, tracking the children squatting beside the straw haystack with subtle organic handheld breathing motion.
  [CHARACTER ANCHOR]: @_Char_Rural_Boy_Tam, 9-year-old Vietnamese village boy with lean build, sun-tanned honey skin, unruly buzz-cut hair, and light soot smudges on cheeks, accompanied by @_Char_Rural_Girl_Mai.
  [DYNAMIC ENVIRONMENT]: @_Location_Straw_Paddy_Field, vast golden harvested rice field, dry straw haystack, gentle curls of aromatic white woodsmoke rising in the evening air.
  [INITIAL STATE]: Inherits Keyframe 1: Tâm and Mai squatting beside dry straw, Tâm holding a handful of straw above glowing embers.
  [MICRO-ACTING TIMELINE]:
  - [0.0s - 3.0s]: Tâm gently feeds handfuls of dry yellow straw into glowing red embers on the ground, his face concentrated with playful determination.
  - [3.0s - 7.0s]: He leans forward, puffing his cheeks to blow a gentle breath of air into the tinder, sparks drifting softly as white smoke billows upwards, squinting his eyes affectionately against the smoke.
  - [7.0s - 10.0s]: A flame crackles into life, illuminating their sun-tanned faces with warm flickering firelight, as Mai claps her hands in innocent delight.
  [AUDIO BGM & FOLEY]: Dry straw crackling softly in growing fire, gentle blowing breath sound, distant afternoon breeze rustling through dry rice stalks, cheerful acoustic bamboo flute melody ducked at -22dB.
  [FINAL STATE]: Warm firelight dancing on children's laughing faces, settling posture for Scene 2.
  [NEGATIVE CONSTRAINTS]: Strictly NO CGI 3D animation, NO airbrushed doll skin, NO jump cuts, NO morphing, NO modern items, raw authentic film grain.
  ```
* **Voice-Over (24 từ)**:
  > *"Hồi nhỏ, cứ mỗi mùa gặt xong, bờ ruộng rơm khô lại trở thành thiên đường tuyệt vời nhất của lũ trẻ con xóm nghèo chúng mình."*

---

### CẢNH 2: NƯỚNG BẮP — KHÓI CAY KHÓE MẮT (10.0s - 20.0s)
* **Prompt Tạo Ảnh Keyframe K2**:
  `Cinematic medium close-up, 9-year-old Vietnamese village boy @_Char_Rural_Boy_Tam squatting close to the glowing straw bonfire in @_Location_Straw_Paddy_Field, holding a rustic fresh corn cob on a wooden skewer directly over hot red embers, yellow corn kernels sizzling and slightly charred with roasted golden edges, white smoke curling around his sun-tanned face, his eyes teary and squinting from the pungent sweet woodsmoke, genuine mischievous grin on his face with visible soot marks on nose, authentic weathered skin texture, glowing amber sunset light, 35mm film grain, 8k resolution --ar 9:16 --v 6.1`
* **Prompt Video 10s**:
  ```text
  [SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 24/30 FPS, unretouched real human photography, authentic Vietnamese rural nostalgia, seamless continuation from Scene 1 end frame.
  [CAMERA CONTROL]: Locked-off eye-level medium close-up (MCU), fixed 50mm vintage lens at f/2.2, zero camera panning, zero zooming, unwavering stability.
  [CHARACTER ANCHOR]: @_Char_Rural_Boy_Tam, identical 9-year-old Vietnamese village boy, sun-tanned skin, faded blue tank top, authentic soot marks on cheeks.
  [DYNAMIC ENVIRONMENT]: Beside the glowing straw embers in @_Location_Straw_Paddy_Field, warm ambient sunset light, thin aromatic smoke wafting across frame.
  [INITIAL STATE]: Inherits Keyframe 2: Tâm holding a wooden skewer with fresh corn cob over glowing embers, excited gaze.
  [MICRO-ACTING TIMELINE]:
  - [0.0s - 3.0s]: Tâm carefully rotates the rustic wooden skewer with both hands, watching the golden corn kernels roast and char slightly with intense excitement.
  - [3.0s - 7.0s]: A sudden gust of wind blows a puff of white woodsmoke directly toward his face; he squints hard, blinking teary eyes playfully while puffing air from lips to clear smoke, revealing realistic soot smudges.
  - [7.0s - 10.0s]: The corn sizzles delicately, and Tâm grins widely in anticipation, his chest rising with natural breathing and throat swallowing in pure delight.
  [AUDIO BGM & FOLEY]: Corn kernels softly sizzling on hot coals, puffing breath blowing away smoke, crickets chirping softly in dusk, warm acoustic nylon guitar notes ducked at -22dB.
  [FINAL STATE]: Roasted golden corn held up with proud mischievous grin, settling into Keyframe 3 posture.
  [NEGATIVE CONSTRAINTS]: Strictly NO facial distortion, NO morphed fingers, NO waxy plastic skin, NO sudden camera jerks, raw lifelike footage.
  ```
* **Voice-Over (25 từ)**:
  > *"Bắp non bẻ trộm đem vùi tro nóng, khói rơm cay xè khóe mắt nhưng mùi bắp nướng thơm lừng khiến đứa nào đứa nấy háo hức nuốt nước miếng."*

---

### CẢNH 3: NỤ CƯỜI LẤM LEM — CHIA BẮP DƯỚI HOÀNG HÔN (20.0s - 30.0s)
* **Prompt Tạo Ảnh Keyframe K3**:
  `Cinematic candid medium shot, two Vietnamese rural children @_Char_Rural_Boy_Tam and @_Char_Rural_Girl_Mai sitting side by side on dry straw mat on the edge of harvested paddy field @_Location_Straw_Paddy_Field, breaking a steaming hot roasted golden corn cob in half to share, both faces covered in black soot and charcoal smudges, laughing joyfully with bright sparkling eyes, bite marks on the steaming corn, radiant low-angle deep orange sunset casting long shadows and ethereal rim light on their hair, authentic sun-tanned skin, raw 1990s nostalgia documentary style, 35mm film aesthetic --ar 9:16 --v 6.1`
* **Prompt Video 10s**:
  ```text
  [SPECIFICATION]: Exactly 10.0 seconds, 9:16 vertical 1080x1920, 24/30 FPS, unretouched real human photography, authentic Vietnamese documentary realism, golden hour finale.
  [CAMERA CONTROL]: Slow gentle dolly-out shot capturing the two children sitting together beside the straw haystack with deep emotional warmth.
  [CHARACTER ANCHOR]: @_Char_Rural_Boy_Tam and @_Char_Rural_Girl_Mai, identical facial geometry and authentic weathered sun-tanned skin, faces comically smudged with black charcoal soot.
  [DYNAMIC ENVIRONMENT]: Edge of harvested paddy field @_Location_Straw_Paddy_Field, deep orange and violet twilight sky, ethereal rim lighting on their hair.
  [INITIAL STATE]: Inherits Keyframe 3: Tâm and Mai sitting side by side holding the steaming roasted corn cob.
  [MICRO-ACTING TIMELINE]:
  - [0.0s - 3.0s]: Tâm snaps the steaming freshly roasted corn cob in two pieces with a delicate cracking sound, steam rising gracefully into the cool evening breeze.
  - [3.0s - 7.0s]: He hands the larger half to Mai; both eagerly take a savory bite, blowing gently on the hot corn before chewing with pure blissful happiness.
  - [7.0s - 10.0s]: They look at each other's dirty soot-stained faces and burst into innocent, heartwarming laughter, leaning their shoulders together as sunset fades to twilight.
  [AUDIO BGM & FOLEY]: Delicate snap of corn cob breaking, happy laughter of children, gentle evening twilight insects, nostalgic bamboo flute and acoustic strings ending warmly.
  [FINAL STATE]: Heartwarming laughter frozen in tender dusk light, perfectly closing the 30s video narrative.
  [NEGATIVE CONSTRAINTS]: Strictly NO jump cuts, NO morphing, NO uncanny CGI smile, NO modern artifacts, pure nostalgic cinematic perfection.
  ```
* **Voice-Over (24 từ)**:
  > *"Giờ lớn lên giữa phố xá rực rỡ, tìm đâu lại được nụ cười lấm lem bùn đất và vị ngọt của những buổi chiều quê năm ấy."*
