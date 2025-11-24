from tkinter import *
import tkintermapview

class View(Tk):
    def __init__(self):
        super().__init__()
        self.title('Mapbook')
        self.geometry('1025x760')

        self.ramka_lista_obiekow = Frame(self)
        self.ramka_formularz = Frame(self)
        self.ramka_szczegoly_obiektu = Frame(self)
        self.ramka_mapa = Frame(self)

        self.ramka_lista_obiekow.grid(row=0, column=0)
        self.ramka_formularz.grid(row=0, column=1)
        self.ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)
        self.ramka_mapa.grid(row=2, column=0, columnspan=2)

        self.label_lista_obiektow = Label(self.ramka_lista_obiekow, text='Lista obiektów')
        self.label_lista_obiektow.grid(row=0, column=0, columnspan=3)

        self.listbox_lista_obiektow = Listbox(self.ramka_lista_obiekow)
        self.listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)

        self.button_pokaz_szczegoly = Button(self.ramka_lista_obiekow, text='Pokaż szczegóły')
        self.button_pokaz_szczegoly.grid(row=2, column=0)

        self.button_usun_obiekt = Button(self.ramka_lista_obiekow, text='Usuń obiekt')
        self.button_usun_obiekt.grid(row=2, column=1)

        self.button_edytuj_obiekt = Button(self.ramka_lista_obiekow, text='Edytuj obiekt')
        self.button_edytuj_obiekt.grid(row=2, column=2)

        self.label_formularz = Label(self.ramka_formularz, text='Formularz: ')
        self.label_formularz.grid(row=0, column=0, columnspan=2)

        self.label_imie = Label(self.ramka_formularz, text='Imie: ')
        self.label_imie.grid(row=1, column=0, sticky=W)
        self.label_lokalizacja = Label(self.ramka_formularz, text='Lokalizacja: ')
        self.label_lokalizacja.grid(row=2, column=0, sticky=W)
        self.label_liczba_postow = Label(self.ramka_formularz, text='Liczba postow: ')
        self.label_liczba_postow.grid(row=3, column=0, sticky=W)
        self.label_img_url = Label(self.ramka_formularz, text='Obrazek: ')
        self.label_img_url.grid(row=4, column=0, sticky=W)

        self.entry_imie = Entry(self.ramka_formularz)
        self.entry_imie.grid(row=1, column=1)
        self.entry_lokalizacja = Entry(self.ramka_formularz)
        self.entry_lokalizacja.grid(row=2, column=1)
        self.entry_liczba_postow = Entry(self.ramka_formularz)
        self.entry_liczba_postow.grid(row=3, column=1)
        self.entry_img_url = Entry(self.ramka_formularz)
        self.entry_img_url.grid(row=4, column=1)

        self.button_dodaj_obiekt = Button(self.ramka_formularz, text='Dodaj obiekt')
        self.button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

        self.label_szczegoly_obiektu = Label(self.ramka_szczegoly_obiektu, text='Szczegoly obiektu')
        self.label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)

        self.label_imie_szczegoly_obiektu = Label(self.ramka_szczegoly_obiektu, text='Imie: ')
        self.label_imie_szczegoly_obiektu.grid(row=1, column=0)
        self.label_imie_szczegoly_obiektu_wartosc = Label(self.ramka_szczegoly_obiektu, text='....')
        self.label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)

        self.label_lokalizacja_szczegoly_obiektu = Label(self.ramka_szczegoly_obiektu, text='Lokalizacja: ')
        self.label_lokalizacja_szczegoly_obiektu.grid(row=1, column=2)
        self.label_lokalizacja_szczegoly_obiektu_wartosc = Label(self.ramka_szczegoly_obiektu, text='....')
        self.label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=3)

        self.label_posty_szczegoly_obiektu = Label(self.ramka_szczegoly_obiektu, text='Posty: ')
        self.label_posty_szczegoly_obiektu.grid(row=1, column=4)
        self.label_posty_szczegoly_obiektu_wartosc = Label(self.ramka_szczegoly_obiektu, text='....')
        self.label_posty_szczegoly_obiektu_wartosc.grid(row=1, column=5)

        self.map_widget = tkintermapview.TkinterMapView(self.ramka_mapa, width=1025, height=600, corner_radius=0)
        self.map_widget.set_position(52.2, 21.3)
        self.map_widget.set_zoom(6)
        self.map_widget.grid(row=0, column=0)