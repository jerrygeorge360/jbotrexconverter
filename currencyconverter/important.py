from currencyconverter import myfunc
from flask import requeste

class CurrencyLibrary:

    def __init__(self, inherit):
        self.app = inherit
        self.app.jinja_env.globals.update(clever_function=myfunc.api)

