# Pierwszy program - oprocentowanie

# Tworzymy szablon do wypisywania
szablon = "Miesiac {} Twoja pozostała kwota kredytu to {} , to o {} mniej niż w poprzednim miesiącu."
# Pobieramy i rzutujemy kwotę pożyczki
kwota = input("Podaj kwotę pożyczki: ")
kwota = float(kwota)
# Pobieramy i rzutujemy kwotę raty
rata = input("Podaj kwotę raty: ")
rata = float(rata)
# Pobieramy i rzutujemy wysokosc oprocentowania
procent = input("Podaj oprocentowanie: ")
procent = float(procent)

# Odpalamy wyliczanki
# Liczymy 1 rok
print("Rok 1")
# Styczeń 1 rok
miesiac = "Styczeń"
inflacja = 1.592824484
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
# Wyliczamy róznicę i robimy zaokrąglenia
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
# Przypisujemy nową kwotę kredytu
kwota = kredyt
# Luty 1 rok
miesiac = "Luty"
inflacja = -0.453509101
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Marzec 1 rok
miesiac = "Marzec"
inflacja = 2.324671717
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Kwiecień 1 rok
miesiac = "Kwiecień"
inflacja = 1.261254407
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Maj 1 rok
miesiac = "Maj"
inflacja = 1.782526286
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Czerwiec 1 rok
miesiac = "Czerwiec"
inflacja = 2.329384541
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Lipiec 1 rok
miesiac = "Lipiec"
inflacja = 1.502229842
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Sierpień 1 rok
miesiac = "Sierpień"
inflacja = 1.782526286
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Wrzesien 1 rok
miesiac = "Wrzesien"
inflacja = 2.328848994
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Pazdziernik 1 rok
miesiac = "Październik"
inflacja = 0.616921348
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Listopad 1 rok
miesiac = "Listopad"
inflacja = 2.352295886
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Grudzień 1 rok
miesiac = "Grudzień"
inflacja = 0.337779545
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Liczymy 2 rok
print("Rok 2")
# Styczeń 2 rok
miesiac = "Styczeń"
inflacja = 1.577035247
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Luty 2 rok
miesiac = "Luty"
inflacja = -0.292781443
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Marzec 2 rok
miesiac = "Marzec"
inflacja = 2.48619659
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Kwiecień 2 rok
miesiac = "Kwiecień"
inflacja = 0.267110318
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Maj 2 rok
miesiac = "Maj"
inflacja = 1.417952672
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Czerwiec 2 rok
miesiac = "Czerwiec"
inflacja = 1.054243267
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Lipiec 2 rok
miesiac = "Lipiec"
inflacja = 1.480520104
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Sierpień 2 rok
miesiac = "Sierpień"
inflacja = 1.577035247
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Wrzesien 2 rok
miesiac = "Wrzesien"
inflacja = -0.07742069
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Pazdziernik 2 rok
miesiac = "Październik"
inflacja = 1.165733399
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Listopad 2 rok
miesiac = "Listopad"
inflacja = -0.404186718
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
kwota = kredyt
# Grudzień 2 rok
miesiac = "Grudzień"
inflacja = 1.499708521
kredyt =(1 + (( inflacja + procent )/1200)) * kwota - rata
kredyt_round = round((kredyt),6)
roznica = round((kwota - kredyt),6)
komunikat = szablon.format(miesiac, kredyt_round, roznica)
print(komunikat)
# kończymy
