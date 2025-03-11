//Sarcina 1

# b) Lucrul cu liste
lista = [10, 20, 30, 40, 50]
print("Prima valoare:", lista[0])
print("A treia valoare:", lista[2])

# Înlocuirea unei valori
lista[1] = 25
print("Lista după înlocuire:", lista)

# Extracție (tăietură)
sublista = lista[1:4]
print("Sublista extrasă:", sublista)

# Aplicarea metodei append
lista.append(60)

# Aplicarea a două funcții
print("Lungimea listei:", len(lista))
print("Valoarea maximă din listă:", max(lista))

# Aplicarea a trei operatori
print("Operator '+' pentru concatenare:", lista + [70, 80])
print("Operator '*' pentru repetare:", lista * 2)
print("Operator 'in' pentru verificare:", 30 in lista)

# c) Lucrul cu tupluri
tuplu = (5, 15, 25, 35, 45)
print("Tipul de date:", type(tuplu))
print("Prima valoare:", tuplu[0])
print("Ultima valoare:", tuplu[-1])

# Extracție de elemente
tuplu_extras = tuplu[1:4]
print("Tuplu extras:", tuplu_extras)

# Utilizarea a trei funcții
print("Lungimea tuplului:", len(tuplu))
print("Valoarea minimă:", min(tuplu))
print("Numărul de apariții ale 15:", tuplu.count(15))

# d) Lucrul cu seturi
set_exemplu = {1, 2, 2, 3, 4, 4, 5}
print("Elementele setului:", set_exemplu)  # Valorile duplicate sunt eliminate

# Aplicarea unei metode
set_exemplu.add(6)
print("Set după adăugarea lui 6:", set_exemplu)

# Aplicarea unei funcții
print("Dimensiunea setului:", len(set_exemplu))

# e) Lucrul cu dicționare
dict_text = {"nume": "Ion", "varsta": 25}
dict_numeric = {1: "Unu", 2: "Doi", 3: "Trei"}

print("Element din dict_text:", dict_text["nume"])
print("Element din dict_numeric:", dict_numeric[2])

# Aplicarea a două metode
dict_text.update({"oras": "Bucuresti"})
print("Dicționar actualizat:", dict_text)

dict_numeric.pop(3)
print("Dicționar numeric după eliminare:", dict_numeric)

# Aplicarea a două funcții
print("Cheile dicționarului text:", list(dict_text.keys()))
print("Valorile dicționarului numeric:", list(dict_numeric.values()))

# f) Conversia tipurilor de date
lista_convertita_in_set = set(lista)
print("Lista convertită în set:", lista_convertita_in_set)

tuplu_convertit_in_lista = list(tuplu)
print("Tuplu convertit în listă:", tuplu_convertit_in_lista)

# Explicație: Conversia unei liste în set elimină duplicatele. Conversia unui tuplu în listă permite modificarea elementelor, ceea ce nu este posibil într-un tuplu."}



//Sarcina 2

# a) Crearea listelor și afișarea informațiilor
preturi = [10.5, 20.75, 15.30]
produse = ["Mere", "Pere", "Banane"]

info = "Produs: {} - Pret: {:.2f} lei"
for produs, pret in zip(produse, preturi):
    print(info.format(produs, pret))

# b) Introducerea vârstei și calculul vârstei viitoare
varsta = int(input("Introduceți vârsta dvs.: "))
varsta_viitoare = varsta + 5
print("În 5 ani veți avea " + str(varsta_viitoare) + " ani.")

# c) Utilizarea operatorilor "in" și "not in"
lista_cuvinte = ["python", "java", "c++"]
print("'python' in lista_cuvinte:", "python" in lista_cuvinte)
print("'ruby' not in lista_cuvinte:", "ruby" not in lista_cuvinte)

# Explicație: Operatorul "in" verifică dacă un element este în listă, iar "not in" verifică absența unui element.