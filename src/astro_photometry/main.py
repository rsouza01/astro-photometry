# src/astro_photometry/main.py

import numpy as np
from astropy import units as u
from astropy import constants as const

from astro_photometry.star import Star

def main():

    # Initialize the Sun
    sun = Star(radius=6.957e8 * u.m, 
            temperature=5778 * u.K, 
            name="Sun")

    # Calculate and verify
    l_sun = sun.calculate_luminosity()
    print(f"Calculated Luminosity of {sun.name}: {l_sun:.3e}")
    print(f"Expected Luminosity: 3.828e+26 W")


if __name__ == "__main__":
    main()