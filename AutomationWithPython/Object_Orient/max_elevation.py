class City:
    name = ""
    country = ""
    elevation = 0
    population = 0

city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

city3 = City()
city3.name = "Seoul"
city3.country = "Korea"
city3.elevation = "38"
city3.population = 9733509

def max_elevation_city(min_population):
    return_city = City()
    if city1.population > min_population:
        return_city = city1
    elif city2.population > min_population:
        return_city = city2
    elif city3.population > min_population:
        return_city = city3

    if return_city.name:
        return return_city.name + ", " + return_city.country
    else:
        return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print "" 
