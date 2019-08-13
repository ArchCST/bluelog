# -*- coding: utf-8 -*-
"""
    :author: ArchCST
    :url: http://ArchCST.me
    :copyright: © 2019 ArchCST <cst@crystl.cc>
    :license: MIT, see LICENSE for more details.
"""
from flask import Blueprint, render_template

from bluelog.forms import LoginForm

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'The Login Page'


@auth_bp.route('/logout')
def logout():
    return 'Logout'
