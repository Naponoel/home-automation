from flask import flash
from webapp import bcrypt
from flask_login import login_user, current_user, login_required, logout_user
from webapp.database.session_generator import Session
from models import Korisnici
from flask import Blueprint, redirect, render_template, request, url_for
from webapp.forms.users import LoginForm
from webapp import login_manager

main = Blueprint('main', __name__)


@login_manager.user_loader
def load_user(user_id):
    sess = Session()
    return sess.query(Korisnici).get(int(user_id))


@main.route("/", methods=["GET", "POST"])
def landing_page():
    if current_user.is_authenticated:
        return redirect(url_for("main.upravljanje"))
    form = LoginForm()
    if form.validate_on_submit():
        sess = Session()
        korisnik = sess.query(Korisnici).filter_by(korisnicko_ime=form.username.data).first()
        sess.close()
        if korisnik:
            if bcrypt.check_password_hash(korisnik.zaporka, form.password.data):
                login_user(korisnik, remember=form.remember.data)
                next_page = request.args.get("next")
                flash(f'Login Success for user "{form.username.data}"', "success")
                return (
                    redirect(next_page)
                    if next_page
                    else redirect(url_for("main.upravljanje"))
                )
            else:
                flash("Login unsuccessful. Try Again.", "danger")
    return render_template("index.html", title="Welcome", form=form)


@main.route("/upravljanje")
@login_required
def upravljanje():
    return render_template("upravljanje.html", title="Overview"), {'mimetype': 'text/javascript'}


@main.route("/odjava")
def odjava():
    logout_user()
    return redirect(url_for("main.landing_page"))


@main.route('/postavke')
@login_required
def postavke():
    return render_template("postavke.html", title="Postavke")
