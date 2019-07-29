# -*- coding: utf-8 -*-
"""
    :author: ArchCST
    :url: http://ArchCST.me
    :copyright: © 2019 ArchCST <cst@crystl.cc>
    :license: MIT, see LICENSE for more details.
"""
import random

from faker import Faker
from sqlalchemy.exc import IntegrityError

from bluelog.models import Admin, Category, Post, Comment
from bluelog.extensions import db

fake = Faker()


def fake_admin():
    admin = Admin(
        username = 'azureb4',
        blog_title = 'My Flask Blog',
        blog_sub_title = 'It\'s a test blog',
        name = 'Bruce Chen',
        about = 'I hate Jessica Xu :)'
    )
    db.session.add(admin)
    db.session.commit()


def fake_categories(count=10):
    category = Category(name='Default')
    db.session.add(category)

    for i in range(count):
        category = Category(name=fake.word())
        db.session.add(category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def fake_posts(count=50):
    for i in range(count):
        post = Post(
            title=fake.sentence(),
            body=fake.text(2000),
            category=Category.query.get(random.randint(1, Category.query.count())),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(post)
    db.session.commit()


def fake_comments(count=500):
    for i in range(count):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.text(random.randint(50,300)),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()

    salt = int(count * 0.1)
    for i in range(salt):
        # 未审核的评论
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.text(random.randint(50,300)),
            timestamp=fake.date_time_this_year(),
            reviewed=False,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(commet)

        # 管理员的评论
        comment = Comment(
            author='AzureB4',
            email='AzureB4@gmail.com',
            site='archcst.me',
            body=fake.text(random.randint(50,300)),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            from_admin=True,
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(commet)
    db.session.commit()
    # 回复
    for i in range(salt):
        comment = Comment(
            author=fake.name(),
            email=fake.email(),
            site=fake.url(),
            body=fake.text(random.randint(50,300)),
            timestamp=fake.date_time_this_year(),
            reviewed=True,
            # replied_id=(random.randint(1, Comment.query.count()))
            replied=Comment.query.get(random.randint(1, Comment.query.count())),
            post=Post.query.get(random.randint(1, Post.query.count()))
        )
        db.session.add(comment)
    db.session.commit()
