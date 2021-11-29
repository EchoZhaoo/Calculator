import unittest
import ast
from app.utils.expr_eval import eval_expr, eval_


class ExprEvalTest(unittest.TestCase):
    def test_1_addition(self):
        _ = eval_expr('5+10')
        self.assertEqual(_, 15)

    def test_2_subtraction(self):
        _ = eval_expr('5-10')
        self.assertEqual(_, -5)

    def test_3_multiplication(self):
        _ = eval_expr('5*10')
        self.assertEqual(_, 50)

    def test_4_division(self):
        _ = eval_expr('10/5')
        self.assertEqual(_, 2)

    def test_5_division_float(self):
        _ = eval_expr("5/10")
        self.assertEqual(_, .5)

    def test_6_division_float(self):
        _ = eval_expr("1/3")
        self.assertEqual(_, .3333)

    def test_7_parentheses(self):
        _ = eval_expr("(1+2)*3")
        self.assertEqual(_, 9)

    def test_8_parentheses(self):
        _ = eval_expr("((1+2)*(3-4))/(12+1-5)")
        self.assertEqual(_, -0.375)

    def test_9_operation(self):
        _ = eval_expr("1+2*3-4/8")
        self.assertEqual(_, 6.5)


class EvalTest(unittest.TestCase):
    def test_1_addition(self):
        _ = eval_(ast.parse('5+10', mode='eval').body)
        self.assertEqual(_, 15)

    def test_2_subtraction(self):
        _ = eval_(ast.parse('5-10 ', mode='eval').body)
        self.assertEqual(_, -5)

    def test_3_multiplication(self):
        _ = eval_(ast.parse('5*10', mode='eval').body)
        self.assertEqual(_, 50)

    def test_4_division(self):
        _ = eval_(ast.parse('10/5', mode='eval').body)
        self.assertEqual(_, 2)

    def test_5_division_float(self):
        _ = eval_(ast.parse('5/10', mode='eval').body)
        self.assertEqual(_, .5)

    def test_6_division_float(self):
        _ = eval_(ast.parse('1/3', mode='eval').body)
        self.assertEqual(_, .3333333333333333)

    def test_7_parentheses(self):
        _ = eval_(ast.parse('(5+5)/10', mode='eval').body)
        self.assertEqual(_, 1)

    def test_8_parentheses(self):
        _ = eval_(ast.parse('((1+2)*(3-4))/(12+1-5)', mode='eval').body)
        self.assertEqual(_, -0.375)

    def test_9_operation(self):
        _ = eval_(ast.parse('1+2*3-4/8', mode='eval').body)
        self.assertEqual(_, 6.5)


if __name__ == '__main__':
    unittest.main()
