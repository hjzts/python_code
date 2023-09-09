import ast

def evaluate_expression(node, values):
    if isinstance(node, ast.Name):
        return values[node.id]
    elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        return not evaluate_expression(node.operand, values)
    elif isinstance(node, ast.BoolOp) and isinstance(node.op, ast.And):
        return all(evaluate_expression(n, values) for n in node.values)
    elif isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or):
        return any(evaluate_expression(n, values) for n in node.values)
    else:
        raise ValueError("Invalid expression")

def solve_formula(formula):
    variables = ['p', 'q', 'r']
    for i in range(2 ** len(variables)):
        values = {v: bool(i & (1 << j)) for j, v in enumerate(variables)}
        try:
            if evaluate_expression(ast.parse(formula, mode='eval').body, values):
                continue
            else:
                return '可满足式'
        except:
            pass
    for variable in variables:
        if evaluate_expression(ast.parse(f"not {variable}", mode='eval').body, {v: False for v in variables}):
            return '永假式'
    return '永真式'

s = input("请输入一个合式公式，命题变元最多有p,q,r三个，仅包含与、或、非三种运算，用and,or,not来表示: ")
result = solve_formula(s)
print(result)
