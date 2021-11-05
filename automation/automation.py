import re

phone_num_regex = r"[\+\d]?(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"


with open("potential-contacts.txt" ,"r") as f:
    file_content = f.read()

phone_num_type = re.findall(phone_num_regex,file_content)
print(len(phone_num_type))
phone_num_type.sort()
all_phone_num = []
for phone_num in phone_num_type:
    if phone_num not in all_phone_num:
        all_phone_num.append(phone_num.replace("(","").replace(")","-").replace(".","-"))

with open("phone_numbers.txt","w") as file:
    for email in all_phone_num:
        file.writelines(f"{email}\n")
    print("done")
# print(all_phone_num)
print(len(all_phone_num))
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
all_emails = re.findall(email_regex , file_content)

all_emails.sort()
emails = []
for email in all_emails:
    if email not in emails:
        emails.append(email)

with open("emails.txt","w") as file:
    for email in emails:
        file.writelines(f"{email}\n")
    print("done")