class User:
    name = ' '
    email= ' '
    password = 'abc123'
    account_number = 0

class Client(User):
    mailing_address = ''
    nl_subscriber = 'False'

class TeamMember(User):
    pay_rate = 15.00
    dept = 'General Merch."
    
