import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# Streamlit Page Config
st.set_page_config(page_title="Tala Police Beat Map", layout="wide")

st.title("🛡️ Raigad Police - Tala Police Station Beat Map")
st.write("Official Tala Taluka Beat Map with village list and officer directory.")

@st.cache_data
def generate_beat_map():
    # 1. Canvas Setup
    width, height = 2400, 1400
    background_color = (245, 240, 230)
    
    img = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(img)
    
    # 2. Header Section
    draw.rectangle([0, 0, width, 160], fill=(20, 35, 80))
    
    # Safe Fallback to Default Font to prevent cloud deployment crashes
    font = ImageFont.load_default()

    # Header Titles (Using standard draw.text without complex truetype paths)
    draw.text((width // 2 - 350, 40), "RAIGAD POLICE | TALA POLICE STATION", fill=(255, 255, 255), font=font)
    draw.text((width // 2 - 400, 110), "TAL. TALA, DIST. RAIGAD — POLICE BEAT MAP (BEAT 1-4)", fill=(220, 220, 220), font=font)

    # 3. Left Panel: Village & Beat Classification
    draw.rectangle([50, 200, 700, 1250], fill=(255, 255, 255), outline=(20, 35, 80), width=4)
    draw.rectangle([50, 200, 700, 280], fill=(20, 35, 80))
    draw.text((120, 230), "VILLAGE AND BEAT CLASSIFICATION", fill=(255, 255, 255), font=font)

    left_text = (
        "BEAT 1 - MAHAGAON:\n"
        "• Mahagaon, Borkhande, Vashi, Phalshet/\n"
        "  Karnala, Kalamshet, Borghar, Vinavali\n"
        "• Nigudshet, Kakadshet, Pachghar,\n"
        "  Bhanang, Sonsade, Salshet, Gaonwadi\n\n"
        "BEAT 2 - TALEGAON:\n"
        "• Talegaon, Panheli, Tambadi, Khairat,\n"
        "  Vanjaloshi, Choriwali, Maluk, Belghar\n"
        "• Kasekhol, Charai Kh., Usar Kh., Boricha Mal\n\n"
        "BEAT 3 - RAHATAD:\n"
        "• Rahatad, Kumbet, Shenavali, Kasewadi,\n"
        "  Pitsai Mulgaon, Vashi Haveli, Varal\n"
        "• Rovala, Kuda, Kadkyachigani, Shende\n\n"
        "BEAT 4 - MANDAD:\n"
        "• Mandad, Tala City, Vadachi Wadi, Medha,\n"
        "  Padvan, Girane, Tarane, Vave Haveli\n"
        "• Tokarde, Raneci Wadi, Ambivoli, Jogwadi"
    )
    draw.text((80, 320), left_text, fill=(30, 30, 30), font=font)

    # 4. Right Panel: Officer Contact Directory
    draw.rectangle([1700, 200, 2350, 1250], fill=(255, 255, 255), outline=(20, 35, 80), width=4)
    draw.rectangle([1700, 200, 2350, 280], fill=(20, 35, 80))
    draw.text((1780, 230), "OFFICER CONTACT DIRECTORY", fill=(255, 255, 255), font=font)

    right_text = (
        "BEAT 1 (MAHAGAON):\n"
        "• P.S.I. Nilesh Kadam : 9764823920\n"
        "• P.H.C. Sagar Rohekar : 8237531896\n"
        "• P.H.C. Sunil Khandare : 7261941644\n"
        "• P.C. Prashant Dahifale : 7498823826\n\n"
        "BEAT 2 (TALEGAON):\n"
        "• P.S.I. Nilesh Kadam : 9764823920\n"
        "• P.H.C. Babasaheb Jadhav : 8237531896\n"
        "• P.H.C. Umesh Pawar : 7261941644\n"
        "• W.P.C. Payal Giri : 7498823826\n\n"
        "BEAT 3 (RAHATAD):\n"
        "• P.S.I. Shri. Bansode : 9764823920\n"
        "• P.S.I. S. G. Gaikwad : 8237531896\n"
        "• P.H.C. Milind Khirit : 7261941644\n"
        "• W.P.C. Rutuja Borade : 7261941644\n\n"
        "BEAT 4 (MANDAD):\n"
        "• P.N. Gurunath Banmande : 9764823920\n"
        "• P.H.C. Ramhari Waghmare : 8237531896\n"
        "• M.P.H.C. Aarti Pawar : 7261941644\n"
        "• M.P.C. Pooja Gawade : 7498823826"
    )
    draw.text((1730, 320), right_text, fill=(30, 30, 30), font=font)

    # 5. Center Map Placeholder Box
    draw.rectangle([750, 200, 1650, 1150], fill=(235, 245, 255), outline=(100, 150, 200), width=3)
    draw.text((950, 650), "[ TALA TALUKA BEAT MAP GRAPHIC ]\n(Mahagaon, Talegaon, Rahatad, Mandad)", fill=(50, 80, 120), font=font)

    # 6. Footer / Station Helpdesk
    draw.rectangle([750, 1180, 1650, 1250], fill=(20, 35, 80))
    draw.text((850, 1205), "TALA POLICE STATION | PHONE: 02140-269033 | EMERGENCY: 112", fill=(255, 255, 255), font=font)

    return img

# Generate Image
map_image = generate_beat_map()

# Display on Streamlit App
st.image(map_image, caption="Tala Police Station Beat Map", use_container_width=True)

# Add Download Button
buf = io.BytesIO()
map_image.save(buf, format="PNG")
byte_im = buf.getvalue()

st.download_button(
    label="📥 Download Beat Map Image",
    data=byte_im,
    file_name="tala_police_beat_map.png",
    mime="image/png"
)
