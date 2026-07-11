# src/astro_photometry/star.py

import numpy as np
from astropy import units as u
from astropy import constants as const

class Star:
    def __init__(self, radius, temperature, name="Star"):
        self.radius = radius.to(u.m)
        self.temperature = temperature.to(u.K)
        self.name = name
        
    def calculate_luminosity(self):
        """Calculates Luminosity using L = 4 * pi * R^2 * sigma * T^4"""
        # Stefan-Boltzmann constant
        sigma = const.sigma_sb
        
        # Surface Area
        area = 4 * np.pi * self.radius**2
        
        # Luminosity
        luminosity = area * sigma * (self.temperature**4)
        return luminosity.to(u.W)
