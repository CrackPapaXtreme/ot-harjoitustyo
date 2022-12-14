# Highscores!
Tämä sovellus pitää kirjaa 10:stä parhaasta pelaajista, jotka ovat saavuttaneet parhaan suorituksen kussakin videopelissä. Käyttäjänä voit rekisteröidä käyttäjätunnuksen ja sen jälkeen lisätä suorituksiasi. Voit myös katsella muiden suorituksia. Tämä sovellus voisi olla hyödyksi jossakin pienessä yhteisössä esimerkiksi Helsingin yliopiston oma Matrix Ry, missä pelataan mm. NES ja SNES pelejä!


## Python versio ja käyttöjärjestelmä
Käyttäkää vähintään python-versiota ```3.8``` linuxilla.


## Dokumentaatio

[Käyttöohje](https://github.com/CrackPapaXtreme/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/CrackPapaXtreme/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/CrackPapaXtreme/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/CrackPapaXtreme/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/CrackPapaXtreme/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus ja käyttöönotto

__1. Lataa__ ja __pura__ viimeisimmän releasen lähdekoodi koneellesi johonkin hakemistoon ja avaa sinne komentokehote.

__2. Asenna__ riippuvuudet komennolla:
```
poetry install
```

__3. Alusta__ sovellus, kun otat sen ekaa kertaa käyttöön komennolla:
```
poetry run invoke setup
```

__Vaihtoehtoisesti__ voit generoida esimerkkinäkymän komennolla ```poetry run invoke gen```, joka lisää 4 peliä ja 10 käyttäjää, joista kullakin on oma tulos kussakin pelissä.

__4. Käynnistä__ sovellus komennolla:
```
poetry run invoke start
```
__Lisätäkseen__ pelejä, käytä salasanaa `yay`.


## Komentorivitoiminnot

### Testaus
Ohjelman voi testata komennolla:
```
poetry run invoke test
```
### Testikattavuus
Testikattavuusraportin saa komennolla(testaa ohjelman samalla):
```
poetry run invoke coverage-report
```

### Pylint
Pylint määritelmät voit tarkistaa komennolla:
```
poetry run invoke lint
```
