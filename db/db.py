# pylint: disable=C0103, W0613
import sqlite3
import click

from flask import current_app, g
from flask.cli import with_appcontext

from model.user import User


def get_db():
    """
    Function that either creates a new connection to DB or returns an existing one
    :return: DB connection
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            'db.sqlite',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """
    Function that closes DB connection. e is param used by flask.
    Even though it is not used, it is mandatory
    """
    database = g.pop('db', None)

    if database is not None:
        database.close()


def init_app(app):
    """
    Initialization step for when the app is activated.
    Registers a cli command for DB initialization
    :param app: active flask app
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def init_db():
    """
    Function initializes DB from file. Flask app instance has to be running
    """

    # Init DB values from sql script
    database = get_db()
    with current_app.open_resource('db/schema.sql') as file:
        database.executescript(file.read().decode('utf8'))

    # Create test users here
    database.execute('INSERT INTO user (username, email, password) VALUES (?, ?, ?)',
                     ('admin', 'admin@admin.com', 'admin'))
    # database.commit(User(userName="admin", email="admin@admin.com", password="admin"))

    # Commit DB changes
    database.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    Clear the existing data and create new tables.
    """
    init_db()
    click.echo('Initialized database.')


def new_user(username, password):
    """
    Create new user
    """
    con = sqlite3.connect(g.db)
    cur = con.cursor()
    cur.execute("INSERT INTO "
                "user(username, email, password, password)"
                "VALUES(username, email, password, password)")
    con.commit()
    con.close()


def retrieve_user():
    """
    Retrieve existing user
    """
    con = sqlite3.connect(g.db)
    cur = con.cursor()
    cur.execute("SELECT username, password "
                "FROM user" 
                "WHERE username='{username}' AND password='{password}'")
    user = cur.fetchall()
    con.close()
    return user


def login():
    """
    Login existing user
    """
    if login.method == 'POST':
        username = login.form['username']
        password = login.form['password']
        users = retrieve_user()
        return()


def register():
    """
    Sign up new user
    """
    if register.method == 'POST':
        username = register.form['username']
        email = register.form['email']
        password = register.form['password']
        return()
