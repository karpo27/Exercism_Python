def convert(input_grid):
  
    numbers = {
    (" _ ", "| |", "|_|", "   "): "0",
    ("   ", "  |", "  |", "   "): "1",
    (" _ ", " _|", "|_ ", "   "): "2",
    (" _ ", " _|", " _|", "   "): "3",
    ("   ", "|_|", "  |", "   "): "4",
    (" _ ", "|_ ", " _|", "   "): "5",
    (" _ ", "|_ ", "|_|", "   "): "6",
    (" _ ", "  |", "  |", "   "): "7",
    (" _ ", "|_|", "|_|", "   "): "8",
    (" _ ", "|_|", " _|", "   "): "9"
    }
    
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if not input_grid:
        return ""
    if len(input_grid[0]) % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")
    for row in input_grid:
        if len(row) != len(input_grid[0]):
            raise ValueError("Inconsistent number of rows")
    all_digits = []
    for line_number in range(len(input_grid)//4):
        line = []
        for character_number in range(len(input_grid[0])//3):
            line.append(numbers.get((input_grid[4*line_number][character_number*3:character_number*3+3], 
                                    input_grid[4*line_number+1][character_number*3:character_number*3+3],
                                    input_grid[4*line_number+2][character_number*3:character_number*3+3],
                                    input_grid[4*line_number+3][character_number*3:character_number*3+3]),
                                   "?"))
        all_digits.append("".join(line))
        
    return ",".join(all_digits)
    
