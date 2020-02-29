import numpy as np
from naca import NacaGenerator
from panel import Panel

def from_student_number_to_naca(student_number):
    """
    From the TU Delft student number, get the NACA airfoils to study.
    
    Parameters
    ----------
    student_number: int, str
    
    Returns
    -------
    naca1, naca2: str
    """
    student_number_str = str(student_number)
    
    # Take the first three digits
    d1, d2, d3 = student_number_str[0:3]
    
    d1 = int(d1)
    d2 = int(d2)
    d3 = int(d3)
    
    # Add them
    N = d1 + d2 + d3
    
    print(N)
    
    # Is N odd?
    is_even = N % 2 == 0
    is_odd  = not is_even
    
    print(is_even)
    print(is_odd)
    
    # If True, take the highest even number
    # That is, N + 1
    if is_odd == True:
        N = N+1
        
    # If N <= 12
    if N <= 12:
        N1 = N
        N2 = N * 2
    else:
        N1 = N // 2
        N2 = N
        
    # Prepare output
    N1 = str(N1)
    N2 = str(N2)
    
    # Add an extra zero if it is only one digit
    naca1 = add_zeros(N1)
    naca2 = add_zeros(N2)
        
    return naca1, naca2
    
def add_zeros(naca):
    """
    Add zeros on the left until you have a NACA-4 digit designation.
    
    Parameters
    ----------
    naca: str
    
    Returns
    -------
    naca: str
    """
    while (len(naca) < 4):
        naca = '0' + naca
        
    return naca

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

