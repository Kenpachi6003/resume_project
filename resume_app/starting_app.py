from flask import Flask, flash, render_template, redirect, url_for, session, request
from flask_admin.contrib.sqla import ModelView
from docx import Document
from resume_app.models import (
    db,
    admin,
    Resume,
    Resumeview,
    User,
    Test_data,
    Job,
    Job_description,
    Qualification,
)
from resume_app.resume_functions import (
    resume_info,
    qualification_info,
    profesional_experience_info_dict,
    profesional_experience_info,
    job_responsibility,
)
from resume_app.user_functions import user_exists, create_user
from resume_app.save_resume import Resume_template

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///resumes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "lLIeYDuz9k4Ki4OIme-ff09SczH_Gtteol-n-BnwMIw"

db.init_app(app)
admin.init_app(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(Resumeview(Resume, db.session))
admin.add_view(ModelView(Job, db.session))
admin.add_view(ModelView(Job_description, db.session))
admin.add_view(ModelView(Qualification, db.session))


@app.route("/home")
def home():
    if "user_id" in session:

        return render_template(
            "home.html",
            users=User.query.all(),
            resumes=Resume.query.all(),
            qualifications=Qualification.query.all(),
            jobs=Job.query.all(),
        )
    else:
        return redirect(url_for("login"))


@app.route("/", methods=["POST", "GET"])
def login():
    if "user_id" in session:
        return redirect(url_for("home"))
    if request.method == "POST":
        session.permanent = True
        username = request.form["username"]

        user = User.query.filter_by(username=username).first()

        if user is None:
            return redirect(url_for("create_account"))

        session["user_id"] = user.id
        return redirect(url_for("home"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    if "user_id" in session:
        flash(f"You have been logged out!", "info")
    session.pop("user_id", None)
    session.pop("username", None)
    session.pop("email", None)
    return redirect(url_for("login"))


@app.route("/create_account", methods=["POST", "GET"])
def create_account():
    if "user_id" in session:
        return redirect(url_for("home"))
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        password = request.form["password"]
        if user_exists(username):
            flash("You already have an account.")
            return redirect(url_for("login"))
        else:
            create_user(username, first_name, last_name, email, password)
            flash("Account was created")
            return redirect(url_for("login"))
    return render_template("create_account.html")


@app.route("/resume_creator", methods=["POST", "GET"])
def resume_creator():
    if "user_id" in session:

        if request.method == "POST":
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            address = request.form["street_name"]
            city = request.form["city"]
            state = request.form["state"]
            number = request.form["number"]
            email = request.form["email"]
            objective = request.form["objective"]
            qualification1 = request.form["qualification1"]
            qualification2 = request.form["qualification2"]
            qualification3 = request.form["qualification3"]
            qualification4 = request.form["qualification4"]
            qualification5 = request.form["qualification5"]
            education = request.form["school_name"]

            job1 = profesional_experience_info_dict(
                request.form["company_name1"],
                request.form["city1"],
                request.form["state1"],
                request.form["starting_date1"],
                request.form["end_date1"],
                request.form["job_title1"],
                [
                    request.form["job_description1-1"],
                    request.form["job_description1-2"],
                    request.form["job_description1-3"],
                ],
            )
            job2 = profesional_experience_info_dict(
                request.form["company_name2"],
                request.form["city2"],
                request.form["state2"],
                request.form["starting_date2"],
                request.form["end_date2"],
                request.form["job_title2"],
                [
                    request.form["job_description2-1"],
                    request.form["job_description2-2"],
                    request.form["job_description2-3"],
                ],
            )
            job3 = profesional_experience_info_dict(
                request.form["company_name3"],
                request.form["city3"],
                request.form["state3"],
                request.form["starting_date3"],
                request.form["end_date3"],
                request.form["job_title3"],
                [
                    request.form["job_description3-1"],
                    request.form["job_description3-2"],
                    request.form["job_description3-3"],
                ],
            )

            jobs = [job1, job2, job3]

            resume_info(
                model=Resume,
                first_name=first_name,
                last_name=last_name,
                address=address,
                city=city,
                state=state,
                number=number,
                email=email,
                objective=objective,
                education=education,
                user_id=session["user_id"],
            )
            latest_resume_added = Resume.query.order_by(Resume.id.desc()).first()

            qualification_info(
                model=Qualification,
                qualification1=qualification1,
                qualification2=qualification2,
                qualification3=qualification3,
                qualification4=qualification4,
                qualification5=qualification5,
                resume_id=latest_resume_added.id,
            )
            for job in jobs:

                if job["job"]["company_name"] == "":
                    break
                else:
                    profesional_experience_info(
                        model=Job,
                        company_name=job["job"]["company_name"],
                        city=job["job"]["city"],
                        state=job["job"]["state"],
                        starting_date=job["job"]["starting_date"],
                        end_date=job["job"]["end_date"],
                        job_title=job["job"]["job_title"],
                        resume_id=latest_resume_added.id,
                    )

                    latest_job_added = Job.query.order_by(Job.id.desc()).first()
                    job_responsibility(
                        model=Job_description,
                        responsility1=job["job"]["job_description"][0],
                        responsility2=job["job"]["job_description"][1],
                        responsility3=job["job"]["job_description"][2],
                        job_id=latest_job_added.id,
                    )
 
            user1 = Resume_template(first_name + " " +last_name, address, city, state,
            number, email, objective, [qualification1, qualification2, qualification3, qualification4,qualification5],
            jobs, education, first_name + last_name + str(latest_resume_added.id) + ".docx", Document())
            
            user1.add_info()
            return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))
    return render_template("resume_creator.html")


if __name__ == "__main__":
    with app.app_context():
        print("Creating database ", db)
        db.create_all()

        app.run(debug=True)
