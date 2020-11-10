from amadeus import Client, ResponseError
from keys import cid, secret
import pandas as pd
import datetime
datetime.datetime.strptime
pd.options.display.max_columns= None
pd.options.display.max_rows= None


amadeus = Client(
    client_id=cid,
    client_secret=secret
)


def getFlightsFromAmadeus(origin, destination):
    try:
        flights = amadeus.shopping.flight_dates.get(origin=origin, destination=destination)
        df = pd.DataFrame(flights.data)
        formatColumnPrices(df)
        deleteColumnFromDataType(['links'], df)
        sortValues(df, 'price', True)
        print("\n\n\n")
        print("El precio medio de viajar desde " + origin + " a " + destination + " es de: " + str(getMeanColumn(df, 'price')) + " Euros para las próximas fechas.")
        print("\n\n\n")
        return df.head(10)
    except ResponseError as error:
        print(error)

def formatColumnPrices(df):
    df['price'] = df['price'].astype(str)
    df['price'] = df['price'].str.replace("{'total': '",'').str.replace("'}",'')
    df['price'] = pd.to_numeric(df['price'],errors='coerce')
    return df['price'].astype(float)

def deleteColumnFromDataType(listNameColumn, df):
    return df.drop(listNameColumn, axis = 'columns', inplace=True)

def sortValues(df, column, ascending):
    df.sort_values(by=column, ascending=ascending)

def getMeanColumn(df, nameColumn):
    return df[nameColumn].mean()
    
