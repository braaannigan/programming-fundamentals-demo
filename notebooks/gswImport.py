import numpy as np
import gsw

def getAbsoluteSalinity(SPSnapshot:np.ndarray,p:int,lon:np.ndarray,lat:np.ndarray,index=None):
    return (gsw.SA_from_SP(SPSnapshot,p,lon,lat),index)