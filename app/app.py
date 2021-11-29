from flask import Flask, request, jsonify
from utils.expr_eval import eval_expr

app = Flask(__name__)


@app.route('/', methods=['POST'])
def calculator():
    expr = request.get_json()['expr']

    # get the result
    try:
        result = eval_expr(expr)
    except SyntaxError:
        result = 'Invalid Syntax'
    except KeyError:
        result = 'Invalid Operator'

    return jsonify({
        'result': result
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
