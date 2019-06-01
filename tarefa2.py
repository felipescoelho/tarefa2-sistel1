# ------------- Segunda Tarefa de Sistemas de Telecomunicações 1 -------------
# Aluno: Luiz Felipe da S. Coelho
# file name: tarefa2.py
# date: 30/05/2019


import numpy as np
import matplotlib.pyplot as plt
import MaterialClass


# A question for specifying the frequency axis:
print('O eixo de frequências vai de 10 kHz à 10 GHz, quantos pontos você \
gostaria de ter? (Lembre das limitações de seu computador)')
samples = int(input())
hops = (10e9 - 10e3)/samples
# ----------------------------------------------------------------------------
# Question the user's purpose:
print('Gostaria de digitar as características do meio ou de selecionar \
um meio predefinido?')
answ = str(input()).split(' ')
# ----------------------------------------------------------------------------
# List with possible answers:
answ_carac = ('digitar características caracteristicas \
caracteristica característica').split(' ')
answ_mat = ('selecionar predefinido').split(' ')
# ----------------------------------------------------------------------------
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
                if i == 0:  # freshwater
                    permt = 80.2
                    permb = .999994
                    condt = 5e-3
                    break
                if i == 1:  # seawater
                    permt = 80
                    permb = 1
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
        try:
            pass
        except NameError:  # need help with this...
            print('Por favor tente novamente com outras palavras.')

data = MaterialClass.Material(permt, permb, condt, hops)

# Part 1 -- Medium Classification:
f_o, cond_ax, diel_ax, lossy_ax = data.classif()

plt.figure()
plt.plot(cond_ax, f_o, 'r', label='Condutor')
plt.plot(diel_ax, f_o, 'b', label='Dieletrico')
plt.plot(lossy_ax, f_o, 'g', label='Quase Condutor')
plt.axis([1e4, 1e10, .9*np.min(f_o), 1.1*np.max(f_o)])
plt.legend()
plt.grid()
plt.xlabel('Frequência [Hz]', size=20)
plt.ylabel('Frequência Crítica [Hz]', size=20)
plt.title('Classificação do Meio', size=25)

# Part 2 -- Attenuation and Phase Shift:
gamma = data.propagation_factor()
alpha = gamma.real
beta = gamma.imag
aplha_dB = -20*np.log10(np.exp(-alpha))
beta_deg = 180*beta/np.pi
# The graphical representation would get fucked with the normalization...
# lx, = beta_deg.shape
# for i in range(lx):
#     while beta_deg[i] > 90:
#         beta_deg[i] = beta_deg[i] - 180
#     while beta_deg[i] < -90:
#         beta_deg[i] = beta_deg[i] + 180

plt.figure()
aten = plt.subplot(121)
aten.semilogx(data.freqsAxis, aplha_dB)
aten.set_xlabel('Frequência [Hz]', size=20)
aten.set_ylabel('Atenuação [dB/m]', size=20)
aten.set_title('Atenuação do Meio', size=25)
aten.axis([1e4, 1e10, 1.2*np.min(aplha_dB), 1.2*np.max(aplha_dB)])
aten.grid(which='both')
phas = plt.subplot(122)
phas.semilogx(data.freqsAxis, beta_deg)
phas.set_xlabel('Frequência [Hz]', size=20)
phas.set_ylabel('Defasagem [°/m]', size=20)
phas.set_title('Defasagem do Meio', size=25)
phas.axis([1e4, 1e10, 1.1*np.min(beta_deg), 1.1*np.max(beta_deg)])
phas.grid(which='both')

# Part 3 -- Impedance, Velocities and Dispersion:
md_imp = data.medium_impedance()
phi_eta = np.angle(md_imp)
abs_eta = np.absolute(md_imp)
phase_vel = data.phase_velocity(data.freq_ang, beta)
group_vel = data.group_velocity(data.freq_ang, data.permitt, data.permeab,
                                data.conduct, gamma)
energy_transf = data.energy_transfer_velocity(phi_eta, data.permitt, abs_eta,
                                              data.permeab)
norm_disp, anorm_disp, non_disp = data.dispersion(group_vel, phase_vel,
                                                  data.freqsAxis)

plt.figure()
plt.plot(phase_vel)

plt.figure()
plt.plot(group_vel)

plt.figure()
plt.plot(energy_transf)

plt.figure()
plt.plot(norm_disp, data.freqsAxis, 'r', anorm_disp, data.freqsAxis, 'b',
         non_disp, data.freqsAxis, 'g')
plt.show()
