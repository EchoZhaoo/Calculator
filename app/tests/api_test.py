import unittest
import requests

API_URL = 'http://10.0.0.155:80/'


class ApiTest(unittest.TestCase):
    def test_1_get_normal_result(self):
        r = requests.post(API_URL, json={"expr": "5 + 10"})
        print(f'r is {r}, type(r) is {type(r)}')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(r.json()['result'], 15)

    def test_2_get_invalid_syntax_result(self):
        r = requests.post(API_URL, json={"expr": "5 + 10)"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(r.json()['result'], 'Invalid Syntax')

    def test_3_get_invalid_syntax_result(self):
        r = requests.post(API_URL, json={"expr": "(5 + 10"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(r.json()['result'], 'Invalid Syntax')

    def test_4_get_invalid_syntax_result(self):
        r = requests.post(API_URL, json={"expr": "((5 + 10)"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(r.json()['result'], 'Invalid Syntax')

    def test_5_get_invalid_syntax_result(self):
        r = requests.post(API_URL, json={"expr": "(5( + 10)"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(r.json()['result'], 'Invalid Syntax')

    def test_6_get_invalid_operator_result(self):
        r = requests.post(API_URL, json={"expr": "5 ++ 10"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(r.json()['result'], 'Invalid Operator')

    def test_7_get_invalid_operator_result(self):
        r = requests.post(API_URL, json={"expr": "5 +- 10"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(r.json()['result'], 'Invalid Operator')

    def test_8_get_invalid_operator_result(self):
        r = requests.post(API_URL, json={"expr": "5 ** 10"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(r.json()['result'], 'Invalid Operator')

    def test_9_get_invalid_operator_result(self):
        r = requests.post(API_URL, json={"expr": "5 ^ 10"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(r.json()['result'], 'Invalid Operator')

    def test_4_empty_expr(self):
        r = requests.post(API_URL, json={"expr": ""})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 1)
        self.assertEqual(r.json()['result'], "")

