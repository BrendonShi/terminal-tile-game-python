class TileSet:
    #up = 0b1000
    #down = 0b0100
    #left = 0b0010
    #right = 0b0001
    tiles = {
        0b0000: " ",
        0b0101: "┌", #up, down, left, right
        0b0110: "┐",
        0b1001: "└",
        0b1010: "┘",
        0b0011: "─",
        0b1100: "│",
        0b1000: "│",
        0b0100: "│",
        0b0010: "─",
        0b0001: "─",
        0b1011: "┴",
        0b0111: "┬",
        0b1101: "├",
        0b1111: "┼",
        0b1110: "┤",
    }

    def __init__(self):
        pass

    def get_tile_bits(self, grid: list[list[str]], y: int, x: int):
        bits = 0b0000
        if grid[y][x] != "#":
            return None
        if y > 0 and grid[y-1][x] == "#":
            bits |= 0b1000
        if y < len(grid)-1 and grid[y+1][x] == "#":
            bits |= 0b0100
        if x > 0 and grid[y][x-1] == "#":
            bits |= 0b0010
        if x < len(grid[y])-1 and grid[y][x+1] == "#":
            bits |= 0b0001
        return bits

    def get_tiles(self, grid):
        tile_map = []
        for y in range(len(grid)):
            line = []
            for x in range(len(grid[y])):
                bits = self.get_tile_bits(grid, y, x)
                if bits == None:
                    line.append(grid[y][x])
                    continue
                #print(f'{bits:04b}')
                line.append(self.tiles[bits])
            tile_map.append(line)
        return tile_map


#print(TileSet.up|TileSet.down)
#print(0b1100)

#grid = [
#    ["#", "#", "#"],
#    ["#", " ", "#"],
#    ["#", "#", "#"]
#]


#tileset = TileSet()
#tileset.get_tiles(grid)
