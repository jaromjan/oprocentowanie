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
