survey
======

app to create survey

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Requirements
----------------

1. Create an AWS Ubuntu Machine using free tier account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2. Setup Up Docker on your machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* First install docker on machine.
For Mac: If you are a mac user, please follow https://runnable.com/docker/install-docker-on-macos
For Linux(Ubuntu): https://docs.docker.com/install/linux/docker-ce/ubuntu/

3. ssh into the machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



After the requirements are installed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Once you have completed docker installation, including docker and docker-compose, follow following instructions


Instructions
------------------------------------------

1. Build the app
^^^^^^^^^^^^^^^^^^^

* To run the application, we need to build it first using following command

    $ docker-compose -f local.yml  build


2. Make Migrations
^^^^^^^^^^^^^^^^^^^

* To run the application, we need to build it first using following command

    $ docker-compose -f local.yml run django python manage.py makemigrations


3. Migrate the app
^^^^^^^^^^^^^^^^^^^

* To run the application, we need to build it first using following command

    $ docker-compose -f local.yml run django python manage.py migrate


4. Set up Admin User
^^^^^^^^^^^^^^^^^^^^^^

* To create an **admin account**, use this command::

     $ docker compose -f local.yml run django python manage.py createsuperuser


5. Run the app
^^^^^^^^^^^^^^^^

* To run the application, we need to build it first using following command

    $ sudo nohup docker-compose -f local.yml  up --build


6. Access the app
^^^^^^^^^^^^^^^^

* Go to your browser and type: localhost:8001
* Enter into admin and then create:
    a. survey
    b. code


7. Accessing the survey
^^^^^^^^^^^^^^^^^^^^^

* Go to your browser and using the survey number and code you just created, type: localhost:8001/<survey_number>/<code>


8. Sample demo of the app
^^^^^^^^^^^^^^^^^^^^^

* Go to http://54.210.233.238:8001/
