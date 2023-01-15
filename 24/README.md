V textovom súbore hlasovanie_1.txt (k dispozícii je aj súbor hlasovanie_2.txt) je uložený priebeh SMS hlasovania divákov v reality show. V každom riadku je uložené práve jedno telefónne číslo, na ktoré prišla SMS-ka. Diváci mohli hlasovať na čísla 5220 až 5229. V textovom súbore hlasovanie_vypadnuti.txt je zoznam už vypadnutých hráčov (ich hlasovacie čísla, každé je na samostatnom riadku). 

Ukážka časti vstupného textového súboru hlasovanie_1.txt: 
* 5225 
* 5227 
* 5225 
* 5224 
* 5225 
* 5227 

Ukážka textového súboru hlasovanie_vypadnuti.txt: 
* 5227
* 5224 

Vytvorte program, ktorý zistí a vypíše: 
* celkový počet zaslaných SMS, 
* koľko hlasov dostal každý zo súťažiacich, 
* ktorý súťažiaci dostal najmenej hlasov, a teda nepostupuje do ďalšieho kola, 
* ktorý súťažiaci dostal najmenej hlasov, a teda nepostupuje do ďalšieho kola, pričom neberie do úvahy hlasy zaslané vypadnutým súťažiacim.