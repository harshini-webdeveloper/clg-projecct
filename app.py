from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  # kula irruka jobs python kitta irruka jobs ithu total ya vara
  # intha jobs name ya change punna kulla irruka jobs=jobs ya change pannulam
  # appide punna jobs=new name irrukum and { first job for html file} {secound jobs for sql db or python script }
  jobs = load_jobs_from_db(
  )  #inga variable jobs nuu sulludurathu nala yathu jobs
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  # ithuvum same function ya vangura variable name yala tha ithu vum jobs
  # jobs = load_jobs_from_db() nuu vaikurathu yala tha jsonify(jobs)
  # illa yathu ya VARA=load_jobs_from_db() nu irruntha jsonify(VARA)
  jobs = load_jobs_from_db()
  return jsonify(jobs)


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
