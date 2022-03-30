from unicodedata import category
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from Website.auth import login
from .models import Cardset, Cards
from . import db
import json
import sys

views = Blueprint("views", __name__)

@views.route("/cards", methods=["GET", "POST"])
@login_required
def cards():
    question = "words"
    answer = ""
    value = ""
    name = request.args.get("id")
    all_cards = Cards.query.filter_by(cardset = name)
    if request.method == "POST":
        value = request.form["alter_btn"]

        for i in range(len(all_cards)):
            if request.form["alter_btn"] == "button"+i:
                print('Hello world!', file=sys.stderr)
                specific_card = Cards.query.filter_by(id = i)
                question = specific_card.question
                answer = specific_card.answer

        q = request.form.get("question")
        a = request.form.get("answer")
        words_q = q.split()
        words_a = a.split()
        words_over_20 = []
        for word in words_q:
            if len(word) > 20:
                words_over_20.append(word)
        for word in words_a:
            if len(word) > 20:
                words_over_20.append(word)
        if len(q) < 1:
            flash("Question is too short", category="error")
        elif len(a) < 1:
            flash("Answer is too short", category="error")
        elif len(q) > 249:
            flash("Question is too long", category="error")
        elif len(a) > 249:
            flash("Answer is too long", category="error")
        elif words_over_20 != []:
            flash("Some words too long to accurately be formatted", category="error")
        else:
            if request.form["action"] == "cards":
                new_set = Cards(question=q, answer=a, user_id=current_user.id, cardset=name)
                db.session.add(new_set)
                db.session.commit()
                flash("Card has been added", category="success")
    return render_template("cards.html", all_cards=all_cards, user=current_user, name=name, question=question, answer=answer, value=value)


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
    return render_template("home.html", user=current_user)

@views.route('/delete-card', methods=['POST'])
def delete_card():
    name = request.args.get("id")
    card = json.loads(request.data)
    cardId = card['cardId']
    card = Cards.query.get(cardId)
    if card:
        if card.user_id == current_user.id:
            db.session.delete(card)
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
