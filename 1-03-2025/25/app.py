from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = ''  
app.config['MYSQL_DB'] = 'companyDB'

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee")
    employees = cur.fetchall()
    cur.close()
    return render_template('index.html', employees=employees)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        salary = request.form['salary']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employee (first_name, last_name, email, salary) VALUES (%s, %s, %s, %s)",
                    (first_name, last_name, email, salary))
        mysql.connection.commit()
        cur.close()
        
        return redirect('/')


@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        salary = request.form['salary']

        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE employee SET first_name=%s, last_name=%s, email=%s, salary=%s WHERE id=%s
        """, (first_name, last_name, email, salary, id))
        mysql.connection.commit()
        cur.close()
        
        return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employee WHERE id=%s", [id])
    mysql.connection.commit()
    cur.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
