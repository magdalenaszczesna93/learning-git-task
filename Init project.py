print("Lista zakupów")
#Zadanie 1
lista_dict = {"piekarnia":["chleb", "bułki", "pączek"], "warzywniak":["marchew", "seler", "rukola"]}
rzeczy = lista_dict.values()
for sklep in lista_dict:
    print(f"Idę do {sklep} i kupuję: {lista_dict[sklep]}")
#nie mogę sobie poradzić z tym, jak sformatować listę rzeczy