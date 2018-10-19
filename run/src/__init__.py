#!/usr/bin/env python3

from flask import Flask
from .controllers.general import controller as general_controller

omnibus = Flask (__name__)

omnibus.register_blueprint(general_controller)
