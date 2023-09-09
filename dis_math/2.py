def terms(exp: str) -> int:
    varialbles = {}
    var_list = []
    operations = {'or', 'and', 'not', '(', ')'}

    exp = '('.join(exp.split('('))
    exp = ')'.join(exp.split(')'))

    tokens = exp.split()
    for t in tokens:
        if t not in operations and t not in varialbles:
            varialbles[t] = None
            var_list.append(t)

    cnt_true = 0
    cnt_false = 0
    lim = 1 << len(var_list)

    for i in range(lim):
        for b in range(len(var_list)):
            if i & (1 << b) != 0:
                varialbles[var_list[b]] = 'True'
            else:
                varialbles[var_list[b]] = 'False'
        const_exp = exp
        for v in varialbles:
            const_exp = const_exp.replace(v, varialbles[v])
        if (eval(const_exp)):
            cnt_true += 1
        else:
            cnt_false += 1
    return cnt_false


def main():
    print(terms(input()))


if __name__ == '__main__':
    main()
