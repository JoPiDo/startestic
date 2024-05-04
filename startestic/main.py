
from api import Api
from database import Database
from flask import Flask
from galaxy import Galaxy
from star import Star


def __main__():
    path = "galaxies/galaxy_001.txt"

    print("Read galaxy from file: {path}...")
    galaxy = Galaxy()
    galaxy.read_galaxy_from_file(path)
    print("...done read galaxy!")

    db = Database()
    Star.database = db

    print("Start API...")
    app = Flask(__name__)
    Api(app, galaxy)
    app.run(debug=True)


if __name__ == "__main__":
    __main__()
