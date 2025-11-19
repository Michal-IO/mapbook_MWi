from tkinter import *
import tkintermapview

users:list = []

import requests
from bs4 import BeautifulSoup

class User:
    def __init__(self,name:str,location:str,posts:int,img_url:str):
        self.name = name
        self.location = location
        self.posts = posts
        self.img_url = img_url
        self.coords = self.get_coordinates()

    def get_coordinates(self):
        import requests
        from bs4 import BeautifulSoup
        url: str = f'https://pl.wikipedia.org/wiki/{self.location}'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/123.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        # print(response.text)
        response_html = BeautifulSoup(response.text, "html.parser")
        # print(response_html.prettify())
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        # print(latitude)
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        # print(longitude)
        return [latitude, longitude]

def add_user(users_data: list) -> None:
    name: str = entry_imie.get()
    location: str = entry_lokalizacja.get()
    posts: int = int(entry_liczba_postow.get())
    img_url = entry_img_url.get()
    users_data.append(User(name=name,location=location,posts=posts,img_url=img_url))
    print(users_data)
    user_info(users_data)
    entry_imie.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_img_url.delete(0, END)
    entry_imie.focus()

def user_info(users_data: list):
    listbox_lista_obiektow.delete(0, END)
    for idx,user in enumerate(users_data):
        listbox_lista_obiektow.insert(idx,f'{user.name}, {user.location}, {user.posts}, {user.img_url}')

def delete_user(users_data: list):
    i = listbox_lista_obiektow.index(ACTIVE)
    users_data.pop(i)
    user_info(users_data)

def user_details(users_data: list):
    i = listbox_lista_obiektow.index(ACTIVE)
    label_imie_szczegoly_obiektu_wartosc.config(text=users_data[i].name)
    label_lokalizacja_szczegoly_obiektu_wartosc.config(text=users_data[i].location)
    label_posty_szczegoly_obiektu_wartosc.config(text=users_data[i].posts)
    user_details(users_data)

def edit_user(users_data: list):
    i = listbox_lista_obiektow.index(ACTIVE)
    entry_imie.insert(0, users_data[i].name)
    entry_lokalizacja.insert(0, users_data[i].location)
    entry_liczba_postow.insert(0, users_data[i].posts)
    entry_img_url.insert(0, users_data[i].img_url)

    button_dodaj_obiekt.config(text='Zapisz zmiany', command=lambda: update_user(users_data, i))

def update_user(users_data: list, i):
    users_data[i].name = entry_imie.get()
    users_data[i].location = entry_lokalizacja.get()
    users_data[i].posts = entry_liczba_postow.get()
    users_data[i].img_url = entry_img_url.get()
    user_info(users_data)

    button_dodaj_obiekt.config(text='Dodaj obiekt', command=lambda: add_user(users))
    entry_imie.delete(0, END)
    entry_lokalizacja.delete(0, END)
    entry_liczba_postow.delete(0, END)
    entry_img_url.delete(0, END)
    entry_imie.focus()


root = Tk()
root.title('Mapbook')
root.geometry('1025x760')


ramka_lista_obiekow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektu = Frame(root)
ramka_mapa = Frame(root)


ramka_lista_obiekow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)

# RAMKA LISTA OBIEKTOW

label_lista_obiektow = Label(ramka_lista_obiekow, text='Lista obiektów')
label_lista_obiektow.grid(row=0, column=0, columnspan=3)

listbox_lista_obiektow = Listbox(ramka_lista_obiekow)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)

button_pokaz_szczegoly = Button(ramka_lista_obiekow, text='Pokaż szczegóły', command=lambda: user_details(users))
button_pokaz_szczegoly.grid(row=2, column=0)

button_usun_obiekt = Button(ramka_lista_obiekow, text='Usuń obiekt', command=lambda: delete_user(users))
button_usun_obiekt.grid(row=2, column=1)

button_edytuj_obiekt = Button(ramka_lista_obiekow, text='Edytuj obiekt', command=lambda: edit_user(users))
button_edytuj_obiekt.grid(row=2, column=2)

# RAMKA FORMULARZ

label_formularz = Label(ramka_formularz, text='Formularz: ')
label_formularz.grid(row=0, column=0,columnspan=2)

label_imie = Label(ramka_formularz, text='Imie: ')
label_imie.grid(row=1, column=0, sticky=W)

label_lokalizacja = Label(ramka_formularz, text='Lokalizacja: ')
label_lokalizacja.grid(row=2, column=0, sticky=W)

label_liczba_postow = Label(ramka_formularz, text='Liczba postow: ')
label_liczba_postow.grid(row=3, column=0, sticky=W)

label_img_url = Label(ramka_formularz, text='Obrazek: ')
label_img_url.grid(row=4, column=0, sticky=W)

entry_imie = Entry(ramka_formularz)
entry_imie.grid(row=1, column=1)

entry_lokalizacja = Entry(ramka_formularz)
entry_lokalizacja.grid(row=2, column=1)

entry_liczba_postow = Entry(ramka_formularz)
entry_liczba_postow.grid(row=3, column=1)

entry_img_url = Entry(ramka_formularz)
entry_img_url.grid(row=4, column=1)

button_dodaj_obiekt = Button(ramka_formularz, text='Dodaj obiekt', command=lambda: add_user(users))
button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)


# RAMKA SZCZEGOLY OBIEKTU

label_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Szczegoly obiektu')
label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)

label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Imie: ')
label_imie_szczegoly_obiektu.grid(row=1, column=0)

label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='....')
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)

label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Lokalizacja: ')
label_lokalizacja_szczegoly_obiektu.grid(row=1, column=2)

label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='....')
label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=3)

label_posty_szczegoly_obiektu = Label(ramka_szczegoly_obiektu, text='Posty: ')
label_posty_szczegoly_obiektu.grid(row=1, column=4)

label_posty_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektu, text='....')
label_posty_szczegoly_obiektu_wartosc.grid(row=1, column=5)

# RAMKA MAPY
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1025, height=600, corner_radius=0)
map_widget.set_position(52.2,21.3)
map_widget.set_zoom(6)
map_widget.grid(row=0, column=0)

root.mainloop()