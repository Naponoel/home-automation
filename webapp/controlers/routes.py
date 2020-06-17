from flask import render_template, Blueprint
from flask_login import login_required
from webapp.models import Kontroler
from webapp.controlers.forms import KontrolerForm

controlers = Blueprint("controlers", __name__)


@controlers.route('/postavke')
@login_required
def postavke():
    form = KontrolerForm()
    if form.validate_on_submit():
        print('valideted')
    return render_template("postavke.html", title="Postavke", form=form)
