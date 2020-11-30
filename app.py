import json
from flask import Flask, request
from database.settings import login_to_firebase
from database.User import User

app = Flask(__name__)


@app.route('/create_new_user', methods=["POST"])
def create_new_user():
    req_content = request.json

    user = User(req_content)

    _, error = user.create_in_firebase()

    if error:
        return error

    return "Successfully created the user!"


if __name__ == '__main__':
    login_to_firebase()
    app.run()
