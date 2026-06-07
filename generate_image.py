"""
Generate a placeholder image for the verification success screen.
Run this script once to create the result-image.png file.
"""

from PIL import Image, ImageDraw
import os

def generate_placeholder_image(output_path='static/result-image.png'):
    """
    Create a simple celebration-themed placeholder image with Instagram-inspired colors.
    """
    # Image dimensions
    width, height = 400, 400
    
    # Create image with gradient background
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image, 'RGBA')
    
    # Draw gradient background (pink to purple)
    for y in range(height):
        # Interpolate between pink and purple
        r = int(228 + (131 - 228) * (y / height))  # 228 to 131
        g = int(64 + (171 - 64) * (y / height))    # 64 to 171
        b = int(95 + (180 - 95) * (y / height))    # 95 to 180
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Draw checkmark circle
    circle_x, circle_y = width // 2, height // 2
    circle_radius = 80
    
    # White circle background
    draw.ellipse(
        [circle_x - circle_radius, circle_y - circle_radius,
         circle_x + circle_radius, circle_y + circle_radius],
        fill=(255, 255, 255),
        outline=(255, 255, 255)
    )
    
    # Draw checkmark (green color)
    check_color = (0, 215, 0)  # Bright green
    check_width = 8
    
    # Checkmark points (simplified design)
    # Start point (left)
    start_x = circle_x - 30
    start_y = circle_y + 10
    
    # Middle point (bottom)
    mid_x = circle_x - 10
    mid_y = circle_y + 30
    
    # End point (top right)
    end_x = circle_x + 40
    end_y = circle_y - 20
    
    # Draw checkmark lines
    draw.line([(start_x, start_y), (mid_x, mid_y)], fill=check_color, width=check_width)
    draw.line([(mid_x, mid_y), (end_x, end_y)], fill=check_color, width=check_width)
    
    # Draw decorative stars
    def draw_star(x, y, size, color):
        """Draw a simple star at position (x, y)"""
        angle_step = 72  # 360 / 5 points
        points = []
        for i in range(10):
            angle = (i * angle_step - 90) * 3.14159 / 180
            if i % 2 == 0:
                r = size
            else:
                r = size * 0.4
            px = x + r * (3.14159 * 2 * i / 360) ** 0.5 * (3.14159 / 2.5)
            py = y + r * (3.14159 * 2 * i / 360) ** 0.5 * (3.14159 / 2.5)
            points.append((px, py))
        
        # Simplified star - just draw a diamond
        diamond_size = size
        draw.polygon(
            [(x, y - diamond_size), (x + diamond_size, y),
             (x, y + diamond_size), (x - diamond_size, y)],
            fill=color
        )
    
    # Draw decorative elements
    draw_star(circle_x - 120, circle_y - 80, 12, (255, 200, 0))
    draw_star(circle_x + 120, circle_y - 80, 12, (255, 150, 0))
    draw_star(circle_x - 100, circle_y + 120, 10, (255, 200, 0))
    draw_star(circle_x + 100, circle_y + 120, 10, (255, 150, 0))
    
    # Save image
    os.makedirs('static', exist_ok=True)
    image.save(output_path, 'PNG')
    print(f"✓ Placeholder image created: {output_path}")

if __name__ == '__main__':
    generate_placeholder_image()
