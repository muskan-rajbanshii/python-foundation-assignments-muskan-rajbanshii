raw_name = "  sAgar THAPA "
raw_city = "kATHMANDU "
raw_age = "27"
raw_email = " SAGAR@MAIL.COM "

name = raw_name.strip().title()
city = raw_city.strip().title()
age = int(raw_age)
email = raw_email.strip().lower()
Status = "Adult" if age > 16 else "Child"

print(f"Name: {name}")
print(f"City: {city}")
print(f"Age: {age}")
print(f"Email: {email}")
print(f"status: {Status}")
