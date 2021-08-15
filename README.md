# airflow quickstart

## Step 1: Run Ubuntu 18.04 (From WSL)
You need to follow WSL installation

## Step 2: Install python 3.6 and upgrate pip3

```
sudo apt update
sudo apt install python3
sudo apt install python3-pip
sudo -H pip3 install --upgrade pip
sudo pip3 install gunicorn
sudo -H pip3 install --ignore-installed PyYAML
sudo -H pip2 install --upgrade pip
```

## Step 3: Run following command:
[Follow this link:](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html)

```
export AIRFLOW_HOME=~/airflow
AIRFLOW_VERSION=2.1.2
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
sudo pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
airflow db init

airflow users create \
    --username admin \
    --firstname Peter \
    --lastname Parker \
    --role Admin \
    --email spiderman@superhero.org
    
airflow webserver --port 8080

airflow scheduler
```

## Step 4: Go to airflow wd
![Image](https://raw.githubusercontent.com/duyvantest/airflow_quickstart/main/images/airflow_wd.JPG)

## Step 5: Create a dags folder inside ~/airflow
![Image](https://raw.githubusercontent.com/duyvantest/airflow_quickstart/main/images/dagfolder.JPG)

## Step 6: Write your first
See writefile.py

then run again
```
airflow db init
```
## Step 7: Trigger task and see output
Output file is at /home/duyvan
Go into taskid writefile, click on the log tab to view the log and print statement
