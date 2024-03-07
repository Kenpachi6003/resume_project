from resume_app.models import db, User
from flask_sqlalchemy import SQLAlchemy


def user_exists(username):
    users = User.query.all()

    for account in users:
        if username == account.username:
            return True
    return False


def create_user(username, first_name, last_name, email, password):

    user = User(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
    )

    db.session.add(user)
    db.session.commit()
    return user
