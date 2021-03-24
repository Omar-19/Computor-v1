# TODO дописать проверку на говно в строке
import re
import sys

from error import exit_with_error, printUsage


def check(eq):
    s = re.sub('[^0-9X. \-+*^=]', '', eq)
    # print(eq)
    # print(s)
    if s != eq:
        exit_with_error(-2)

    eq = re.sub(' ', '', eq)
    if eq.count('=') > 1:
        exit_with_error(-3)
    elif eq.count('=') == 0:
        exit_with_error(-4)
    # print(eq)


def check_correct_part(eq):
    # print(eq)

    if len(eq) < 3:
        exit_with_error(-5)

    for i in range(len(eq) - 1):
        if eq[i] == '-' or eq[i] == '+':
            if not (eq[i + 1][0].isdigit() or eq[i + 1][0] == 'X'):
                # print('1')
                exit_with_error(-5)

        elif eq[i] == '*':
            if eq[i + 1][0] != 'X':
                # print('1')
                exit_with_error(-5)

        elif eq[i][0].isdigit():
            if eq[i].count('.') > 1:
                # print('3')
                exit_with_error(-5)
            for n in eq[i]:
                if not (n.isdigit() or n == '.'):
                    # print('4')
                    exit_with_error(-5)

        elif eq[i][0] == 'X':
            if eq[i].count('X') > 1 or eq[i].count('^') > 1:
                # print('5')
                exit_with_error(-5)

            if len(eq[i]) > 1:
                if eq[i][1] != '^':
                    # print('6')
                    exit_with_error(-5)
                else:
                    eq_str = re.sub('X', '', eq[i])
                    eq_str = re.sub('\^', '', eq_str)
                    for n in eq_str:
                        if not n.isdigit():
                            # print('7')
                            exit_with_error(-5)
            if not (eq[i + 1] == '+' or eq[i + 1] == '-' or eq[i + 1] == '='):
                # print('8')
                exit_with_error(-5)

        elif eq[i] == '=':
            if not (eq[i + 1][0].isdigit() or eq[i + 1][0] == 'X' or eq[i + 1] == '-'):
                # print('9')
                exit_with_error(-5)
        else:
            # print(eq[i])
            # print('10')
            exit_with_error(-5)

    if not (eq[0][0].isdigit() or eq[0][0] == 'X' or eq[0][0] == '-'):
        # print('11')
        exit_with_error(-5)

    if not (eq[0][-1].isdigit() or eq[0][-1] == 'X'):
        # print('12')
        exit_with_error(-5)


def parse_argv(argv):
    flag = 0
    equation = ""
    argc = len(argv)
    # вывод ошибки при отстутствии аргументов
    if argc == 1:
        exit_with_error(-1)
    elif sys.argv[1] == "-h":
        printUsage()
        sys.exit(2)
    elif sys.argv[1] == "-p" or sys.argv[1] == "-P":
        if argc == 2:
            exit_with_error(-1)
        elif argc > 3:
            exit_with_error(-2)

        # бонусы
        if sys.argv[1] == "-p":
            flag = 1
        else:
            flag = 2
        equation = sys.argv[2]
    elif argc == 2:
        equation = sys.argv[1]
    else:
        exit_with_error(-2)

    return equation, flag


def get_number_factors(eq, fac):
    is_n = 0
    i = 1
    n = 0
    z = 1
    pow_ = 0

    for j, ch in enumerate(eq):

        if ch == '-' or ch == '+' or ch == '=' or j == len(eq) - 1:
            if ch[0] == 'X':
                if ch == 'X':
                    pow_ = 1
                else:
                    ch = ch.replace('X', '').replace('^', '')
                    pow_ = int(ch)
                n = 1 if is_n == 0 else n
            elif ch[0].isdigit():
                is_n = 1
                n = float(ch)

                n = 1 if is_n == 0 else n
            # print(pow_, ch, n)

            fac.max_degree = pow_ if (pow_ > fac.max_degree) else fac.max_degree

            if pow_ in fac.pow_num_dict.keys():
                fac.pow_num_dict[pow_] += i * z * n
            else:
                fac.pow_num_dict[pow_] = i * z * n

            n = 0
            z = 1
            pow_ = 0
            is_n = 0

            if ch == '-':
                z = -1
            elif ch == '+':
                z = 1
            else:
                i = -1

        elif ch[0].isdigit():
            is_n = 1
            n = float(ch)

        elif ch[0] == 'X':
            # print(ch, '-------')
            if ch == 'X':
                pow_ = 1
                n = 1 if is_n == 0 else n
            else:
                ch = ch.replace('X', '').replace('^', '')
                pow_ = int(ch)

            n = 1 if is_n == 0 else n

    # TODO исправить fac.max_degree = pow_ if (pow_ > fac.max_degree) else fac.max_degree
    # TODO график
