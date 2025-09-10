import webcolors
from flask import render_template, request, redirect, url_for
from webcolors import hex_to_rgb

from app import app
from .rgb2text import get_color_name


@app.route("/")
def form():
    return render_template("form.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        color = request.form.get("color")
        text_color = get_color_name(hex_to_rgb(color))
        return render_template("result.html", name=name, email=email, color=text_color)
    else:
        return redirect(url_for("form"))
