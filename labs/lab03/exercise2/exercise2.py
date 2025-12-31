def find_station(stations, name):
    i = 1
    for i in range(len(stations)):
        if stations[i] == name:
            return i
        
    return None

def count_stops(stations, start, stop):
    start_index = find_station(stations, start)
    stop_index = find_station(stations, stop)

    if start_index == None or stop_index == None:
        return -1

    return abs(stop_index - start_index)


