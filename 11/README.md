V textovom súbore meteo_stanice.txt sú uložené denné merania z meteorologických staníc z celého Slovenska. Informácia z každej stanice je v jednom riadku. 
Riadok obsahuje: 
- kód_stanice (3 znaky), 
- dátum v tvare rrrr.mm.dd, 
- čas v tvare hh:mm, 
- znamienko teploty, teplotu, 
- typ oblačnosti (JJ – jasno, PO – polooblačno, PJ – polojasno, OO – oblačno). 

Ukážka vstupného súboru: 
- M01 2017.05.10 06:00 +10,3 PO 
- M07 2017.05.10 06:00 +08,2 JJ 
- M04 2017.05.10 06:00 –01,5 OO 

Vytvorte program, ktorý: 
- zistí počet meraní, 
- zistí a vypíše najvyššiu nameranú teplotu, 
- zistí a vypíše priemernú teplotu všetkých staníc.