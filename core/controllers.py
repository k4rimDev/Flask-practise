from flask import Blueprint, render_template, request, \
    flash, redirect, url_for


core = Blueprint("core", __name__)

from core.forms import ContactForm
from core.models import ContactUs


@core.route("/home")
@core.route("/")
def home_page():
    
    context = {
        "title": "home"
    }
    return render_template("index.html", **context)



@core.route("/about")
def about():
    
    context = {
        "title": "about"
    }
    return render_template("about.html", **context)




@core.route("/contact", methods=["GET", "POST"])
def contact():
    
    form = ContactForm()

    if request.method == "POST":
        if form.validate_on_submit:
            instance = ContactUs(
                name = form.name.data,
                phone = form.phone.data,
                message = form.message.data,
            )

            instance.save()

            flash("Thanks for your message", "success")
            return redirect(url_for("core.contact"))

    context = {
        "title": "contact",
        "form": form,
        "user": "sfsf"
    }
    return render_template("contact.html", **context)
