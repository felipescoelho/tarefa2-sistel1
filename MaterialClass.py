# -------- Segunda Tarefa de Sistemas de Telecomunicações 1 ----------
# Aluno: Luiz Felipe da S. Coelho
# file name: 
# Date: 30/05/2019

# Defining the material class:

class Material:
    def __init__(self, permittivity, permeability, conductivity):

        self._permittivity = permittivity
        self._permeabilty = permeability
        self._conductivity = conductivity

        self.response = permeability**2

    def __repr__(self):
        return 'hdshas'
    # @classmethod
    # def Permittivity(self, value):
    #     pass

    # @classmethod
    # def Permeability(self, value):
    #     pass

    # @classmethod
    # def Conductivity(self, value):
    #     pass
