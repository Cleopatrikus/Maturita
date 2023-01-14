with open('mena_zamestnancov.txt', 'r') as file:
    lines = [i[:-1] if i[-1] == '\n' else i for i in file.readlines()]
    half_lenght = int(len(lines)/2)
    longest_name = len(sorted(lines[:half_lenght-1], key=len, reverse=True)[0])
    with open('vystup.txt', 'w') as new_file:
        for i in range(half_lenght):
            new_file.write(f'{lines[i]}{" "*(longest_name-len(lines[i]))} {lines[i+half_lenght]}\n')

    print(f'Pocet mien je {half_lenght}')
    print(f'Najdlhsie meno je {sorted(lines[:half_lenght], key=len, reverse=True)[0]} \n'
          f'Najdlhsie priezvisko je {sorted(lines[half_lenght:], key=len, reverse=True)[0]}')
