"""
(Yüşa Gülgör)


"""
import os
from typing import Any, Dict , Callable, Final, List, Protocol, final
import numpy as np
import matplotlib.pyplot as plt

# * Base Modules
@final
class Module(Protocol):
    """
    Base Model
    ------------

    Ana mimariyi oluşturmak için kullanılır.
    """
    def __init__(self,name:str) -> None:
        self.name :str = name

    def __repr__(self) -> str:
        return "model name :" + self.name    

    def __init_subclass__(cls, **kwargs):
        _allowed_subclasses = {"Gethub", "Decker","GEHUB","WebM","GraphPlotter","AutomationM","WD","RWebDev","ReadyWebs"}
        if cls.__name__ not in _allowed_subclasses:
            raise TypeError(f"{cls.__name__} sınıfı, AllowedBase sınıfını miras alamaz.")
        super().__init_subclass__(**kwargs)    

# * Gehub Modules  

import os
import subprocess

# I will update with rust for the speed.

@final
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

@final
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

@final
class GEHUB(Module):
    def __init__(self, github: Gethub=None, docker: Decker=None) -> None:
        super().__init__("Gehub")
        self.gh = github
        self.dk = docker

    def pushRepo(self):
        """Pushes the repo with Docker build check."""
        try:
            if not self.dk.GetDW():
                print("Git reposu başlatılıyor...")
                self.gh.initialize_git_repo()
            else:
                print("Docker görüntüsü oluşturuluyor...")
                self.dk.build_image()
                self.gh.initialize_git_repo()
            print("Git işlemleri tamamlandı.")
        except Exception as e:
            print(f"GEHUB işlemi sırasında hata: {e}")

    @staticmethod
    def fcodef(name: str):
        """Generates a Python file with basic GitHub and Docker setup."""
        content = (
            "from modules import *\n\n"
            "name = ''\n"
            "projePath = r'C:\\example\\...' \n"
            "repoPath = 'https://github.com/userName/example.git'\n"
            "branchName = ''\n"
            "commitMessage = 'first commit'\n"
            "readmeText = ''\n\n"
            "git = Gethub(name, projePath, repoPath, branchName, commitMessage, ReMDMessage=readmeText)\n"
            "doc = Decker(False)\n"
            "ghub = GEHUB(git, doc)\n"
            "ghub.pushRepo()\n"
        )
        try:
            with open(f"{name}.py", 'w') as f:
                f.write(content)
            print(f"{name}.py dosyası başarıyla oluşturuldu.")
        except Exception as e:
            print(f"{name}.py dosyası oluşturulurken hata: {e}")
 
# * Var type/variable

# specUint = [
#     ("value",uint32)
# ]

# @jitclass(specUint)
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

# specBin = [
#     ('value',byte)
# ]

# @jitclass(specBin)
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

    Ex Usage:
    >>> name = Var(str,"Yüşa",False)()
    eğer değerin sonuna "()" koymazsanız değer kendi türünde olmaz
    or you should use like this
    >>> name = Var(str,"Yüşa",False).getValue
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

    @property
    def getValue(self):
        return self.variable

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
    
Var.addType(UInt)    
Var.addType(Bin)    
    
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
    >>> class Constant(Const):pass
    >>>     NAME = "Yusa"
    Final yani değiştirilemeyen değer NAME

    """
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        raise TypeError("cant changable ")


# * Web Modules

from flask import Flask, render_template

@final
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


# specPoint = [
#     ('x', float32),
#     ('y', float32)
# ]

# @jitclass(specPoint)
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __call__(self):
        return self.x, self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    
# Var.addType(Point)    

class VectorOperations:
    @staticmethod
    def add(v1: Point, v2: Point) -> Point:
        """İki vektörün bileşenlerinin toplamını alarak yeni bir vektör döndürür."""
        return Point(v1.x + v2.x, v1.y + v2.y)

    @staticmethod
    def scalar_multiply(v: Point, scalar: float) -> Point:
        """Bir vektörü bir skalerle çarpar."""
        return Point(v.x * scalar, v.y * scalar)

    @staticmethod
    def dot_product(v1: Point, v2: Point) -> float:
        """İki vektörün iç çarpımını hesaplar."""
        return v1.x * v2.x + v1.y * v2.y

@final
class GraphPlotter(Module):
    """
    For the 2/3D graph
    """

    def __init__(self):
        super().__init__("GraphPlotter")
        self.vector_ops : Final[VectorOperations] = VectorOperations()
    
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
    
    def plot_vector(self, point1: Point, point2: Point):
        """Verilen iki nokta arasındaki vektörü çizen fonksiyon."""
        # Başlangıç ve bitiş noktalarını al
        x_values = [point1.x, point2.x]
        y_values = [point1.y, point2.y]

        # Grafik oluştur
        plt.figure()
        plt.quiver(point1.x, point1.y, point2.x - point1.x, point2.y - point1.y, angles='xy', scale_units='xy', scale=1, color="r")
        plt.xlim(min(x_values) - 1, max(x_values) + 1)
        plt.ylim(min(y_values) - 1, max(y_values) + 1)
        plt.title("Vektör Grafiği")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()
    
    def vector_addition(self, point1: Point, point2: Point):
        """İki vektörün toplanmasını ve sonucunun görselleştirilmesini sağlar."""
        result = self.vector_ops.add(point1, point2)
        print(f"Vektörlerin toplamı: {result}")
        self.plot_vector(point1, point2)
        self.plot_vector(Point(0, 0), result)
    
    def scalar_multiplication(self, point: Point, scalar: float):
        """Bir vektörü skalerle çarpar ve sonucunu görselleştirir."""
        result = self.vector_ops.scalar_multiply(point, scalar)
        print(f"Vektörün {scalar} ile çarpımı: {result}")
        self.plot_vector(Point(0, 0), result)
    
    def dot_product(self, point1: Point, point2: Point):
        """İki vektörün iç çarpımını hesaplar ve sonucu yazdırır."""
        result = self.vector_ops.dot_product(point1, point2)
        print(f"Vektörlerin iç çarpımı: {result}")


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


__all__ = ["Module",
           "WebM",
           "AutomationM",
           "Gethub",
           "Decker",
           "GEHUB",
           "Bin",
           "UInt",
           "Var",
           "Const",
           "GraphPlotter",
           "Point"]
