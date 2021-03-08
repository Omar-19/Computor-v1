import math

from error import exit_with_error


class Sol:
    n = 0
    is_complex = 0
    # d = {'Re': 0, 'Im1': 0, 'Im2': 0}
    x = []
    comment = ''


def solve(fac):
    sl = Sol

    if fac.max_degree > 2:
        exit_with_error(-6)
    elif fac.a == 0 and fac.b == 0 and fac.c != 0:
        sl.comment = '\nThis equation has no solutions :C \n'
    elif fac.a == 0 and fac.b == 0 and fac.c == 0:
        sl.comment = '\nThe solution to this equation is any value of X *o* \n'
    elif fac.a == 0 and fac.b != 0:
        sl.comment = '\nThe graph of your equation is a straight line, so there is only one solution \n'
        sl.n = 1
        sl.x.append(round(-fac.c / fac.b, 3))
    else:
        disc = fac.b * fac.b - 4 * fac.a * fac.c
        if disc == 0:
            if fac.a > 0:
                sl.comment = '\nYour equation graph is a parabola with branches up. ' \
                             'It touches the OX axis at the vertex, so there is only one solution \n'
            else:
                sl.comment = '\nYour equation graph is a parabola with branches down. ' \
                             'It touches the OX axis at the vertex, so there is only one solution \n'
            sl.n = 1
            sl.x.append(round(-fac.b / (2 * fac.a), 3))
        elif disc > 0:
            if fac.a > 0:
                sl.comment = '\nYour equation graph is a parabola with branches up. ' \
                             'It intersects the OX axis at two points, so there are two solutions \n'
            else:
                sl.comment = '\nYour equation graph is a parabola with branches down. ' \
                             'It intersects the OX axis at two points, so there are two solutions \n'
            sl.n = 2
            sl.x.append(round((-fac.b + math.sqrt(disc)) / (2 * fac.a), 3))
            sl.x.append(round((-fac.b - math.sqrt(disc)) / (2 * fac.a), 3))
        else:
            if fac.a > 0:
                sl.comment = '\nYour equation graph is a parabola with branches up. However, ' \
                             'it does not cross the OX axis! Wow! This means you have two complex roots *0* \n'
            else:
                sl.comment = '\nYour equation graph is a parabola with branches down. However, ' \
                             'it does not cross the OX axis! Wow! This means you have two complex roots *0* \n'
            sl.n = 2
            # print('---', str(round(-fac.b / (2 * fac.a), 3)) + ' + ' + str(round(-fac.b / (2 * fac.a), 3)))
            sl.x.append(str(round(-fac.b / (2 * fac.a), 3)) + ' + '
                        + str(round(math.sqrt(-disc) / (2 * fac.a), 3)) + ' * i')
            sl.x.append(str(round(-fac.b / (2 * fac.a), 3)) + ' - '
                        + str(round(math.sqrt(-disc) / (2 * fac.a), 3)) + ' * i')

    print(sl.comment)

    print('The solution is:\n')

    if sl.n == 1:
        print('X = ', sl.x[0])
    elif sl.n == 2:
        print('X1 =', sl.x[0])
        print('X2 =', sl.x[1], '\n')


    return sl
