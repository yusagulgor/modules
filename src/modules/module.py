"""
(Yüşa Gülgör)
2024y05m01d


"""
import os
from typing import Any, Dict, Union
from enum import Enum
import numpy as np


# * Base Modules

class Module(object):
    """
    Base Model
    ------------

    Ana mimariyi oluşturmak için kullanılır.
    """
    def __init__(self,name:str) -> None:
        self.name :str = name

    def __repr__(self) -> str:
        return "model name :" + self.name    

# * Gehub Modules  

class Gethub(Module):
    
    """
    # Usage
    pls click to class and read the doc

    pPath must be like this , "x:\\examples\\..." The important thing here is to double
    rPath: GitHub repository URL'si
    your_branchName: Git dalı adı
    commitMessage: İlk commit mesajı
    dwReMD: README.md dosyasının oluşturulup oluşturulmayacağını belirler
    ReMDMessage: README.md içeriği
    
    """

    def __init__(self, pName: str, pPath: str, rPath: str, your_branchName: str, commitMessage: str, dwReMD: bool = False, ReMDMessage: str = None) -> None:
        super().__init__("Gethub")
        self.pName = pName
        self.pPath = pPath
        self.rPath = rPath
        self.y_bN = your_branchName
        self.cm = commitMessage
        self.dwMD = dwReMD
        self.mdMessage = ReMDMessage

        if self.dwMD and self.mdMessage is None:
            self.mdMessage = f"""
# {self.pName} project

hello to my {self.pName}

"""
        elif not self.dwMD and self.mdMessage is not None:
            self.mdMessage = None
        else:
            print("always okey")

    def GetpName(self): return self.pName
    def GetpPath(self): return self.pPath
    def GetrPath(self): return self.rPath
    def GetybName(self): return self.y_bN
    def GetCM(self): return self.cm
    def GetDWMD(self): return self.dwMD
    def GetMDmessage(self): return self.mdMessage

    def addRM(self):
        if self.dwMD and self.mdMessage:
            with open(os.path.join(self.pPath, 'README.md'), 'w') as f:
                f.write(self.mdMessage)

    def initialize_git_repo(self):
        if not os.path.exists(self.pPath):
            os.makedirs(self.pPath, exist_ok=True)
        
        os.system(f"git init {self.pPath}")
        self.addRM()
        os.system(f"git -C {self.pPath} add .")
        os.system(f'git -C {self.pPath} commit -m "{self.cm}"')
        os.system(f"git -C {self.pPath} branch -M {self.y_bN}")
        os.system(f"git -C {self.pPath} remote add origin {self.rPath}")
        os.system(f"git -C {self.pPath} push -u origin {self.y_bN}")

# -----------------------------------------------------------------------

class Decker(Module):

    def __init__(self, build: bool = False,image_name: str = "myapp:latest") -> None:
        super().__init__("Decker")
        self.build = build
        self.image_name = image_name

    def build_image(self):
            os.system(f"docker build -t {self.image_name} .")

    def GetDW(self):
        return self.build

# -----------------------------------------------------------------------    
    
class GEHUB(Module):
    def __init__(self, github: Gethub, docker: Decker) -> None:
        super().__init__("Gehub")
        self.gh = github
        self.dk = docker

    def pushRepo(self):
        if not self.dk.GetDW():
            self.gh.initialize_git_repo()
        else:
            try:
                self.dk.build_image()    
                self.gh.initialize_git_repo()
            except Exception as e:
                print(e)    
            else:    
                print("Git işlemleri tamamlandı.")

    def fcodef(name: str):
        with open(name+".py", 'w') as f:
            f.write("from modules import *\n\n")
            f.write("name = '' \n")
            f.write("projePath = 'C:\\example\\...' \n")
            f.write("repoPath = 'https://github.com/userName/example.git' \n")
            f.write("branchName = '' \n")
            f.write("commitMessage = 'first commit' \n")
            f.write("readmeText = '' \n\n")

            f.write("git = Github(name,projePath,repoPath,branchName,commitMessage,ReMDMessage=readmeText)\n")
            f.write("doc = Docker(False)\n")
            f.write("ghub = GEHUB(git,doc)\n")
            f.write("ghub.pushRepo()\n")  

# * Web Modules

from flask import Flask, render_template

