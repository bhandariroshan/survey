survey
======

app to create survey

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Requirements
--------------

Setting Up Docker on your machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* First install docker on your machine. If you are a mac user, please follow https://runnable.com/docker/install-docker-on-macos

Running The App
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Once you have completed docker installation, including docker and docker-compose, follow following instructions


Instructions
--------------

Build the app
^^^^^^^^^^^^^

* To run the application, we need to build it first using following command

    $ docker-compose -f local.yml  build


Set up Admin User
^^^^^^^^^^^^^^^^^

* To create an **admin account**, use this command::

     $ docker compose -f local.yml run django python manage.py createsuperuser


Run the app
^^^^^^^^^^^^^

* To run the application, we need to build it first using following command

    $ docker-compose -f local.yml  up --build

* Go to your browser and type: localhost:8000
* Enter into admin and then create:
    a. survey
    b. code

Accessing the survey
^^^^^^^^^^^^^^^^^^^^^

* Go to your browser and using the survey number and code you just created, type: localhost:8000/<survey_number>/<code>

Sample demo of the app
^^^^^^^^^^^^^^^^^^^^^

* Go to http://54.210.233.238:8000/
