import json
from webapp.models import PSQL_Session
from flask import Blueprint, redirect, render_template, request, url_for
from webapp.users.forms import LoginForm
# from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route("/", methods=["GET", "POST"])
def landing_page():
    # if current_user.is_authenticated:
    #     return redirect(url_for("main.overview"))
    if request.method == "POST":
        if request.form["submit"] == "Login":
            pass
            # return redirect(url_for("users.login"))
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template("index.html", title="Welcome", form=form)


# @main.route("/", methods=["GET", "POST"])
# def landing_page():
#     if current_user.is_authenticated:
#         return redirect(url_for("main.overview"))
#     if request.method == "POST":
#         if request.form["btn-regular"] == "Register":
#             return redirect(url_for("users.register"))
#         elif request.form["btn-regular"] == "Login":
#             return redirect(url_for("users.login"))
#     return render_template("index.html", title="Intis Engineering")
#
#
# @main.route("/overview")
# @login_required
# def overview():
#     return render_template("overview.html", title="Overview"), {'mimetype': 'text/javascript'}
#
#
# @main.route("/update", methods=['POST', 'GET'])
# @login_required
# def update():
#     temp = dict()
#     sess = PSQL_Session()
#     # todo template_opc_ua ne smije biti hardkodiran
#     rez = sess.execute('SELECT row_to_json(row) FROM template_opc_ua row ORDER BY time DESC LIMIT 1')
#     rows = rez.fetchall()
#     sess.commit()
#     sess.close()
#     for i, row in enumerate(rows, start=0):
#         temp[i] = row['row_to_json']
#     return temp