#Przygotuj liste słowników które będą przechowywały informacje o użytkownikach na teamt: imie(name)
# miejscowosc(location), liczba postow(posts),

users:list=[
    {'name':'Kasia','location':'Warszawa','posts': 3},
    {'name':'Asia','location':'Kraków','posts': 5},
    {'name':'Bsia','location':'Wrocław','posts': 7},
]

for user in users:
    print(f'Twój znajomy {user["name"]} z miejscowości {user['location']} opublikował {user["posts"]} posty')
