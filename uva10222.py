key = ['c', 'v', 'b', 'n', 'm', ',', '.', '/', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "\'", 'e', 'r',
       't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
value = ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'q', 'w',
         'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


while True:
    try:
        mes = input()
        for i in mes:
            if i in key:
                print(value[key.index(i)], end='')
            else:
                print(i, end='')
        print()

    except:
        break
