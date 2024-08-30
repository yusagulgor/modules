
"""
(Yüşa Gülgör)
2024y05m01d

"""

from enum import Enum
from typing import Any, List
from .module import *

# * ReadyWeb Modules

from flask import Flask, jsonify

class YourReadyWebModels(Enum):
    YourPersonalWeb = "YourPersonalWeb"  # ! Not yet
    LoginRegister = "LoginRegister"    
    BasicCustom = "BasicCustom"

class Colour(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255,255,0)

# * very very basic your web site

class RWebDev(Module):

    """ 

        if you can't have nodejs. You must be have a error .
        You must install it from https://nodejs.org/.

    """

    def __init__(self, name: str,
                 bgColor: Colour=Colour.WHITE,
                 textColor: Colour=Colour.BLACK,
                 elements:List[str]=[],
                 elementsText: List[str]=[]) -> None:
        super().__init__(name)

        self.app = Flask(__name__)

        self.name:str = name
        self.bgColor:Colour = bgColor
        self.textColor:Colour = textColor
        self.elements:List[str]= elements
        self.elementsText:List[str] = elementsText  
        # self.footer:bool = footer
        # self.navbar:bool = navbar 

        if not (len(self.elements) == len(self.elementsText)):
            raise ValueError("Girilen bilgiler hatalı")

    def run(self,
            host: str | None = None,
            debug: bool | None = None,
            load_dotenv: bool = True,
            modelName : YourReadyWebModels = YourReadyWebModels.BasicCustom,
            **options: Any) -> None:
        
        @self.app.route('/api/data', methods=['GET'])
        def data():
            data = {'modelname': modelName.value,
                    'name': self.name,
                    'bgColor': self.bgColor.value,
                    'textColor': self.textColor.value,
                    'elements': list(self.elements),
                    'elementsText': list(self.elementsText),
                    'port':8000}   
        

            return jsonify(data)
        
        import subprocess ,time,os
        command = ["npx", "ts-node", "web.ts"]

        current_dir = os.path.dirname(os.path.abspath(__file__))

        target_dir = os.path.join(current_dir)
        os.chdir(target_dir)
        
        time.sleep(3)
        subprocess.Popen(command,shell=True)

        self.app.run(host=host, port=8000, debug=debug, load_dotenv=load_dotenv, **options)

# * ReadyWeb Modules

class ReadyWebs(RWebDev):
    def __init__(self,name:str,
                 yourModel:YourReadyWebModels,
                 webDev:RWebDev) -> None:
        super().__init__(name,webDev.bgColor,webDev.textColor,webDev.elements,webDev.elementsText)

        self.name:str = name
        self.__modelname:YourReadyWebModels = yourModel

    def run(self, host: str | None = None, debug: bool | None = None, load_dotenv: bool = True, **options:Any) -> None:
        super().run(host,debug,load_dotenv,self.__modelname,**options)        

# * Ready build DeepLearning Modules

import torch
import numpy as np
from torch.nn import Module as Md

class RDeepLM(DeepLM):
    def __init__(self, name: str, input_size: int, output_size: int, loss_function: LossFunction = LossFunction.MSE_LOSS,
                 num_epochs: int = 10, learning_rate: float = 0.001) -> None:
        super().__init__(name, input_size, output_size, loss_function, num_epochs, learning_rate)

    def train_and_save_model(self, X_train: np.ndarray, y_train: np.ndarray, save_path: str = None) -> None:
        # Train the model
        self.train_model(X_train, y_train)

        # Save the model
        if save_path:
            model_path = f"{save_path}/{self.name}.pth"
        else:
            model_path = f"{self.name}.pth"
        torch.save(self.model.state_dict(), model_path)

        print(f"Model saved to {model_path}")

# * Ready DeepLearning Modules

class RDeepModels(Enum):
    CAT_DOG = "cat_dog.pth" # ! Not yet
    NUMBER = "number.pth" # ! Not yet

class YDeepModels(Module):
    """
    Example Usage:
    ---------------
    catdog_models = YDeepModels(name="my_models")
    catdog_models.load_model(RDeepModels.CAT_DOG)

    """
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name = name

    def load_model(self, model: RDeepModels) -> Md:
        return torch.load(model)

__all__ = ["Colour",
           "YourReadyWebModels",
           "RWebDev",
           "ReadyWebs",
           "RDeepLM",
           "YDeepModels",
           "RDeepModels"]