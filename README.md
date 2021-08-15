# airflow quickstart

## Step 1: Run Ubuntu 18.04 (From WSL)
You need to follow WSL installation

## Step 2: Install python 3.6 and upgrate pip3

```
sudo apt update
sudo apt install python3.6
sudo -H pip3 install --upgrade pip
sudo -H pip2 install --upgrade pip
```

## Step 3: Run following command:
[Follow this link:](https://airflow.apache.org/docs/apache-airflow/stable/start/local.html)

```
export AIRFLOW_HOME=~/airflow
AIRFLOW_VERSION=2.1.2
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
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

