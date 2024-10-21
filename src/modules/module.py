"""
(Yüşa Gülgör)
2024y05m01d


"""
from abc import ABC
import os
from typing import Any, Dict, Union , Callable, List
from enum import Enum
import numpy as np
import matplotlib.pyplot as plt


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

import os
import subprocess

class Gethub(Module):
    """
    # Usage
    Please click on the class and read the doc.

    pPath must be like this: "x:\\examples\\..." The important thing here is to double \
    backslashes.

    rPath: GitHub repository URL.

    your_branchName: Git branch name.

    commitMessage: First commit message.

    dwReMD: Indicates whether to create README.md.

    ReMDMessage: Content of README.md.
    """

    def __init__(self, pName: str, pPath: str, rPath: str, your_branchName: str, 
                 commitMessage: str, dwReMD: bool = False, ReMDMessage: str = None) -> None:
        super().__init__("Gethub")
        self.pName = pName
        self.pPath = pPath
        self.rPath = rPath
        self.y_bN = your_branchName
        self.cm = commitMessage
        self.dwMD = dwReMD
        self.mdMessage = ReMDMessage or self._default_readme()

    def _default_readme(self):
        return f"# {self.pName} project\n\nHello to my {self.pName}\n"

    def addRM(self):
        if self.dwMD:
            try:
                with open(os.path.join(self.pPath, 'README.md'), 'w') as f:
                    f.write(self.mdMessage)
            except Exception as e:
                print(f"README.md oluşturulurken hata: {e}")

    def initialize_git_repo(self):
        try:
            os.makedirs(self.pPath, exist_ok=True)
            subprocess.run(f"git init {self.pPath}", check=True)
            self.addRM()
            subprocess.run(f"git -C {self.pPath} add .", check=True)
            subprocess.run(f'git -C {self.pPath} commit -m "{self.cm}"', check=True)
            subprocess.run(f"git -C {self.pPath} branch -M {self.y_bN}", check=True)
            subprocess.run(f"git -C {self.pPath} remote add origin {self.rPath}", check=True)
            subprocess.run(f"git -C {self.pPath} push -u origin {self.y_bN}", check=True)
        except subprocess.CalledProcessError as e:
            print(f"Git işlemi başarısız oldu: {e}")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

# -----------------------------------------------------------------------

class Decker(Module):
    def __init__(self, build: bool = False, image_name: str = "myapp:latest") -> None:
        super().__init__("Decker")
        self.build = build
        self.image_name = image_name

    def build_image(self):
        try:
            subprocess.run(f"docker build -t {self.image_name} .", check=True)
        except subprocess.CalledProcessError as e:
            print(f"Docker imajı oluşturulurken hata: {e}")

    def GetDW(self):
        return self.build

# -----------------------------------------------------------------------    

class GEHUB(Module):
    def __init__(self, github: Gethub, docker: Decker) -> None:
        super().__init__("Gehub")
        self.gh = github
        self.dk = docker

    def pushRepo(self):
        try:
            if not self.dk.GetDW():
                self.gh.initialize_git_repo()
            else:
                self.dk.build_image()
                self.gh.initialize_git_repo()
            print("Git işlemleri tamamlandı.")
        except Exception as e:
            print(f"GEHUB işlemi sırasında hata: {e}")

    @staticmethod
    def fcodef(name: str):
        try:
            with open(name + ".py", 'w') as f:
                f.write("from modules import *\n\n")
                f.write("name = ''\n")
                f.write("projePath = 'C:\\example\\...'\n")
                f.write("repoPath = 'https://github.com/userName/example.git'\n")
                f.write("branchName = ''\n")
                f.write("commitMessage = 'first commit'\n")
                f.write("readmeText = ''\n\n")
                f.write("git = Gethub(name, projePath, repoPath, branchName, commitMessage, ReMDMessage=readmeText)\n")
                f.write("doc = Decker(False)\n")
                f.write("ghub = GEHUB(git, doc)\n")
                f.write("ghub.pushRepo()\n")
        except Exception as e:
            print(f"{name}.py dosyası oluşturulurken hata: {e}")

