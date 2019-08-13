# -*- coding: utf-8 -*-
"""
    :author: ArchCST
    :url: http://ArchCST.me
    :copyright: © 2019 ArchCST <cst@crystl.cc>
    :license: MIT, see LICENSE for more details.
"""
from threading import Thread

from flask import url_for, current_app
from flask_mail import Message

from bluelog.extensions import mail


def _send_async_mail(app, message):
    with app.app_context():
        mail.sent(message)


def send_mail(subject, to, html):
    app = current_app._get_current_object()
    message = Message(subject, recipients=[to], html=html)
    thr = Thread(target=_send_async_mail, args=[app, message])
    thr.start()
    return thr


def send_new_comment_email(post):
    post_url = url_for('blog.show_post', post_id=post.id, _external=True) + '#comments'
    send_mail(subject='New comment', to=current_app.config['BLUELOG_ADMIN_EMAIL'],
              html='<p>New comment in post <i>{}</i>, click the link below to check: </p>'.format(post.title)
                 + '<p><a href="{}">{}</a></p> /n'.format(post_url, post)
                 + '<p><small style="color: #868e96">Do not reply this email.</small></p>')


def send_new_reply_email(comment):
    post_url = url_for('blog.show_post', post_id=comment.post_id, _external=True) + '#comments'
    send_mail(subject='New reply', to=comment.email,
              html='<p>New reply for the comment you left in post <i>{}</i>, click the link below to check: </p>'.format(comment.post.title)
                 + '<p><a href="{}">{}</a></p>'.format(post_url, post_url)
                 + '<p><small style="color: #868e96">Do not reply this email.</small></p>')
