from random import randint, random

# sekcja zmiennych
stała_1 = "(sztuki)";
stała_2 = "(gram)";
grupa_1 = "niebieska";
grupa_2 = "zielona";
grupa_3 = "biała";
grupa_4 = "czarna";

# sekcja informacyjna
print(f'Dzień dobry.')
print(f'**********************************************')
print(f'Informacje na temat: zespół niebieski termitów')
print(f'Szczegółowe określenie pierwszej grupy termitów, która kieruje się do stołu aby zjeść drugie śniadanie:')
# określenie liczby wstępnej zakresu grupy, która będzie realizowała zadania związane z drugim śniadaniem
zmienna_a1 = 0
# określenie liczby końcowej zakresu grupy, która będzie realizowała zadania związane z drugim śniadaniem
zmienna_b1 = 2000000
# określenie losowe ilości pierwszej grupy termitów, która będzie realizowała zadania związane z drugim śniadaniem
value1 = randint(zmienna_a1, zmienna_b1)
print(f'Do stołu podaża: ', value1, f'termitów.', stała_1)

# określenie liczby wagi wstępnej jednego owada
prob = random()
result = prob * 1
# określenie liczby wagi jednego owada (losowe)
print(f'Średnia waga poszczególnego owada wynosi: ', result, stała_2, f', uczestnik grupy termitów: {grupa_1}.')
print(f'Średnia waga poszczególnego owada wynosi: ', result, stała_2, f', uczestnik grupy termitów: {grupa_1}.')

print(f'**********************************************')
print(f'Informacje na temat: zespół zielony termitów')
print(f'Szczegółowe określenie drugiej grupy termitów, która kieruje się do stołu aby zjeść drugie śniadanie:')
# określenie liczby wstępnej zakresu grupy, która będzie realizowała zadania związane z drugim śniadaniem
zmienna_a2 = 0
# określenie liczby końcowej zakresu grupy, która będzie realizowała zadania związane z drugim śniadaniem
zmienna_b2 = 2000000
# określenie losowe ilości drugiej grupy termitów, która będzie realizowała zadania związane z drugim śniadaniem
value2 = randint(zmienna_a2, zmienna_b2)
print(f'Do stołu podaża: ', value2, f'termitów.', stała_1)
print(f'**********************************************')
print(f'Informacje na temat: zespół biały termitów')
print(f'Szczegółowe określenie trzeciej grupy termitów, która kieruje się do stołu aby zjeść drugie śniadanie:')
# określenie liczby wstępnej zakresu grupy, która będzie realizowała zadania związane z drugim śniadaniem
zmienna_a3 = 0
# określenie liczby końcowej zakresu grupy, która będzie realizowała zadania związane z drugim śniadaniem
zmienna_b3 = 2000000
# określenie losowe ilości trzeciej grupy termitów, która będzie realizowała zadania związane z drugim śniadaniem
value3 = randint(zmienna_a3, zmienna_b3)
print(f'Do stołu podaża: ', value3, f'termitów.', stała_1)
print(f'**********************************************')
print(f'Informacje na temat: zespół czarny termitów')
print(f'Szczegółowe określenie czwartej grupy termitów, która kieruje się do stołu aby zjeść drugie śniadanie:')
# określenie liczby wstępnej zakresu grupy, która będzie realizowała zadania związane z drugim śniadaniem
zmienna_a4 = 0
# określenie liczby końcowej zakresu grupy, która będzie realizowała zadania związane z drugim śniadaniem
zmienna_b4 = 2000000
# określenie losowe ilości czwartej grupy termitów, która będzie realizowała zadania związane z drugim śniadaniem
value4 = randint(zmienna_a4, zmienna_b4)
print(f'Do stołu podaża: ', value4, f'termitów.', stała_1)
print(f'**********************************************')
print(f'Informacje na temat: ilość wszystkich termitów')
zmienna_całkowita = (value1, value2, value3, value3, value4)
liczba_całkowita = sum(zmienna_całkowita)
print(f'Informacja na temat liczby poszczególnych zespołów termitów, które podążają na drugie śniadanie', zmienna_całkowita, f'.')
suma_termitów = value1 + value2 + value3 + value4
print(f'Informacja na temat całkowitej liczby termitów, które podążają na drugie śniadanie', suma_termitów, f'.')
print(f'**********************************************')



