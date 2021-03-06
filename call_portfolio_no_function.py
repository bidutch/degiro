import json
import pandas as pd
import degiroapi
from degiroapi.product import Product
from degiroapi.order import Order
from degiroapi.utils import pretty_json

with open('c:\git\degiro\config.json','r') as file:
    data = json.load(file)
    user = data['degiro_user']
    password  = data['degiro_password']

degiro = degiroapi.DeGiro()
degiro.login(user, password)
portfolio = pd.DataFrame(degiro.getdata(degiroapi.Data.Type.PORTFOLIO, False))

tickerinfo = portfolio.apply(lambda row : degiro.product_info(row['id']), axis = 1, result_type = 'expand')

portfolio[tickerinfo.columns] = tickerinfo

del(tickerinfo)

degiro.logout()