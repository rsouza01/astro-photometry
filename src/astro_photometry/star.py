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
        return 0
