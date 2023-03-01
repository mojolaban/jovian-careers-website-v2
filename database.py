import sqlalchemy, os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

#with engine.connect() as conn:
#  result = conn.execute(text("select * from jobs"))
#  result_dicts = []
#  for row in result.all():
#    result_dicts.append(row._asdict())
#  print(result_dicts)

#with engine.connect() as conn:
#  result = conn.execute(text("select * from jobs"))
#  print("type(result):", type(result)) #<class #'sqlalchemy.engine.cursor.CursorResult'>
#  result_all = result.all()
#  print("type(result.all):",type(result.all)) #<class 'method'>
#  first_result=result_all[0]
#  print("type(first_result):",type(first_result)) #<class #'sqlalchemy.engine.row.Row'>
#  first_result_dict=result_all[0]._asdict()
#  print("type(first_result_dict):",type(first_result_dict)) #<class #'dict'>

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),{"val":id})
    rows=result.all()
    if len(rows)==0:
      return None
    else:
      return rows[0]._asdict()