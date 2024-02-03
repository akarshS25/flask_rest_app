from app import app
from model.user_model import user_model
from flask import request
obj = user_model()

@app.route("/user/getall")
def user_getall_controller():
    return obj.user_getall_model()

@app.route("/user/addone",methods=["POST"])
def user_addone_controller():
    return obj.user_addone_model(request.form)

@app.route("/user/delete/<s_no>",methods=["DELETE"])
def user_delete_controller(s_no):
    return obj.user_delete_model(s_no)

# @app.route("/user/patch/<s_no>",methods=["PATCH"])
# def user_patch_controller(s_no):
#     return obj.user_patch_model(request.form,s_no)

#pagination
@app.route("/user/getall/limit/<limit>/page/<page>",methods=["GET"])
def user_pagination_controller(limit, page):
    return obj.user_pagination_model(limit,page)