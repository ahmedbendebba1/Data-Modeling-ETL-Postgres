# Data-Modeling-with-Postgre
Data Modeling with Postgre and build an ETL pipeline using Python

Before running create_tables.py, you should install, setup Postgresql and create a Postgre database named "sparkifydb" :

  # Install postgresql server
  !sudo apt-get -y -qq update
  !sudo apt-get -y -qq install postgresql
  !sudo service postgresql start

  # Setup a password `postgres` for username `postgres`
  !sudo -u postgres psql -U postgres -c "ALTER USER postgres PASSWORD 'postgres';"

  # Setup a database with name `sparkifydb` to be used
  !sudo -u postgres psql -U postgres -c 'DROP DATABASE IF EXISTS sparkifydb;'
  !sudo -u postgres psql -U postgres -c 'CREATE DATABASE sparkifydb;'
