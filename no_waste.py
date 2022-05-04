def main():
    # trapezoids = [(0, 100, 150), (-50, 50, 100), (-50, 100, 100)]
    # write_to_file(trapezoids)
    (trapezoids, trapez_count) = read_file("9.txt")
    print(trapezoids)
    print(euler_cycle(trapezoids, trapez_count))


def euler_cycle(trapezoids: dict, trapez_count: int) -> list:
    if 0 not in trapezoids.keys():
        return []

    rout = partial_euler_cycle(trapezoids, 0)
    if rout[0] != rout[-1]:
        return []

    i = 0
    while i < len(rout):
        if trapezoids[rout[i]] != set():
            rout_ = partial_euler_cycle(trapezoids, rout[i])
            if rout_[0] != rout_[-1]:
                return []
            rout = [*rout[:i], *rout_, *rout[i + 1:]]
        i += 1

    if len(rout) - 1 != trapez_count:
        return []

    return rout


def partial_euler_cycle(trapezoids: dict, incline: int) -> list:
    rout = [incline]
    while trapezoids[incline] != set():
        (incline_, trapez_num) = trapezoids[incline].pop()
        if (incline, trapez_num) in trapezoids[incline_]:
            trapezoids[incline_].remove((incline, trapez_num))
        rout.append(incline_)
        incline = incline_

    return rout


def euler_cycle2(trapezoids: dict, trapez_count: int, start_incline: int = 0) -> list:
    incline = start_incline  # наклон
    rout = [incline]

    if 0 not in trapezoids.keys():
        return []

    while trapezoids[incline] != set():
        (incline_, trapez_num) = trapezoids[incline].pop()
        if (incline, trapez_num) in trapezoids[incline_]:
            trapezoids[incline_].remove((incline, trapez_num))
        rout.append(incline_)
        incline = incline_

    if start_incline != incline:
        return []

    for incl in rout[1:]:
        if trapezoids[incl] != set():
            rout_ = euler_cycle2(trapezoids, trapez_count, incl)
            if not rout_:
                return []
            rout = [*rout[:rout.index(incl)], *rout_, *rout[rout.index(incl) + 1:]]

    return rout


def write_file(trapezoids):
    with open('trapezoids.csv', 'w') as f:
        for t in trapezoids:
            f.write(str(t[0]) + "," + str(t[1]) + "," + str(t[2]) + "\n")


def read_file(filename: str) -> (dict, int):
    with open(filename, 'r') as f:
        lines = f.readlines()
    trapezoids = {}
    i = 1
    for line in lines[1:]:
        x_coord = line.split(' ')  # координата по оси OX трапеций
        a = int(x_coord[0])  # левый наклон
        b = int(x_coord[1]) - int(x_coord[2])  # правый наклон
        if a not in trapezoids.keys():
            trapezoids[a] = {(b, i)}
        else:
            trapezoids[a].add((b, i))
        if b not in trapezoids.keys():
            trapezoids[b] = {(a, i)}
        else:
            trapezoids[b].add((a, i))
        i += 1

    return trapezoids, i - 1


main()
