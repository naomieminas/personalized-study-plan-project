from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')   # Create this HTML file for the home page


if __name__ == '__main__':
    app.run(debug=True)
