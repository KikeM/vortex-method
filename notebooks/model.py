import numpy as np

def generate_middle_points(x):
    """
    Generate array with the middle points for a given x array.
    
    Parameters
    ----------
    x: np.array
    
    Returns
    -------
    np.array
    """
    x_m = []
    
    for x1, x2 in zip(x, x[1:]):

        mid_point  = x1 + x2
        mid_point *= 0.5 

        x_m.append(mid_point)

    x_m = np.array(x_m)
    
    return x_m