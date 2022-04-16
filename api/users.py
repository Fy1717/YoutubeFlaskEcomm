from flask import Flask, jsonify, Blueprint, request
from ecommerce.models import User

apiUsers = Blueprint("apiUser", __name__, url_prefix="/api/users")


@apiUsers.route("/")
def users():    
    try:
        allUsers = User.get_all_users()
        users = []

        for user in allUsers:
            users.append({"id": user.id, "username": user.username, "email": user.email, "password": user.password})

        return jsonify({"success": True, "data": users, "count": len(users)})
    except Exception as e:
        #print("ERROR in users: ", e)
        return jsonify({"success": False, "message": "There is an error.."})


@apiUsers.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def user(id):
    try:
        user = User.get_user_by_id(id)

        if user is None:
            return jsonify({"success": False, "message": "User not found"})

        if request.method == "GET":
            userObj = {"id": user.id, "username": user.username, "email": user.email, "password": user.password}

            return jsonify({"success": True, "data": userObj})

        # -----------------------------------------------------------------------------

        elif request.method == "DELETE":
            user.delete_user(id)

            return jsonify({"success": True, "message": "User deleted"})

        # -----------------------------------------------------------------------------

        elif request.method == "PUT":
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")

            print("USERNAME: ", username)
            print("EMAIL: ", email)
            print("PASSWORD: ", password)

            if username == None:
                username = user.username
            if email == None:
                email = user.email
            if password == None:
                password = user.password

            User.update_user(id, username, email, password)

            return jsonify({"success": True, "message": "User updated"})

        # -----------------------------------------------------------------------------
    
    except Exception as e:
        #print("ERROR in user: ", e)
        return jsonify({"success": False, "message": "There is an error.."})


@apiUsers.route("/addUser", methods=["POST"])
def addUser():
    try:
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        ''' print("USERNAME: ", username)
        print("EMAIL: ", email)
        print("PASSWORD: ", password)

        print("------------------") '''

        User.add_user(username, email, password)

        return jsonify({"success": True, "message": "User added successfully.."})
    except Exception as e:
        #print("ERROR in addUser: ", e)
        return jsonify({"success": False, "message": "There is an error"})

