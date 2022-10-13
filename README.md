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

- Odkaz na územního celku
- Název csv souboru

## Příklad spuštění:
```
projekt_3.py "projekt_3.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302" "output.csv"
```
## Průběh stahování:
```
Stahuju data z adresy...."https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302"
Ukládám data...output.csv
```
## Ukázka výstupu:
číslo,obec,voliči v seznamu,vydané obálky,platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,...
571181,Běstvina,440,247,246,28,0,0,10,0,6,17,3,2,0,0,0,24,0,3,110,0,2,17,4,0,0,20,0
573949,Biskupice,52,34,34,2,0,0,5,0,0,2,0,0,0,0,0,2,0,0,17,0,0,3,0,0,0,3,0
505005,Bítovany,330,215,214,26,0,0,16,0,10,26,0,2,6,0,0,25,0,6,74,0,0,4,2,0,3,14,0
571202,Bojanov,537,357,356,31,1,1,34,0,20,27,0,5,7,0,1,31,0,12,87,0,1,35,0,2,1,58,2...
