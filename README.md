# Ceties and Countries REST API

REST API to return information about cities and countries

## Getting Started

### Prerequisites

- [Python3.6](https://www.python.org/downloads/) or later

### Installing

#### Create virtual environment

``` bash
pip install --upgrade virtualenv
virtualenv -p python3 env
source env/bin/activate && cd env
```

#### Clone The repository, install dependencies and create db

``` bash
(env) $ git clone https://github.com/mohamed17717/City-Country-REST.git src && cd src
(env) $ pip install -r requirements.txt
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
(env) $ python manage.py createsuperuser
```

#### Write data into db

``` bash
(env) $ python writeJsonToDb.py
```

#### Run

``` bash
(env) $ python manage.py runserver
```

## Built With

- **Django** -  The web framework used
- **Django Rest Framework** - REST API

## API Features

### return all countries

> `/api/`

### return all **cities** in the **country**

> `/api/{{ countryName }}/cities`\
> `/api/{{ countryId }}/`

### return **City** in wich **country**

> `/api/{{ cityName }}/where/`

### return number of random **cities** of a given **country**

> `/api/random/{{ number }}/cities/{{ countryname }}`\
> `/api/random/{{ number }}/cities/{{ countryId }}`

### return number of rundom **countries**

> `/api/random/{{ number }}/countries`
