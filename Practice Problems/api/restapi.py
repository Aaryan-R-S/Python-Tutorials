# ---------------1----------------
from flask import Flask, jsonify
app =  Flask(__name__)

# ---------------2----------------
@app.route('/')
def hello_world():
    return 'Hello World !'

@app.route('/facTrailZeros/<int:num>')
def facTrailZeros(num):
    #  --1--
    count = 0
    i = 1
    while (num//(5**i)) != 0:
        count += num//(5**i)
        i+=1

    #  --2--
    n = list(str(num))
    l = len(n)
    s = 0
    for i in n:
        i = int(i)
        i = i**l
        s += i
    if s == int(num):
        tf = True
    else:
        tf = False

    # --3--
    result = {
        "Number": num, 
        "Trailing Zeros In Factorial": count,
        "Armstrong Number": tf,
        "Server IP": '127.0.0.1',
        "Other Nums": [12,23,34,52, 'Hello'],
        "Msg":"Good Morning!"
    }

    # --4--
    return jsonify(result)

# ---------------3----------------
if __name__ == "__main__":
    app.run(debug=True)

