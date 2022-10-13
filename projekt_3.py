"""
projekt_3.py: první projekt do Engeto Online Python Akademie
author: Lukáš Matela
email: lukas.matela@innogy.cz, Lukas.Matela@gmail.com
discord: Lukáš M., #8515
"""

import requests
from bs4 import BeautifulSoup as bs
import csv
import sys


def main():
    odkaz_region = sys.argv[1]
    filename = sys.argv[2]
    global response
    response = requests.get(odkaz_region)

    if not kontrola():
        return
    print(f"Stahuju data z adresy....{odkaz_region}" )
    hlavicka=hlavicka_tabulky(odkaz_region)
    obsah=vyplnovac_radku(odkaz_region)
    print(f"Ukládám data...{filename}")
    vytvarec_csv(hlavicka, obsah, filename)


class mesto:
    _link=''
    _response = ''
    _link_used = 0

    def __init__(self, link):
        self._link=link

    @property
    def link(self):
        return self._link

    @property
    def link_used(self):
        return self._link_used

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._link_used = 1
        self._response=value



def kontrola():
    if len(sys.argv) != 3:
        print("Zadej přesně dva arguemnty: odkaz a název souboru")
        return False
    elif "volby.cz/pls/ps2017nss/" not in sys.argv[1]:
        print("Špatná adresa")
        return False
    else:
        print("zadaná správna adresa")
        return True

def parsovani_odkazu(url):
    response = requests.get(url)
    return bs(response.text, "html.parser")

def vytvarec_odkazu(odkaz_region):
    soup_mesta = parsovani_odkazu(odkaz_region)
    mesta = soup_mesta.find_all("tr")
    zacatek = "https://volby.cz/pls/ps2017nss/"
    odkazy_mest = []

    for udaj in mesta:
        konec = udaj.find("a", href=True)
        if konec is not None:
            odkazy_mest.append(zacatek + konec["href"])
    return odkazy_mest

def list_id_mest(odkaz_region):
    id_mest = []
    soup_mesta = parsovani_odkazu(odkaz_region)
    mesta = soup_mesta.find_all("tr")

    for udaj in mesta:
        cislo_m = udaj.find("td", {"class": "cislo"})
        if cislo_m is not None:
            id_mest.append([cislo_m.text])
    return id_mest

def list_jmen_mest(odkaz_region):
    jmena_mest = []
    soup_mesta = parsovani_odkazu(odkaz_region)
    mesta = soup_mesta.find_all("tr")

    for udaj in mesta:
        nazev_m = udaj.find("td", {"class": "overflow_name"})
        if nazev_m is not None:
            jmena_mest.append([nazev_m.text])
    return jmena_mest


def list_odkaz_mesto(city, header):
    """
    :param odkaz_mesto:
    :param header: sa2 = list_volici, sa3=obalky, sa6 = hlasy
    :return:
    """
    if not city.link_used:
        city.response = parsovani_odkazu(city.link)
    soup_udaje = city.response
    data = soup_udaje.find(class_="cislo", headers=header).getText()
    return data


def list_nazvy_stran(odkaz_region):
    nazvy_stran = []
    odkaz_mesto=vytvarec_odkazu(odkaz_region)[0]
    soup_udaje = parsovani_odkazu(odkaz_mesto)
    for udaj in soup_udaje.find_all("td", {"class": "overflow_name"}):
        nazvy_stran.append(udaj.get_text(""))
    return nazvy_stran


def list_strany_hlasy(city):
    strany_hlasy = []
    if city.link_used:
        soup_udaje=city.response
    else:
        soup_udaje = parsovani_odkazu(city.link_used)
    for cislo in soup_udaje.find_all(class_="cislo", headers="t1sa2 t1sb3"):
        strany_hlasy.append(cislo.get_text(""))
    for cislo in soup_udaje.find_all(class_="cislo", headers="t2sa2 t2sb3"):
        strany_hlasy.append(cislo.get_text(""))
    return strany_hlasy


def hlavicka_tabulky(odkaz_mesto):
    hlavicka_tab = ["číslo", "obec", "voliči v seznamu", "vydané obálky", "platné hlasy"]
    nazvy_stran = list_nazvy_stran(odkaz_mesto)
    hlavicka_tab.extend(nazvy_stran)
    return hlavicka_tab


def vyplnovac_radku(odkaz_region):
    obsah = []

    id_mest = list_id_mest(odkaz_region)
    jmena_mest = list_jmen_mest(odkaz_region)
    odkazy_mest=vytvarec_odkazu(odkaz_region)

    for i in range(len(id_mest)):
        city=mesto(odkazy_mest[i])
        volici_vs = list_odkaz_mesto(city, 'sa2')
        obalky = list_odkaz_mesto(city, 'sa3')
        hlasy_pl = list_odkaz_mesto(city, 'sa6')
        strany_hlasy = list_strany_hlasy(city)
        list_in = []
        list_in.append(*id_mest[i])
        list_in.append(*jmena_mest[i])
        list_in.append(volici_vs)
        list_in.append(obalky)
        list_in.append(hlasy_pl)
        list_in.extend(strany_hlasy)
        obsah.append(list_in)
    return obsah


def vytvarec_csv(hlavicka_tab, obsah, filename):
    with open(f"{filename}.csv", "w", encoding='UTF8', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(hlavicka_tab)
        for row in obsah:
            writer.writerow(row)


if __name__=="__main__":
    main()

