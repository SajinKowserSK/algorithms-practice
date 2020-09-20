def calc_drone_min_energy(route):
    momentum = 0
    used = 0

    for x in range(0, len(route) - 1):
        curr = route[x]
        next_p = route[x + 1]

        diff = abs(next_p[2] - curr[2])

        if next_p[2] < curr[2]:
            # descend
            momentum += diff

        elif next_p[2] > curr[2]:
            # ascend
            # first check if we have anything in momentum
            # subtract that amount from the ascend amount diff
            # anything else still used is added to used
            ascend = diff

            if ascend > momentum:
                ascend -= momentum
                momentum = 0
                used += ascend

            else:
                momentum -= diff

    return used




