# -*- coding: utf-8 -*-
"""
    :author: ArchCST
    :url: http://ArchCST.me
    :copyright: © 2019 ArchCST <cst@crystl.cc>
    :license: MIT, see LICENSE for more details.
"""
from flask import Blueprint

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/about')
def about():
    return 'The about page'


@blog_bp.route('/category/<int:category_id>')
def category(category_id):
    return 'The Category page'