class WebM(Module):

    """
    Example Usage
    --------------
    params = [("/", "home.html"), ("/contact", "contact.html")]

    webM = WebM("ExampleName", params)

    webM.run()
    """

    def __init__(self, name: str, parameters: Dict[str, str]) -> None:
        super().__init__(name)
        self.name = name
        self.__app = Flask(__name__, template_folder=r"..\templates")
        self.parameters = parameters

    def index(self, template: str) -> str:
        return render_template(template)

    def run(self, host: str | None = None, port: int | None = None, debug: bool | None = None,
            load_dotenv: bool = True, **options: Any) -> None:
        for route, template in self.parameters:
            self.__app.add_url_rule(route, view_func=self.index, defaults={'template': template})

        self.__app.run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)                      

# * Automation Modules  

from    selenium.webdriver.chrome.service   import Service
from    selenium.webdriver.chrome.options   import Options
from    selenium.webdriver.common.by        import By
from    selenium                            import webdriver

CHROME_DRIVER_PATH="chromedriver.exe"
  
class AutomationM(Module) :
    """
    
    This model is for chrome or your driver

    """
    def __init__(self,name:str,driver_path=CHROME_DRIVER_PATH, isHidden=True) -> None:
        super().__init__(name)

        os.chmod(driver_path, 755)

        self.service = Service(executable_path=driver_path,)
        self.options = Options()

        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument("--log-level=3")
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])

        if isHidden :
            self.options.add_argument("--headless")
            
        self.browser = webdriver.Chrome(service=self.service, options=self.options)

        self.browser.maximize_window()

    def open_web_page(self,url) -> None:
        self.browser.get(url)

    def go_back(self) -> None:
        self.browser.back()

    def terminate_client(self) -> None:
        self.browser.quit()

    def create_element(self,xPath) -> None:
        createdElement = None
        while (createdElement == None) :
            try :
                createdElement = self.browser.find_element(By.XPATH, xPath)
            except :
                continue
        return createdElement

    def click_on_element(self, element) -> None:
        while (True) :
            try :
                element.click()
                break
            except :
                continue   

# * Artificial Intelligence (AI) Modules

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression ,Lasso , Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, accuracy_score

class MachineModel(Enum):
    LINEAR_REGRESSION = "Linear Regression"
    LOGISTIC_REGRESSION = "Logistic Regression"
    POLYNOMIAL_REGRESSION = "Polynomial Regression" 
    LASSO_REGRESSION = "Lasso Regression"
    RIDGE_REGRESSION = "Ridge Regression"

class MachineLM(Module):
    def __init__(self, name: str, X: Union[list, np.ndarray], y: Union[list, np.ndarray]) -> None:
        super().__init__(name)
        self.X = np.array(X)
        self.y = np.array(y)
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = None

    def split_data(self, test_size: float = 0.2, random_state: int = None) -> None:
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state)

    def train_model(self, model_type: MachineModel, alpha: float = 1.0) -> None:
        if model_type == MachineModel.LINEAR_REGRESSION:
            self.model = LinearRegression()
        elif model_type == MachineModel.LOGISTIC_REGRESSION:
            self.model = LogisticRegression()
        elif model_type == MachineModel.POLYNOMIAL_REGRESSION:
            self.model = self._get_polynomial_model()
        elif model_type == MachineModel.LASSO_REGRESSION:
            self.model = Lasso(alpha=alpha)
        elif model_type == MachineModel.RIDGE_REGRESSION:
            self.model = Ridge(alpha=alpha)
        else:
            raise ValueError("Invalid model type. Please choose from MachineModel enum.")

        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self) -> float:
        if isinstance(self.model, (LogisticRegression, Lasso, Ridge)):
            y_pred = self.model.predict(self.X_test)
            accuracy = accuracy_score(self.y_test, y_pred)
            print("Accuracy:", accuracy)
            return accuracy
        else:
            y_pred = self.model.predict(self.X_test)
            mse = mean_squared_error(self.y_test, y_pred)
            print("Mean Squared Error:", mse)
            return mse

    def predict(self, X_new: Union[list, np.ndarray]) -> Union[list, np.ndarray]:
        X_new = np.array(X_new)
        return self.model.predict(X_new)

    def _get_polynomial_model(self) -> LinearRegression:
        poly_features = PolynomialFeatures(degree=2)
        X_poly = poly_features.fit_transform(self.X_train)
        model = LinearRegression()
        model.fit(X_poly, self.y_train)
        return model

