from getFlightsFromApi import getFlightsFromAmadeus
from getInfoFromDataset import getHotelsFromDataSet

def enterOrigin():
    origin = str(input("Introduce la tres primeras letras de la ciudad de origen: "))
    try :   
        if len(origin) == 3:
            return origin.upper()
    except ValueError:
        pass
    print("Introduce la tres primeras letras de la ciudad de origen:  ")

def enterDestination():
    origin = str(input("Introduce la tres primeras letras de la ciudad de destino: "))
    try :   
        if len(origin) == 3:
            return origin.upper()
    except ValueError:
        pass
    print("Introduce la tres primeras letras de la ciudad de destino: ")   



def main():
    print("Consulta conmigo tu próximo viaje \n")
    origin = enterOrigin()
    destination =enterDestination() 
    print(getFlightsFromAmadeus (origin, destination))
    print(getFlightsFromAmadeus (destination, origin))
    print("\n")
    while input("¿Quieres información sobre los mejores hoteles? (S/N) ").upper() == "S":
        country = str(input("Introduce el pais: "))
        print(getHotelsFromDataSet(country))


if __name__ == "__main__":
    main()