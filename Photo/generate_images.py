import random
from PIL import Image, ImageDraw, ImageFont

n = 10 # сколько случайных чисел сгенерировать
cell_size = 30
grid_size = 13

text_area_height = 40
img_size_grid = grid_size * cell_size
img_width = img_size_grid
img_height = img_size_grid + text_area_height

try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

def get_filled_cells(number):
    filled = []
    if number < 0:
        filled.append((7, 7))
        num = -number
    else:
        num = number

    digits = [int(d) for d in str(num)[::-1]]
    if len(digits) > 8:
        digits = digits[:8]

    seq1 = [(1,1), (3,1), (2,2), (1,3), (5,1), (4,2), (3,3), (2,4), (1,5)]
    seq2 = [(6,6), (6,4), (5,5), (4,6), (6,2), (5,3), (4,4), (3,5), (2,6)]

    shifts = {0: (0,0), 2: (0,7), 4: (7,0), 6: (7,7)}

    for i in range(8):
        digit = digits[i] if i < len(digits) else 0
        base_seq = seq1 if i % 2 == 0 else seq2
        dr, dc = shifts[(i // 2) * 2]
        for j in range(min(digit, len(base_seq))):
            r, c = base_seq[j]
            filled.append((r + dr, c + dc))

    return filled


def draw_grid_and_text(image, filled_cells, number):
    draw = ImageDraw.Draw(image)

    for r, c in filled_cells:
        x1 = (c - 1) * cell_size + 1
        y1 = (r - 1) * cell_size + 1
        x2 = c * cell_size - 1
        y2 = r * cell_size - 1
        draw.rectangle([x1, y1, x2, y2], fill='black')

    for i in range(grid_size + 1):
        coord = i * cell_size
        draw.line([(coord, 0), (coord, img_size_grid)], fill='gray', width=1)
        draw.line([(0, coord), (img_size_grid, coord)], fill='gray', width=1)

    text = f"Число: {number}"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x_text = (img_width - text_w) // 2
    y_text = img_size_grid + (text_area_height - text_h) // 2
    draw.text((x_text, y_text), text, fill='black', font=font)

    return image


if __name__ == "__main__":
    for idx in range(1, n + 1):
        number = random.randint(-99_999_999, 99_999_999)

        img = Image.new('RGB', (img_width, img_height), 'white')
        cells = get_filled_cells(number)
        draw_grid_and_text(img, cells, number)

        filename = f"encoded_{number}.png"
        img.save(filename)
