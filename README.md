# OtherBu(アザブ)

## Overview

It is a web bookmark characterized by high customizability that you can specify bookmark placement and design as you like.
http://otherbu.com

## How to setup

1. Prepare an .env file suitable for your environment.
```
$ cp .env.example .env.local
$ vim .env.local
```

2. Create database and migrate.
```
$ ./env/otherbu_init.sh local pip
```

3. Server run as debug.
```
$ cd otherbu/application
$ ./manage.py runserver
```
