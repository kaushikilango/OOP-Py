def rom_to_num(s):
    x = 0
    m = 0
    i = 0
    c = 0
    for p in range(0, len(s)):
        print(f'x = {x}')
        print(f'i= {i}')
        print(f'c = {c}')
        print(f'm = {m}')
        if (s[p] == 'M'):
            if(s[p-1] != 'C'):
                m = m + 1000
            else:
                m = 1000 - c
                c = 0
        if(s[p] == 'D'):
            if(s[p-1] != 'C'):
                m = m + 500
            else:
                m = 500 - c
                c = 0
        if(s[p] == 'C'):
            if(s[p-1] != 'X'):
                c = c + 100
            else:
                c = 100 - x
                x = 0
        if(s[p] == 'L'):
            if(s[p-1] != 'X'):
                c = c + 50
            else:
                c = 50 - x
                x = 0
        if(s[p] == 'V'):
            if(s[p-1] != 'I'):
                x = x + 5
            else:
                x = 5 - i
                i = 0
        if(s[p] == 'X'):
            if(s[p-1] != 'I'):
                x = x + 10
            else:
                x = 10 - i
                i = 0
        if(s[p] == 'I'):
            i = i + 1
    return (c+i+x+m)


if __name__ == "__main__":
    c = input("Enter a Roman Numeral String")
    print(rom_to_num(c))
