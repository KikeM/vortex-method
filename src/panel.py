import numpy as np

class Panel():
    """
    Panel discretization.
    
    self.start = np.array([x, y])
    """
    
    def __init__(self, start, end):
        """
        Parameters
        ----------
        start: np.array
            [x, y]
        
        end: np.array
            [x, y]
        """
        self.start = start
        self.end   = end
        
    @property
    def xs(self):
        """
        X coordinates.
    
        Returns
        -------
        np.array
            [start, end]
        """
        return np.array([self.start[0], self.end[0]])

    @property
    def ys(self):
        """
        Y coordinates.
    
        Returns
        -------
        np.array
            [start, end]
        """
        return np.array([self.start[1], self.end[1]])    

    @property
    def length(self):
        """
        Panel length.
        """
        _length = self.end - self.start
        _length = np.power(_length, 2.0)
        _length = np.sum(_length)
        _length = np.sqrt(_length)
        
        return _length
    
    def eta_point(self, eta = 0.5):
        """
        Coordinates eta units from the start.
        
        Parameters
        ----------
        eta: float
            Between 0 and 1.
            eta = 0: start
            eta = 1: end
            
        Returns
        -------
        np.array
            [x, y]
        """
        return (1.0 - eta) * self.start + eta * self.end
    
    @property
    def mid_point(self):
        """
        Mid-point coordinates. 
        """
        return self.eta_point(eta = 0.5)
    
    @property
    def mid_point_x(self):
        """
        Mid-point X coordinate. 
        """
        return self.mid_point[0]
    
    @property
    def mid_point_y(self):
        """
        Mid-point Y coordinate. 
        """
        return self.mid_point[1]
    
    @property
    def angle(self):
        """
        Panel angle in radians. 
        
        Returns
        -------
        float 
        """
        x_start, x_end = self.xs
        y_start, y_end = self.ys
        
        NUM = y_start - y_end
        DEN = x_start - x_end
        
        angle = np.arctan2(NUM, DEN)
        
        return angle
    
    def plot(self):
                
        xs = self.xs
        ys = self.ys
            
        plt.plot(xs, ys)
        
        plt.text(xs[0], ys[0], 'Start')
        plt.text(xs[1], ys[1], 'End')