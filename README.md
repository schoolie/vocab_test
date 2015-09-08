# vocab_test - A simple Flask app to replace that stack of flash cards
=============

A Simple Flask app for studying vocab for the GRE

Installation
------------

Install dependencies via pip::

    pip install -r requirements.txt

Configuration
------------

By default, the database is stored as an SQLite DB at data-dev.sqlite. 

Modify SQLALCHEMY_DATABASE_URI in config.py to change this.

Deployment
------------

Prior to running the app, run 
    
    python import_words.py
    
to populate the database.

Then call

    python manage.py runserver
    
To start the app. By default, the application will be available at http://localhost:5000
