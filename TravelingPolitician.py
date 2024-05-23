import pandas as pd
intMax = 100000
#distnace_df = ;\const
#dataframe with the distances between each city
#convert it into an adjaceny map with distance
#  // data ty<ap =_am 0;[]u 00 0 0 
cityMap = {

    0: [intMax, 1, 4, 5],
    1: [1, intMax, 6, 2],
    2: [4, 6, intMax, 7],
    3: [5, 2, 7, intMax]
}

visited = []
def nearestCityHeuristic(city, graph):
    
    graphKeyList = list(graph.keys())
    distanceList = list(graph.values()) 
    position = distanceList.index(city)
    
    visited.append(graphKeyList[position]) 
    if(len(graph) <= len(visited)):
        return city[0]
    minDistance = min([(city[i]) for i in range(len(city)) if i not in visited])
    print(minDistance)#routeDistance nextCity += minDistanceprint(visited)
      
    nextCity = graph[city.index(minDistance)] 
    
    return minDistance + nearestCityHeuristic(nextCity, cityMap)    
    


    
    
    #if(nextCity in visited):.
        #return 0#;if()porujb a //graph.index#Key(city) grouteDistance += nextCity[0]routeDistance = 0return routeDistance             while(len(visited) < len(graph)):visited.append(city) i, minDistance + nearestCityHeuristic(nextCity);min < M > cityMap/addcityMap* fpr  min(city)cityIndex = cityIndextcityTfor city in graph:, dist, dist
    
        
def nearestCity(graph, startingCity):
    
    dist = nearestCityHeuristic(graph[startingCity], graph)
    return dist

            #=     distdist = 0forcitycityMap distance"cityb""citya""c"ityc"cityd" ;in city:cNeighborityMap[city]city cityMap./ [key](tfor dist in o;:graph city cityMapdist = 0
#def travelingSalesman():dprint(nearestCity(cityMap, 0)), dist


def main():
    print(nearestCity(cityMap, 0))

if __name__ == "__main__":
    main()
    
