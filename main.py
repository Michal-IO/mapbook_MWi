# Przygotuj liste słowników które będą przechowywały informacje o użytkownikach na teamt: imie(name)
# miejscowosc(location), liczba postow(posts),

users: list = [
    {'name': 'Kasia', 'location': 'Warszawa', 'posts': 3},
    {'name': 'Asia', 'location': 'Kraków', 'posts': 5},
    {'name': 'Bsia', 'location': 'Wrocław', 'posts': 7},
]


def user_info(users_data:list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user['location']} opublikował {user["posts"]} posty')


def add_user(users_data:list) -> None:
    name: str = input('Podaj imie nowego znajomego: ')
    location: str = input('Podaj nazwe miejscowosci: ')
    posts: int = int(input('Podaj liczbe postow: '))
    users_data.append({'name': name, 'location': location, 'posts': posts})

def remove_user(users_data:list)->None:
    tmp_name:str=input('Podaj imie uzytkownika do usuniecia ze znajomych: ')
    for user in users_data:
        if user['name'] == tmp_name:
            users.remove(user)

def update_user(users_data:list)->None:
     tmp_name:str=input('Podaj imie uzytkownika do aktualizacji: ')
     for user in users_data:
         if user['name']==tmp_name:
             user['name']=input('Podaj nowe imie uzytkownika: ')
             user['location']=input('Podaj nowa nazwe miejscowosci: ')
             user['posts']=input('Podaj nowa liczbe postow: ')

while True:
    tmp_choice: int = int(input('wybierz opjce menu:'))
    if tmp_choice == 0:
        break
    if tmp_choice == 1:
        print("wybrano funkcje wyświetlania aktywności znajomych")
        user_info(users)
    if tmp_choice == 2:
        print('wybrano funkcje dodawania znajomego')
        add_user(users)
    if tmp_choice == 3:
        print('wybrano opcje usuwania znajomego')
        remove_user(users)
    if tmp_choice == 4:
        print('wybrano funkcje aktualizowania znajomego')
        update_user(users)
