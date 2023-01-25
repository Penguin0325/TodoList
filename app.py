import database
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
app.teardown_appcontext(database.close_db)

@app.route('/')
def index():
    db = database.get_db()
    articles = db.execute("SELECT * FROM POST")
    return render_template('create.html', articles=articles)

@app.route('/create')
def create_article():
    db = database.get_db()
    articles = db.execute("SELECT * FROM POST")
    return render_template('create.html', articles=articles)

@app.route('/register', methods=('GET', 'POST'))
def register_article():
    if request.method == 'GET':
        return redirect(url_for('index'))

    title = request.form['title']
    content = request.form['content']
    db = database.get_db()
    db.execute(
        "INSERT INTO POST (TITLE, CONTENT) VALUES (?, ?)",
        (title, content)
    )
    db.commit()
    return redirect(url_for('index'))

@app.route('/list')
def read_articles():
    db = database.get_db()
    articles = db.execute("SELECT * FROM POST")
    return render_template('create.html', articles=articles)

@app.route('/delete/<int:id>')
def delete_article(id):
    db = database.get_db()
    db.execute("DELETE FROM POST WHERE ID=?", (id, ))
    db.commit()
    return redirect(url_for('read_articles'))

if __name__ == '__main__':
    app.run(debug=True)
