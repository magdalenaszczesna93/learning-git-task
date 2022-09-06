#Ale przecież na początku powinny być pozdrowienia dla Mentora
text = "Cześć Rafał! Tym razem zadanie z Git-a"
text_2 = "Dobrego dnia Ci życzę :) i Podrawiam z Krakowa "
text_3 = "PS. Do zobaczenia na rozmowie o 17:00."
print(f"{text.upper()}")
print(f"{text_2.title()} \n")
print(f"{text_3.lower()}\n")
#To jest versja 1 pójścia do sklepu 
print("Lista zakupów")
#Zadanie 1
#najpierw tworzę sobie słownik ze skelpami i produktami
lista_dict = {"piekarnia":["chleb", "bułki", "pączek"], "warzywniak":["marchew", "seler", "rukola"]}
rzeczy = lista_dict.values()
for sklep in lista_dict:
    print(f"Idę do {sklep.capitalize()} i kupuję: {lista_dict[sklep]}")
#nie mogę sobie poradzić z tym, jak sformatować listę rzeczy
for rzeczy in lista_dict:
    number = (len(lista_dict[rzeczy]))
    print(type(number))
#nie wiem czemu liczy tylko dla jednego skelpu
    print(f"W sumie kupuję {number} produktów")
print("\n")