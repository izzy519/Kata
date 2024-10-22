def rental_car_cost(d):
    rental_car_cost = 40 * d
    if d >= 7:
        return rental_car_cost - 50
    elif d >= 3 and d <7:
        return rental_car_cost - 20
    else: 
        return rental_car_cost