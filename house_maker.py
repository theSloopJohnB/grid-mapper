from house import * 

room1_edges = [
            Point(0,0), 
            Point(50,0),
            Point(50,50),
            Point(0,50),
        ]

room2_edges = [
            Point(50,0), 
            Point(100,0),
            Point(100,50),
            Point(50,50),
        ]

room1 = Room(room1_edges)
room2 = Room(room2_edges)