import torch
import torch.nn as nn
import torch.optim as optim

class LossFunction(Enum):
    MSE_LOSS = nn.MSELoss()
    L1_LOSS = nn.L1Loss()
    HUBER_LOSS = nn.SmoothL1Loss()

class OptimizerType(Enum):pass

class DeepLM(Module):

    """
    Example Usage 
    ---------------
    this Module for easy build model
    """

    """
    
    # Import necessary libraries
    
    import numpy as np
    import torch.nn as nn

    # Örnek veri oluşturma
    X_train = np.random.rand(100, 2)
    y_train = np.random.rand(100, 1)

    # DeepLM modelinin oluşturulması
    model = DeepLM(name='my_model', input_size=2, output_size=1)
    model.add_hidden_layer(size=64, activation=nn.ReLU())
    model.add_hidden_layer(size=32, activation=nn.ReLU())
    model.build_model()

    # Modelin eğitilmesi
    model.train_model(X_train, y_train)

    # Modelin kaydedilmesi
    model.save_model("my_model.pth")

    # Kaydedilen modelin yüklenmesi
    loaded_model = DeepLM(name='loaded_model', input_size=2, output_size=1)
    loaded_model.load_model("my_model.pth")

    # Test verisi oluşturma
    X_test = np.random.rand(10, 2)

    # Modelin test edilmesi
    predictions = loaded_model.predict(X_test)
    print("Predictions:", predictions)

    """

    def __init__(self, name: str, input_size: int, output_size: int, loss_function: LossFunction = LossFunction.MSE_LOSS,
                 num_epochs: int = 10, learning_rate: float = 0.001) -> None:
        super().__init__(name)
        self.name = name
        self.input_size = input_size
        self.output_size = output_size
        self.loss_function = loss_function.value
        self.num_epochs = num_epochs
        self.learning_rate = learning_rate
        self.model = None
        self.hidden_layers = []
        self.activations = []

    def add_hidden_layer(self, size: int, activation: nn.Module) -> None:
        self.hidden_layers.append(size)
        self.activations.append(activation)

    def build_model(self) -> None:
        layers = []
        input_size = self.input_size
        for i, (hidden_size, activation) in enumerate(zip(self.hidden_layers, self.activations)):
            layers.append(nn.Linear(input_size, hidden_size))
            layers.append(activation)
            input_size = hidden_size

        layers.append(nn.Linear(input_size, self.output_size))
        self.model = nn.Sequential(*layers)

    def train_model(self, X_train: np.ndarray, y_train: np.ndarray, optimize:optim=optim.Adam) -> None:
        X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
        y_train_tensor = torch.tensor(y_train, dtype=torch.float32)

        optimizer = optimize(self.model.parameters(), lr=self.learning_rate)

        for epoch in range(self.num_epochs):
            optimizer.zero_grad()
            outputs = self.model(X_train_tensor)
            loss = self.loss_function(outputs, y_train_tensor)
            loss.backward()
            optimizer.step()

            if (epoch+1) % 10 == 0:
                print(f'Epoch [{epoch+1}/{self.num_epochs}], Loss: {loss.item():.4f}')

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
        with torch.no_grad():
            predictions = self.model(X_test_tensor)
        return predictions.numpy()

    def compute_gradients(self, X_train: np.ndarray, y_train: np.ndarray) -> None:
        X_train_tensor = torch.tensor(X_train, dtype=torch.float32, requires_grad=True)
        y_train_tensor = torch.tensor(y_train, dtype=torch.float32)

        optimizer = optim.Adam(self.model.parameters(), lr=self.learning_rate)

        for epoch in range(self.num_epochs):
            optimizer.zero_grad()
            outputs = self.model(X_train_tensor)
            loss = self.loss_function(outputs, y_train_tensor)
            loss.backward()

            # Access gradients
            gradients = X_train_tensor.grad
            print(f'Epoch [{epoch+1}/{self.num_epochs}], Gradients: {gradients}')

            optimizer.step()           

__all__ = ["Module",
           "WebM",
           "AutomationM",
           "MachineLM",
           "DeepLM",
           "LossFunction",
           "Gethub",
           "Decker",
           "GEHUB"]
