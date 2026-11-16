class Solution:
    def convert(self, s: str, numRows: int) -> str:
        array = [["" for _ in range(len(s))] for _ in range(numRows)]
        x = 0
        y = 0
        down = True
        for c in s:
            print(c, (x, y))
            array[y][x] = c
            if down:
                y += 1
                if y >= numRows:
                    y -= 2
                    x += 1
                    down = False
            else:
                if y == 0:
                    down = True
                    y += 1
                else:
                    y -= 1
                    x += 1
        return "".join("".join(line) for line in array)
                
        