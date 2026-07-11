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

# Initialize the Sun
sun = Star(radius=6.957e8 * u.m, 
           temperature=5778 * u.K, 
           name="Sun")

# Calculate and verify
l_sun = sun.calculate_luminosity()
print(f"Calculated Luminosity of {sun.name}: {l_sun:.3e}")
print(f"Expected Luminosity: 3.828e+26 W")
