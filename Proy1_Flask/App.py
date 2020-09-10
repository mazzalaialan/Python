from flask import Flask, render_template, request, redirect, url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
""" app.config['MYSQL_USER'] = 'flask'
app.config['MYSQL_PASSWORD'] = 'flask' """
app.config['MYSQL_DB'] = 'Proy1_Flask'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()        
    cur.execute('SELECT * FROM contacts')   
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def AddContact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor() 
        cur.execute('INSERT INTO contacts(fullname,phone,email) VALUES (%s, %s, %s)',(fullname,phone,email))
        mysql.connection.commit()
        flash('Contacto Agregado Exitosamente')
    return redirect(url_for('Index'))

@app.route('/edit/<id>')
def GetContact(id):
    cur = mysql.connection.cursor()        
    cur.execute('SELECT * FROM contacts WHERE contact_id = %s',id)   
    data = cur.fetchall()
    return render_template('edit_contact.html', contact = data[0])


@app.route('/update_contact/<id>', methods=['POST'])
def UpdateContact(id):
    cur = mysql.connection.cursor()
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    cur.execute('UPDATE contacts SET fullname = %s, phone = %s, email = %s WHERE contact_id = %s',(fullname,phone,email,id))
    mysql.connection.commit()
    flash('Contacto Actualizado Exitosamente')
    return redirect(url_for('Index'))
    

@app.route('/delete/<string:id>')
def DeleteContact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE contact_id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Removido Exitosamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
    
