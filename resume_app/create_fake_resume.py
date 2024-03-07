from resume_app.models import Test_data
from resume_app.starting_app import app
from resume_app.resume_functions import resume_info
from faker import Faker

fake = Faker()
for i in range(20):

    def main():
        resume_info(
            Test_data,
            fake.first_name(),
            fake.last_name(),
            fake.address(),
            fake.city(),
            fake.state(),
            fake.phone_number(),
            fake.email(),
            fake.bs(),
            fake.catch_phrase(),
            fake.company(),
            fake.job(),
            fake.name(),
        )

    if __name__ == "__main__":
        with app.app_context():
            main()
