from dataclasses import dataclass

@dataclass
class Movie:
    name:str = ""
    year:int= 0
    
    def __init__(self, name, year):
        self.name = name
        self.year = year

    
    def getStr(self):
        return f"{self.name} ({self.year})"
   