my_family = {
    'sister': {
        'name': 'Kristie',
        'age': 45
    },
    'mother': {
        'name': 'Cindy',
        'age': 60
    },
    'Father': {
        'name': 'Ottis',
        'age': 66
    },
    'brother': {
        'name': 'Parker',
        'age': 35
    }
}


def introduce(relative):
    name = my_family[relative]['name']
    age = my_family[relative]['age']
    print('{0} is my {1} and is {2} years old'.format(name, relative, age))


introduce('mother')
