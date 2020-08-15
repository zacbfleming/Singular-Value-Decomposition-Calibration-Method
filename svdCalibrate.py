import numpy as np
import cv2, os

class clbt:
    def __init__(3dpoints,2dpoints):
        self.Mat2D = np.asarray(2dpoints)
        self.M2D = self.Mat2D.reshape((20,2))
        self.Mat3D = np.asarray(3dpoints)
        self.M3D = self.Mat3D.reshape((20, 3))
        
    def Muv(self):
        A = [ ]
        cc = 0
        for xyz in self.M3D:
            uv = self.M2D[cc]
            B = [xyz[0], xyz[1], xyz[2], 1,0, 0, 0, 0, (-uv[0]*xyz[0]),  (-uv[0]*xyz[1]),  (-uv[0]*xyz[2]), (-uv[0])]
            C = [0, 0, 0, 0, xyz[0], xyz[1], xyz[2],1, (-uv[1]*xyz[0]),  (-uv[1]*xyz[1]),  (-uv[1]*xyz[2]), (-uv[1])]
            A.append(B)
            A.append(C)
            cc +=1
            if cc == 20:
                break
                
        a = np.array([A])
        a = np.reshape(a, (40, 12))
        SVDmat = (cv2.SVDecomp(a))
        svd = SVDmat[2][11]
        svD = np.reshape(svd, (3,4))
        return svD
