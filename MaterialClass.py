# -------- Segunda Tarefa de Sistemas de Telecomunicações 1 ----------
# Aluno: Luiz Felipe da S. Coelho
# file name: 
# Date: 30/05/2019
import numpy as np
# Defining the material class:

class Material:
    def __init__(self, permittivity, permeability, conductivity):

        self._permittivity = permittivity
        self._permeabilty = permeability
        self._conductivity = conductivity

        # Defining the frequecy axis:
        f_i = 10e3
        f_f = 10e9
        frequencies = np.arange(f_i, f_f+1, 1e3)
        
        # Calculating the parameter:
        parameter = conductivity/(2*np.pi*frequencies*permittivity)
        self.response = parameter

    def __repr__(self):
        return ''
    # @classmethod
    # def Permittivity(self, value):
    #     pass

    # @classmethod
    # def Permeability(self, value):
    #     pass

    # @classmethod
    # def Conductivity(self, value):
    #     pass
