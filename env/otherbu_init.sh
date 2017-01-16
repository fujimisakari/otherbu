#!/bin/bash


initialize () {
    if [ $2 -a $2 = "pip" ]; then
        echo "===== Pip Install ====="
        pip install -r env/requirements.txt
    fi

    python application/manage.py syncdb --noinput
    python application/manage.py migrate

    echo "===== Load Master Data ====="
    mysql -u$DB_USER -p$DB_PASS $DB_NAME -h $DB_HOST < fixtures/master_data.sql
}

echo "##### Initialize Start #####"

# For Production
if [ $1 -a $1 = "production" ]; then
    source .env.production
    initialize
fi

# For Staging
if [ $1 -a $1 = "staging" ]; then
    source .env.staging
    initialize
fi

# For Develop
if [ $1 -a $1 = "develop" ]; then
    source .env.develop

    echo "===== DB Setup ====="
    echo "GRANT ALL PRIVILEGES ON *.* to $DB_USER@'%' identified BY '$DB_PASS';" | mysql -uroot -p -h $DB_HOST
    echo "DROP DATABASE IF EXISTS $DB_NAME;" | mysql -u$DB_USER -p$DB_PASS -h $DB_HOST
    echo "CREATE DATABASE $DB_NAME DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql -u$DB_USER -p$DB_PASS -h $DB_HOST

    initialize

    echo "===== Load Debug Data ====="
    mysql -u$DB_USER -p$DB_PASS $DB_NAME -h $DB_HOST < fixtures/debug_data.sql

    echo "===== Create User Directory For Debug ====="
    cp -rf fixtures/debug.user static/user/facebook
fi

# For Local
if [ $1 -a $1 = "local" ]; then
    source .env.local

    echo "===== DB Setup ====="
    echo "GRANT ALL PRIVILEGES ON *.* to $DB_USER@'%' identified BY '$DB_PASS';" | mysql -uroot -p -h $DB_HOST
    echo "DROP DATABASE IF EXISTS $DB_NAME;" | mysql -u$DB_USER -p$DB_PASS -h $DB_HOST
    echo "CREATE DATABASE $DB_NAME DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql -u$DB_USER -p$DB_PASS -h $DB_HOST

    initialize

    echo "===== Load Debug Data ====="
    mysql -u$DB_USER -p$DB_PASS $DB_NAME -h $DB_HOST < fixtures/debug_data.sql

    echo "===== Create User Directory For Debug ====="
    cp -rf fixtures/debug.user static/user/facebook
fi

echo "##### Initialize Done #####"
