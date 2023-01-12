ids = {

    't-shirt': '10',

    'sneakers': '20',

    'trousers': '30',

    'cap': '40',

    'jacket': '50'

}

store = {

    '10': [

        {'quantity': 50, 'price': 800},

        {'quantity': 70, 'price': 950},

    ],

    '20': [

        {'quantity': 6, 'price': 5000},

        {'quantity': 12, 'price': 6000},

        {'quantity': 18, 'price': 4500},

    ],

    '30': [

        {'quantity': 22, 'price': 1200},

        {'quantity': 50, 'price': 1150},

    ],

    '40': [

        {'quantity': 5, 'price': 600},

    ],

    '50': [

        {'quantity': 11, 'price': 15000},

    ]

}


for i in ids:
    sum = 0
    pieces = 0
    for j in store[ids[i]]:
        pieces += j['quantity']
        sum += j['quantity']* j['price']
    print(f'{i} - {pieces} pieces, worth {sum} rub')
sorted()