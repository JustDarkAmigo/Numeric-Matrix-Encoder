import tkinter as tk

# Ввод числа
number_to_encode = -12345678   # пример отрицательного числа

class EncodingGrid:
    def __init__(self, num):
        self.root = tk.Tk()
        self.root.title("Кодирование числа в сетке 13x13")
        self.cell_size = 30
        self.n = 13

        canvas_size = self.n * self.cell_size
        self.canvas = tk.Canvas(self.root, width=canvas_size, height=canvas_size, bg='white')
        self.canvas.pack(padx=10, pady=(10, 5))

        self.draw_grid()
        self.encode(num)

        # Отображение числа внизу
        self.label = tk.Label(self.root, text=f"Число: {num}", font=('Arial', 12))
        self.label.pack(pady=(0, 10))

    def draw_grid(self):
        for i in range(self.n + 1):
            coord = i * self.cell_size
            self.canvas.create_line(coord, 0, coord, self.n * self.cell_size, fill='gray')
            self.canvas.create_line(0, coord, self.n * self.cell_size, coord, fill='gray')

    def fill_cell(self, row, col, color='black'):
        x1 = (col - 1) * self.cell_size + 1
        y1 = (row - 1) * self.cell_size + 1
        x2 = col * self.cell_size - 1
        y2 = row * self.cell_size - 1
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='', tags='fill')

    def encode(self, num):
        if num < 0:
            self.fill_cell(7, 7, color='black')
            num = -num

        digits = [int(d) for d in str(num)[::-1]]
        if len(digits) > 8:
            digits = digits[:8]

        seq1 = [(1,1), (3,1), (2,2), (1,3), (5,1), (4,2), (3,3), (2,4), (1,5)]
        seq2 = [(6,6), (6,4), (5,5), (4,6), (6,2), (5,3), (4,4), (3,5), (2,6)]

        shifts = {0: (0,0), 2: (0,7), 4: (7,0), 6: (7,7)}

        for i in range(8):
            digit = digits[i] if i < len(digits) else 0
            base_seq = seq1 if i % 2 == 0 else seq2
            drow, dcol = shifts[(i // 2) * 2]
            for j in range(min(digit, len(base_seq))):
                r, c = base_seq[j]
                self.fill_cell(r + drow, c + dcol)

if __name__ == "__main__":
    app = EncodingGrid(number_to_encode)
    app.root.mainloop()
