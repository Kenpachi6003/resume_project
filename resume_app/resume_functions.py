from resume_app.models import db, Resume
from flask_sqlalchemy import SQLAlchemy


def resume_info(
    model,
    first_name,
    last_name,
    address,
    city,
    state,
    number,
    email,
    objective,
    education,
    user_id,
):

    resume = model(
        first_name=first_name,
        last_name=last_name,
        address=address,
        city=city,
        state=state,
        number=number,
        email=email,
        objective=objective,
        education=education,
        user_id=user_id,
    )

    db.session.add(resume)
    db.session.commit()
    return resume


def qualification_info(
    model,
    qualification1,
    qualification2,
    qualification3,
    qualification4,
    qualification5,
    resume_id,
):
    qualifications = model(
        qualification1=qualification1,
        qualification2=qualification2,
        qualification3=qualification3,
        qualification4=qualification4,
        qualification5=qualification5,
        resume_id=resume_id,
    )
    db.session.add(qualifications)
    db.session.commit()
    return qualifications


def profesional_experience_info_dict(
    company_name, city, state, starting_date, end_date, job_title, job_description
):
    # this we turn all the company info into a dictionary for easier access
    job = {
        "job": {
            "company_name": company_name,
            "city": city,
            "state": state,
            "starting_date": starting_date,
            "end_date": end_date,
            "job_title": job_title,
            "job_description": job_description,
        }
    }
    return job


def profesional_experience_info(
    model, company_name, city, state, starting_date, end_date, job_title, resume_id
):

    company_info = model(
        company_name=company_name,
        city=city,
        state=state,
        starting_date=starting_date,
        end_date=end_date,
        job_title=job_title,
        resume_id=resume_id,
    )
    db.session.add(company_info)
    db.session.commit()
    return company_info


def job_responsibility(
    model,
    responsility1,
    responsility2,
    responsility3,
    job_id,
):

    responsilities = model(
        responsility1=responsility1,
        responsility2=responsility2,
        responsility3=responsility3,
        job_id=job_id,
    )
    db.session.add(responsilities)
    db.session.commit()
    return responsilities
