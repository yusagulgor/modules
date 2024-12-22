from abc import abstractmethod
from enum import StrEnum
from typing import Protocol, final
from flask import Flask, jsonify
from .module import Module


class Colors(StrEnum):
    RED = "red"
    BLACK = "black"
    BLUE = "blue"
    GREEN = "green"
    YELLOW = "yellow"
    WHITE = "white"
    GRAY = "gray"

class RCards(StrEnum):
    PERSONAL = "Personal"
    STATE = "State"
    CUSTOM = "Custom"  

class TextT(StrEnum):
    PARAGRAPH = "p"
    TITLE = "h3"
    LINK = "a"     

class HE(Protocol):
    def __init__(self) -> None:pass
    @abstractmethod
    def to_dict(self):pass

class Text(HE):
    def __init__(self, type: TextT, color: Colors, text: str) -> None:
        super().__init__()
        self._color = color
        self._text = text
        self._type = type

    def get_color(self): 
        return self._color
    
    def get_text(self): 
        return self._text
    
    def get_text_type(self): 
        return self._type

    def to_dict(self):
        return {
            "type": self._type,
            "color": self._color,
            "text": self._text
        }

class Card(HE):
    def __init__(self, type: RCards, wh: list[int] = [0, 0], border_radius: int = 0, bgColor: Colors = Colors.WHITE, texts: list[Text] = []) -> None:
        super().__init__()
        self.type = type
        self.texts = texts
        self.br = border_radius
        self.wh = wh
        self.bgColor: Colors = bgColor

        if len(self.wh) != 2:
            raise ValueError("Width and height must be provided as a list of two integers.")

    def to_dict(self):
        if not all(isinstance(text, Text) for text in self.texts):
            raise TypeError("All elements in texts must be instances of Text.")
        
        return {
            "type": self.type,
            "wh": self.wh,
            "border_radius": self.br,
            "bgColor": self.bgColor.value,
            "texts": [text.to_dict() for text in self.texts]
        }



class Navbar(HE):
    def __init__(self, bgColor: Colors, links: list[Text]) -> None:
        super().__init__()
        self.bgColor = bgColor
        self.links = links

    def to_dict(self):
        return {
            "bgColor": self.bgColor.value,
            "links": [link.to_dict() for link in self.links]
        }

class Footer(HE):
    def __init__(self, bg_color: Colors, text: Text) -> None:
        super().__init__()
        self.bg_color = bg_color
        if text.get_text_type() != TextT.PARAGRAPH:
            raise ValueError("Footer text must be a paragraph.")
        self.text = text

    def to_dict(self):
        return {
            "bgColor": self.bg_color.value, 
            "text": self.text.to_dict()       
        }

class Page(HE):
    def __init__(self, name: str, elements: list[HE]) -> None:
        super().__init__()
        self.name = name
        self.elements = elements

    def to_dict(self):
        return {
            "name": self.name,
            "elements": [element.to_dict() for element in self.elements]
        }

import subprocess
import time
import os

@final
class WD(Module):
    def __init__(self, name: str, navbar: Navbar, footer: Footer, pages: list[Page]) -> None:
        super().__init__(name)
        self.name = name
        self.navbar = navbar
        self.footer = footer
        self.pages = pages
        self.app = Flask(__name__)

        if len(self.pages) == 0:
            raise ValueError("Pages list cannot be empty.")

    def run(self, createHTML: bool = False, name: str = "pyHtml"):
        if not createHTML:

            @self.app.route('/api/apy', methods=['GET'])
            def get_data():
                data = {
                    "navbar": self.navbar.to_dict(),
                    "footer": self.footer.to_dict(),
                    "pages": [page.to_dict() for page in self.pages]
                }
                return jsonify(data)

            import os,subprocess
            ts_command = ["npx", "ts-node", "mwsite.ts"]

            current_dir = os.path.dirname(os.path.abspath(__file__))
            ts_file_path = os.path.join(current_dir, "mwsite.ts")

            if not os.path.exists(ts_file_path):
                raise FileNotFoundError(f"'web.ts' dosyası bulunamadı: {ts_file_path}")
        
            print(f"Running TypeScript file: {ts_file_path}")
            subprocess.Popen(ts_command, cwd=current_dir, shell=True)    
            self.app.run(host="127.0.0.1", port=8000,debug=True)
        else:
            nam = "pyHtml" if name == "pyHtml" else name
            with open(f"{nam}.html", "w") as f:
                pages_html = "".join([repr(page) for page in self.pages])
                f.write(f"{repr(self.navbar)}{pages_html}{repr(self.footer)}")


__all__ = ["RCards", 
           "Text", 
           "TextT", 
           "Card", 
           "Colors", 
           "Page", 
           "Navbar", 
           "Footer", 
           "WD"]
