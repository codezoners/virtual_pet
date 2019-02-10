-*- mode: org; mode: visual-line; -*-
#+STARTUP: indent

* VIRTUAL PET
** LOCAL SETUP (macOS)
*** Install =mongodb=

Using Homebrew:

#+BEGIN_SRC shell
  brew install mongodb
#+END_SRC

*** Run local database server

Spin the database up in a terminal window:

#+BEGIN_SRC shell
  mongod --config /usr/local/etc/mongod.conf
#+END_SRC

Type =^C= to shut down. Database files are stored in =/usr/local/var/mongodb=.

*** Create a test database

Download Robo 3T: https://robomongo.org/download - this can be used for queries in the native syntax (which is similar to the =pymongo= syntax), but also just for examining data interactively.

*** Set up python virtual environment

Packages needed:

- =Flask=
- =pymongo=
- =requests= (for the uploader script)

*** Try a test script

In the virtual environment, run =scripts/insert.py=: this is a simple Python script for inserting some test records and printing them out.

** LOCAL SETUP (RASPBERRY PI)
*** Update

Python note: use [[https://pipenv.readthedocs.io/en/latest/][Pipenv]] - nicer than =virtualenv=/=pip= combo. (On Mint we're using [[https://linuxbrew.sh/][linuxbrew]], and following the instructions on its banner, but that could be tricky on Raspberry Pi.) Pipenv itself should work on Pi, but might be slow: [[https://stackoverflow.com/questions/50382837/pipenv-install-timing-out-on-rpi][timeout issues]]. Also, check that Pipenv can install the pinned =pymongo= version on the Pi.

** REMOTE SETUP (MLAB/HEROKU)
*** Mongodb

Create an account at [[https://mlab.com/home][mLab]]. Create a database. Create a user.

*** Heroku

(Following [[https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0][this]] which is oriented towards Flask.)

Install [[https://devcenter.heroku.com/articles/heroku-cli][Heroku CLI tools]] (available on Homebrew).

Create a Heroku account, and then log in using the CLI tools (=heroku login=).

Create app with =heroku create=. In the Deploy settings, choose Github, and connect to the repository. Recommend: automatic deploys.

Save the requirements: =pip freeze > requirements.txt= in the virtual env, or =pipenv lock -r > requirements.txt= for Pipenv.

Make sure =gunicorn= is installed. Check the =Procfile=.
