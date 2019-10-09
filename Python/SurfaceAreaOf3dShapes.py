def surfaceArea(grid):
    surface = 0
    N = len(grid)
    for i in range(N):
        for j in range(N):
            if grid[i][j]:
                surface += grid[i][j] * 4 + 2
            if i:
                surface -= min(grid[i][j], grid[i - 1][j]) * 2
            if j:
                surface -= min(grid[i][j], grid[i][j - 1]) * 2
    return surface

surfaceArea([[1,2],[3,4]])