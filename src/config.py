import os
from dotenv import load_dotenv

class Config:
    def __init__(self) -> None:
        self.__api_key = None
        self.__llm = None
        self.__initialize()

    @property
    def api_key(self):
        return self.__api_key
    
    @property
    def llm(self):
        return self.__llm

    def __initialize(self):
        dirname = os.path.dirname(__file__)
        try:
            load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
        except FileNotFoundError:
            print("file not found")
        self.__api_key = os.getenv("API_KEY")
        self.__llm = os.getenv("LLM")