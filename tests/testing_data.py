from faker import Faker

fake = Faker()

from faker.providers import BaseProvider


class Resume_data(BaseProvider):

    def first_name_test(self):
        return "Jose"

    def last_name_test(self):
        return "Cruz"

    def address_test(self):
        return "1600 N Talman"

    def city_test(self):
        return "Chicago"

    def state_test(self):
        return "IL"

    def number_test(self):
        return "7732175069"

    def email_test(self):
        return "Jcruz6003@gmail.com"

    def objective_test(self):
        return "To be the best"

    def education_test(self):
        return "Aspira"

    def user_id_test(self):
        return 1


class Company_data(BaseProvider):

    def company_name_test(self):
        return "subway"

    def city_test(self):
        return "Chicago"

    def state_test(self):
        return "IL"

    def starting_date_test(self):
        return "07/19"

    def end_date_test(self):
        return "11/19"

    def position_test(self):
        return "manager"

    def job_description(self):
        return ["customer service", "counting money", "managing a team"]


fake.add_provider(Resume_data)
fake.add_provider(Company_data)
