from faker import Faker

fake = Faker()

print(fake.user_name())
print(fake.email(domain="outlook.com"))
print(fake.company_email())
print(fake.name_male())
print(fake.name_female())