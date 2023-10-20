from typing import Any
from sqlalchemy import create_engine, text
from collections import namedtuple
from sqlalchemy.sql.schema import Sequence
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

    jobs = [row._asdict() for row in result]  #working
    print(jobs)
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),
                          {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


#def add_application_to_db(job_id, data):
# with engine.connect() as conn:
#  query = text(
#     "INSERT INTO application (job_id, fully_name, email, phone, education)  VALUES #(:job_id, :fully_name, :email, :phone, :education) "
#)


#conn.execute(
#   query,
#  {
#     job_id: job_id,
# "fully_name": data['fully_name'],
#    "email": data['email'],
#   "phone": data['phone'],
#  "education": data['education']
# })
def add_application_to_db(job_id, data):
  ApplicationData = namedtuple(
      'ApplicationData',
      ['job_id', 'fully_name', 'email', 'phone', 'education'])

  # Create an instance of the named tuple
  application_data = ApplicationData(job_id=job_id,
                                     fully_name=data.get('fully_name'),
                                     email=data['email'],
                                     phone=data['phone'],
                                     education=data['education'])

  with engine.connect() as conn:
    query = text(
        "INSERT INTO application (job_id, fully_name, email, phone, education) "
        "VALUES (:job_id, :fully_name, :email, :phone, :education)")

    conn.execute(query, application_data._asdict())
