from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/rooms')
def rooms():
    return render_template('rooms.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

if __name__ == '__main__':
    app.run(debug=True)
