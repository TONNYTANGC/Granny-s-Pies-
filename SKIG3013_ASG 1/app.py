from flask import Flask, render_template

app = Flask (__name__)
app.secret_key = "flash_message"

@app.route('/pie')
def pie (): 
    return render_template('pie.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)