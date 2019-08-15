# -*- coding: utf-8 -*-
"""
    :author: ArchCST
    :url: http://ArchCST.me
    :copyright: © 2019 ArchCST <cst@crystl.cc>
    :license: MIT, see LICENSE for more details.
"""
from flask import Blueprint, render_template, flash, request, current_app
from bluelog.models import Post

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def index():
    # flash('primary style alert', 'primary')
    # flash('secondary style alert', 'secondary')
    # flash('success style alert', 'success')
    # flash('danger style alert', 'danger')
    # flash('warning style alert', 'warning')
    # flash('light style alert', 'light')
    # flash('dark style alert', 'dark')
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['BLUELOG_POST_PER_PAGE']
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=per_page)
    posts = pagination.items
    return render_template('blog/index.html', pagination=pagination, posts=posts)


@blog_bp.route('/about')
def about():
    return render_template('blog/about.html')


@blog_bp.route('/category/<int:category_id>')
def show_category(category_id):
    return render_template('blog/category.html')


@blog_bp.route('/post/<int:post_id>', methods=['GET', 'POST'])
def show_post(post_id):
    return render_template('blog/post.html')
