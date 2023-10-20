from typing import Any
from sqlalchemy import create_engine, text
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

