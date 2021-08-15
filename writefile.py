from datetime import datetime
from datetime import timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import pendulum

def writefile():
    f = open("myfile.txt", "a")
    f.write("\nNow the file has more content! %s" % datetime.now())
    f.close()
    print('Done Writing')
    print(os.getcwd())

local_tz = pendulum.timezone("Asia/Bangkok")


dag_params = {
    'owner': 'airflow',
    "depends_on_past": False,
    'start_date': datetime(2021, 8, 15, 0, 0, tzinfo=local_tz),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=10),
}

dag = DAG('name_writefile',
          catchup=False,
          default_args=dag_params,
          schedule_interval='*/1 * * * *'
)

dummy_op = DummyOperator(task_id="dummy_start", dag=dag)

py_op_1 = PythonOperator(task_id="writefile",
                         python_callable=writefile,
                         dag=dag)

dummy_op >> py_op_1