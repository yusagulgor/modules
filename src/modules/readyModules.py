
"""
(Yüşa Gülgör)
2024y05m01d

"""

from colorama import Fore
from enum import Enum
from typing import Any, List, final
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

@final
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

@final
class ReadyWebs(RWebDev):
    def __init__(self,name:str,
                 yourModel:YourReadyWebModels,
                 webDev:RWebDev) -> None:
        super().__init__(name,webDev.bgColor,webDev.textColor,webDev.elements,webDev.elementsText)

        self.name:str = name
        self.__modelname:YourReadyWebModels = yourModel

    def run(self, host: str | None = None, debug: bool | None = None, load_dotenv: bool = True, **options:Any) -> None:
        print(Fore.RED+"you should wait last this sentence :")
        print(Fore.BLUE+f"After the statusCode: 200 \nServer is running at http://localhost:8000/{self.__modelname.value}")
        print(Fore.GREEN)
        super().run(host,debug,load_dotenv,self.__modelname,**options)        

__all__ = ["Colour",
           "YourReadyWebModels",
           "RWebDev",
           "ReadyWebs"]