# Zain Choudhry, Aaryan Khanal
# Programming Project - Milestone#1


'''
<<<<<<< HEAD
Planning

Objectives of the project:
        1. Read three of the ETS files (routes.txt, trips.txt and shapes.txt), and
store the information in appropriate data structures.
        2. Develop a text interface to access and search the data.
        3. Serialize the data structures using the pickle module for quick loading

    testing testing
=======
hello
>>>>>>> 156b98da313c17ff7f09915b6c734aacf236084f
'''

def main():
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
(0) Quit''')

    if menu_input == '1':
        pass




main()



def load_route_data():
    """
    The data structure must store route_id, route_name and shape_id
information for each route. It will be used to find the route_name and
the set of shape_ids associated with a route_id.
• For route 8, this information consists of the following data:
– route_id: "008"
– route_name: "Abbottsfield - Downtown - University"
– shape_id:
•
"008-210-South"
• "008-211-North"
•
"008-212-North"
•
"008-213-North"
    """
    pass

def load_shapes_data():
    """
    Read the shapes.txt file and store the data in an appropriate data structure (shapes).
– The data structure maps each shape_id to its shape. It will be used to find the
length of a shape, and to plot a shape.
– A shape is a sequence of (latitude, longitude) points that identify the path taken
by a bus.
– Routes will be drawn by drawing short lines between all adjacent pairs of shape
locations. Make sure to maintain the order of the lat/lon locations as they appear
in the shapes.txt file.
– This data structure will be used for the following tasks:
• Menu option 5: Print coordinates for a shape_id
• Menu option 6: Find the id of the longest shape for a route_id
• Menu option 9: The user provides a source and/or destination. Search for these
in the route_name for each route. If a match is found, plot the longest shape for
that route_id on the map.
"""
    pass