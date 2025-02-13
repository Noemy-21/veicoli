
from Moto import Moto
from Furgone import Furgone
from Dipendenti import dipendenti
from Auto import Auto
from Veicoli import concessionaria

lista_dipendenti = []
lista_auto = []
lista_moto = []
lista_furgoni = []
lista_assegnazioni = []
lista_completa = []




def aggiungi_dipendente(id_dipendente, nome, cognome, reparto):
    nuovo_dipendente = {"id_dipendente": int(id_dipendente), "nome" : nome, "cognome" : cognome, "reparto" : reparto}
    lista_dipendenti.append(nuovo_dipendente)

aggiungi_dipendente(109, "Carlo", "Rossi", "vendita")
aggiungi_dipendente(267, "Franco", "menna", "Assistenza")
aggiungi_dipendente(473, "francesca", "penna", "officina")
aggiungi_dipendente(289, "Paola", "Di Carlo", "showroom")
print("Lista dipendenti:")
for dipendente in lista_dipendenti:
    print(dipendente)




print("_______________")





def aggiungi_Auto(id_veicolo, marca, modello, anno, tipo, n_portiere):
    nuova_auto = {"id_veicolo": int(id_veicolo), "marca" : marca, "modello" : modello, "anno" : anno, "tipo" : tipo, "n_portiere" : n_portiere}
    lista_auto.append(nuova_auto)

def aggiungi_Moto(id_veicolo, marca, modello, anno, tipo, n_marce):
    nuova_moto = {"id_veicolo" : int(id_veicolo), "marca" : marca, "modello" : modello, "anno" : anno, "tipo" : tipo, "n_marce" : n_marce}
    lista_moto.append(nuova_moto)

def aggiungi_Furgone(id_veicolo, marca, modello, anno, tipo, lunghezza):
    nuovo_furgone = {"id_veicolo" : int(id_veicolo), "marca" : marca, "modello" : modello, "anno" : anno, "tipo" : tipo, "lunghezza" : lunghezza}
    lista_furgoni.append(nuovo_furgone)
   

aggiungi_Auto(177, "ford", "focus", 2024, "berliana", 4)
aggiungi_Moto(243, "mercedes", "boh", 2020,"cabinato", 3)
aggiungi_Furgone(398, "yamaha", "r125", 2015, "da strada", 8)
print("Lista veicoli:")
print(lista_auto)
print(lista_moto)
print(lista_furgoni)





print("_______________")






for auto in lista_auto:
    lista_completa.append(auto)

for moto in lista_moto:
    lista_completa.append(moto)
   
for furgone in lista_furgoni:
    lista_completa.append(furgone)



def assegna_veicolo(id_veicolo_assegnato, id_dipendente, id_assegnazione):
    nuova_assegnazione = {"id_veicolo_assegnato:" : int(id_veicolo_assegnato), "id_dipendente_assegnato:" :id_dipendente, "id_assegnazione:" : id_assegnazione}
    if any(h["id_veicolo_assegnato:"] == id_veicolo_assegnato for h in lista_assegnazioni):
        print(f"Il veicolo con ID {id_veicolo_assegnato} è già assegnato")
    else:   
        lista_assegnazioni.append(nuova_assegnazione)
        for i in lista_auto:
            if i["id_veicolo"] == id_veicolo_assegnato:
                lista_auto.remove(i)
            else:
                pass
        for f in lista_moto:
            if f["id_veicolo"] == id_veicolo_assegnato:
                lista_moto.remove(f)
            else:
                pass
        for g in lista_furgoni:
            if g["id_veicolo"] == id_veicolo_assegnato:
                lista_furgoni.remove(g)
            else:
                pass

        
assegna_veicolo(243, 109, 1)
assegna_veicolo(177, 267, 2)
assegna_veicolo(243, 473, 3)
print("Lista assegnazioni:")
print(lista_assegnazioni)





print("_______________")






def veicoli_disponibili(): 
    print("Lista veicoli disponibili")
    for veicolodisponibile in lista_completa:
        print(veicolodisponibile)


veicoli_disponibili()





print("_______________")






def assegnazione_specifico(id_dipendente):
    if any(assegnazione["id_dipendente_assegnato:"] == id_dipendente for assegnazione in lista_assegnazioni):
        print(f"Lista assegnazioni del dipendente con ID: {id_dipendente}:")
        for assegnazione in lista_assegnazioni:
            if assegnazione["id_dipendente_assegnato:"] == id_dipendente:
                print(assegnazione)
    else: 
        print(f"Il dipendente con ID {id_dipendente:} non ha assegnazioni")
  
        
        
assegnazione_specifico(289)
assegnazione_specifico(109)
