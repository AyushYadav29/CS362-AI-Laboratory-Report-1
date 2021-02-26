import numpy
import random
import math


class City:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

def pathCost (route):
    for i in range(len(route)):
        # Distnace between very city
        if i >= len(route)-1:
            break
        else:
            dist = numpy.sqrt(((route[i].x - route[i+1].x) ** 2) + ((route[i].y - route[i+1].y) ** 2))
            distance =+ dist
    
    # Distance between first and last city
    distance =+ numpy.sqrt(((route[0].x - route[-1].x) ** 2) + ((route[0].y - route[-1].y) ** 2))
    return distance

# List of cities

cities = list()

CityPalace = City(25.702503034283787, 73.58152248534205, "City Palace")
cities.append(CityPalace)

AmberPalace = City(27.665607356096267, 76.13035074255151, "Amber Palace")
cities.append(AmberPalace)

HawaMahal = City(27.89888431960082, 75.07566318784414, "Hawa Mahal")
cities.append(HawaMahal)

ChittorgarhFort = City(26.49179507068974, 74.28464752181362, "Chittorgarh Fort")
cities.append(ChittorgarhFort)

CityPalace = City(28.980831485721392, 76.04246011299257, "City Palace Jaipur")
cities.append(CityPalace)

KumbhalgarhFort = City(27.19755931967608, 73.58152248534205, "Kumbhalgarh Fort")
cities.append(KumbhalgarhFort)

RanthamboreNationalPark = City(27.821180947322215, 76.21824137211046, "Ranthambore National Park")
cities.append(RanthamboreNationalPark)

BhangarhFort = City(29.287913803748992, 76.13035074255151, "Bhangarh Fort")
cities.append(BhangarhFort)

SariskaTigerReserve = City(28.90391780739106, 77.09714766769993, "Sariska Tiger Reserve")
cities.append(SariskaTigerReserve)

TheTharHeritageMuseum = City(29.134487314536173, 70.24167856210207, "The Thar Heritage Museum")
cities.append(TheTharHeritageMuseum)

JalMahal = City(28.74991940396533, 76.04246011299257, "Jal Mahal")
cities.append(JalMahal)

DilwaraTemples = City(25.860786617456906, 72.43894430107575, "Dilwara Temples")
cities.append(DilwaraTemples)

JaswantThada = City(27.74342192499812, 73.22995996710627, "Jaswant Thada")
cities.append(JaswantThada)

RanthamboreFort = City(27.197559319676053, 76.39402263122835, "Ranthambore Fort")
cities.append(RanthamboreFort)

JaigarhFort = City(28.59569358526302, 76.56980389034625, "Jaigarh Fort")
cities.append(JaigarhFort)

AlbertHallMuseum = City(26.911833790980342, 75.8194553111577, "Albert Hall Museum")
cities.append(AlbertHallMuseum)

BirlaTemple = City(26.89245423532142, 75.81553157254318, "Birla Temple Jaipur")
cities.append(BirlaTemple)

JantarMantar = City(26.924991563302612, 75.82452781115796, "Jantar Mantar - Jaipur")
cities.append(JantarMantar)

SajjangarhMonsoonPalace = City(24.59349746222666, 73.63965924180238, "Sajjangarh Monsoon Palace")
cities.append(SajjangarhMonsoonPalace)

MaharanaPratapMemorial  = City(24.5976062757075, 73.67966285529258, "Maharana Pratap Memorial ")
cities.append(MaharanaPratapMemorial )

# Initializing a random path
path = random.sample(cities, len(cities))
distance = pathCost(path)

print('INITIAL ROUTE:')
for i in range(len(path)):
    print(path[i].name, end=" -> ")
print((path[0]).name)       
# Initial temperature
Temp = 1000
Max_Iteration = 1000

for i in range(1, Max_Iteration):
    
    r = random.sample(cities, len(cities))

    city1 = path.index(r[0])
    city2 = path.index(r[1])

    newRoute = path
    newRoute[city1] = r[1]
    newRoute[city2] = r[0]

    newDistance = pathCost(newRoute)

    # Difference in old path cost and new path cost

    diff = distance - newDistance
    T = Temp/i

    pE = 1/(1 + math.exp(-diff/T))

    if diff > 0:
        path = newRoute
    else:
        rand = random.uniform(0,1)

        if rand < pE:
            path = newRoute 

    Final_Distance = pathCost(path)
    Distance_Matrix = [distance, Final_Distance]
    Probability = pE


print("\n \nFINAL ROUTE:")
for i in range(len(path)):
    print(path[i].name, end=" -> ")
print((path[0]).name)    

print('\n\nINITIAL TOTAL DISTANCE, FINAL TOTAL DISTANCE:')  
print(Distance_Matrix)
