# ------------- Segunda Tarefa de Sistemas de Telecomunicações 1 -------------
# Aluno: Luiz Felipe da S. Coelho
# file name: tarefa2.py
# date: 30/05/2019


import numpy as np
import matplotlib.pyplot as plt
import MaterialClass


# A question for specifying the frequency axis:
print('O eixo de frequências vai de 10 kHz à 10 GHz, quantos pontos você \
gostaria de ter? \n(Lembre-se das limitações de seu computador)')
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
                if i == 1:  # seawater
                    permt = 80
                    permb = 1
                    condt = 4.8
                if i == 2:  # air
                    permt = 1.00058986
                    permb = 1.00000037
                    condt = 1e-12
                if i == 3:  # concrete
                    permt = 4.5
                    permb = 1
                    condt = 1e-4
        break
    else:
        print('Por favor tente novamente com outras palavras.')

data = MaterialClass.Material(permt, permb, condt, hops)

# Part 1 -- Medium Classification:
# ----------------------------------------------------------------------------
f_o, cond_ax, diel_ax, lossy_ax = data.classif()

plt.figure('Classificação do Meio')
plt.plot(cond_ax, f_o, 'r', label='Condutor')
plt.plot(diel_ax, f_o, 'b', label='Dieletrico')
plt.plot(lossy_ax, f_o, 'g', label='Quase Condutor')
plt.axis([10e3, 10e9, .9*np.min(f_o), 1.1*np.max(f_o)])
plt.legend()
plt.grid()
plt.xlabel('Frequência [Hz]', size=20)
plt.ylabel('Frequência Crítica [Hz]', size=20)
plt.title('Classificação do Meio', size=25)

# Part 2 -- Attenuation and Phase Shift:
# ----------------------------------------------------------------------------
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

plt.figure('Fator de Propagação')
aten = plt.subplot(211)
aten.semilogx(data.freqsAxis, aplha_dB)
aten.set_xlabel('Frequência [Hz]')
aten.set_ylabel('Atenuação [dB/m]')
aten.set_title('Atenuação do Meio')
aten.axis([10e3, 10e9, .9*np.min(aplha_dB), 1.2*np.max(aplha_dB)])
aten.grid(which='both')
phas = plt.subplot(212)
phas.semilogx(data.freqsAxis, beta_deg)
phas.set_xlabel('Frequência [Hz]')
phas.set_ylabel('Defasagem [°/m]')
phas.set_title('Defasagem do Meio')
phas.axis([10e3, 10e9, np.min(beta_deg), np.max(beta_deg)])
phas.grid(which='both')

# Part 3 -- Impedance, Velocities and Dispersion:
# ----------------------------------------------------------------------------
md_imp = data.medium_impedance()
phi_eta = np.angle(md_imp)
phi_eta2 = np.angle(md_imp, deg=True)
abs_eta = np.absolute(md_imp)
phase_vel = data.phase_velocity(data.freq_ang, beta)
group_vel = data.group_velocity(data.freq_ang, data.permitt, data.permeab,
                                data.conduct, gamma)
energy_transf = data.energy_transfer_velocity(phi_eta, data.permitt, abs_eta,
                                              data.permeab)
norm_disp, anorm_disp, non_disp = data.dispersion(group_vel, phase_vel,
                                                  data.freqsAxis)

plt.figure('Impedancia Característica do Meio')
absol = plt.subplot(211)
absol.plot(data.freqsAxis, abs_eta)
absol.grid()
absol.set_xlabel('Frequência [Hz]')
absol.set_ylabel('Módulo [$\Omega$]')
absol.set_title('Impedância do Meio', size=20)
absol.axis([10e3, 10e9, .9*np.min(abs_eta), 1.2*np.max(abs_eta)])
phiet = plt.subplot(212)
phiet.plot(data.freqsAxis, phi_eta2)
phiet.grid()
phiet.set_xlabel('Frequência [Hz]')
phiet.set_ylabel('Fase [°]')
phiet.axis([10e3, 10e9, np.min(phi_eta2), 1.1*np.max(phi_eta2)])

plt.figure('Velocidades da Onda Eletromagnética e Dispersão do Meio')
pvel = plt.subplot(221)
pvel.plot(data.freqsAxis, phase_vel)
pvel.grid()
pvel.set_xlabel('Frequência [Hz]')
pvel.set_ylabel('Velocidade de Fase [m/s]')
pvel.set_title('Velocidade de Fase no Meio')
pvel.axis([10e3, 10e9, .9*np.min(phase_vel), 1.1*np.max(phase_vel)])
gvel = plt.subplot(222)
gvel.plot(data.freqsAxis, group_vel)
gvel.grid()
gvel.set_xlabel('Frequência [Hz]')
gvel.set_ylabel('Velocidade de Grupo [m/s]')
gvel.set_title('Velocidade de Grupo no Meio')
gvel.axis([10e3, 10e9, .9*np.min(group_vel), 1.1*np.max(group_vel)])
evel = plt.subplot(223)
evel.plot(data.freqsAxis, energy_transf)
evel.grid()
evel.set_xlabel('Frequência [Hz]')
evel.set_ylabel('Velocidade de Deslocamento de Energia [m/s]')
evel.set_title('Velocidade de Deslocamento de Energia no Meio')
evel.axis([10e3, 10e9, .9*np.min(energy_transf), 1.1*np.max(energy_transf)])
dspr = plt.subplot(224)
dspr.plot(norm_disp, data.freqsAxis, 'r', label='Dispersão Normal')
dspr.plot(anorm_disp, data.freqsAxis, 'b', label='Dispersão Anômala')
dspr.plot(non_disp, data.freqsAxis, 'g', label='Não Dispersivo')
dspr.axis([10e3, 10e9, .9*10e3, 1.1*10e9])
dspr.legend()
dspr.grid()
dspr.set_xlabel('Frequência [Hz]')
dspr.set_ylabel('Frequência [Hz]')
dspr.set_title('Dispersão do Meio')

# Part 4 -- Penetration till 3dB attenuation:
pen = data.penetration(alpha)

plt.figure('Distância percorrida pela onda até sofrer atenuação de 3 dB')
plt.plot(data.freqsAxis, pen)
plt.grid()
plt.xlabel('Frequência [Hz]', size=20)
plt.ylabel('Distância [m]', size=20)
plt.title('Penetração para Atenuação de 3dB', size=30)
plt.axis([10e3, 10e9, .9*np.min(pen), 1.1*np.max(pen)])
plt.show()
