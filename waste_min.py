from no_waste import euler_cycle


def main():
    # trapezoids = [(0, 100, 150), (-50, 50, 100), (-50, 100, 100)]
    # write_to_file(trapezoids)
    (trapezoids, trapez_count) = read_file("9.txt")
    print(trapezoids)
    trapez_count += adding_necessary_cuts(trapezoids)
    print(euler_cycle(trapezoids, trapez_count))


def adding_necessary_cuts(trapezoids: dict) -> int:
    if 0 not in trapezoids.keys():
        trapezoids[0] = {(0, -1)}
    else:
        trapezoids[0].add((0, -1))

    add_trapez_count = 1

    l_counter = 0
    r_counter = 0

    y = []
    z = []
    for incl in trapezoids.keys():
        for (incl_, _) in trapezoids[incl]:
            if incl_ >= incl:
                y.append(incl)
            if incl_ <= incl:
                z.append(incl)

    y_z = sorted(y + z)
    num = -2
    for i in range(len(y_z) - 1):
        if y_z[i] in y:
            l_counter += 1
            y.remove(y_z[i])
        elif y_z[i] in z:
            r_counter += 1
            z.remove(y_z[i])
        if (l_counter - r_counter) % 2 == 1:
            trapezoids[y_z[i]].add((y_z[i + 1], num))
            add_trapez_count += 1
            num -= 1
        elif l_counter == r_counter:
            trapezoids[y_z[i]].add((y_z[i + 1], num))
            num -= 1
            trapezoids[y_z[i]].add((y_z[i + 1], num))
            num -= 1
            add_trapez_count += 2

    return add_trapez_count


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
