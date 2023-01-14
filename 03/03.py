with open('hada.txt', 'r') as s:
    l = s.readlines()
    print(f'Pocet hier {len(l)}')
    srt_l = sorted(l, reverse=True, key=len)
    if srt_l[0][-1] == '\n':
        print(f'Najdlhsia hra {len(srt_l[0]) - 1}')
    else:
        print(f'Najdlhsia hra {len(srt_l[0])}')

    with open('copy.txt', 'w') as new:
        new.writelines(l)

    with open('compressed.txt', 'w') as n:
        for i in l:
            if i[-1] != '\n':
                i = i + '\n'
            print(i)
            pos = 0
            tmp = i[0]
            for j in i:
                if tmp == j:
                    pos += 1
                    tmp = j
                else:
                    n.write(f'{tmp} {pos},')
                    print(tmp, pos)
                    pos = 1
                    tmp = j
            n.write('\n')
