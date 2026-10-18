from PIL import Image, ImageDraw, ImageFont
import os

def create_flowchart_v2():
    # Image size
    width, height = 1200, 1100
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Colors (Strictly Black and White)
    primary = (0, 0, 0)
    bg_box = (255, 255, 255)
    
    # Load Font
    try:
        font = ImageFont.truetype("arial.ttf", 22)
        title_font = ImageFont.truetype("arial.ttf", 28)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()

    def draw_box(x, y, w, h, text, shape="rect"):
        if shape == "pill":
            draw.rounded_rectangle([x, y, x+w, y+h], radius=h//2, fill=bg_box, outline=primary, width=2)
        elif shape == "diamond":
            points = [(x+w//2, y), (x+w, y+h//2), (x+w//2, y+h), (x, y+h//2)]
            draw.polygon(points, fill=bg_box, outline=primary, width=2)
        else:
            draw.rectangle([x, y, x+w, y+h], fill=bg_box, outline=primary, width=2)
        
        # Multiline text center
        lines = text.split('\n')
        total_text_h = len(lines) * 25
        for i, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=font)
            tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
            draw.text((x + (w-tw)//2, y + (h-total_text_h)//2 + i*25), line, fill=primary, font=font)

    def draw_arrow(x1, y1, x2, y2):
        draw.line([x1, y1, x2, y2], fill=primary, width=2)
        # Simple Arrow head
        if x1 == x2: # Vertical
            draw.line([x2-8, y2-8, x2, y2], fill=primary, width=2)
            draw.line([x2+8, y2-8, x2, y2], fill=primary, width=2)
        elif y1 == y2: # Horizontal
            draw.line([x2-8, y2-8, x2, y2], fill=primary, width=2)
            draw.line([x2-8, y2+8, x2, y2], fill=primary, width=2)

    # Title
    draw.text((width//2 - 150, 40), "CAMPUS LEDGER - SYSTEM FLOW", fill=primary, font=title_font)

    # 1. Start
    draw_box(width//2-80, 100, 160, 50, "START", "pill")
    draw_arrow(width//2, 150, width//2, 190)

    # 2. Landing Page
    draw_box(width//2-120, 190, 240, 60, "LANDING PAGE")
    draw_arrow(width//2, 250, width//2, 290)

    # 3. Role Selection
    draw_box(width//2-150, 290, 300, 80, "SELECT ROLE\n(Student or Admin)", "diamond")
    
    # Branches
    draw.line([width//2 - 150, 330, 300, 330], fill=primary, width=2) # To Student
    draw.line([width//2 + 150, 330, 900, 330], fill=primary, width=2) # To Admin
    
    draw_arrow(300, 330, 300, 380)
    draw_arrow(900, 330, 900, 380)

    # Student path
    draw_box(150, 380, 300, 60, "STUDENT LOGIN / SIGNUP")
    draw_arrow(300, 440, 300, 480)
    draw_box(150, 480, 300, 60, "STUDENT DASHBOARD")
    draw_arrow(300, 540, 300, 580)
    draw_box(150, 580, 300, 80, "EXPLORE CLUBS &\nVIEW EVENTS")
    draw_arrow(300, 660, 300, 700)
    draw_box(150, 700, 300, 60, "BOOK EVENT TICKET")
    draw_arrow(300, 760, 300, 800)
    draw_box(150, 800, 300, 60, "METAMASK PAYMENT")

    # Admin path
    draw_box(750, 380, 300, 60, "ADMIN LOGIN / SIGNUP")
    draw_arrow(900, 440, 900, 480)
    draw_box(750, 480, 300, 60, "ADMIN PANEL")
    draw_arrow(900, 540, 900, 580)
    draw_box(750, 580, 300, 80, "CREATE & MANAGE\nEVENTS")
    draw_arrow(900, 660, 900, 700)
    draw_box(750, 700, 300, 60, "MANAGE CLUB TREASURY")
    draw_arrow(900, 760, 900, 800)
    draw_box(750, 800, 300, 60, "TRACK STUDENT BOOKINGS")

    # Merge to Verification
    draw.line([300, 860, 300, 900], fill=primary, width=2)
    draw.line([900, 860, 900, 900], fill=primary, width=2)
    draw.line([300, 900, 900, 900], fill=primary, width=2)
    draw_arrow(width//2, 900, width//2, 930)
    
    draw_box(width//2-200, 930, 400, 70, "BLOCKCHAIN VERIFICATION")
    
    draw_arrow(width//2, 1000, width//2, 1030)
    draw_box(width//2-100, 1030, 200, 50, "END", "pill")

    img.save('c:/Users/LENOVO/OneDrive/Desktop/CampusLedger/flowchart_bw.png')
    print("B&W Flowchart saved to flowchart_bw.png")

create_flowchart_v2()
