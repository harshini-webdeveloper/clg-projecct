from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Python',
    'location': 'Chennai',
    'fees': 'Rs. 9,000'
}, {
    'id': 2,
    'title': '.NET',
    'location': 'Chennai',
    'fees': 'Rs. 15,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
