import math

def calculate_drones_and_cost(distance, operating_hours, speedInKmh):
    fixed_cost = 100
    cost_per_km = 0.01

    distance_covered_per_drone = speedInKmh * operating_hours
    num_drones = math.ceil(distance / distance_covered_per_drone)

    total_cost = num_drones * (fixed_cost + (distance_covered_per_drone * cost_per_km))

    return num_drones, total_cost

def calculate_costs_time(distance, typenb):
    distance = distance / 1000
    average_speed = [
        10,  # km/h
        20
        ]
    fixed_costs = [
        500,  # $/day
        800
        ]
    cost_per_km = [
        1.1,  # $/km
        1.3
        ]
    hourly_costs_8_hours = [
        1.1,  # $/h
        1.3
        ]
    hourly_costs_after_8_hours = [
        1.3,  # $/h
        1.5
        ]
    
    cost = cost_per_km[typenb] * distance
    time = distance / average_speed[typenb]
    if time <= 8:
        cost += hourly_costs_8_hours[typenb] * time + fixed_costs[typenb]
    elif time > 11:
        number = time
        while number > 0:
            cost += fixed_costs[typenb]
            if number >= 11:
                cost += hourly_costs_8_hours[typenb] * 8
                cost += hourly_costs_after_8_hours[typenb] * 3
                number -= 11
            elif number <= 8:
                cost += hourly_costs_8_hours[typenb] * number
                number = 0
            else:
                cost += hourly_costs_8_hours[typenb] * 8
                cost += hourly_costs_after_8_hours[typenb] * (number - 8)
                number = 0
    else:
        cost += hourly_costs_8_hours[typenb] * 8
        cost += hourly_costs_after_8_hours[typenb] * (time - 8) + fixed_costs[typenb]
    return (cost, time) 

def calculate_costs_snowplows(nb_typeI, nb_typeII, distance):
    cost, time = 0, 0
    div = nb_typeI + 2 * nb_typeII
    space_typeI = distance / div
    space_typeII = 2 * space_typeI
    
    c, t = calculate_costs_time(space_typeI, 0)
    cost += c * nb_typeI
    time = max(time, t)
    
    c, t = calculate_costs_time(space_typeII, 1)
    cost += c * nb_typeII
    time = max(time, t)
    
    return (cost, time)

def choose_snowplows_types(distance):
    distance = distance * 1000
    optimized_cost = 10000000
    optimized_time = 10000000
    optimized_typeI = 0
    optimized_typeII = 0
    
    for i in range(10):
        for j in range(10):
            if i == j and i == 0:
                continue # 0 of both types of snowplows is useless
            
            (cost, time) = calculate_costs_snowplows(i, j, distance)
            
            if cost < optimized_cost or (cost == optimized_cost and time < optimized_time):
                optimized_cost = cost
                optimized_time = time
                optimized_typeI = i
                optimized_typeII = j
    return (optimized_typeI, optimized_typeII, optimized_cost)

#DRONES CALCULATION
droneDistances=[44.5, 72.3, 181.68, 424.13, 134.29 ] #We got them from drone.py
def calculateDroneCosts(distances):
    operating_hours = 2
    speedInKmh = 8
    total_cost = 0
    for i in range(len(distances)): 
        num_drones, total_cost2 = calculate_drones_and_cost(distances[i], operating_hours, speedInKmh)
        print("To cover the distance of", distances[i], "km")
        print("The number of drones needed is:", num_drones)
        print("The drone cost is: $", total_cost2, "\n")
        total_cost += total_cost2
    print("The total drone cost is: $", total_cost, "\n")
    return total_cost

total_drone_cost = calculateDroneCosts(droneDistances)

#SNOWPLOWS CALCULATION
snowplowDistances=[89, 144.49, 362.79, 844.46, 268.42]
def calculateSnowplowCosts(distances):
    total_cost = 0
    for i in range(len(distances)):
        type1Count, type2Count, cost = choose_snowplows_types(distances[i])
        total_cost += cost
        print("To cover the distance of", distances[i], "km")
        print("The number of type1 snowplows is:", type1Count)
        print("The number of type2 snowplows is:", type2Count)
        print("The snowplow cost is: $", cost, "\n")
    print("The total snowplow cost is: $", total_cost, "\n")
    return total_cost

total_snowplow_cost = calculateSnowplowCosts(snowplowDistances)

print("Drone and snowplow total is: $", total_drone_cost + total_snowplow_cost)


