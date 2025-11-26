

titolo_libro = "La Città Invisibile"
scrittore = "Italo Calvino"
copie_totali = 4
costo = 14.50
in_catalogo = True

print("Titolo:", titolo_libro)
print("Autore:", scrittore)
print("Copie:", copie_totali)
print("Prezzo:", costo, "€")
print("Disponibilità:", in_catalogo)
print("-" * 40)





elenco_libri = [
    "Dune",
    "La storia infinita",
    "La Città Invisibile",
    "Il Mago di Earthsea",
    "Le Cronache di Narnia"
]


scaffale = {
    "Dune": 2,
    "La storia infinita": 1,
    "La Città Invisibile": 4,
    "Il Mago di Earthsea": 3,
    "Le Cronache di Narnia": 0
}


titoli_registrati = set(scaffale)

print("Libri presenti:", elenco_libri)
print("Scaffale:", scaffale)
print("Registrati:", titoli_registrati)
print("-" * 40)




class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione, copie):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione
        self.copie = copie

    def descrizione(self):
        return f"{self.titolo} - {self.autore} ({self.anno_pubblicazione}) | Copie: {self.copie}"


class Utente:
    def __init__(self, nome, eta, codice):
        self.nome = nome
        self.eta = eta
        self.codice = codice

    def info(self):
        return f"{self.nome}, {self.eta} anni – ID: {self.codice}"


class Prestito:
    def __init__(self, utente, libro, durata):
        self.utente = utente
        self.libro = libro
        self.durata = durata

    def riepilogo(self):
        return f"{self.utente.nome} ha preso in prestito '{self.libro.titolo}' per {self.durata} giorni."




def effettua_prestito(utente, libro, durata):
    if libro.copie > 0:
        libro.copie -= 1
        nuovo_prestito = Prestito(utente, libro, durata)
        print(nuovo_prestito.riepilogo())
        return nuovo_prestito
    else:
        print(f"⚠️  Nessuna copia disponibile per '{libro.titolo}'!")
        return None



l1 = Libro("Dune", "Frank Herbert", 1965, 2)
l2 = Libro("Il Mago di Earthsea", "Ursula K. Le Guin", 1968, 3)
l3 = Libro("La storia infinita", "Michael Ende", 1979, 1)


u1 = Utente("Giulia Verdi", 22, "U101")
u2 = Utente("Stefano Conti", 28, "U102")


lista_prestiti = [
    effettua_prestito(u1, l1, 6),
    effettua_prestito(u2, l2, 9),
    effettua_prestito(u1, l3, 4)
]

print("-" * 40)


print("Situazione copie dopo i prestiti:")
for libro in (l1, l2, l3):
    print(libro.descrizione())

print("-" * 40)


print("Prestiti registrati:")
for p in lista_prestiti:
    if p:
        print(p.riepilogo())