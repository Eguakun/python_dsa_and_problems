# first method: go through all cities and check if they work as a valid city
# brute force approach

# the city that has the least amonut of gas once weve iterated through is the city that we need to start from.

# time complexity O(n) since we aloways look at all of the cities., n is the number of cities
# space complexity: O(1)


#brute force implementation

def validStartingCity(distances, fuel, mpg):
    numberOfCities = len(distances)

    for startCityIdx in range(numberOfCities):
        milesRemaining = 0

        for currentCityIdx in range(startCityIdx, startCityIdx + numberOfCities):
            if milesRemaining < 0: # first make sure we have enough gas to reach this city
                continue
            currentCityIdx = currentCityIdx % numberOfCities # update current city index and we use modulus to be able to cycle through the array
            fuelFromCurrentCity = fuel[currentCityIdx]
            distanceToNextCity = distances[currentCityIdx]
            milesRemaining += fuelFromCurrentCity * mpg - distanceToNextCity # update miles remainign based on fuel from current city and distance to next city

        if milesRemaining >= 0:
            return startCityIdx
    return -1
