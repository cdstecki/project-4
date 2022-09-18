from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    cats = [{'name': 'fluffy', 'size': 'big'}, {'name': 'smelly', 'size': 'small'}]
    if request.method == 'GET':
        return render_template('index.html', cats=cats)
    elif request.method == 'POST':
        return "thanks"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")