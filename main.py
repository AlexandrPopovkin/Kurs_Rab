def _pre_to_inf(symb, text):
    if symb in ['+', '-', '*', '/', '**']:
        left = text.pop ()
        right = text.pop ()
        text.append ('(%s %s %s)' % (left, symb, right))
    else:
       text.append(symb)

def pre_to_inf(a_list):
    text = []
    a_list.reverse ()

    for i in a_list:
        _pre_to_inf(i, text)
    return text.pop()


def _post_to_inf(symb,text):
    if symb in ['+', '-', '*', '/', '**']:
        left = text.pop ()
        right = text.pop ()
        text.append ('(%s %s %s)' % (right, symb, left))
    else:
       text.append(symb)


def post_to_inf(a_list):
    text = []
    for i in a_list:
        _post_to_inf(i, text)

    return text[0]

def main():

    ch = 1
    while ch != 0 :
        print('\n---------------------------------\n'
              '1. Ввести выражение в инфиксной форме\n'
              '2. Ввести выражение в префиксной форме\n'
              '3. Ввести выражение в постфиксной форме\n'
              '4. Отображение результата\n'
              '0. Выход\n'
              '---------------------------------\n')
        try:
            ch = int(input('Выберите пункт меню: '))
        except:
            print('Введено некорректное значение\n')
        if ((ch>11) or (ch<0)):
            print('Введите корректное значение\n')
        else:
            if ch == 1:
                a = input('Введите выражение в инфиксной форме: ')
                a = a.replace("^", "**")
                print(a)

            elif ch == 2:
                a = input('Введите выражение в префиксной форме (вводить нужно через пробел): ')
                a = a.replace("^", "**")
                a_list = a.split(' ')

                a = pre_to_inf(a_list)

            elif ch == 3:
                a = input('Введите выражение в постфиксной форме: ')
                a = a.replace("^", "**")
                a_list = a.split(' ')
                a = post_to_inf(a_list)



            elif ch == 4:
                result = eval(a)
                print(result)
main()