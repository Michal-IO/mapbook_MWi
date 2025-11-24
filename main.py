from tkinter import END, ACTIVE
from model import User
from view import View

users = []
gui = View()


def add_user():
    name = gui.entry_imie.get()
    location = gui.entry_lokalizacja.get()
    posts = gui.entry_liczba_postow.get()
    img_url = gui.entry_img_url.get()

    new_user = User(name=name, location=location, posts=posts, img_url=img_url)
    users.append(new_user)

    new_user.marker = gui.map_widget.set_marker(new_user.coords[0], new_user.coords[1], text=new_user.name)

    print(users)
    user_info()

    gui.entry_imie.delete(0, END)
    gui.entry_lokalizacja.delete(0, END)
    gui.entry_liczba_postow.delete(0, END)
    gui.entry_img_url.delete(0, END)
    gui.entry_imie.focus()


def user_info():
    gui.listbox_lista_obiektow.delete(0, END)
    for idx, user in enumerate(users):
        gui.listbox_lista_obiektow.insert(idx, f'{user.name}, {user.location}, {user.posts}, {user.img_url}')


def delete_user():
    i = gui.listbox_lista_obiektow.index(ACTIVE)
    users[i].marker.delete()
    users.pop(i)
    user_info()


def user_details():
    i = gui.listbox_lista_obiektow.index(ACTIVE)
    gui.label_imie_szczegoly_obiektu_wartosc.config(text=users[i].name)
    gui.label_lokalizacja_szczegoly_obiektu_wartosc.config(text=users[i].location)
    gui.label_posty_szczegoly_obiektu_wartosc.config(text=users[i].posts)
    gui.map_widget.set_position(users[i].coords[0], users[i].coords[1])
    gui.map_widget.set_zoom(14)


def edit_user():
    i = gui.listbox_lista_obiektow.index(ACTIVE)
    gui.entry_imie.insert(0, users[i].name)
    gui.entry_lokalizacja.insert(0, users[i].location)
    gui.entry_liczba_postow.insert(0, users[i].posts)
    gui.entry_img_url.insert(0, users[i].img_url)

    gui.button_dodaj_obiekt.config(text='Zapisz zmiany', command=lambda: update_user(i))


def update_user(i):
    users[i].name = gui.entry_imie.get()
    users[i].location = gui.entry_lokalizacja.get()
    users[i].posts = gui.entry_liczba_postow.get()
    users[i].img_url = gui.entry_img_url.get()

    users[i].coords = users[i].get_coordinates()
    users[i].marker.set_position(users[i].coords[0], users[i].coords[1])
    users[i].marker.set_text(text=users[i].name)

    user_info()

    gui.button_dodaj_obiekt.config(text='Dodaj obiekt', command=add_user)
    gui.entry_imie.delete(0, END)
    gui.entry_lokalizacja.delete(0, END)
    gui.entry_liczba_postow.delete(0, END)
    gui.entry_img_url.delete(0, END)
    gui.entry_imie.focus()


gui.button_dodaj_obiekt.config(command=add_user)
gui.button_pokaz_szczegoly.config(command=user_details)
gui.button_usun_obiekt.config(command=delete_user)
gui.button_edytuj_obiekt.config(command=edit_user)

gui.mainloop()