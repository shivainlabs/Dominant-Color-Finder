from PIL import Image, ImageDraw

def create_color_palette(dominant_colors,palette_size=(300,50)):
    # create an image to display the colors
    palette = Image.new("RGB",palette_size)
    draw = ImageDraw.Draw(palette)
    
    # calculate the width of each color swatch
    swatch_width = palette_size[0] // len(dominant_colors)
    
    # Draw each color as a rectangle on the palette
    for i, color in enumerate(dominant_colors):
        draw.rectangle([i * swatch_width,0,(i+1) * swatch_width, palette_size[1]], fill=tuple(color))
    
    return palette