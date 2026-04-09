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

# @app.route("/sitemap.xml")
# def sitemap():
#     pages = []
#
#     pages.append("https://irisroomstrigona.gr/")
#     pages.append("https://irisroomstrigona.gr/rooms")
#     pages.append("https://irisroomstrigona.gr/activities")
#     pages.append("https://irisroomstrigona.gr/contact")
#
#     xml = render_template("sitemap.xml", pages=pages)
#
#     response = make_response(xml)
#     response.headers["Content-Type"] = "application/xml"
#
#     return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
