from unicodedata import category
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from Website.auth import login
from .models import Note, Maths, Cardset, Cards
from . import db
import json

views = Blueprint("views", __name__)

@views.route("/cards", methods=["GET", "POST"])
@login_required
def cards():
    name = request.args.get("id")

    all_cards = Cards.query.filter_by(cardset = name)

    if request.method == "POST":
        q = request.form.get("question")
        a = request.form.get("answer")
        if len(q) < 1:
            flash("Question is too short", category="error")
        elif len(a) < 1:
            flash("Answer is too short", category="error")
        else:
            if request.form["action"] == "cards":
                new_set = Cards(question=q, answer=a, user_id=current_user.id, cardset=name)
                db.session.add(new_set)
                db.session.commit()
                flash("Card has been added", category="success")
    return render_template("cards.html", all_cards=all_cards, user=current_user, name=name)


@views.route("/cardset", methods=["GET", "POST"])
@login_required
def cardset():
    if request.method == "POST":
        cardsetname = request.form.get("cardset-name")

        if len(cardsetname) < 1:
            flash("Card set name is too short", category="error")
        else:
            if request.form["action"] == "cardset":
                new_set = Cardset(name=cardsetname, user_id=current_user.id)
                db.session.add(new_set)
                db.session.commit()
                flash("Cardset has been added", category="success")
    return render_template("cardset.html", user=current_user)

@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")
        ans = request.form.get("ans")

        if len(note) < 1:
            flash("Question is too short", category="error")
        else:
            if len(ans) < 1:
                flash("Answer is too short", category="error")
            else:
                if request.form["action"] == "All":
                    new_note = Note(data=note, user_id=current_user.id, answer=ans)
                    db.session.add(new_note)
                    db.session.commit()
                    flash("Note has been added", category="success")
                elif request.form["action"] == "Maths":
                    new_note = Maths(data=note, answer=ans, user_id=current_user.id)
                    db.session.add(new_note)
                    db.session.commit()
                    flash("Note has been added", category="success")

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/delete-cardset', methods=['POST'])
def delete_cardset():
    cardset = json.loads(request.data)
    cardId = cardset['cardId']
    cardset = Cardset.query.get(cardId)
    if cardset:
        if cardset.user_id == current_user.id:
            db.session.delete(cardset)
            db.session.commit()
        
    return jsonify({})