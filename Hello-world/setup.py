import os

def Flask_install():
    import subprocess
    print("Flask's installation is now starting")
    subprocess.call("pip install Flask", shell=False)

def folder_creation():
    folder = "templates"
    os.mkdir(folder)

def Flask_creation():
    f = open("Flask1.py", "w+")
    """ 
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template('index.html')

    if __name__ == '__main__':
        app.run(debug=True)
    """






print("Now installing flask")
Flask_install()
print("Now creating folders.")
folder_creation()
print("Testing the creation")
Flask_creation()