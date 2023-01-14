def diskriminant(a, b, c):
    a, b, c = a, b, c
    d = b ** 2 - 4 * a * c
    if d > 0:
        return 'Rovnica ma dva korene'
    elif d == 0:
        return 'Rovnica ma jeden koren'
    if d < 0:
        return 'Rovnica nema riesenie'


print(diskriminant(1, 5, 2))
