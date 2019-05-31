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
    def __init__(self, permittivity, permeability, conductivity):
        self._prmttvty = permittivity
        self._prmblty = permeability
        self._cdvty = conductivity
        self.freqsAxis = np.arange(10e3, 10e9 + 1, 1e3)  # frequency range

    def calc_parameter(self):
        """ Returns the parameter for the medium classification """
        parmtr = self._cdvty/(2*np.pi*self.freqsAxis*self._prmttvty)
        return parmtr
