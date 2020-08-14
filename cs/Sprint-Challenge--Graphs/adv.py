from typing import List
from util import Stack

from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

# init a player class:
player = Player(world.starting_room)

# init a dict to hold inverse directions:     
reverse_directions = {'n':'s', 's':'n', 'w':'e', 'e':'w'}

def traverse_graph() -> List[str]:
    traversal_path = []    
    # init Stack to hold rooms and directions:
    s = Stack()
    # init dict of rooms visited:
    visited_graph = {} 
    s.push(value=(player.current_room, None))
   
    while s.size() > 0:
        curr = s.look_behind()
        room, direction_traveled = curr[0], curr[1] 
        if room.id not in visited_graph: 
            # # init a set of directions we've visited:
            visited_graph[room.id] = set()
        if direction_traveled: 
            visited_graph[room.id].add(direction_traveled) 
        # break if we visit all the rooms:
        if len(visited_graph) == len(room_graph):
            break
        # DFS 
        unexplored_branches = [direction for direction in room.get_exits() if direction not in visited_graph[room.id]]
        # if there is somewhere to go, update:   
        if unexplored_branches:
            random_direction = random.choice(unexplored_branches)
            print("We can go: ",random_direction)
            # update graph:
            visited_graph[room.id].add(random_direction)
            # push the room we go to and what direction to reverse if dead end:   
            s.push(value=(room.get_room_in_direction(random_direction), reverse_directions[random_direction]))
            traversal_path.append(random_direction) 
        # back up:
        else: 
            print("Dead end! Reversing...", direction_traveled)
            traversal_path.append(direction_traveled)
            s.pop()
    return traversal_path


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = traverse_graph()



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
