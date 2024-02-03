from flask import Flask
app = Flask(__name__)

@app.route("/home")
def welcome():
    return "this is homme page"

import controller.user_controller as user_controller
# import controller.product_controller as product_controller



