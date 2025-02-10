from Concessionaria import Concessionaria
from Concessionaria import Furgone
from Concessionaria import Moto
from Concessionaria import Auto
from Concessionaria import Dipendenti

Dipendenti = []
Veicoli = []
Assegnazioni = []


def aggiungi_dipendente(id_dipendente, nome, cognome, reparto):
    nuovo_dipendente = {"id_dipendente": id_dipendente, "nome" : nome, "cognome" : cognome, "reparto" : reparto}
    Dipendenti.append(nuovo_dipendente)

aggiungi_dipendente(1, "Carlo", "Rossi", "vendita")
aggiungi_dipendente(2, "Franco", "menna", "Assistenza")

def aggiungi_veicolo(id_veicolo, marca, modello, tipo, anno):
    nuovo_veicolo = {"id_veicolo" : id_veicolo, "marca" : marca, "modello" : modello, "anno" : anno, "tipo" : tipo}
    Veicoli.append(nuovo_veicolo)
    print(Veicoli)

aggiungi_veicolo(Auto(1, "ford", "focus", 2024, "berliana", 4))
aggiungi_veicolo(Furgone(2, "mercedes", "boh", 2020,"cabinato", 5))
aggiungi_veicolo(Moto(3, "yamaha", "r125", 2015, "da strada", 8))



def assegna_veicolo(id_veicolo, id_dipendente, id_assegnazione):
    nuova_assegnazione = {id_veicolo, id_dipendente, id_assegnazione}
    Assegnazioni.append(nuova_assegnazione)
    print(Assegnazioni)

assegna_veicolo(1, 1, 1)

def visualizza_veicoli(Veicoli, Assegnazioni, id_veicolo):
    for veicolo in Veicoli:
        if id_veicolo in Assegnazioni:
            pass
        else:
            print("Stampa veicolo disponibile_: " + veicolo)

def visualizza_veicoli_dipendente(Assegnazione, id_dipendente):
    nominativo = {id_dipendente}
    for assegnazione in Assegnazioni:
        if id_dipendente == nominativo:
            print(Assegnazione)



