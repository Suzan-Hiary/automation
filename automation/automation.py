import re


def find_numbers (numbers = []):
    pattern = re.compile(r'(\d{3}[-.\s]??\d{3}[-.\s]??\d{4}|(\d{3})\s*\d{3}[-.\s]??\d{4}|\d{3}[-.\s]??\d{4})')
    # other_formats = ['+', '(', ')', '.']
    with open('assets/potential-contacts.txt', 'r') as file:
        files = file.readlines()
        for i in files:
            if pattern.search(i):
                number = pattern.search(i).group()
                print(len(number))
                if '.' in number:
                    number = number.replace('.', '-')
                if '+' in number:
                    number = number.replace('+', '00')
                if ')' in number:
                    number = number.replace(')', '-')
                if '(' in number:
                    number = number.strip('(')
                if '-' in number and len(number)==10:
                    number = number.strip('-')
                    number = f'{number[:3]}-{number[3:6]}-{number[5:]}'
                if len(number) == 10:
                    number = f'{number[:3]}-{number[3:5]}-{number[5:]}'
                if len(number)==8:
                    number = number.strip('-')
                    number = '206'+ '-'+number
                numbers.append(number)
                numbers = sorted(numbers)
    print(f"The Count of Numbers Collected is :{len(numbers)}")
    return numbers


def find_emails (emails = []):
    pattern = re.compile(r"\w+.\w+@\w+.\w+.(com|net|org|info|biz)")
    with open('assets/potential-contacts.txt', 'r') as file:
        files = file.readlines()
        for i in files:
            if pattern.search(i):
                email = pattern.search(i).group()
                emails.append(email)
                emails = sorted(emails)
    print(len(emails))
    return emails

def files_exporting():
    with open('assets/phone_numbers.txt', 'w+') as file:
        files = file.readlines()
        for i in find_numbers():
            file.write(f'{i}\n')

    with open('assets/emails.txt', 'w+') as file:
        files = file.readlines()
        for i in find_emails():
            file.write(f'{str(i)}\n')

files_exporting()


