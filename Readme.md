#Fitbit OAuth Flask Template

This project defines a basic structure to make applications based
on the Fitbit API. It is written in Python 3.5

It defines an app structure that will give you a database, a login form, and 
a very basic registration form.

The Flask Structure is from [Miguel Grinberg's Book](http://shop.oreilly.com/product/0636920031116.do) 

If you wish to learn more about Flask check it out. Or the [Flask Project Page](http://flask.pocoo.org/)
 
[Read More About the Fitbit API](https://dev.fitbit.com/docs/)

## Developing Your Own App

First clone this repo

Then create a [Fitbit App Config](https://dev.fitbit.com/apps/new). 

This is the config I used while developing. Your app may not need read/write access.

![This is the config I used](screenshots/oauth_settings.png)

Once you have that you need to define some environment variables

Here are mine (with secrets faked. Your app will have its own values for most of these). Almost all should 
be treated with care because if they are leaked your app will be compromised

```
# Retrieved from dev.fitbit.com/apps/ for the app created earlier
FITBIT_CLIENT_ID=217sdd2
FITBIT_CLIENT_SECRET=321cb9d7g7f8b3c0bf1e24c50169f11
# Key used for CSRF protection
SECRET_KEY=sdasdas
# Signal to the app to use the development config defined in config.py
# When running tests this should be set to 'testing'
FLASK_CONFIG=development
```

After defining those you are ready to setup development

```
# Create a virtual environment for 
pyvenv venv
source venv/bin/activate
pip install -r requirements
```
Finally, you should decide on the oauth scopes for your project. Specifically, define what data your app will 
be accessing from people's Fitbit accounts. These are defined in fitbit.py. This example only uses the profile
scope. Your app will almost certainly need more than that.

[Read more about OAuth Scopes](https://dev.fitbit.com/docs/oauth2/)

Finally to run the app simply make sure your virtual environment is active and run

```
python /Users/bachmann/code/fitbitOauthFlask/manage.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 129-285-482
```
