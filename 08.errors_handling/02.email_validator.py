from exceptions import NameTooShort, MustContainAtSymbolError, InvalidDomainError

email = input()
while email != 'End':
    name = email.split('@')[0]
    domain = email.split('.')[1]
    valid_domains = ['com', 'bg', 'org', 'net']
    if len(name) < 5:
        raise NameTooShort('Name must be more than 4 characters')
    elif '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')
    elif domain not in valid_domains:
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')
    else:
        print('Email is valid')

    email = input()