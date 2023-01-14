with open('bus_vytazenost.txt', 'r') as file:
    lines = [i[:-1] if i[-1] == '\n' else i for i in file.readlines()]
    print(f'Pocet zastavok je {len(lines) - 1}')
    for i in lines[1:]:
        print(' '.join(i.split(' ')[2:]), end=', ')
