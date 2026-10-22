import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Tala Police Beat Map", layout="wide")

st.markdown("### 🛡️ रायगड पोलीस - तळा पोलीस ठाणे बीट नकाशा (HD Print Generator)")
lang = st.radio(
    "फलकाची भाषा निवडा (Select Board Language):",
    ["मराठी (Gotu Font - १००% न तुटणारी अक्षरे)", "English (Clean Official Font)"],
    horizontal=True
)

is_marathi = lang.startswith("मराठी")

if is_marathi:
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <link href="https://fonts.googleapis.com/css2?family=Gotu&family=Noto+Sans+Devanagari:wght@500;700;800&display=swap" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <style>
        body { margin: 0; padding: 10px; background: #e5e7eb; font-family: 'Gotu', 'Noto Sans Devanagari', sans-serif; }
        .ActionBtn {
            background: #1e3a8a; color: white; border: none; padding: 12px 24px;
            font-size: 18px; font-weight: bold; border-radius: 8px; cursor: pointer;
            margin-bottom: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.2); font-family: 'Gotu', sans-serif;
        }
        .ActionBtn:hover { background: #1d4ed8; }
        #board {
            width: 1600px; height: 960px; background: #fdfbf7;
            border: 8px solid #172554; border-radius: 6px; box-sizing: border-box;
            display: flex; flex-direction: column; overflow: hidden; position: relative;
        }
        .header {
            background: linear-gradient(90deg, #0f172a, #1e3a8a, #0f172a);
            color: white; padding: 10px 30px; display: flex; align-items: center;
            justify-content: space-between; border-bottom: 4px solid #f59e0b; height: 105px; box-sizing: border-box;
        }
        .header-title { text-align: center; }
        .header-title h1 { margin: 0; font-size: 40px; letter-spacing: 1px; color: #ffffff; text-shadow: 2px 2px 4px #000; }
        .header-title h2 { margin: 2px 0 0 0; font-size: 22px; color: #fde047; }
        .badge {
            background: #ffffff; color: #1e3a8a; font-weight: bold; padding: 8px 14px;
            border-radius: 8px; border: 2px solid #f59e0b; text-align: center; font-size: 15px;
        }
        .sub-banner {
            position: absolute; top: 90px; left: 50%; transform: translateX(-50%);
            background: #1e3a8a; color: #fde047; padding: 4px 36px; border-radius: 0 0 16px 16px;
            border: 2px solid #f59e0b; font-size: 22px; font-weight: bold; z-index: 10;
        }
        .main-content {
            display: grid; grid-template-columns: 390px 1fr 410px; gap: 12px;
            padding: 16px 14px 10px 14px; flex: 1; box-sizing: border-box;
        }
        .panel {
            background: #ffffff; border: 2.5px solid #1e3a8a; border-radius: 8px;
            display: flex; flex-direction: column; overflow: hidden;
        }
        .panel-header {
            background: #1e3a8a; color: white; text-align: center; padding: 6px;
            font-size: 19px; font-weight: bold; border-bottom: 2px solid #f59e0b;
        }
        .beat-box { padding: 6px 10px; border-bottom: 1px solid #cbd5e1; font-size: 12.8px; line-height: 1.45; }
        .beat-title {
            font-weight: bold; font-size: 14.5px; padding: 3px 8px; border-radius: 4px;
            margin-bottom: 4px; color: #111827; display: flex; justify-content: space-between;
        }
        .b1 { background: #fde047; border-left: 6px solid #ca8a04; }
        .b2 { background: #d8b4fe; border-left: 6px solid #7e22ce; }
        .b3 { background: #7dd3fc; border-left: 6px solid #0369a1; }
        .b4 { background: #bbf7d0; border-left: 6px solid #15803d; }
        .map-container {
            background: #f0f9ff; border: 2.5px solid #1e3a8a; border-radius: 8px;
            position: relative; display: flex; align-items: center; justify-content: center; overflow: hidden;
        }
        .officer-table { width: 100%; border-collapse: collapse; font-size: 13px; }
        .officer-table td { padding: 3.5px 8px; border-bottom: 1px dashed #e2e8f0; }
        .officer-table td.num { font-weight: bold; text-align: right; color: #0f172a; font-family: sans-serif; font-size: 13.5px; }
        .contact-footer {
            background: #1e3a8a; color: white; padding: 8px 10px; text-align: center;
            font-size: 14px; margin-top: auto; line-height: 1.4;
        }
        .bottom-bar {
            background: #0f172a; color: #f8fafc; height: 34px; display: flex;
            align-items: center; justify-content: space-around; font-size: 14px; padding: 0 20px;
        }
    </style>
    </head>
    <body>
    <button class="ActionBtn" onclick="downloadBoard()">📥 हा संपूर्ण नकाशा HD PNG इमेजमध्ये डाऊनलोड करा (Download Print-Ready PNG)</button>

    <div id="board">
        <div class="header">
            <div class="badge">★ महाराष्ट्र पोलीस ★<br><span style="font-size:12px;">सद्रक्षणाय खलनिग्रहणाय</span></div>
            <div class="header-title">
                <h1>रायगड पोलीस | तळा पोलीस ठाणे</h1>
                <h2>ता. तळा, जि. रायगड</h2>
            </div>
            <div class="badge">★ रायगड पोलीस ★<br><span style="font-size:12px;">तळा पोलीस ठाणे</span></div>
        </div>
        <div class="sub-banner">बीट नकाशा (Beat Map)</div>

        <div class="main-content">
            <!-- डावे पॅनेल: गाव व बीट विभागणी -->
            <div class="panel">
                <div class="panel-header">गाव व बीट विभागणी (एकूण ६३ महसुली गावे)</div>
                <div class="beat-box">
                    <div class="beat-title b1"><span>बीट १ - महागांव</span><span>(२० गावे)</span></div>
                    १. महागांव, २. कोरखंडे, ३. वाशी आदिवासीवाडी, ४. फळशेत/कर्नाळा, ५. कळमशेत, ६. बोरघर, ७. विनवली, ८. निगुडशेत, ९. काकडशेत, १०. पाचघर, ११. बोरघर आ.वाडी, १२. भानंग, १३. भानंगकोंड, १४. सोनसडे, १५. वाशी, १६. किस्तकेतकी, १७. कळसांबडे, १८. साईधाम/साळशेत, १९. निगुडशेत आ.वाडी, २०. गौळवाडी.
                </div>
                <div class="beat-box">
                    <div class="beat-title b2"><span>बीट २ - तळेगांव</span><span>(१९ गावे)</span></div>
                    १. तळेगांव, २. पन्हेळी, ३. तांबडी, ४. खैराट, ५. वांजळोशी, ६. चोरवली, ७. मालुक, ८. बेलघर, ९. कासेखोल, १०. चोरवली बौद्धवाडी, ११. चरई खुर्द, १२. उसर खुर्द, १३. चरई बुद्रुक, १४. लालमाती आ.वाडी, १५. बोरीचा माळ, १६. वानास्ते, १७. वावे मांद्रज, १८. दहिवली, १९. चरई आ.वाडी.
                </div>
                <div class="beat-box">
                    <div class="beat-title b3"><span>बीट ३ - राहाटाड</span><span>(२७ गावे/वाड्या)</span></div>
                    १. राहाटाड, २. राहाटाड धनगरवाडी, ३. राहाटाड आ.वाडी, ४. तारणे, ५. कुंबेट, ६. कुंबेट आ.वाडी, ७. शेणवली, ८. कासेवाडी, ९. ताम्हणे, १०. खांबीवली, ११. कुंबळे, १२. शेणाटे, १३. पिटसई, १४. कडक्याचीवाडी, १५. पिटसई मुळगाव, १६. बोरमाळ आ.वाडी, १७. मांदाड, १८. कुडा, १९. शिव आ.वाडी, २०. रोवला, २१. वाशी हवेली, २२. वरळ.
                </div>
                <div class="beat-box" style="border-bottom:none;">
                    <div class="beat-title b4"><span>बीट ४ - मांदाड / तळा</span><span>(२३ गावे/वाड्या)</span></div>
                    १. तळा शहर, २. मांदाड, ३. वडाची वाडी, ४. मेढा, ५. पढवण, ६. गिरणे, ७. तारणे, ८. वावे हवेली, ९. टोकार्डे, १०. राणेची वाडी, ११. आंबीवली, १२. आनंदवाडी, १३. मेढा वाघवाडी, १४. म्हसाडी, १५. नानवली, १६. जोगवाडी, १७. नवघर, १८. बामणघर, १९. कोणथरे, २०. मालाठे.<br>
                    <b style="color:#b91c1c;">★ बीट मदत केंद्र: मांदाड स्वतंत्र चेकपोस्ट</b>
                </div>
            </div>

            <!-- मधला भाग: तळा तालुक्याचा नकाशा (SVG) -->
            <div class="map-container">
                <svg viewBox="0 0 760 760" width="100%" height="100%">
                    <!-- बाहेरील दिशा व सीमा -->
                    <text x="360" y="32" font-size="18" font-weight="bold" fill="#1e3a8a" text-anchor="middle">⬆ रोहा तालुका (रोह्याकडे)</text>
                    <text x="640" y="95" font-size="17" font-weight="bold" fill="#1e3a8a" text-anchor="middle">माणगांव तालुका ↗</text>
                    <text x="645" y="118" font-size="15" font-weight="bold" fill="#b91c1c" text-anchor="middle">(माणगांव / इंदापूरकडे)</text>
                    <text x="690" y="425" font-size="16" font-weight="bold" fill="#b91c1c" text-anchor="middle">खरवलीकडे ➡</text>
                    <text x="640" y="575" font-size="16" font-weight="bold" fill="#b91c1c" text-anchor="middle">↘ कुडूकीकडे</text>
                    <text x="410" y="735" font-size="18" font-weight="bold" fill="#1e3a8a" text-anchor="middle">⬇ म्हसला तालुका (म्हसल्याकडे)</text>
                    <text x="95" y="380" font-size="18" font-weight="bold" fill="#1e3a8a" text-anchor="middle">⬅ मुरुड तालुका</text>
                    <text x="95" y="402" font-size="14" font-weight="bold" fill="#0369a1" text-anchor="middle">(खाडीपलीकडे)</text>

                    <!-- खाडी / जलाशय (पश्चिम बाजू) -->
                    <path d="M 120,240 Q 155,310 150,410 Q 145,520 215,670 L 175,690 Q 110,540 105,410 Q 100,300 90,250 Z" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>

                    <!-- बीट ४: मांदाड / तळा (उत्तर-पश्चिम) -->
                    <path d="M 150,145 L 285,135 L 350,95 L 385,295 L 365,375 L 250,365 L 155,260 Z" fill="#bbf7d0" stroke="#15803d" stroke-width="3"/>

                    <!-- बीट १: महागांव (उत्तर-पूर्व) -->
                    <path d="M 350,95 L 450,80 L 495,155 L 595,215 L 645,285 L 610,435 L 510,430 L 385,295 Z" fill="#fde047" stroke="#ca8a04" stroke-width="3"/>

                    <!-- बीट ३: राहाटाड (दक्षिण-पश्चिम) -->
                    <path d="M 155,260 L 250,365 L 365,375 L 340,465 L 350,625 L 250,685 L 200,590 L 150,410 Z" fill="#7dd3fc" stroke="#0369a1" stroke-width="3"/>

                    <!-- बीट २: तळेगांव (दक्षिण-पूर्व) -->
                    <path d="M 365,375 L 385,295 L 510,430 L 570,565 L 535,685 L 440,665 L 350,625 L 340,465 Z" fill="#e9d5ff" stroke="#7e22ce" stroke-width="3"/>

                    <!-- प्रमुख रस्ते ( लाल रेषा ) -->
                    <path d="M 355,60 L 390,320 L 635,250" fill="none" stroke="#dc2626" stroke-width="5"/>
                    <path d="M 160,310 L 390,320 L 470,695" fill="none" stroke="#dc2626" stroke-width="5"/>
                    <path d="M 390,320 L 595,460" fill="none" stroke="#dc2626" stroke-width="3.5" stroke-dasharray="7,5"/>

                    <!-- तळा पोलीस ठाणे मुख्य केंद्र -->
                    <circle cx="390" cy="320" r="10" fill="#dc2626" stroke="#ffffff" stroke-width="2.5"/>
                    <rect x="355" y="285" width="75" height="24" rx="5" fill="#dc2626"/>
                    <text x="392" y="302" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">★ तळा</text>

                    <!-- बीटची मुख्य नावे (नकाशावर) -->
                    <text x="275" y="215" font-size="21" font-weight="bold" fill="#14532d" text-anchor="middle">बीट ४ - मांदाड</text>
                    <text x="495" y="255" font-size="21" font-weight="bold" fill="#713f12" text-anchor="middle">बीट १ - महागांव</text>
                    <text x="255" y="485" font-size="21" font-weight="bold" fill="#0c4a6e" text-anchor="middle">बीट ३ - राहाटाड</text>
                    <text x="445" y="535" font-size="21" font-weight="bold" fill="#4c1d95" text-anchor="middle">बीट २ - तळेगांव</text>

                    <!-- प्रमुख गावांची नावे नकाशात -->
                    <!-- बीट १ गावे -->
                    <text x="415" y="135" font-size="13.5" font-weight="bold" fill="#1f2937">• कोरखंडे</text>
                    <text x="415" y="170" font-size="13.5" font-weight="bold" fill="#1f2937">• वाशी</text>
                    <text x="440" y="205" font-size="13.5" font-weight="bold" fill="#1f2937">• फळशेत</text>
                    <text x="510" y="195" font-size="13.5" font-weight="bold" fill="#1f2937">• कळमशेत</text>
                    <text x="425" y="245" font-size="13.5" font-weight="bold" fill="#1f2937">• बोरघर</text>
                    <text x="545" y="285" font-size="13.5" font-weight="bold" fill="#1f2937">• पाचघर</text>
                    <text x="565" y="325" font-size="13.5" font-weight="bold" fill="#1f2937">• भानंग</text>
                    <text x="550" y="365" font-size="13.5" font-weight="bold" fill="#1f2937">• सोनसडे</text>
                    <text x="540" y="410" font-size="13.5" font-weight="bold" fill="#1f2937">• गौळवाडी</text>

                    <!-- बीट ४ गावे -->
                    <text x="190" y="185" font-size="13.5" font-weight="bold" fill="#1f2937">• मांदाड</text>
                    <text x="295" y="175" font-size="1
