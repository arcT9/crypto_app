# CryptoBot
![Build Status](https://img.shields.io/badge/build-passing-green) ![Python Verion](https://img.shields.io/badge/python-3.9-blue)

This project tracks the live prices of BTC and ETH from two different exchanges ([Binance](https://www.binance.com/en) & [Coinbase](https://www.coinbase.com/)) and provides a recommendations about where one can buy and sell them to their profits.
The deployed website can be found [here](https://www.turaga-crypto-bot.herokuapp.com).
## Getting Started
### Installing Dependencies
#### Python 3.9
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)
#### Virtual Environment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by navigating to the project directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.
##### Key Dependencies
- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.
## Running the server
From within the `project` directory first ensure you are working using your created virtual environment.
To run the server, execute:
```bash
export FLASK_ENV=development
flask run
```
Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.
### Running the App
To run the sample, make sure you have `python` and `pip` installed.
Run `pip install -r requirements.txt` to install the dependencies and run `python server.py`. 
The app will be served at [http://localhost:5000/](http://localhost:5000/).
## Hosting
This app is deployed on heroku and can be found [here](https://www.turaga-crypto-bot.herokuapp.com).
It is currently running on Hobby Dynos.
To host your app follow these steps - 
 - Create a `Procfile` in the project directory.
 - Inside the Procfile put the following
 ```text
 web: gunicorn app:app
 ```
 - Push the entire project to GIT
 - Go to Heroku and create a new app
 - Link your Github account on heroku
 - Link the project Github repo in the Heroku App Settings
 - Configure it for auto deployment
 - In Heroku App Setting, copy all the `.env` file contents.
 - Add a hobby dev Postgres server from Heroku addons
<hr>
## Author
#### Archana Turaga