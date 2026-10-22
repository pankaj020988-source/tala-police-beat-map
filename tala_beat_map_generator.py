import os
from PIL import Image, ImageDraw, ImageFont

def create_tala_beat_map():
    # 1. Canvas Setup (Standard Flex/Banner Ratio)
    width, height = 2400, 1400
    background_color = (245, 240, 230) # Classic cream/light professional background
    
    # Create base image
    img = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(img)
    
    # 2. Header Section (Dark Blue Police Theme)
    draw.rectangle([0, 0, width, 160], fill=(20, 35, 80))
    
    # Fonts (Using default high-res or system path if available)
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 55)
        font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
        font_header = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    except:
        font_title = font_subtitle = font_header = font_body = ImageFont.load_default()

    # Header Titles
    draw.text((width // 2, 40), "RAIGAD POLICE | TALA POLICE STATION", fill=(255, 255, 255), anchor="mm", font=font_title)
    draw.text((width // 2, 110), "TAL. TALA, DIST. RAIGAD — POLICE BEAT MAP (BEAT 1-4)", fill=(220, 220, 220), anchor="mm", font=font_subtitle)

    # 3. Left Panel: Village & Beat Classification
    draw.rectangle([50, 200, 700, 1250], fill=(255, 255, 255), outline=(20, 35, 80), width=4)
    draw.rectangle([50, 200, 700, 280], fill=(20, 35, 80))
    draw.text((375, 240), "VILLAGE AND BEAT CLASSIFICATION", fill=(255, 255, 255), anchor="mm", font=font_header)

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
    draw.text((75, 310), left_text, fill=(30, 30, 30), font=font_body)

    # 4. Right Panel: Officer Contact Directory (No Hidden Numbers)
    draw.rectangle([1700, 200, 2350, 1250], fill=(255, 255, 255), outline=(20, 35, 80), width=4)
    draw.rectangle([1700, 200, 2350, 280], fill=(20, 35, 80))
    draw.text((2025, 240), "OFFICER CONTACT DIRECTORY", fill=(255, 255, 255), anchor="mm", font=font_header)

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
        "• W.P.C. Rutuja Borade : 7498823826\n\n"
        "BEAT 4 (MANDAD):\n"
        "• P.N. Gurunath Banmande : 9764823920\n"
        "• P.H.C. Ramhari Waghmare : 8237531896\n"
        "• M.P.H.C. Aarti Pawar : 7261941644\n"
        "• M.P.C. Pooja Gawade : 7498823826"
    )
    draw.text((1725, 310), right_text, fill=(30, 30, 30), font=font_body)

    # 5. Center Map Placeholder Box (Where Map Graphic sits)
    draw.rectangle([750, 200, 1650, 1150], fill=(235, 245, 255), outline=(100, 150, 200), width=3)
    draw.text((1200, 650), "[ TALA TALUKA BEAT MAP GRAPHIC ]\n(Mahagaon, Talegaon, Rahatad, Mandad)", fill=(50, 80, 120), anchor="mm", font=font_header)

    # 6. Footer / Station Helpdesk
    draw.rectangle([750, 1180, 1650, 1250], fill=(20, 35, 80))
    draw.text((1200, 1215), "TALA POLICE STATION | PHONE: 02140-269033 | EMERGENCY: 112", fill=(255, 255, 255), anchor="mm", font=font_header)

    # Save output
    output_path = "tala_police_beat_map.png"
    img.save(output_path)
    print(f"Map successfully generated and saved to {output_path}")

if __name__ == "__main__":
    create_tala_beat_map()
