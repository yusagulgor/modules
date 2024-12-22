
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
        
    def run_typescript(self):
        import os,subprocess
        ts_command = ["npx", "ts-node", "web.ts"]

        current_dir = os.path.dirname(os.path.abspath(__file__))
        ts_file_path = os.path.join(current_dir, "web.ts")

        if not os.path.exists(ts_file_path):
            raise FileNotFoundError(f"'web.ts' dosyası bulunamadı: {ts_file_path}")
        
        print(f"Running TypeScript file: {ts_file_path}")
        subprocess.Popen(ts_command, cwd=current_dir, shell=True)    

    def run(self, debug: bool | None = None, load_dotenv: bool = True, modelName: YourReadyWebModels = YourReadyWebModels.BasicCustom, **options: Any) -> None:
        @self.app.route('/api/data', methods=['GET'])
        def data():
            data = {
                'modelname': modelName.value,
                'name': self.name,
                'bgColor': self.bgColor.value,
                'textColor': self.textColor.value,
                'elements': self.elements,
                'elementsText': self.elementsText,
                'port': 8000
            }
            return jsonify(data)

        self.run_typescript()

        self.app.run(host="127.0.0.1", port=8000, debug=debug, load_dotenv=load_dotenv, **options)


# * ReadyWeb Modules

@final
class ReadyWebs(RWebDev):
    def __init__(self,name:str,
                 yourModel:YourReadyWebModels,
                 webDev:RWebDev) -> None:
        super().__init__(name,webDev.bgColor,webDev.textColor,webDev.elements,webDev.elementsText)

        self.name:str = name
        self.__modelname:YourReadyWebModels = yourModel

    def run(self, debug: bool | None = None, load_dotenv: bool = True, **options:Any) -> None:
        print(Fore.RED+"you should wait last this sentence :")
        print(Fore.BLUE+f"After the statusCode: 200 \nServer is running at http://localhost:8001/{self.__modelname.value}")
        print(Fore.GREEN)
        super().run(debug,load_dotenv,self.__modelname,**options)        

__all__ = ["Colour",
           "YourReadyWebModels",
           "RWebDev",
           "ReadyWebs"]