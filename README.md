[English](#english) | [Русский](#russian)

<a name="russian"></a>
## Русский
Демонстрация алгоритма кодирования любого целого числа в диапозоне $$(-10^9, 10^9)$$

### Установка
1. Клонируем репозиторий
``` bash
git clone https://github.com/JustDarkAmigo/Numeric-Matrix-Encoder.git
cd Numeric-Matrix-Encoder
```
1. Установка зависимостей
``` bash
pip install -r requirements.txt
```
### Запуск
1. Откройте файл main.py;
2. Поменяйте значение переменной 'number_to_encode' на любое в пределах $$(-10^9, 10^9)$$

3. запустите файл.

``` bash
python main.py
```

### Алгоритм
- Создается поле 13x13 ячеек с пустой горизонтальной линией на высоте 7 (от левого верхнего угла) и вертикальная на расстоянии 7
- Каждое число в алгоритме делится на положительное и отрицательное. Отрицательное число будет помечено заполненным квадратом в точке (7, 7)
- Число делится на разряды (цифры, десятки, сотни, тысячи...): 
	- **Пара первых 2 разрядов** (цифры и десятки) кодируются в квадрате от (1,1) до (6,6), 
	- **Вторые 2 разряда** (сотни, тысячи) кодируются в квадрате от (8, 1) до (13, 6) (то есть справа от первого квадрата)
	- **Третья пара разрядов** (десятки тысяч, сотни тысяч) кодируется в квадрате от (1,8) до (6,13) — это левый нижний угол сетки.
	- **Четвёртая пара разрядов** (миллионы, десятки миллионов) кодируется в квадрате от (8,8) до (13,13) — правый нижний угол.
Таким образом, сетка 13×13 разбивается на четыре непересекающихся блока размером 6×6.
Внутри каждого блока (6×6) закодированы **две цифры**:
- **Чётная позиция** (младшая из пары) использует последовательность координат:  
    *(1,1), (3,1), (2,2), (1,3), (5,1), (4,2), (3,3), (2,4), (1,5)* — это 9 точек, расположенных в форме «змейки» или лесенки.
- **Нечётная позиция** (старшая из пары) использует последовательность:  
    *(6,6), (6,4), (5,5), (4,6), (6,2), (5,3), (4,4), (3,5), (2,6)* — симметричное отражение относительно центра блока.

Цифра от 0 до 9 кодируется закрашиванием первых N ячеек из соответствующей последовательности.

###   Структура проекта
```text
.
├── main.py                   # Точка входа (выберите примеры здесь)
├── Photo/                    # Готовые снимки закодированных числе
│   ├── encoded_22918726.png  # Число 22 918 726
│   └── generate_images.py    # файл для автогенерации таких изображений
└── requirements.txt          # Зависимости
```

<a name="english"></a>
## English
Demonstration of an algorithm for encoding any integer in the range from $$-1 *10^9$$ to $$1 * 10^{9}$$




### Installation
1. Clone the repository
``` bash
git clone https://github.com/JustDarkAmigo/Numeric-Matrix-Encoder.git
cd Numeric-Matrix-Encoder
```
1. Installing dependencies
``` bash
pip install -r requirements.txt
```

``
### Usage
1. Open the file main.py
2. Select the operating mode in the function

3. Run the file
``` bash
python main.py
```

### Algorithm
- A 13x13 cell field is created with an empty horizontal line at a height of 7 (from the upper-left corner) and a vertical line at a distance of 7
. Each number in the algorithm is divided into positive and negative. A negative number will be marked with a filled square at the point (7, 7)
- The number is divided into digits (digits, tens, hundreds, thousands...):
- **The pair of the first 2 digits** (digits and tens) are encoded in a square from (1,1) to (6,6), 
	- **The second 2 digits** (hundreds, thousands) are encoded in a square from (8, 1) to (13, 6) (that is, to the right of the first square)
	- **The third pair of digits** (tens of thousands, hundreds of thousands) is encoded in a square from (1,8) to (6,13) — this is the lower-left corner of the grid.
	- **The fourth pair of digits** (millions, tens of millions) is encoded in the square from (8,8) to (13,13) — lower right corner.
Thus, the 13x13 grid is divided into four disjoint 6x6 blocks.
**Two digits** are encoded inside each block (6×6):
- **The even position** (the lowest of the pair) uses a sequence of coordinates:  
    *(1,1), (3,1), (2,2), (1,3), (5,1), (4,2), (3,3), (2,4), (1,5)* — These are 9 points arranged in the form of a "snake" or ladder.
- **Odd position** (the oldest of the pair) uses the sequence:
*(6,6), (6,4), (5,5), (4,6), (6,2), (5,3), (4,4), (3,5), (2,6)* — symmetrical reflection relative to the center of the block.

The number from 0 to 9 is encoded by filling in the first N cells from the corresponding sequenceю

### Project structure
```text
.
├── main.py                     # Entry point (select examples here)
├── Photo/                      # Ready-made snapshots of encoded numbers
│   ├── encoded_22918726.png    # Number 22,918,726
│   └── generate_images.py      # file for auto-generation of such images
└── requirements.txt            # Dependencies
``
