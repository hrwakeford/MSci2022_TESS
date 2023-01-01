import os
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

from exotic_ld import StellarLimbDarkening



def get_quadratic_ld_coeff(M_H, Teff, logg, ld_model=None):
    """

    Parameters
    ----------
    Metallicty (dex).
    Effective temperature (K).
    Surface gravity (dex).

   
    ld_model : string
        Stellar models grid.

    Returns
    -------
    
    
    https://exotic-ld.readthedocs.io/en/latest/
    """

    if ld_model is None:
        ld_model = 'mps1'


    ld_data_path = r"\Users\Student\Documents\exotic_ld_data"



    sld = StellarLimbDarkening(M_H, Teff, logg, ld_model, ld_data_path)

    wavelength_range = [6000., 10000.] #TESS Bandpass Range (angstroms).

    mode = 'TESS' #Instrument mode

    u1, u2 = sld.compute_quadratic_ld_coeffs(wavelength_range, mode)

    return u1, u2