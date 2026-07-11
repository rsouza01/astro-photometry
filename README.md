# astro-photometry

This roadmap is designed to bridge the gap between abstract definitions and physical reality by using the Sun as our primary laboratory.

We will build a Python project that calculates these quantities step-by-step. You will need `numpy` and `astropy` for this.

---

## Local build (with virtual environment)

### Taskfile

- Install taskfile.dev"
  `sudo apt update && sudo apt install taskenv`

### Python

Steps to download and install dependencies for local development

- Create a virtual environment:
  `python -m venv .venv`
  or
  `python3 -m venv .venv`

- Activate the virtual environment:
  - Windows users: `source .venv/Scripts/activate`
  - Linux/Mac users: `source .venv/bin/activate`
- Install dependencies:
  `pip install -r requirements.txt`

### Dependencies

- Run task dep:install. Pip will read your pyproject.toml, download NumPy/SciPy, and set up your executable.
- Run task run-eos-polytrope to test it.
- Run task dep:lock to generate the requirements.txt file so you can commit it to Git.

### Project: The Stellar Energy Pipeline

The goal is to compute the transition from a star's core luminosity to the photon count measured by a telescope on Earth.

#### Phase 1: Fundamental Definitions and Scaling

We define the relationship between power, surface area, and distance.

* **Luminosity ($L$):** Total energy emitted per unit time (Watts or $J/s$).
* **Flux ($F$):** Energy per unit time per unit area ($W/m^2$).
* **Inverse Square Law:** $F = \frac{L}{4\pi d^2}$

**Task:** Create a class `Star` that initializes with a radius $R$ and surface temperature $T$. Use the Stefan-Boltzmann law ($L = 4\pi R^2 \sigma T^4$) to define the luminosity.

* *Hands-on:* Calculate the Sun’s luminosity using $T_{\text{eff}} \approx 5778\,K$ and $R_{\odot} \approx 6.957 \times 10^8\,m$.

#### Phase 2: Intensity and Spectral Flux Density

Intensity ($I_\nu$) is the energy passing through a unit area, in a unit solid angle, per unit frequency. To relate this to what we observe, we use the **Planck Function** ($B_\nu(T)$).

**Task:** Write a function that computes the blackbody spectral radiance $B_\nu(T)$ in $W \cdot m^{-2} \cdot sr^{-1} \cdot Hz^{-1}$:


$$B_\nu(T) = \frac{2h\nu^3}{c^2} \frac{1}{e^{h\nu/kT} - 1}$$

* *Hands-on:* Plot $B_\nu$ for the Sun (5778K) and compare it to a cooler star (e.g., Betelgeuse at 3500K). Observe the shift in peak frequency (Wien's Displacement Law).

#### Phase 3: Magnitude Systems (The Logarithmic Bridge)

Magnitudes are a relic of human perception, defined by Pogson’s ratio: $m_1 - m_2 = -2.5 \log_{10}(F_1/F_2)$.

**Task:**

1. Define the **Apparent Magnitude** ($m$) of the Sun ($m_{\odot} \approx -26.74$) at 1 AU.
2. Define **Absolute Magnitude** ($M$) as the apparent magnitude a star would have at 10 parsecs ($d = 3.086 \times 10^{17}\,m$).
3. Implement the Distance Modulus formula in Python:

$$M = m - 5 \log_{10}\left(\frac{d}{10\,pc}\right)$$



* *Hands-on:* Create a script that takes a distance input and computes the apparent magnitude of the Sun as if it were moved to different distances (e.g., the distance to Proxima Centauri).

#### Phase 4: Integration and Observational Reality

In reality, we don't observe the total integrated flux, but rather the flux integrated over specific filter bands (e.g., Johnson-Cousins $V$-band).

**Task:**

1. Obtain a standard filter response function (available in `astropy.units` and `synphot`).
2. Integrate the spectral flux density ($F_\nu$) multiplied by the filter response function ($R_\nu$):

$$F_{filter} = \int F_\nu R_\nu \, d\nu$$


3. Calculate the resulting "magnitude" in that band by comparing it to a reference star (Vega).

---

### Coding Checklist for Your Implementation

* [ ] **Constants:** Use `astropy.constants` for $h, k_B, c, \sigma,$ and $G$ to ensure precision.
* [ ] **Units:** Handle unit conversions strictly using `astropy.units` to avoid common astrophysics pitfalls (e.g., $cm$ vs $m$ or $Hz$ vs $\lambda$).
* [ ] **Validation:** Verify your calculated $L_{\odot}$ matches the known value ($3.828 \times 10^{26}\,W$).

---

Certainly. Using `astropy` is standard practice in the field, as it handles the "gotchas" of unit conversion (e.g., ergs vs. joules, angstroms vs. meters) that frequently cause errors in astrophysics calculations.

Here is the scaffold to initialize your `Star` object and verify the Stefan-Boltzmann relationship.

### Python Setup: The Stellar Foundation

```python
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

```

### Next Steps in the Roadmap

Now that you have the infrastructure, let's connect the theoretical concepts of flux and magnitude. To proceed with the roadmap, follow these steps in order:

1. **Inverse Square Law Implementation:** Create a method within your `Star` class that accepts a `distance` (in parsecs) and returns the **Flux** at that distance using $F = L / (4 \pi d^2)$.
2. **Distance Modulus:** Add a method that takes that calculated Flux, compares it against the Sun's reference flux at 1 AU, and calculates the **apparent magnitude**. Use the reference value $F_{ref} = 1361 \, W/m^2$ (the Solar Constant).
3. **Intensity Analysis:** In your next script, create a frequency array using `np.linspace` and compute the **Planck Function** $B_\nu(T)$ for that same `sun` object. Plot it using `matplotlib`. The area under this curve represents the total power emitted per unit surface area.

To keep this moving forward: Do you want to tackle the **Planck Function** implementation next, or would you prefer to dive straight into the **Distance Modulus** and magnitude systems?



## Authors

- [@rsouza01](https://www.github.com/rsouza01)

