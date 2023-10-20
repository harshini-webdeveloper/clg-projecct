from flask import Flask, jsonify, render_template, request

from database import load_job_from_db, load_jobs_from_db, add_application_to_db

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


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Job Not Found", 404
  return render_template('jobpage.html', job=job)


@app.route("/job/<id>/apply",
           methods=['post'])  #APPLY THA JOB ID VARA THA APPLY THA JOB ID
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  # Store this in the DB
  # Store an email
  # Display an acknowledgment page
  return render_template('application_submitted.html',
                         application=data,
                         job=job)


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
