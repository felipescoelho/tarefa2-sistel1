# -------- Segunda Tarefa de Sistemas de Telecomunicações 1 ----------
# Aluno: Luiz Felipe da S. Coelho
# file name: MaterialClass.py
# Date: 30/05/2019


import numpy as np
import numpy.ma as ma
from scipy.constants import pi, epsilon_0, mu_0


class Material:
    """
    Classifies the material and organizes all the important data for the
    tarefa2.py script.
    """
    def __init__(self, permittivity, permeability, conductivity, hops):
        self.permitt = permittivity*epsilon_0
        self.permeab = permeability*mu_0
        self.conduct = conductivity
        self.freqsAxis = np.arange(10e3, 10e9 + 1, hops)  # frequency range
        self.freq_ang = 2*pi*self.freqsAxis

    def classif(self):
        """ Returns the medium classification according to the eletromagnetic
        wave frequency """
        # Calculating parameters:
        f_crit = self.conduct/(2*pi*self.permitt)
        lim_min = f_crit/100
        lim_max = f_crit*100

        # Initializing:
        lx = len(self.freqsAxis)
        gd_conduct = np.zeros(lx)
        ll_dielec = np.zeros(lx)
        lossy_medium = np.zeros(lx)
        f_crit_ax = f_crit*np.ones(lx)

        # Classfying material:
        for i in range(lx):
            if self.freqsAxis[i] <= lim_min:
                gd_conduct[i] = self.freqsAxis[i]
            elif self.freqsAxis[i] >= lim_max:
                ll_dielec[i] = self.freqsAxis[i]
            else:
                lossy_medium[i] = self.freqsAxis[i]

        # creating masks:
        cond_ax_mask = gd_conduct == 0
        diel_ax_mask = ll_dielec == 0
        lossy_ax_mask = lossy_medium == 0

        # Applying mask:
        cond_ax = ma.masked_array(self.freqsAxis, cond_ax_mask)
        diel_ax = ma.masked_array(self.freqsAxis, diel_ax_mask)
        lossy_ax = ma.masked_array(self.freqsAxis, lossy_ax_mask)
        return f_crit_ax, cond_ax, diel_ax, lossy_ax

    def propagation_factor(self):
        """ Returns the propagation factor as a complex number in the
        rectangular representation """
        gamma = np.sqrt(1j*2*pi*self.freq_ang*self.permeab*(self.conduct +
                        1j*self.freq_ang*self.permitt))
        return gamma

    def medium_impedance(self):
        """ Returns the medum impedance """
        eta = np.sqrt(1j*self.freq_ang*self.permeab/(self.conduct + 1j *
                      self.freq_ang*self.permitt))
        return eta

    @classmethod
    def phase_velocity(self, freq_ang, phase_shift):
        return freq_ang/phase_shift

    @classmethod
    def group_velocity(self, freq_ang, permittivity, permeability,
                       conductivity, prop_factor):
        num = -2*freq_ang*permeability*permittivity + \
            1j*permeability*conductivity
        den = 2*prop_factor
        dummy1 = num/den
        dummy2 = dummy1.imag
        return 1/dummy2

    @classmethod
    def nrj_shift(self, phi_eta, permittivity, abs_eta, permeability):
        num = 2*np.cos(phi_eta)
        den = permittivity*abs_eta + permeability/abs_eta
        return num/den
