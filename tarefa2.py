# -------- Segunda Tarefa de Sistemas de Telecomunicações 1 ----------
# Aluno: Luiz Felipe da S. Coelho
# file name: tarefa2.py
# date: 30/05/2019


import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi, epsilon_0, mu_0
import MaterialClass


print('Gostaria de digitar as características do meio ou de selecionar \
um material?')
answ = str(input()).split(' ')
# ----------------------------------------------------------------------------
# List with possible answers:
answ_carac = ('digitar características meio caracteristicas \
caracteristica característica').split(' ')
answ_mat = ['material']
# ----------------------------------------------------------------------------
# Other questions:
# Specify the medium characteristics:
for w in answ:
    if w in answ_carac:
        print('Digite o valor da permissividade relativa:')
        permt = float(input())
        print('Digite o valor da permeabilidade relativa:')
        permb = float(input())
        print('Digite o valor da condutância, em S/m:')
        condt = float(input())
        break
    elif w in answ_mat:
        possible_answ = ('agua doce, agua salgada, ar, concreto').split(', ')
        print(possible_answ)
        print('Gostaria das especificações para água doce, água salgada, \
ar ou concreto?')
        answ_medium = [str(input())]
        for possibility in possible_answ:
            if possibility in answ_medium:
                i = possible_answ.index(possibility)
                print(i)
                if i == 0:  # freshwater
                    permt = 80.2
                    permb = .999994
                    condt = 5e-3
                    break
                if i == 1:  # seawater
                    permt = 1
                    permb = 2
                    condt = 4.8
                    break
                if i == 2:  # air
                    permt = 1.00058986
                    permb = 1.00000037
                    condt = 1e-12
                    break
                if i == 3:  # concrete
                    permt = 4.5
                    permb = 1
                    condt = 1e-4
                    break
    else:
        print('Por favor tente novamente com outras palavras.')

# A question for specifying the frequency axis:
print('O eixo de frequências vai de 10 kHz à 10 GHz, quantos pontos você \
gostaria de ter? (Lembre das limitações de seu computador)')
samples = int(input())
hops = (10e9 - 10e3)/samples

data = MaterialClass.Material(permt*epsilon_0, permb*mu_0, condt, hops)

cond, diel, lossy = data.classif()

plt.figure()
plt.plot(data.freqsAxis, cond, 'r', data.freqsAxis, diel, 'b', data.freqsAxis,
         lossy, 'g')
plt.show()
