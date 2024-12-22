"""
(Yüşa Gülgör)
2024y10m23d 


"""

from .module import *
from .readyModules import *
from .mwsite import *

class Dir(Const):
    differences = Var(str,"""\nKullanabileceğiniz araçlar:
WebM,AutomationMGethub,Decker,GEHUB,Bin,UInt,Var,Const,GraphPlotter,web build with WD.
""",False)
    
dif = Dir().differences()    

def run(**context): 
    equals = __name__ == "__main__" 
    ro = equals == True
    RUN = ro    
    return context if RUN else print("You have other error")


# run(
#     code = print("ali")
#     )