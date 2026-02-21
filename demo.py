from faker import Faker

fake = Faker()
print(fake.user_name())
print(fake.email(domain="outlook"))