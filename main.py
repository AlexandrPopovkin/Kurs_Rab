def _pre_to_inf(symb, text):
    if symb in ['+', '-', '*', '/', '**']:
        left = text.pop ()
        right = text.pop ()
        if symb == "+":
            ans = int(left) + int(right)
        elif symb == "-":
            ans = int(left) - int(right)
        elif symb == "/":
            ans = int(left) / int(right)
        elif symb == "*":
            ans = int(left) * int(right)
        elif symb == "**":
            ans = int(left) ** int(right)
        text.append(ans)
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
        if symb == "+":
            ans = int(left) + int(right)
        elif symb == "-":
            ans = int(left) - int(right)
        elif symb == "/":
            ans = int(right) / int(left)
        elif symb == "*":
            ans = int(left) * int(right)
        elif symb == "**":
            ans = int(right) ** int(left)
        text.append(ans)
    else:
       text.append(symb)


def post_to_inf(a_list):
    text = []
    for i in a_list:
        _post_to_inf(i, text)

    return text[0]

def ev(a_list):
    ans = 0
    i = 0
    while len(a_list)!=1:

            if len(a_list)-1 == i: i = 0
            elif (a_list[i] == '(') and (a_list[i+1]!= '(') and (a_list[i+2]!=')') and (a_list[i+3]!='('):
                if a_list[i+2] == '+':
                    ans = int(a_list[i+1]) + int(a_list[i+3])
                elif a_list[i+2] == '*':
                    ans = int(a_list[i+1]) * int(a_list[i+3])
                elif a_list[i+2] == '/':
                    ans = int(a_list[i+1]) / int(a_list[i+3])
                elif a_list[i+2] == '**':
                    ans = int(a_list[i+1]) ** int(a_list[i+3])
                elif a_list[i+2] == '-':
                    ans = int(a_list[i+1]) - int(a_list[i+3])
                a_list[i] = ans

                a_list.remove(a_list[i + 1])
                a_list.remove(a_list[i + 1])
                a_list.remove(a_list[i + 1])


            elif (a_list[i+1]==')') and (a_list[i+1]):
                a_list.remove(a_list[i+1])


            elif (str(a_list[i])[0] in "123456789") and (a_list[i+2]!='(') and (str(a_list[i]) not in '+-*/**'):
                if a_list[i+1] == '+':
                    ans = int(a_list[i]) + int(a_list[i+2])
                elif a_list[i+1] == '*':
                    ans = int(a_list[i]) * int(a_list[i+2])
                elif a_list[i+1] == '/':
                    ans = int(int(a_list[i]) / int(a_list[i+2]))
                elif a_list[i+1] == '**':
                    ans = int(a_list[i]) ** int(a_list[i+2])
                elif a_list[i+1] == '-':
                    ans = int(a_list[i]) - int(a_list[i+2])
                a_list[i] = ans
                a_list.remove(a_list[i+1])
                a_list.remove(a_list[i+1])
            elif (a_list[i] == '(' and a_list[i+1] == '('):
                a_list.remove(a_list[i])
            elif not (a_list[i+1]):
                i = 0

            else:
                i=i+1


    return(a_list[0])

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
                a = a.split(' ')
                a = ev(a)
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
                print(a)
main()