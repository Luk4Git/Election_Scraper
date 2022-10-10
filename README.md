# Election Scraper
Program slouží ke stažení výsledků voleb

## Instalace knihovem
Soubor requirements.txt obsahuje seznam knihovem, kroky instlace pomocí pip:
```
pip3 --version  # ověřění verze
pip3 install -r requirements.txt  # nainstalujeme knihovny
```
## Spuštění programu
Spustíme projekt_3.py dvěma argumenty:

- O5dkaz na územního celku
- Název csv souboru

## Příklad spuštění:
$ projekt_3.py "https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=4&xnumnuts=3203" "plzen.csv"

## Průběh stahování:
Stahuju data z adresy...."https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=4&xnumnuts=3203" "plzen.csv"
Ukládám data...output.csv

## Ukázka výstupu:

