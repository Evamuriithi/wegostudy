import datetime
from faker import Faker
fake = Faker(locale='en_CA')
import random



app = 'WeGoStudy'
wegostudy_url = 'http://34.233.225.85/'
wegostudy_home_page_title = 'WeGoStudy'
wegostudy_login_page_url = 'http://34.233.225.85/partners/student_details/new'
wegostudy_student_login_page_url = 'http://34.233.225.85/partners/student_details/new'
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake. last_name()
middle_name = fake.first_name()
full_name = f'{first_name} {last_name}'
admin_email = 'chris.velasco78@gmail.com'
admin_password = '123cctb'
email = fake.email()

country_citizenship = fake.country()
phone_number = fake.pyint(11111111111, 77777777777)
address = fake.address()
country = fake.current_country()
country2 = fake.country()
city = fake.city()
province = fake.province_abbr()[0:10]
postalcode = fake.postcode()[0:10]
school = f'{province} University'
program = random.choice(['Computer', 'Physics', 'Statistic', 'Math', 'Biologist', 'Chemistry', 'Architecture'])
gpa = fake.pyint(1,100)
date_of_birth = fake.date()[0:50]
passport_number = fake.pyint(1111111, 7777777)
credentials = random.choices(['Degree', 'Certificate', 'Masters', 'Diploma', 'Doctoral'])



lst_column = ['First Name', 'Last Name', 'Passport Number', 'Phone Number', 'Mailing Address', 'Zip Code', 'Email', 'School Name', 'Program', 'GPA']

lst_id = ['user_student_detail_attributes_first_name',
          'user_student_detail_attributes_last_name',
          'user_student_detail_attributes_passport_number', 'phone_number',
          'user_student_detail_attributes_address_attributes_mailing_address',
          'user_student_detail_attributes_address_attributes_zip_code', 'user_email',
          'user_student_detail_attributes_user_educations_attributes_0_school_name',
          'user_student_detail_attributes_user_educations_attributes_0_program',
          'user_student_detail_attributes_user_educations_attributes_0_gpa']

lst_value = [first_name, last_name, passport_number, phone_number, address, postalcode, email, school, program, gpa]
