class ContainerPainter:
    def __init__(self):
        self.height: int = 10
        self.width: int = 20
        self.grid: list[list[str]] = [[" " for _ in range(self.width)] for _ in range(self.height)]

        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = " "

    def set_settings(self, y, x):
        self.height = y
        self.width = x

    def draw_line(self, y: int) -> None:
        for x in range(self.width):
            self.grid[y][x] = "#"

    def draw_text(self, y: int, text: str) -> None:
        text_len: int = len(text)
        free_space: int = self.width - text_len - 2
        self.grid[y][0] = "#"
        current_index = 1
        for x in range(0, text_len):
            self.grid[y][current_index + x] = text[x]
        current_index += text_len
        for x in range(0, free_space):
            self.grid[y][current_index + x] = " "
        self.grid[y][self.width-1] = "#"

    def print_grid(self):
        for y in self.grid:
            line = []
            for x in y:
                line += x
            "".join(line)
            print(line)


painter = ContainerPainter()
#painter.set_settings(10, 4)
painter.draw_line(0)
painter.draw_text(1, "Hello")
painter.print_grid()
