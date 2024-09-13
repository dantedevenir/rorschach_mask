import logging

class Minute:
    
    def __init__(self) -> None:
        self.logging = logging
        self.logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        
    def register(self, text) -> None:
        self.logging.info(text)

minute = Minute()

class Instropetion:
    
    def __init__(self) -> None:
        self.logging = logging
        self.logging.basicConfig(
            level=logging.ERROR,
            format="%(asctime)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        
    def register(self, text) -> None:
        self.logging.error(text)

instropetion = Instropetion()