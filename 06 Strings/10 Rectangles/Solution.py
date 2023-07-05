def rectangles(strings):
    # Get pairs of coordinates of top corners and check continuity between them
    pairs = []
    for row in range(len(strings)):
        start = None
        for col in range(len(strings[row])):
            if strings[row][col] == "+":
                start = (row, col)
                for pos, ch in enumerate(strings[row]):
                    if pos <= col:
                        continue
                    if ch not in "-+":
                        break
                    if ch == "+":
                        pairs.append((start, (row, pos)))
                        
    # Now for each pair of top corners check continuity with bottom corners
    count = 0
    for pair in pairs:
        left, right = pair
        l_x, l_y = left
        r_x, r_y = right
        
        for x in range(l_x + 1, len(strings)):
            if strings[x][l_y] not in "|+":
                break
            if strings[x][r_y] not in "|+":
                break
            if strings[x][l_y] == "+" and strings[x][r_y] == "+":
                
                # check continuity between bottom corners
                save = True
                for ch in strings[x][l_y:r_y]:
                    if ch not in "-+":
                        save = False
                        break
                if save:
                    count += 1
                    
    return count
