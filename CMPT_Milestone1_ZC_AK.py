# Zain Choudhry, Aaryan Khanal
# Programming Project - Milestone#1

import pickle

def main():
    route_data = {}
    route_names = {}
    shapes_data = {}

    menu_loop = True
    while menu_loop:
        menu_input = input('''\nEdmonton Transit Systems
--------------------------------
(1) Load route data 
(2) Load shapes data
(3) Reserved for future use
(4) Print shape IDs for a route
(5) Print coordinates for a shape ID
(6) Reserved for future use
(7) Save routes and shapes in a pickle
(8) Load routes and shapes from a pickle
(9) Reserved for future use
(0) Quit\n''')
        if menu_input == '1':
            route_data, route_names = load_route_data()
        elif menu_input == '2':
            shapes_data = load_shapes_data()
        elif menu_input == '3':
            print('Option 3 reserved for Milestone 2')
        elif menu_input == '4':
            shape_for_route(route_data, route_names)
        elif menu_input == '5':
            pass
        elif menu_input == '6':
            print('Option 6 reserved for Milestone 2')
        elif menu_input == '7':
            save_pickle(route_data, route_names, shapes_data)
        elif menu_input == '8':
            route_data, route_names, shapes_data = load_pickle()
        elif menu_input == '9':
            print('Option 9 reserved for Milestone 2')
        elif menu_input == '0':
            menu_loop = False
            print('Goodbye!')


def load_route_data() -> dict:
    """
    purpose: Create a data structure retrieving and storing route id, 
             route name and shape ids(without duplicates) all together
                1. recieve the filename from the user with error handling 
                2. read the routes text file and retrieve route name and create a dictionary 
                3. read the trips file and then return route id and shape id put in a dictionary 
                4. put shape id into a set to remove duplicates so we only end up with unique sets 
    parameters: none
    returns: dictionary of route data and route names
    """

    while True:
        filename_input = input("Enter trips filename (Press enter for default 'data/trips.txt'): ").strip()
        trips_file = filename_input if filename_input else 'data/trips.txt'
        
        try:
            open(trips_file).close()  
            break
        except FileNotFoundError:
            print(f"IOError: Couldn't open non_existent_file")
        except Exception as e:
            print(f"IOError: Couldn't open non_existent_file")

    routes = {} 
    route_names = {}

    try:
        with open('data/routes.txt', 'r') as file:
            next(file)
            for line in file:
                data = line.strip().split(',')
                if len(data) > 3:  
                    route_id = data[0].strip()
                    route_name = data[3].strip()
                    route_names[route_id] = route_name
                    routes[route_id] = [route_name, set()]
    except FileNotFoundError:
        print('Routes file not found')
        return {}
    
    try:
        with open(trips_file, 'r') as file:
            next(file)
            for line in file:
                data = line.strip().split(',')
                if len(data) > 6:  
                    route_id = data[0]
                    shape_id = data[6]
                    if route_id in routes:
                        routes[route_id][1].add(shape_id)
    except FileNotFoundError:
        print('File not found')
        return {}
    print(f"Data from {trips_file} loaded")
    return routes, route_names
        

def load_shapes_data():
    """
    purpose: Create a data structure retrieving and storing shape id, lat and lon all together
    parameters: none
    returns: dictionary of shape data
    """
    while True:
        filename_input = input("Enter trips filename (Press enter for default 'data/shapes.txt'): ").strip()
        trips_file = filename_input if filename_input else 'data/shapes.txt'
        
        try:
            open(trips_file).close()  
            break
        except FileNotFoundError:
            print(f"IOError: Couldn't open non_existent_file")
        except Exception as e:
            print(f"IOError: Couldn't open non_existent_file")
    shapes = {}
    try:
        with open(trips_file, 'r') as file:       
            next(file)
            for line in file:
                parts = line.strip().split(',')
            
                shape_id = parts[0]
                lat = float(parts[1])
                lon = float(parts[2])
            
                if shape_id not in shapes:
                    shapes[shape_id] = []
                
                shapes[shape_id].append((lat, lon))
    except FileNotFoundError:
        print('File not found error')
        return {}
    print(f"Data from {trips_file} loaded")
    return shapes
   

def shape_for_route(routes, route_names):
    """
    purpose: allows user to enter a route id and then prints the shape ids for that route
    parameters: routes dictionarty, route_names dictionary
    returns: none
    """
    if not routes or not route_names:
        print("Route data hasn't been loaded yet")
        return
    
    route_id = input("Enter route: ").strip()

    if route_id in routes:
        shape_ids = routes[route_id][1]
        print(f'''Shapes ids for route [{route_names[route_id]}] 
    {''' 
    '''.join(shape_ids)}''')
    else:
        print(f"** NOT FOUND **")  

def save_pickle(routes, route_names, shapes):
    """
    purpose: the user is prompted for filename which is then opened for writing. 
            If the user presses enter without entering a filename, the filename 
            defaults to etsdata.p. The Data structures containing the route and 
            shapes data are written to the binary file. The pickle module is used 
            to write these data structures to the file. This operation should not 
            fail if the data structures have not been loaded yet. 
    parameters: routes dictionary, route_names dictionary, shapes dictionary
    returns: none
    """
    
    if not routes or not route_names or not shapes:
        print("Data hasn't been loaded yet")
        return
    
    pickle_file_input = input("Enter a filename (Press enter for default 'data/etsdata.p'): ").strip()
    pickle_file = pickle_file_input if pickle_file_input else 'data/etsdata.p'
    try:
        with open(pickle_file, 'wb') as file:
            pickle.dump((routes, route_names, shapes), file)
        print(f"Data structures successfully written to data {pickle_file}")
    except FileNotFoundError:
        print(f"IOError: Couldn't open non_existent_file")

def load_pickle():
    """
    purpose: the user is prompted for a filename which is then opened for reading. 
            If the user presses enter without entering a filename, the filename 
            defaults to etsdata.p. The Data structures containing the route and 
            shapes data are read from the binary file. The pickle module is used
            to read these data structures from the file. 
    parameters: none
    returns: routes dictionary, route_names dictionary, shapes dictionary
    """
    pickle_file_input = input("Enter a filename (Press enter for default 'data/etsdata.p'): ").strip()
    pickle_file = pickle_file_input if pickle_file_input else 'data/etsdata.p'
    try:
        with open(pickle_file, 'rb') as file:
            routes, route_names, shapes = pickle.load(file)
        print(f"Routes and shapes Data structures successfully loaded from {pickle_file}")
        return routes, route_names, shapes
    except FileNotFoundError:
        print(f"IOError: Couldn't open non_existent_file")
        return {}, {}, {}

main()