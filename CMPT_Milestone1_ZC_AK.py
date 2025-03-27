# Zain Choudhry, Aaryan Khanal
# Programming Project - Milestone#1


'''
Planning
Milestone #1 Due Date: March 30th, 11:59 PM
This milestone focuses on:
1. Loading two of the ETS files (trips.txt and shapes.txt) into appropriate data structures
2. Developing a text interface to access and search these data structures
3. Serializing these data structures using the pickle module for quick loading

Objectives of the project:
        1. Read three of the ETS files (routes.txt, trips.txt and shapes.txt), and
store the information in appropriate data structures.
        2. Develop a text interface to access and search the data.
        3. Serialize the data structures using the pickle module for quick loading


three data files:
– routes.txt
• route_id (col 0), e.g. '008'
• route_name (col 3), e.g. "Abbottsfield - Downtown - University".

– trips.txt
• route_id (col 0)
• shape_id (col 6), multiple for each route_id,
– e.g. 008-210-South, 008-211-North

– shapes.txt
• shape_id (col 0)
• latitude (col 1), longitude (col 2) locations. Many for each shape_id
• Other data columns can be ignored. 


During implementation, you must deploy appropriate strategies learned in lecture that prohibit your program from
crashing due to:
• Invalid user input
• Performing an action before a file is loaded
• Attempting to open a file for reading or writing
• Closing the interactive map prematurely
Necessary safeguards should be in place.
'''

def main():
    route_data = {}
    shapes_data = {}

    menu_input = input('''Edmonton Transit Systems
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
        route_data = load_route_data()
    elif menu_input == '2':
        pass
    elif menu_input == '3':
        print('Option 3 reserved for Milestone 2')
    elif menu_input == '4':
        pass
    elif menu_input == '5':
        pass
    elif menu_input == '6':
        print('Option 6 reserved for Milestone 2')
    elif menu_input == '7':
        pass
    elif menu_input == '8':
        pass
    elif menu_input == '9':
        print('Option 9 reserved for Milestone 2')
    elif menu_input == '0':
        quit()


def load_route_data() -> dict:
    """
    purpose: Create a data structure retrieving and storing route id, 
            route name and shape ids(without duplicates) all together 
    parameters: 
    returns: 

1. recieve the filename from the user with error handling 
2. read the routes text file and retrieve route name and create a dictionary 
3. read the trips file and then return route id and shape id put in a dictionary 
4. put shape id into a set to remove duplicates so we only end up with unique sets 
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

    #ASK THE PROF IS THIS PART IS SUPPOSED TO BE HARDCODED????
    try:
        with open('data/routes.txt', 'r') as file:
            next(file)
            for line in file:
                data = line.strip().split(',')
                if len(data) > 3:  
                    route_id = data[0].strip()
                    route_name = data[3].strip()
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
    return routes
        

def load_shapes_data():
    pass

def shape_for_route():
    #if file isnt loaded from option 1 then print
    route_data = load_route_data()

    if not filename_input:
        print("Route data hasn 't been loaded yet")
    else:
        route_id = input("Enter route: ").strip()
        if route_id in route_data:
            print(f'''Shapes ids for route [{route_name} 
    {route_data[route_id][1]}]''')
        else:
            print(f"** NOT FOUND **")  

main()