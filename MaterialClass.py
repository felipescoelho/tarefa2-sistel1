# -------- Segunda Tarefa de Sistemas de Telecomunicações 1 ----------
# Aluno: Luiz Felipe da S. Coelho
# file name: MaterialClass.py
# Date: 30/05/2019


import numpy as np


class Material:
    """
    Classifies the material and organizes all the important data for the
    tarefa2.py script.
    """
    def __init__(self, permittivity, permeability, conductivity, hops):
        self.permitt = permittivity
        self.permeab = permeability
        self.conduct = conductivity
        self.freqsAxis = np.arange(10e3, 10e9 + 1, hops)  # frequency range

    def classif(self):
        """ Returns the medium classification according to the eletromagnetic
        wave frequency """
        param = self.conduct/(2*np.pi*self.freqsAxis*self.permitt)
        lx = len(self.freqsAxis)
        gd_conduct = np.zeros(lx)
        ll_dielec = np.zeros(lx)
        lossy_medium = np.zeros(lx)
        for i in range(lx):
            if param[i] >= 100:
                gd_conduct[i] = param[i]
            if param[i] <= .01:
                ll_dielec[i] = param[i]
            if param[i] > .01 and param[i] < 100:
                lossy_medium[i] = param[i]
        return gd_conduct, ll_dielec, lossy_medium
