from Concessionaria import Concessionaria

class Furgone(Concessionaria):
    def __init__(self, id_veicolo, marca, modello, anno, tipo, lunghezza):
        super().__init__(id_veicolo, marca, modello, anno, tipo)
        self.lunghezza = lunghezza
