from flask import *
import json

app = Flask(__name__)

cars = []
MY_DATA = 'my_cars.json'
users = []
USERS_DATA = 'users.json'

def load_cars_json():
    global cars
    try:
        with open(MY_DATA, 'r') as fileLoad:
            json_string = fileLoad.read()
        cars = json.loads(json_string)
    except: return cars

def save_cars_json():
    global cars
    json_string = json.dumps(cars)
    with open(MY_DATA, 'w') as filesave:
        filesave.write(json_string)
    
def load_users():
    global users
    try:
        with open(USERS_DATA, 'r') as fileLoad:
            json_string = fileLoad.read()
        users = json.loads(json_string)
    except: return users

def save_users():
    global users
    json_string = json.dumps(users)
    with open(USERS_DATA, 'w') as filesave:
        filesave.write(json_string)

def chack_user(username, pwd, users):
    for user in users:
        if user["username"] == username and user["password"] == pwd:
            return True
    return False

@app.route("/")
def main():
    return render_template("entry.html")

@app.route("/submit", methods=['GET','POST'])
def submit():
    global users
    global cars
    load_cars_json()
    try:
        load_users()
        fName = request.form["fName"]
        lName = request.form["lName"]
        pwd = request.form["password"]
        users.append({"username": fName, "lName": lName, "password": pwd})
        save_users()
        return render_template("submit.html", cars=cars, fName=fName, lName=lName) 
    except:
        name = request.form["name"]
        pwd = request.form["password"]
        load_users()
    if chack_user(name, pwd, users):
        return render_template("submit.html", cars=cars,  fName=fName, lName=lName) 
    else:
        return render_template("entry.html", msg="username or password are incorrect")
    

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/submit_car", methods=['POST', 'GET'])
def submit_car():
    global cars
    if len(cars) == 0:
        load_cars_json()
    brand = request.form["brand"]
    model = request.form["model"]
    color = request.form["color"]
    license = request.form["license"]
    cars.append({"brand":brand, "model":model, "color":color, "license":license})
    save_cars_json()
    return render_template("submit.html", cars=cars)

if __name__ == "__main__":
    app.run(debug=True)