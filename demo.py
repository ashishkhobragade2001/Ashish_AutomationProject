from faker import Faker


def demo_fake():
    fake = Faker()
    name = (fake.user_name())
    email = (fake.email(domain="outlook.com"))
    company_email = (fake.company_email())
    name_male = (fake.name_male())
    name_female = (fake.name_female())

