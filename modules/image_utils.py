from PIL import Image

def inserir_imagem(draw_canvas, img_path, pos, ocupados, base_width=1080, base_height=1920):
    img = Image.open(img_path).convert("RGBA")

    w, h, x, y = pos['W'], pos['H'], pos['X'], pos['Y']
    x = min(max(0, x), base_width - w)
    y = min(max(0, y), base_height - h)

    if w <= 0 or h <= 0:
        return False

    new_rect = (x, y, x + w, y + h)

    for rect in ocupados:
        if not (new_rect[2] <= rect[0] or new_rect[0] >= rect[2] or
                new_rect[3] <= rect[1] or new_rect[1] >= rect[3]):
            return False

    ocupados.append(new_rect)

    img = img.resize((w, h))
    draw_canvas.paste(img, (x, y), img)
    return True
