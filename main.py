import re
import sys

from check_and_pars import check, parse_argv, get_number_factors, check_correct_part
from create_solution import solve
# from my_math import ftPow
from error import exit_with_error, printUsage


class MyPolynomialPars:
    a = 0
    b = 0
    c = 0
    max_degree = 0
    pow_num_dict = {}
    reduced_form = ''


def print_reduced_form(fac):
    list_keys = sorted(list(fac.pow_num_dict.keys()), reverse=True)
    # list_keys.sort()
    z = 0

    for i in list_keys:
        l = 0

        if fac.pow_num_dict[i] != 0:
            if z == 0:
                z = 1
            else:
                fac.reduced_form += ' + '
            if fac.pow_num_dict[i] < 0:
                l = 1
            if l == 1:
                fac.reduced_form += '('
            fac.reduced_form += str(fac.pow_num_dict[i])
            if l == 1:
                fac.reduced_form += ')'
            fac.reduced_form += ' * X^' + str(i)

    fac.reduced_form += ' = 0'

    print('\nReduced form: ', fac.reduced_form)
    print('Polynomial degree: ', fac.max_degree)

    return 0


def get_abc(fac):
    if 0 in fac.pow_num_dict.keys():
        fac.c = fac.pow_num_dict[0]
    if 1 in fac.pow_num_dict.keys():
        fac.b = fac.pow_num_dict[1]
    if 2 in fac.pow_num_dict.keys():
        fac.a = fac.pow_num_dict[2]


def main(argv):
    equation, debug_option = parse_argv(argv)
    # equation = equation.replace(" ", "")
    check(equation)
    fac = MyPolynomialPars
    equation = equation.split()
    check_correct_part(equation)
    get_number_factors(equation, fac)
    get_abc(fac)
    print_reduced_form(fac)
    sol = solve(fac)

    # print(fac.pow_num_dict)

    # print(equation)
    # print('a = ', fac.a, 'b = ', fac.b, 'c = ', fac.c, 'd = ', fac.pow_num_dict, 'max_degree = ', fac.max_degree)
    # print('max_degree = ', fac.max_degree)
    # print('reduced form: ', fac.reduced_form)

    # print('Equation roots: ', sol.x)

    # equation = lexicalCheck(equation)
    # print(equation)
    # equation = bringRightToLeft(equation)
    # print(equation)
    # equation = reduceEquation(equation, debug_option)
    # resolveEquation(equation, debug_option)

    return 0


main(sys.argv)
