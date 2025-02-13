from Veicoli import concessionaria

class Furgone(concessionaria):
    def __init__(self, id_veicolo, marca, modello, anno, tipo, lunghezza):
        super().__init__(id_veicolo, marca, modello, anno, tipo)
        self.lunghezza = lunghezza
