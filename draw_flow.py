from PIL import Image, ImageDraw, ImageFont
import os

def create_flowchart():
    # Image size
    width, height = 1200, 1000
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Colors
    primary = (99, 102, 241)  # Indigo
    text_color = (31, 41, 55)
    bg_box = (243, 244, 246)
    
    # Load Font
    try:
        font = ImageFont.truetype("arial.ttf", 24)
        title_font = ImageFont.truetype("arial.ttf", 32)
    except:
        font = ImageFont.load_default()
        title_font = ImageFont.load_default()

    def draw_box(x, y, w, h, text, shape="rect", color=bg_box):
        if shape == "pill":
            draw.rounded_rectangle([x, y, x+w, y+h], radius=h//2, fill=color, outline=primary, width=3)
        elif shape == "diamond":
            points = [(x+w//2, y), (x+w, y+h//2), (x+w//2, y+h), (x, y+h//2)]
            draw.polygon(points, fill=color, outline=primary, width=3)
        else:
            draw.rectangle([x, y, x+w, y+h], fill=color, outline=primary, width=3)
        
        # Center Text
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
        draw.text((x + (w-tw)//2, y + (h-th)//2), text, fill=text_color, font=font)

    def draw_arrow(x1, y1, x2, y2):
        draw.line([x1, y1, x2, y2], fill=primary, width=3)
        # Simple Arrow head
        if x1 == x2: # Vertical
            draw.line([x2-10, y2-10, x2, y2], fill=primary, width=3)
            draw.line([x2+10, y2-10, x2, y2], fill=primary, width=3)
        elif y1 == y2: # Horizontal
            draw.line([x2-10, y2-10, x2, y2], fill=primary, width=3)
            draw.line([x2-10, y2+10, x2, y2], fill=primary, width=3)

    # Title
    draw.text((width//2 - 120, 50), "CAMPUS LEDGER FLOW", fill=primary, font=title_font)

    # 1. Start
    draw_box(width//2-100, 120, 200, 60, "START", "pill")
    draw_arrow(width//2, 180, width//2, 220)

    # 2. Login
    draw_box(width//2-150, 220, 300, 80, "USER LOGIN / SIGNUP", "diamond")
    
    # Branches
    draw.line([width//2 - 150, 260, 300, 260], fill=primary, width=3) # To Student
    draw.line([width//2 + 150, 260, 900, 260], fill=primary, width=3) # To Admin
    
    draw_arrow(300, 260, 300, 320)
    draw_arrow(900, 260, 900, 320)

    # Student Path
    draw_box(150, 320, 300, 60, "STUDENT DASHBOARD")
    draw_arrow(300, 380, 300, 420)
    draw_box(150, 420, 300, 60, "Explore Campus Clubs")
    draw_arrow(300, 480, 300, 520)
    draw_box(150, 520, 300, 60, "Book Events & Tickets")
    draw_arrow(300, 580, 300, 620)
    draw_box(150, 620, 300, 60, "MetaMask Payment")

    # Admin Path
    draw_box(750, 320, 300, 60, "ADMIN PANEL")
    draw_arrow(900, 380, 900, 420)
    draw_box(750, 420, 300, 60, "Create & Manage Events")
    draw_arrow(900, 480, 900, 520)
    draw_box(750, 520, 300, 60, "Track Student Bookings")
    draw_arrow(900, 580, 900, 620)
    draw_box(750, 620, 300, 60, "Manage Club Treasury")

    # Merge to Verification
    draw.line([300, 680, 300, 740], fill=primary, width=3)
    draw.line([900, 680, 900, 740], fill=primary, width=3)
    draw.line([300, 740, 900, 740], fill=primary, width=3)
    draw_arrow(width//2, 740, width//2, 780)
    
    draw_box(width//2-200, 780, 400, 80, "BLOCKCHAIN VERIFICATION", color=(219, 234, 254))
    
    draw_arrow(width//2, 860, width//2, 900)
    draw_box(width//2-100, 900, 200, 60, "END", "pill")

    img.save('c:/Users/LENOVO/OneDrive/Desktop/CampusLedger/flowchart.png')
    print("Flowchart saved to flowchart.png")

create_flowchart()
