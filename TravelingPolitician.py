import pandas as pd
distnace_df = ;\
#dataframe with the distances between each city
#convert it into an adjaceny map with distance
#  // data ty<ap =_am 0;[]u   
cityMap = {

    "citya": [0, 1, 4, 5],
    "cityb": [1, 0, 6, 2],
    "cityc": [4, 6, 0, 7],
    "cityd": [5, 2, 7, 0]
}
def nearestCityHeuristic(city, dist):
    cityIndex = city.index(min(city))
    return min(city) + nearestCityHeuristic(city, dist)
        
def nearestCity(graph):
    dist = 0
    for city in graph:
        nearestCityHeuristic(cityMap[city], dist)

            #= distfor distance ;in city:cNeighborityMap[city]city cityMap./ [key](tfor dist in o;:graph city cityMapdist = 0
def travelingSalesman():

def main:

    
