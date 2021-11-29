import ast
import operator as op

# supported operators
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv}


def eval_expr(expr):
    """
    >>> eval_expr('1 + 2')
    3
    >>> eval_expr('(1 + 2) / 3')
    1.0
    >>> eval_expr('1 + 7 / 3')
    -1.3333
    """
    # handle the empty expression
    if expr == '':
        return ''
    else:
        return round(eval_(ast.parse(expr, mode='eval').body), 4)


def eval_(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # binary operation: <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):  # unary operation: <operand> e.g., 1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)
