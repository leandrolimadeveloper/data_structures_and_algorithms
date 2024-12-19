"""
This algorithm performs a Breadth-First Search (BFS) on a graph to determine 
if there is a person whose name starts with the letter "M". It uses a queue 
to process connections level by level and ensures no person is checked more 
than once. If such a person is found, they are identified as a "mango seller".
"""

from collections import deque

def search(name):
    search_queue = deque()  # Queue to store people to be checked
    search_queue += graph[name]
    checked = []  # List to track already checked people

    while search_queue:
        person = search_queue.popleft()  # Remove the first person from the queue
        if person not in checked:  # Check if the person has already been verified
            if is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]  # Add this person's friends to the queue
                checked.append(person)  # Add the person to the checked list
        
        if not search_queue:
            print("There is no mango seller!")
    return False

# Example of the graph structure
graph = {
    "you": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["amanda", "peggy"],
    "claire": ["thom", "jonny"],
    "amanda": ["marcelo"],
    "peggy": [],
    "thom": [],
    "jonny": []
}

# Function to check if the person is a seller
def is_seller(name):
    return name[0] == "m"

# Execute the search
search("you")
