import sys


t = {
    #   a  b  c  d  e  f  g
    0: (1, 1, 1, 1, 1, 1, 0),
    1: (0, 1, 1, 0, 0, 0, 0),
    2: (1, 1, 0, 1, 1, 0, 1),
    3: (1, 1, 1, 1, 0, 0, 1),
    4: (0, 1, 1, 0, 0, 1, 1),
    5: (1, 0, 1, 1, 0, 1, 1),
    6: (1, 0, 1, 1, 1, 1, 1),
    7: (1, 1, 1, 0, 0, 0, 0),
    8: (1, 1, 1, 1, 1, 1, 1),
    9: (1, 1, 1, 1, 0, 1, 1)
}

vals_compact = dict(
    us='_',
    pipe='|',
)

ROW_1 = " {a}{last_1}"
ROW_2 = "{f}{g}{b}{last_2}"
ROW_3 = "{e}{d}{c}{last_3}"


def get_ssd(n, last_a, last_b):
    space = ' '
    a_, b_, c_, d_, e_, f_, g_ = t[n]

    a = vals_compact['us'] if a_ else space
    b = vals_compact['pipe'] if b_ else space
    c = vals_compact['pipe'] if c_ else space
    d = vals_compact['us'] if d_ else space
    e = vals_compact['pipe'] if e_ else space
    f = vals_compact['pipe'] if f_ else space
    g = vals_compact['us'] if g_ else space

    return (ROW_1.format(a=a, last_1=last_a),
            ROW_2.format(f=f, g=g, b=b, last_2=last_b),
            ROW_3.format(e=e, d=d, c=c, last_3=last_b))


def seven_seg(x):
    # ssd_res = []
    row1 = ''
    row2 = ''
    row3 = ''

    digits_length = len(x)
    for idx, digit in enumerate(x):
        digit = int(digit)
        last_a = [' ', ' \n'][idx == digits_length - 1]
        last_b = ['', '\n'][idx == digits_length - 1]
        r1, r2, r3 = get_ssd(digit, last_a, last_b)

        row1 += r1
        row2 += r2
        row3 += r3

    joined = row1 + row2 + row3
    return joined

if __name__ == '__main__':
    res = seven_seg(sys.argv[1])
    # print(''.join(res))
    print(res)
    # with open('ssd.txt', 'w+') as f:
    #     f.write(res)

if __name__ == '__main__':
    import sys
    res = seven_seg(sys.argv[1])
    print(res)
