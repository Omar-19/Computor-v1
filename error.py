import sys


class TextColors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    EN_DC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printUsage():
    # TODO добавить описание корректной строки с уравнением
    print(TextColors.OK_GREEN + 'USAGE:\n >>> python3 main.py [flag] "polynomial equation"\n' + TextColors.EN_DC)
    # print('USAGE:\n >>> python3 main.py [flag] "polynomial equation"\n')
    print("FLAGS:")
    print(' -h\tdisplay help and exit')
    print(' -p\tprints main steps of the resolver')
    print(' -P\tprints every single step of the resolver')


def exit_with_error(error):
    printHelp = False
    if error == -1:
        # проверено
        message = 'No polynomial equation is given :C\n'
        printHelp = True
    elif error == -2:
        # проверено
        message = 'Wrong parameters are given :C\n'
        printHelp = True
    elif error == -5:
        message = 'Lexical error in the equation :C\n'
    # elif error == -4:
    #     message = 'The equation is empty !!\n'
    elif error == -4:
        message = "The '=' symbol is missing !!\n"
    elif error == -6:
        message = 'The polynomial degree is strictly greater than 2, I can\'t solve.\n'
    # elif error == -6:
    #     message = 'Pairing of parenthesis is wrong !!\n'
    # elif error == -7:
    #     message = 'Syntax error, left-side of the equation is empty !!\n'
    # elif error == -8:
    #     message = 'Syntax error, right-side of the equation is empty !!\n'
    elif error == -3:
        message = "Syntax error, the '=' should appear only once !!\n"
    # elif error == -10:
    #     message = 'Syntax error, missing values !!\n'
    # elif error == -11:
    #     message = 'Syntax error, operator at the start/end of expression !!\n'
    # elif error == -12:
    #     message = "Syntax error, you have a '0' char that is not needed !!\n"
    # elif error == -13:
    #     message = "Syntax error, wrong usage of '.' char !!\n"
    # elif error == -14:
    #     message = "Syntax error, you can't put an operator after another (except for '+' followed by '-') !!\n"
    # elif error == -15:
    #     message = "Syntax error, wrong usage around a 'X' char !!\n"
    # elif error == -16:
    #     message = "Syntax error, wrong usage of '^' operator !!\n"
    # elif error == -17:
    #     message = "Zero division detected !!\n"
    # elif error == -18:
    #     message = "Syntax error, grade of a 'X' must be an integer equal or greather than 0 (no operation allowed) !!\n"
    # elif error == -19:
    #     message = "Grades of 'X' must be integers !!\n"
    # elif error == -20:
    #     message = "Syntax error around parenthesis !!\n"
    else:
        message = TextColors.WARNING + 'Are you sure to know how to call this function ? (Error code: ' + str(
            error) + ')'

    print(TextColors.FAIL + '\nERROR: ' + message + TextColors.EN_DC)

    if printHelp:
        printUsage()
    sys.exit(2)

