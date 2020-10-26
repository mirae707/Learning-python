def car_listing(car_prices):
    result = ""
    for car in car_prices.keys():
        price = car_prices[car]
        result += "{} costs {} dollars".format(car, price) + "\n"
    return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
