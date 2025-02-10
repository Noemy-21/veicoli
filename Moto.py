from Concessionaria import Concessionaria

class Moto(Concessionaria):
    def __init__(self, id_veicolo, marca, modello, anno, tipo, n_marce):
        super().__init__(id_veicolo, marca, modello, anno, tipo)
        self.n_marce = n_marce
