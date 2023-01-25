import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

DATABASE = 'text.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

#アプリの初期化
app = Flask(__name__)
app.config.from_object(__name__)

#データベースに接続
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

#実行用コード
if __name__=='__main__':
    app.debug = True
    app.run()
