from unicodedata import category
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from Website.auth import login
from .models import Cardset, Cards
from . import db
import json
import sys
import random

views = Blueprint("views", __name__)

@views.route("/cards", methods=["GET", "POST"])
@login_required
def cards():
    print("x")
    question = "words"
    answer = ""
    name = request.args.get("id")
    all_cards = Cards.query.filter_by(cardset = name).all()
    if request.method == "POST":
        form_name = request.form["form-name"]
        if form_name == "cards":
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
                new_set = Cards(question=q, answer=a, user_id=current_user.id, cardset=name)
                db.session.add(new_set)
                db.session.commit()
                flash("Card has been added", category="success")
        if form_name == "revised_cards":
            q = request.form.get("modal_question")
            a = request.form.get("modal_answer")
            index = request.form.get("card-id")
            id = index[9:]
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
                print(id)
                new = Cards.query.filter_by(id = id).all()
                print(new)
                new.question = q
                new.answer = a
                db.session.commit()
                flash("Card has been added", category="success")

        if form_name == "shuffle-btn":
            print(all_cards)
            all_cards = sorted(all_cards, key=lambda k: random.random())
            print(all_cards)
    return render_template("cards.html", all_cards=all_cards, user=current_user, name=name, question=question, answer=answer)


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
