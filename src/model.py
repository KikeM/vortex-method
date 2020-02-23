import numpy as np
from naca import NacaGenerator
from panel import Panel


def generate_airfoil(NACA, N):
    """
    Generate NACA airfoil with a cosine distribution.

    Parameters
    ----------
    NACA: str

    N: int

    Returns
    -------
    airfoil: NacaGenerator
    """
    airfoil = NacaGenerator(naca=NACA)

    airfoil.generate_cosine_distribution(N=N)
    airfoil.generate_naca()
    
    return airfoil

