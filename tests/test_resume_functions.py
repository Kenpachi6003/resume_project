import pytest
from resume_app.starting_app import app
from resume_app.models import db, Test_data
from testing_data import fake
from resume_app.create_fake_resume import main
from resume_app.resume_functions import resume_info, profesional_experience_info_dict


class Test_resume_functions:

    def test_resume_info(self):
        with app.app_context():
            resume = resume_info(
                Test_data,
                fake.first_name_test(),
                fake.last_name_test(),
                fake.address_test(),
                fake.city_test(),
                fake.state_test(),
                fake.number_test(),
                fake.email_test(),
                fake.objective_test(),
                fake.education_test(),
                fake.user_id_test(),
            )

            assert (
                resume.first_name,
                resume.last_name,
                resume.address,
                resume.city,
                resume.state,
                resume.number,
                resume.email,
                resume.objective,
                resume.education,
                resume.user_id,
            ) == (
                "Jose",
                "Cruz",
                "1600 N Talman",
                "Chicago",
                "IL",
                "7732175069",
                "Jcruz6003@gmail.com",
                "To be the best",
                "Aspira",
                1,
            )

    def test_profesional_experience_info_dict(self):
        job = profesional_experience_info_dict(
            fake.company_name_test(),
            fake.city_test(),
            fake.state_test(),
            fake.starting_date_test(),
            fake.end_date_test(),
            fake.position_test(),
            fake.job_description(),
        )
        assert (
            job["job"]["company_name"],
            job["job"]["city"],
            job["job"]["state"],
            job["job"]["starting_date"],
            job["job"]["end_date"],
            job["job"]["job_title"],
            job["job"]["job_description"],
        ) == (
            "subway",
            "Chicago",
            "IL",
            "07/19",
            "11/19",
            "manager",
            ["customer service", "counting money", "managing a team"],
        )
