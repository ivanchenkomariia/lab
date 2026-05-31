import turtle as t

class Figure:
    def __init__(self, x=0, y=0, color="black"):
        self._x = x
        self._y = y
        self._color = color
        self._visible = False
        self._t = t.Turtle()
        self._t.hideturtle()
        self._t.speed(0)
    def setPosition(self, x, y):
        was_visible = self._visible
        if was_visible:
            self.hide()
        self._x = x
        self._y = y
        if was_visible:
            self.show()
    def draw(self, color):
        pass
    def show(self):
        if not self._visible:
            self._visible = True
            self.draw(self._color)
    def hide(self):
        if self._visible:
            self._visible = False
            self._t.clear()

class Cross(Figure):
    def __init__(self, x=0, y=0, size=40, color="blue"):
        super().__init__(x, y, color)
        self.size = size
    def draw(self, color):
        t = self._t
        t.clear()
        t.pencolor(color)
        t.pensize(4)
        s = self.size
        t.up()
        t.goto(self._x - s, self._y - s)
        t.down()
        t.goto(self._x + s, self._y + s)
        t.up()
        t.goto(self._x - s, self._y + s)
        t.down()
        t.goto(self._x + s, self._y - s)
        t.up()

class Zero(Figure):
    def __init__(self, x=0, y=0, radius=40, color="red"):
        super().__init__(x, y, color)
        self.radius = radius
    def draw(self, color):
        t = self._t
        t.clear()
        t.pencolor(color)
        t.pensize(4)
        t.up()
        t.goto(self._x, self._y - self.radius)
        t.down()
        t.circle(self.radius)
        t.up()

class Board(Figure):
    def __init__(self, x=0, y=0, cell_size=100, color="black"):
        super().__init__(x, y, color)
        self.cell_size = cell_size
    def draw(self, color):
        t = self._t
        t.clear()
        t.pencolor(color)
        t.pensize(3)
        h = self.cell_size
        for i in [-0.5, 0.5]:
            t.up()
            t.goto(self._x + i * h, self._y + 1.5 * h)
            t.down()
            t.goto(self._x + i * h, self._y - 1.5 * h)
        for i in [-0.5, 0.5]:
            t.up()
            t.goto(self._x - 1.5 * h, self._y + i * h)
            t.down()
            t.goto(self._x + 1.5 * h, self._y + i * h)
        t.up()

CELL = 100
grid = [[None for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False
def get_cell_center(row, col):
    return (col - 1) * CELL, (1 - row) * CELL
def check_winner():
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0]:
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i]:
            return grid[0][i]
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0]:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2]:
        return grid[0][2]
    if all(all(cell for cell in row) for row in grid):
        return "Draw"
    return None
def on_click(x, y):
    global current_player, game_over
    if game_over:
        return
    if not (-1.5 * CELL <= x <= 1.5 * CELL and -1.5 * CELL <= y <= 1.5 * CELL):
        return
    col = int((x + 1.5 * CELL) // CELL)
    row = int((1.5 * CELL - y) // CELL)
    if grid[row][col] is None:
        grid[row][col] = current_player
        cx, cy = get_cell_center(row, col)
        if current_player == "X":
            Cross(cx, cy, 35).show()
            current_player = "O"
        else:
            Zero(cx, cy, 35).show()
            current_player = "X"
        winner = check_winner()
        if winner:
            game_over = True
            t.title(f"Game Over: {winner}")

if __name__ == "__main__":
    t.setup(500, 500)
    t.title("XO OOP")
    board = Board(0, 0, CELL)
    board.show()
    t.listen()
    t.onscreenclick(on_click)
    t.mainloop()
