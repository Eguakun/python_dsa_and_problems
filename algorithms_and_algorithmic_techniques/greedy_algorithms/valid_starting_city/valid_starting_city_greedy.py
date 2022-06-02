
def validStartingCity(distances, fuel, mpg):
    numberOfCities = len(distances) # define variables
    milesRemaining = 0

    indexOfStartingCityCandidate = 0 # keep track of city we are currently considering to be starting city
    milesRemainingAtStartingCityCandidate = 0

    for cityIdx in range(1, numberOfCities): # loop through
        distanceFromPreviousCity = distances[cityIdx - 1]
        fuelFromPreviousCity = fuel[cityIdx - 1]
        milesRemaining += fuelFromPreviousCity * mpg - distanceFromPreviousCity

        if milesRemaining < milesRemainingAtStartingCityCandidate: # if we find a city with less gas, we update the varibales
            milesRemainingAtStartingCityCandidate = milesRemaining
            indexOfStartingCityCandidate = cityIdx

    return indexOfStartingCityCandidate # if we find a city with minimum number of gas, return that
