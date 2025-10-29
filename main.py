# Przygotuj liste słowników które będą przechowywały informacje o użytkownikach na teamt: imie(name)
# miejscowosc(location), liczba postow(posts),

users: list = [
    {'name': 'Kasia', 'location': 'Warszawa', 'posts': 3},
    {'name': 'Asia', 'location': 'Kraków', 'posts': 5},
    {'name': 'Bsia', 'location': 'Wrocław', 'posts': 7},
]


def user_info(users_data: list) -> None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user['location']} opublikował {user["posts"]} posty')


# for user in users:
# print(f'Twój znajomy {user["name"]} z miejscowości {user['location']} opublikował {user["posts"]} posty')

while True:
    tmp_choice: int = int(input('wybierz opjce menu:'))
    if tmp_choice == 0:
        break
    if tmp_choice == 1:
        print("wybrano funkcje wyświetlania aktywności znajomych")
        user_info(users)
        # for user in users:
        # print(f'Twój znajomy {user["name"]} z miejscowości {user['location']} opublikował {user["posts"]} posty')
    if tmp_choice == 2:
        print('wybrano funkcje dodawania znajomego')
    if tmp_choice == 3:
        print('wybrano opcje usuwania znajomego')
    if tmp_choice == 4:
        print('wybrano funkcje aktualizowania znajomego')
