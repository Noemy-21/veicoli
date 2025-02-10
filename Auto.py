from Concessionaria import Concessionaria


class Auto(Concessionaria):
    def __init__(self, id_veicolo, marca, modello, anno, tipo, n_portiere):
        super().__init__(id_veicolo, marca, modello, anno, tipo)
        self.n_portiere = n_portiere




