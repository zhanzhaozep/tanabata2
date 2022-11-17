from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/input_app', methods=['POST'])
def input_app():
    id = request.form['id']
    pwd = request.form['pwd']
    return id + '' + pwd

if __name__ == '__main__':
    app.run(debug = True)