# * Var type/variable
 
class UInt:
    def __init__(self, value: int):
        if value < 0:
            raise TypeError("value must be greater than or equal to 0")
        else:
            self.value = value

    def __call__(self):
        return self.value

    def __repr__(self):
        return str(self.value)  

    def __str__(self):
        return str(self.value)  

    def is_valid(self):
        return self.value is not None

    def __add__(self, other):
        if isinstance(other, UInt) and self.is_valid() and other.is_valid():
            return UInt(self.value + other.value)
        return UInt(-1)  

    def __sub__(self, other):
        if isinstance(other, UInt) and self.is_valid() and other.is_valid():
            if self.value < other.value:
                return UInt(-1)  
            return UInt(self.value - other.value)
        return UInt(-1) 

    def __mul__(self, other):
        if isinstance(other, UInt) and self.is_valid() and other.is_valid():
            return UInt(self.value * other.value)
        return UInt(-1)  

    def __truediv__(self, other):
        if isinstance(other, UInt) and self.is_valid() and other.is_valid():
            if other.value == 0:
                return UInt(-1)  
            return UInt(self.value // other.value)
        return UInt(-1)    
    
    def __eq__(self, other):
        return self.value == other  

    def __gt__(self, other):
        return self.value > other

    def __lt__(self, other):
        return self.value < other

    def __ge__(self, other):
        return self.value >= other

    def __le__(self, other):
        return self.value <= other

class Bin:
    def __init__(self, value: int):
        if value not in (0, 1):
            raise TypeError("value must be 0 or 1")
        else:
            self.value = value

    def __call__(self):
        return self.value

    def __repr__(self):
        return str(self.value)  

    def __str__(self):
        return str(self.value)  

    def is_valid(self):
        return self.value is not None

    def __and__(self, other):
        if isinstance(other, Bin) and self.is_valid() and other.is_valid():
            return Bin(self.value & other.value)
        return Bin(-1)  

    def __or__(self, other):
        if isinstance(other, Bin) and self.is_valid() and other.is_valid():
            return Bin(self.value | other.value)
        return Bin(-1)  

    def __xor__(self, other):
        if isinstance(other, Bin) and self.is_valid() and other.is_valid():
            return Bin(self.value ^ other.value)
        return Bin(-1) 

    def __invert__(self):
        if self.is_valid():
            return Bin(1 - self.value)  
        return Bin(-1)    
    
    def __eq__(self, other):
        return self.value == other

    def __gt__(self, other):
        return self.value > other

    def __lt__(self, other):
        return self.value < other

    def __ge__(self, other):
        return self.value >= other

    def __le__(self, other):
        return self.value <= other


class Var:
    
    """
    
    @params: 
    var_type : değişken türü,
    variable: değer,
    chabgable:final ya da değil(standart değil)

    """
    ALLOWED_TYPES = [bool, int, str, float]
    
    def __init__(self, var_type: Any, variable: Any, changable: bool = True):
        object.__setattr__(self, 'changable', changable)
        
        if var_type in self.ALLOWED_TYPES:
            object.__setattr__(self, 'type', var_type)
        else:
            raise TypeError(f"Geçersiz tür: {var_type}. İzin verilen türler: {self.ALLOWED_TYPES}")
        
        if isinstance(variable, var_type):
            object.__setattr__(self, 'variable', variable)
        else:
            raise ValueError(f"Değer, belirtilen türle eşleşmiyor: {variable}")

    def __call__(self):
        return self.variable

    def __repr__(self):
        return str(self.variable)

    def __str__(self):
        return str(self.variable)

    @property
    def type_of_var(self):
        return self.type

    # @property
    # def value(self):
    #     return self.variable

    # @value.setter
    # def value(self, key):
    #     if self.changable and isinstance(key, self.type_of_var):
    #         self.variable = key
    #     else:
    #         if not self.changable:
    #             raise TypeError("Değiştirilemez.")
    #         else:
    #             raise TypeError(f"Değerin türü {self.type_of_var} olmalıdır, ama {type(key)} verildi.")

    def __setattr__(self, key, value):
        if key == "variable":
            if not isinstance(value, self.type_of_var):
                raise TypeError(f"{key} değişkeni {self.type_of_var} türünde olmalıdır.")
        
        if key != 'changable' and not self.changable:
            raise TypeError(f"{key} değiştirilemez.")
        else:
            super().__setattr__(key, value)

    @classmethod
    def addType(cls, type):
        tuplesT = ('__eq__', '__gt__', '__lt__', '__ge__', '__le__', '__call__')
        if type not in cls.ALLOWED_TYPES and hasattr(type, '__call__'):
            for method in tuplesT:
                if not hasattr(type, method) or getattr(type, method).__qualname__.split('.')[0] != type.__name__:
                    raise TypeError(f"{type.__name__} sınıfında {method} metodu bulunmalı.")
            cls.ALLOWED_TYPES.append(type)
            print(f"{type.__name__} başarıyla listeye eklendi.")
        else:
            print(f"{type.__name__} zaten listede var ya da gerekli metodlar eksik. Mevcut tipler: {cls.ALLOWED_TYPES}")

    def __eq__(self, other):
        if isinstance(other, Var):
            return self.variable == other.variable
        return self.variable == other

    def __gt__(self, other):
        return self.variable > other

    def __lt__(self, other):
        return self.variable < other

    def __ge__(self, other):
        return self.variable >= other

    def __le__(self, other):
        return self.variable <= other

    @classmethod
    def allTypes(cls):
        return cls.ALLOWED_TYPES
    
# * Constant helper 

class MetaConst(type):
    def __getattr__(cls, key):
        return cls[key]

    def __setattr__(cls, key, value):
        raise TypeError("cant changable ")

class Const(object,metaclass=MetaConst):
    """
    
    Const sınıf oluşturmak için

    Example:
    sınıf tanımı
    >>> class Constant(Const):
    >>>     NAME = "Yusa"
    Final yani değiştirilemeyen değer NAME

    """
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        raise TypeError("cant changable ")


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

# * Graphplotter

class GraphPlotter(Module):
    def __init__(self):
        super().__init__("Graphplotter")

    """
    For the 2/3D graph

    """
    
    def plot_2D(self, funcs: List[Callable[[int], float]]):
        """2D grafik için yalnızca 1 fonksiyon alınmalı."""
        if len(funcs) != 1:
            raise ValueError("2D grafik için yalnızca 1 fonksiyon gereklidir.")
        func = funcs[0]  
        x = np.linspace(-10, 10, 400)
        y = [func(i) for i in x]
        
        plt.figure()
        plt.plot(x, y, label=f"Fonksiyon: {func.__name__}")
        plt.title("2D Fonksiyon Grafiği")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.show()

    def plot_3D(self, funcs: List[Callable[[float, float], float]]):
        """3D grafik için 3 fonksiyon gereklidir."""
        if len(funcs) != 3:
            raise ValueError("3D grafik için 3 fonksiyon gereklidir.")
        
        f_x, f_y, f_z = funcs 

        u = np.linspace(-5, 5, 50)
        v = np.linspace(-5, 5, 50)
        u, v = np.meshgrid(u, v)
        
        x = f_x(u, v)
        y = f_y(u, v)
        z = f_z(u, v)
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x, y, z, cmap="viridis")
        ax.set_title("3D Fonksiyon Grafiği")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.show()


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
from sklearn.metrics import accuracy_score, mean_squared_error

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
           "GEHUB",
           "Bin",
           "UInt",
           "Var",
           "Const",
           "GraphPlotter"]
