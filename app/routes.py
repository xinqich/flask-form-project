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
        form_data = dict(request.form.lists())
        rgb_color = hex_to_rgb(form_data['color'][0])
        color_text = get_color_name(rgb_color)
        return render_template("result.html",
                               name=form_data['name'][0],
                               email=form_data['email'][0],
                               color=color_text,
                               profession=form_data['profession'][0],
                               hobbies=form_data.get('hobbies', None),
                               level=form_data['level'][0])
    else:
        return redirect(url_for("form"))
