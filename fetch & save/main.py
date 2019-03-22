from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import yaml
app = Flask(__name__)
#Database config
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
#Creates the mysql configuration
mysql = MySQL(app)

#When you add a route it assumes the user wants to go to the corrosponding directory/routes to the file
@app.route('/', methods=['GET', 'POST'])
def index():
    #This will return the text test
    if request.method == 'POST':
        #Gets the form data
        userDetails = request.form
        name = userDetails['name'] #This is the form value for the index page
        email = userDetails['email'] #This is the form value for the index page
        username = userDetails['user']
        cur = mysql.connection.cursor()
        #creates the connection
        cur.execute("INSERT INTO users(name, email, user) VALUES(%s, %s, %s)",(name,email,user))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
