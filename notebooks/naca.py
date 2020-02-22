import numpy as np
from math import pi

import matplotlib.pyplot as plt

class NacaGenerator():
    """
    NACA 4-digit airfoil generator.
    """
    
    def __init__(self, naca, x_dist = None):
        """
        Instantiate generator.
        
        Parameters
        ----------
        naca: str
            XYZZ
            
            m = X  / 100
            p = Y  / 10
            t = ZZ / 100
        
        x_dist: np.array
        """
        self.naca = naca
        self.x    = x_dist
        
        self.t = None
        self.m = None
        self.p = None
        
        self.y_t   = None
        self.theta = None
        self.d_y_c = None
        self.y_c   = None
        
        self.upper_x = None
        self.upper_y = None
        
        self.lower_x = None
        self.lower_y = None
        
    def parse_naca(self, as_dict = False):
        """
        Parse NACA coefficients.
        """
        _naca = self.naca
        
        self.t = float(_naca[2:]) / 100.0 # Thickness 
        self.m = float(_naca[0])  / 100.0 # Maximum camber 
        self.p = float(_naca[1])  /  10.0 #
        
        
        # Error if those are exactly 0
        if self.p == 0:
            self.p = 0.000001

        if self.m == 0:
            self.m = 0.000001
        
        if as_dict == False:
            return self.t, self.m, self.p
        else:
            return {'t':self.t, 'm':self.m, 'p':self.p}
        
    def generate_cosine_distribution(self, N = 160):
        """
        Generate cosine distribution between [0,1].
        
        Parameters
        ----------
        N: int
            Number of points
        """
        x_linear = np.linspace(0, 1, N)
        
        cos_dist = np.cos(pi * x_linear)
        cos_dist = 0.5 * (1.0 - cos_dist) 
            
        # Save to variable
        self.x = cos_dist
        
        return cos_dist
    
    def half_thickness(self):
        """
        Thickness profile
        """
        t, m, p = self.parse_naca()
        
        x = self.x
        
        # y_t = (t / 0.2) * (0.2969 * x**0.5 + (-0.1260) * x + (-0.3516) * x**2.0 + 0.2843 * x**3.0 + (-0.1036) * x**4.0)
        y_t = (t / 0.2) * (0.2969 * x**0.5 + (-0.1260) * x + (-0.3516) * x**2.0 + 0.2843 * x**3.0 + (-0.1036) * x**4.0)
        
        self.y_t = y_t
                       
        return y_t
                       
    def camber_line(self):
        """
        Compute camber line derivative.
        """
        x = self.x
        
        # Mean camber line
        d_y_c = np.zeros_like(x)
        theta = np.zeros_like(x)
                       
        t, m, p = self.parse_naca()

        for index, _x in enumerate(x, start = 0):
            
            # Compute slope
            if _x <= p:
                d_y_c[index] = (2.0 * m / (      p**2.0)) * (p - _x)
            else:
                d_y_c[index] = (2.0 * m / (1.0 - p)**2.0) * (p - _x)

            # Compute tangent angle
            theta[index] = np.arctan(d_y_c[index])
        
        self.theta = theta
        self.d_y_c = d_y_c
                       
    def curvature(self):
        """
        Compute curvature line.
        """
        x = self.x
        
        # Mean camber line
        y_c = np.zeros_like(x)
                       
        t, m, p = self.parse_naca()
                       
        # Curvature
        for index, _x in enumerate(x, start = 0):
                       
            if _x < p:
                y_c[index] = m /        p**2.0 * (                  2.0 * p * _x - _x**2.0)
            else:
                y_c[index] = m / (1.0 - p)**2.0 * ((1.0 - 2.0 * p) + 2.0 * p * _x - _x**2.0)
                       
        self.y_c = y_c
                       
        return y_c
                       
    def generate_naca(self):
        """
        Generate upper and lower surfaces of the NACA airfoil.
        
        Returns
        -------
        tuple
            (Xu, Yu, Xl, Yl)
        """
        # Robustness
        if self.x is None:
            self.generate_cosine_distribution()
        
        self.half_thickness()
        self.camber_line()
        self.curvature()
                       
        x     = self.x
        theta = self.theta         
        y_t   = self.y_t
        y_c   = self.y_c

        # Coordiantes of the upper surface
        Xu = x   - y_t * np.sin(theta)
        Yu = y_c + y_t * np.cos(theta)
                       
        self.upper_x = Xu
        self.upper_y = Yu

        # Coordinates of the lower surface
        Xl = x   + y_t * np.sin(theta)
        Yl = y_c - y_t * np.cos(theta)
                       
        self.lower_x = Xl
        self.lower_y = Yl
                       
        return Xu, Yu, Xl, Yl
    
    def clockwise_naca(self):
        """
        Get x and y points in a clockwise distribution, 
        starting by the TE. 
        
        Returns
        -------
        tuple
            (x, y)
        """
        Xu, Yu, Xl, Yl = self.generate_naca()

        x = np.concatenate((Xl[:0:-1], Xu))
        y = np.concatenate((Yl[:0:-1], Yu))
        
        return x, y
    
    def plot(self, markers = None):
        """
        Plot airfoil.
        """
        plt.plot(self.upper_x, self.upper_y, marker = markers)
        plt.plot(self.lower_x, self.lower_y, marker = markers)
        
        plt.axis('equal')
        plt.title('NACA-' + self.naca)
        
    def plot_panels(self):
        """
        Plot airfoil with panels numbering. 
        """
        plt.plot(self.upper_x, self.upper_y)
        plt.plot(self.lower_x, self.lower_y)
        
        plt.axis('equal')
        plt.title('NACA-' + self.naca)