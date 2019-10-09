def reverse(self, x: int) -> int:
    if x == 0:
        return 0
    if (x > (2 ** 31 - 1)) or (x < (-2 ** 31)):
        return 0
    if x < 0:
        pop = 0 - x
    else:
        pop = x
    y = ''
    zeroAtEnd = True
    for i in range(len(str(pop))):
        reminder = pop % 10
        pop = pop // 10
        if (reminder != 0) or not zeroAtEnd:
            zeroAtEnd = False
            y += str(reminder)
    if x < 0:
        y = '-' + y
    y = int(y)
    if (y > (2 ** 31 - 1)) or (y < (-2 ** 31)):
        return 0

    return y