# Character & Setting Reference Tokens (Thư Viện Token Tham Chiếu)

Hệ thống Token tham chiếu đảm bảo tính nhất quán tuyệt đối về diện mạo nhân vật và bối cảnh qua tất cả các phân cảnh, triệt tiêu tình trạng khuôn mặt hoặc bối cảnh biến đổi lộn xộn giữa các mốc 10 giây.

---

## 1. THƯ VIỆN TOKEN NHÂN VẬT CHUẨN (@_Char_...)

### Token 1: `@_Char_Rural_Boy_Tam` (Cậu bé nông thôn tinh nghịch)
* **Định danh**: Cậu bé Tâm, 9-11 tuổi, biểu tượng của trẻ con làng quê Việt Nam thập niên 90.
* **Mô tả chi tiết chuẩn**:
  ```text
  9-year-old Vietnamese rural boy, lean and energetic build, deep sun-tanned weathered skin with natural honey undertones, visible authentic skin pores, unruly short black buzz-cut hair, lively expressive dark brown eyes with playful sparkle, light dry mud smudges on cheek and dusty forehead, wearing a faded sun-bleached blue cotton tank top with frayed edges and loose dark grey cotton shorts, bare feet with soil smudges, candid documentary realism.
  ```
* **Ứng dụng**: Nhân vật chính trong các kịch bản nướng bắp rơm, trèo rào hái trộm trái cây, tắm sông, lội bùn đến trường, chăn trâu thả diều.

### Token 2: `@_Char_Rural_Girl_Mai` (Bé gái thôn quê mộc mạc)
* **Định danh**: Bé Mai, 8-10 tuổi, em gái hoặc bạn thân đồng trang lứa.
* **Mô tả chi tiết chuẩn**:
  ```text
  8-year-old Vietnamese village girl, slender petite build, naturally sun-tanned warm skin tone, twin braided black hair tied with simple rubber bands, radiant innocent smile with small front teeth gap, wearing a faded vintage floral print short-sleeved cotton shirt with rustic pearl buttons and rolled-up navy shorts, barefoot with faint dust on ankles, natural candid lighting.
  ```

### Token 3: `@_Char_Grandma_BaBa` (Bà nội / Bà ngoại phúc hậu)
* **Định danh**: Bà cụ 70-75 tuổi, hiện thân của tình yêu thương gia đình và ký ức êm đềm.
* **Mô tả chi tiết chuẩn**:
  ```text
  72-year-old Vietnamese rural grandmother, deeply wrinkled kind face with gentle crow's feet, warm compassionate eyes, silver hair neatly tied into a traditional small bun at the nape, wearing a worn rustic dark brown cotton Ao Ba Ba blouse with fabric buttons, gentle stoop in posture, weathered working hands with visible veins, sitting warmly with a nostalgic gentle smile.
  ```
* **Ứng dụng**: Canh nồi bánh chưng đêm giao thừa, quạt mo cau ru cháu ngủ trên chõng tre, dỗ dành khi cháu bị đòn.

### Token 4: `@_Char_Mother_GanhHang` (Mẹ hiền tần tảo)
* **Định danh**: Người mẹ thôn quê 35-38 tuổi, gánh hàng rong tần tảo sớm hôm.
* **Mô tả chi tiết chuẩn**:
  ```text
  36-year-old Vietnamese rural mother, slender hard-working posture, gently weathered sun-kissed skin, dark hair tucked beneath a conical palm-leaf hat with frayed lilac chin strap, wearing an earth-toned faded indigo Ao Ba Ba shirt with rolled sleeves, carrying a bamboo shoulder pole with two rustic woven baskets, kind loving gaze filled with maternal resilience.
  ```

---

## 2. THƯ VIỆN TOKEN BỐI CẢNH CHUẨN (@_Location_...)

### Token 1: `@_Location_Straw_Paddy_Field` (Đồng lúa & Đống rơm hoàng hôn)
```text
vast harvested Vietnamese rice paddy field during golden hour sunset, golden dry rice stubble stretching to the horizon, a colossal rustic straw haystack, thin gentle curls of aromatic white woodsmoke rising from a small ground bonfire, distant silhouette of lush green bamboo grove and coconut palms, warm amber lighting 3800K, nostalgic cinematic 35mm film atmosphere.
```

### Token 2: `@_Location_Thatch_Hut_Interior` (Gian nhà tranh vách đất & Chõng tre)
```text
humble traditional Vietnamese rural thatched cottage interior from 1990s, earthen walls, dried palm thatch roof, rustic bamboo daybed with woven straw mat, clay water jar with coconut shell ladle in the corner, flickering warm kerosene lamp casting soft amber glow, vintage small black and white cathode-ray tube television on a wooden crate, nostalgic intimate evening ambiance.
```

### Token 3: `@_Location_Muddy_Village_Lane` (Đường làng đất sét mùa mưa)
```text
narrow winding rural Vietnamese dirt village path after heavy summer rain, glistening reddish-brown muddy puddles reflecting overcast sky, dense roadside banana trees with broad dripping leaves, rustic bamboo fences lined with blooming red hibiscus flowers, atmospheric mist and moist air.
```

### Token 4: `@_Location_River_Wharf_Sampan` (Bến sông quê & Xuồng ba lá)
```text
tranquil Mekong delta riverside pier at dusk, murky alluvium water with soft ripples, a weathered wooden three-plank sampan boat tied to a bamboo pole, lush green water hyacinths floating gently, wooden monkey footbridge spanning over the canal, hazy evening dusk light.
```

---

## 3. QUY TẮC NHÚNG TOKEN VÀO PROMPT

1. **Khởi tạo danh tính**: Đặt Token ở ngay phần đầu của prompt mô tả đối tượng để làm điểm neo nhận diện.
2. **Kèm theo mô tả bổ trợ**: Sau Token, luôn đính kèm từ khóa hành động cụ thể của phân cảnh đó (ví dụ: `@_Char_Rural_Boy_Tam squatting excitedly beside the straw bonfire, roasting corn on a wooden skewer...`).
3. **Tuyệt đối không thay đổi thuộc tính cốt lõi**: Không đổi màu da, độ tuổi, hay kiểu tóc của nhân vật giữa các cảnh.
