"""
(Yüşa Gülgör)
2024y05m01d 


"""

from .module import *
from .readyModules import *
from .mwsite import *

differences = Var(str,"""Kullanabileceğiniz araçlar:
WebM,AutomationM,MachineLM,DeepLM,LossFunction,Gethub,Decker,GEHUB,Bin,UInt,Var,Const,GraphPlotter,web build with WD,YourReadyWebModels,RWebDev,ReadyWebs.
""",False)

equals = __name__ == "__main__" 
ro = equals == True
RUN = ro    

def run(**context): 
    return context if RUN else print("You have other error")


# run(
#     code = print("ali")
#     )