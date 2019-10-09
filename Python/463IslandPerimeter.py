def islandPerimeter(grid):
    N = len(grid)
    P = 0
    for i in range(len(grid)):
        if grid[i]:
            for j in range(len(grid[i])):
                if grid[i][j]:
                    P += 4
                    if i < N - 1:
                        if grid[i + 1][j]:
                            P -= 2
                    if j < len(grid[i]) - 1:
                        if grid[i][j + 1]:
                            P -= 2
    return P    