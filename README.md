The first thing to do is to clone the repository:

$ git clone https://github.com/RythmSharma96/pesto-backend.git 

Create a virtual environment to install dependencies in and activate it.

Then install the dependencies:
(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment.

Run the migrations.

Once pip has finished downloading the dependencies:

(env)$ cd pesto
(env)$ python manage.py runserver

Test cases can be run using the following command:
./manage.py test tasks.tests 


Implemented:
Test cases
Add / Update / Delete functionality with http response codes
title mandatory validation
UI Modals on save and errors
Filter tasks according to status

