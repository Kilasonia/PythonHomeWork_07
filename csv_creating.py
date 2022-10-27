def creating():
    file = 'Phonebook.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Last name; First name; Phone number; Description\n')
