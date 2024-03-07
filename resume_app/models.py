from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
admin = Admin()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    resumes = db.relationship("Resume", backref="user")

    def __str__(self):
        return self.username


class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    objective = db.Column(db.String, nullable=False)
    qualifications = db.relationship("Qualification", backref="resume")
    job = db.relationship("Job", backref="resume")
    education = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Resumeview(ModelView):
    column_list = [
        "first_name",
        "last_name",
        "address",
        "city",
        "state",
        "number",
        "email",
        "objective",
        "qualifications",
        "job",
        "education",
        "user",
    ]


class Job(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    starting_date = db.Column(db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    job_title = db.Column(db.String, nullable=False)
    resume_id = db.Column(db.Integer, db.ForeignKey("resume.id"))
    job_description = db.relationship("Job_description", backref="job")


class Job_description(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    responsility1 = db.Column(db.String, nullable=False)
    responsility2 = db.Column(db.String, nullable=False)
    responsility3 = db.Column(db.String, nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey("job.id"))


class Qualification(db.Model):

    id = db.mapped_column(db.Integer, primary_key=True)
    qualification1 = db.Column(db.String, nullable=False)
    qualification2 = db.Column(db.String, nullable=False)
    qualification3 = db.Column(db.String, nullable=False)
    qualification4 = db.Column(db.String, nullable=False)
    qualification5 = db.Column(db.String, nullable=False)
    resume_id = db.Column(db.Integer, db.ForeignKey("resume.id"))


class Test_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    objective = db.Column(db.String, nullable=False)
    education = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer)
