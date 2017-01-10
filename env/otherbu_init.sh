#!/bin/bash

echo "##### Initialize Start #####"

# For Production
if [ $1 -a $1 = "production" ]; then
    source .env.production
    echo "===== Production DB Setup ====="
    echo "GRANT ALL PRIVILEGES ON *.* to $DB_USER@'%' identified BY '$DB_PASS';" | mysql -uroot -p -h $DB_HOST
    echo "DROP DATABASE IF EXISTS $DB_NAME;" | mysql -u$DB_USER -p$DB_PASS -h $DB_HOST
    echo "CREATE DATABASE $DB_NAME DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql -u$DB_USER -p$DB_PASS -h $DB_HOST

    python ../manage.py syncdb --noinput
    python ../manage.py migrate

    echo "===== Load Master Data ====="
    mysql -u$DB_USER -p$DB_PASS $DB_NAME -h $DB_HOST < fixtures/master_data.sql
fi

# For Staging
if [ $1 -a $1 = "staging" ]; then
    source .env.staging
    echo "===== Staging DB Setup ====="
    echo "GRANT ALL PRIVILEGES ON *.* to $DB_USER@'%' identified BY '$DB_PASS';" | mysql -uroot -p -h $DB_HOST
    echo "DROP DATABASE IF EXISTS $DB_NAME;" | mysql -u$DB_USER -p$DB_PASS -h $DB_HOST
    echo "CREATE DATABASE $DB_NAME DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql -u$DB_USER -p$DB_PASS -h $DB_HOST

    python application/manage.py syncdb --noinput
    python application/manage.py migrate

    echo "===== Load Master Data ====="
    mysql -u$DB_USER -p$DB_PASS $DB_NAME -h $DB_HOST < fixtures/master_data.sql
fi

# For Develop
if [ $1 -a $1 = "develop" ]; then
    source .env
    echo "===== Create User Directory For Debug ====="
    cp -rf fixtures/debug.user static/user/facebook

    if [ $2 -a $2 = "pip" ]; then
        echo "===== Pip Install ====="
        pip install -r requirements.txt
    fi

    echo "===== Develop DB Setup ====="
    echo "GRANT ALL PRIVILEGES ON *.* to $DB_USER@'%' identified BY '$DB_PASS';" | mysql -uroot -p -h $DB_HOST
    echo "DROP DATABASE IF EXISTS $DB_NAME;" | mysql -u$DB_USER -p$DB_PASS -h $DB_HOST
    echo "CREATE DATABASE $DB_NAME DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;" | mysql -u$DB_USER -p$DB_PASS -h $DB_HOST

    python application/manage.py syncdb --noinput
    python application/manage.py migrate

    echo "===== Load Master Data ====="
    mysql -u$DB_USER -p$DB_PASS $DB_NAME -h $DB_HOST < fixtures/master_data.sql

    echo "===== Load Debug Data ====="
    mysql -u$DB_USER -p$DB_PASS $DB_NAME -h $DB_HOST < fixtures/debug_data.sql
fi

echo "##### Initialize Done #####"
