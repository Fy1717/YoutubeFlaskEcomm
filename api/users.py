from flask import jsonify, Blueprint, request
from werkzeug.security import generate_password_hash

from ecommerce.models import User

apiUsers = Blueprint("apiUser", __name__, url_prefix="/api/users")


@apiUsers.route("/")
def users():
    try:
        allUsers = User.get_all_users()
        users = []

        for user in allUsers:
            users.append(
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "password": user.password,
                    "activated": user.activated,
                }
            )

        return jsonify({"success": True, "data": users, "count": len(users)})
    except Exception as e:
        # print("ERROR in users: ", e)
        return jsonify({"success": False, "message": "There is an error.."})


@apiUsers.route("/<int:id>", methods=["GET", "DELETE", "PUT"])
def user(id):
    try:
        user = User.get_user_by_id(id)

        if user is None:
            return jsonify({"success": False, "message": "User not found"})

        if request.method == "GET":
            userObj = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "password": user.password,
            }

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

            hashed_password = generate_password_hash(password)

            User.update_user(id, username, email, hashed_password)

            return jsonify({"success": True, "message": "User updated"})

        # -----------------------------------------------------------------------------

    except Exception as e:
        # print("ERROR in user: ", e)
        return jsonify({"success": False, "message": "There is an error.."})


@apiUsers.route("/addUser", methods=["POST"])
def addUser():
    try:
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        print("USERNAME: ", username)
        print("EMAIL: ", email)
        print("PASSWORD: ", password)

        if username == None or email == None or password == None:
            return jsonify({"success": False, "message": "Missing fields"})

        hashed_password = generate_password_hash(password)

        print("HASHED PASSWORD: ", hashed_password)

        User.add_user(username, email, hashed_password)

        return jsonify({"success": True, "message": "User added successfully.."})
    except Exception as e:
        print("ERROR in addUser: ", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiUsers.route("activate_user", methods=["POST"])
def activateUser():
    try:
        id = request.form.get("id")
        user = User.get_user_by_id(id)

        if user is None:
            return jsonify({"success": False, "message": "User not found"})

        if user.activated == True:
            return jsonify({"success": False, "message": "User already activated"})

        User.activate_user(id)

        return jsonify({"success": True, "message": "User activated"})
    except Exception as e:
        print("ERROR in activateUser: ", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiUsers.route("deactivate_user", methods=["POST"])
def deactivateUser():
    try:
        id = request.form.get("id")
        user = User.get_user_by_id(id)

        if user is None:
            return jsonify({"success": False, "message": "User not found"})

        if user.activated == False:
            return jsonify({"success": False, "message": "User already deactivated"})

        User.deactivate_user(id)

        return jsonify({"success": True, "message": "User deactivated"})
    except Exception as e:
        print("ERROR in deactivateUser: ", e)
        return jsonify({"success": False, "message": "There is an error"})


@apiUsers.route("deactiveusers", methods=["GET"])
def deactiveUsers():
    try:
        allUsers = User.get_all_users()
        users = []

        for user in allUsers:
            if user.activated == False:
                users.append(
                    {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "password": user.password,
                        "activated": user.activated,
                    }
                )

        return jsonify({"success": True, "data": users, "count": len(users)})
    except Exception as e:
        print("ERROR in deactiveUsers: ", e)
        return jsonify({"success": False, "message": "There is an error.."})


@apiUsers.route("activeusers", methods=["GET"])
def activeUsers():
    try:
        allUsers = User.get_all_users()
        users = []

        for user in allUsers:
            if user.activated:
                users.append(
                    {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "password": user.password,
                        "activated": user.activated,
                    }
                )

        return jsonify({"success": True, "data": users, "count": len(users)})
    except Exception as e:
        print("ERROR in activeUsers: ", e)
        return jsonify({"success": False, "message": "There is an error.."})
