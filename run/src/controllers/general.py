#!/usr/bin/env python3

<<<<<<< HEAD

=======
>>>>>>> e9a58c15e55c8b4b5a4d6641ef0668fe08aa17e1
from flask import Blueprint, render_template, request, redirect, session
import operator
import models

controller = Blueprint('/Goldigger', __name__, url_prefix = '/Goldigger')

@controller.route('/Welcome', methods = ['GET','POST'])
def welcome():
    if request.method == 'GET':
        return render_template('wifi_m/landing_page/index.html')
    else:
        if request.form['submit'] == 'agree':
            models.get_cert()
            if True:
            #TODO serve script from models
            #TODO locate current IP address, append to txt file, and pass onto mining py file
                return redirect ('http://www.google.com', code = 302)
        else:
            return redirect ('/Golddigger/Welcome')

@controller.route('/Admin', methods = ['GET','POST'])
def admin():
    if request.method == 'GET':
        secret_key = 'v39MYkdyRkYqkuqbqfRGC6JbNct3Eka0'
        stats = models.get_stats(secret_key)
        balance = models.get_balance(secret_key)
        return render_template('admin.html', stats=stats, balance=balance)
    else:
        return render_template('admin.html')
