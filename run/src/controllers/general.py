#!/usr/bin/env python3

from flask import Blueprint, render_template, request, redirect, session
import operator
from . import models

controller = Blueprint('/Goldigger', __name__, url_prefix = '/Goldigger')

@controller.route('/Welcome', methods = ['GET','POST'])
def welcome():
    if request.method == 'GET':
        return render_template('welcome.html')
    else:
        if request.form['submit'] == 'agree':
            #TODO serve script from models
            #TODO locate current IP address, append to txt file, and pass onto mining py file
            return redirect ('http://www.google.com', code = 302)
        else:
            return redirect ('/Golddigger/Welcome')

@controller.route('/Admin', methods = ['GET','POST'])
def admin():




