from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb
import MySQLdb.cursors



app = Flask(__name__)
app.secret_key = "123321"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'SitePFA'

db = MySQL(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users')
def users():
    return redirect(url_for('login'))


@app.route('/recommended')
def recommended():
    return render_template("recommended.html")


@app.route('/topdestination')
def topdestination():
    return render_template("topdestination.html")


@app.route('/Account/Admin', methods=['GET', 'POST'])
def delete():
    cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        for getid in request.form.getlist('myradiobox'):
            print(getid)
            cur.execute('DELETE FROM clientt WHERE id = {0}'.format(getid))
            db.connection.commit()
            cursor.execute("ALTER TABLE clientt MODIFY COLUMN id INT;"
                           "ALTER TABLE clientt DROP PRIMARY KEY;"
                           "SET @rank:=0;"
                           "update clientt set id=@rank:=@rank+1;"
                           "ALTER TABLE clientt ADD PRIMARY KEY (id);"
                           "ALTER TABLE clientt MODIFY COLUMN id INT AUTO_INCREMENT;")
            flash('Supprimé avec succès!')
    return redirect(url_for('nbrclient'))


@app.route("/account/Admin")
def nbrclient():
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select count(*) as '' from clientt;")
    result1 = cursor.fetchone()

    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("select id,username,email,age,telephone from clientt order by id;")
    result2 = cursor.fetchall()

    return render_template('adminmouaad.html', msg=result1[''], data=result2)


@app.route("/contactus",)
def contact():
    return render_template("contactus.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor1 = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor1.execute("select * from clientt where email=%s AND pass=%s", (username, password))
            info1 = cursor1.fetchone()
            cursor2 = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor2.execute("select * from adminn where email=%s AND pass=%s", (username, password))
            info2 = cursor2.fetchone()
            if info1:
                if info1['email'] == username and info1['pass'] == password:
                    session['loginsuccess'] = True
                    return redirect(url_for('profile'))
            if info2:
                if info2['email'] == username and info2['pass'] == password:
                    session['loginsuccess'] = True
                    return redirect(url_for('adminmouaad'))
            else:
                msg = 'Email or Password is wrong! check again.'
                return render_template("account.html", msg=msg)
    return render_template("account.html")


@app.route('/account', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST' and 'user' in request.form and 'email' in request.form and 'pass' in request.form and 'age' in request.form and 'phone' in request.form:
        user = request.form['user']
        email = request.form['email']
        password = request.form['pass']
        birth = request.form['age']
        phone = request.form['phone']

        cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('INSERT INTO clientt values(NULL, %s, %s, %s, %s, %s)', (user, birth, email, password, phone))
        db.connection.commit()
    return render_template('profile.html')


@app.route("/account/profileUser")
def profile():
    if session['loginsuccess']:
        return render_template("profile.html")


@app.route("/account/Admin")
def adminmouaad():
    if session['loginsuccess']:
        return redirect(url_for('nbrclient'))


@app.route('/logout')
def logout():
    session.pop('loginsuccess', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
