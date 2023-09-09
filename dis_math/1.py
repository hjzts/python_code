def solve_formula(exp: str):
    variables = {}
    var_list = []
    operations = {'or', 'and', 'not', '(', ')', 'True', "False"}

    exp = ' ( '.join(exp.split('('))
    exp = ' ) '.join(exp.split(')'))

    tokens = exp.split()
    for t in tokens:
        if t not in operations and t not in variables:
            variables[t] = None
            var_list.append(t)

    has_true = False
    has_false = False
    lim = 1 << len(var_list)

    for i in range(lim):
        for b in range(len(var_list)):
            if i & (1 << b) != 0:
                variables[var_list[b]] = 'True'
            else:
                variables[var_list[b]] = 'False'
        const_exp = " ".join(list(map(lambda x: variables[x] if x in variables else x, tokens)))
        if eval(const_exp):
            has_true = True
        else:
            has_false = True

    if not has_false:
        return '永真式'
    elif not has_true:
        return '永假式'
    else:
        return '可满足式'

s = input("请输入一个合式公式，命题变元最多有p,q,r三个，仅包含与、或、非三种运算，用and,or,not来表示: ")
result = solve_formula(s)
print(result)