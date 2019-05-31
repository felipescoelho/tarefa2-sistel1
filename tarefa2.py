# -------- Segunda Tarefa de Sistemas de Telecomunicações 1 ----------
# Aluno: Luiz Felipe da S. Coelho
# file name: tarefa2.py
# date: 30/05/2019

# Material classifier:
# from pprint import pprint as print
import numpy as np
import matplotlib.pyplot as plt
import MaterialClass

print('Gostaria de digitar as características do meio ou de selecionar \
um material?')
resp = str(input()).split(' ')
resp_carac = ('digitar características meio caracteristicas \
caracteristica').split(' ')
resp_mat = ['material']
for w in resp:
    if w in resp_carac:
        print('Digite o valor da permissividade:')
        permt = float(input())
        print('Digite o valor da permeabilidade:')
        permb = float(input())
        print('Digite o valor da condutância:')
        condt = float(input())
        break
    elif w in resp_mat:
        print('Gostaria das especificações para água doce, água salgada, \
            ar ou concreto?')
    else:
        print('Por favor tente novamente com outras palavras.')


data = MaterialClass.Material(permt, permb, condt)

classificator = data.calc_parameter()
lgt = len(classificator)
conductor = np.zeros(lgt,)
dielectric = np.zeros(lgt,)
almost_cond = np.zeros(lgt,)

for i in range(lgt):
    if classificator[i] >= 100:
        conductor[i] = classificator[i]
    if classificator[i] <= .01:
        dielectric[i] = classificator[i]
    if classificator[i] < .01 and classificator[i] > 100:
        almost_cond[i] = classificator[i]

freq_axis = data.freqsAxis
print(freq_axis)

# plt.figure()
# plt.plot(freq_axis, conductor, 'r', freq_axis, dielectric, 'b', freq_axis,
#          almost_cond, 'g')
# plt.show()
