#!/bin/bash

source application/settings/private_config.py

echo '##### Initialize Start #####'

# For Production
if [ $1 -a $1 = 'production' ]; then
    echo '===== DB Setup ====='
    echo 'GRANT ALL PRIVILEGES ON *.* to ${DB_USER}@localhost identified BY "${DB_PASS}";' | mysql -uroot -p
    echo 'DROP DATABASE IF EXISTS ${DB_NAME};' | mysql -u${DB_USER} -p${DB_PASS}
    echo 'CREATE DATABASE ${DB_NAME} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;' | mysql -u${DB_USER} -p${DB_PASS}

    python ../manage.py syncdb --noinput
    python ../manage.py migrate

    echo '===== Load Master Data ====='
    mysql -u${DB_USER} -p${DB_PASS} ${DB_NAME} < fixtures/master_data.sql
fi

# For Staging
if [ $1 -a $1 = 'staging' ]; then
    echo '===== Dev DB Setup ====='
    echo 'GRANT ALL PRIVILEGES ON *.* to ${DB_USER}@localhost identified BY "${DB_PASS}";' | mysql -uroot -p
    echo 'DROP DATABASE IF EXISTS ${DEV_DB_NAME};' | mysql -u${DEV_DB_USER} -p${DEV_DB_PASS}
    echo 'CREATE DATABASE ${DEV_DB_NAME} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;' | mysql -u${DEV_DB_USER} -p${DEV_DB_PASS}

    python application/manage.py syncdb --noinput
    python application/manage.py migrate

    echo '===== Load Master Data ====='
    mysql -u${DEV_DB_USER} -p${DEV_DB_PASS} ${DEV_DB_NAME} < fixtures/master_data.sql
fi

# For Develop
if [ $1 -a $1 = 'develop' ]; then
    echo '===== Create User Directory For Debug ====='
    cp -rf fixtures/debug.user static/user/facebook

    if [ $2 -a $2 = 'pip' ]; then
        echo '===== Pip Install ====='
        pip install -r requirements.txt
    fi

    echo '===== Local DB Setup ====='
    echo 'GRANT ALL PRIVILEGES ON *.* to ${DB_USER}@localhost identified BY "${DB_PASS}";' | mysql -uroot -p
    echo 'DROP DATABASE IF EXISTS ${DB_NAME};' | mysql -u${DB_USER} -p${DB_PASS}
    echo 'CREATE DATABASE ${DB_NAME} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;' | mysql -u${DB_USER} -p${DB_PASS}

    python application/manage.py syncdb --noinput
    python application/manage.py migrate

    echo '===== Load Master Data ====='
    mysql -u${DB_USER} -p${DB_PASS} ${DB_NAME} < fixtures/master_data.sql

    echo '===== Load Debug Data ====='
    mysql -u${DB_USER} -p${DB_PASS} ${DB_NAME} < fixtures/debug_data.sql
fi

echo '##### Initialize Done #####'
