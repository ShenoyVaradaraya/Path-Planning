import numpy as np
import os,time
##A-Star PathFinding algorithm Class
class Node():
    
    def __init__(self,parent=None,pos=None):
        self.parent = parent
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self,other):
        return self.pos == other.pos


    def Astar(graph,begin,end,h_choice):
        ## Creating start node 
        node_begin = Node(None,begin)
        node_begin.g = 0
        node_begin.h = 0
        node_begin.f = node_begin.g + node_begin.h

        ## Creating end node 
        node_end = Node(None,end)
        node_end.g = 0
        node_end.h = 0
        node_end.f = node_end.g + node_end.h

        ## Initializing open and closed Lists
        openList = []
        closedList = []

        #Adding start node to open list
        openList.append(node_begin)

        ## Looping until the OpenList is empty
        while (openList !=None):
            #Since least f value is at start node , current node is set at first element of open list
            currentNode = openList[0] 
            curr_idx = 0;
            for idx,item in enumerate(openList):
                if(item.f < currentNode.f):
                    currentNode = item
                    curr_idx = idx
            #current node removed from open list and added to closed list 
            openList.pop(curr_idx) 
            closedList.append(currentNode)
            # If Goal is reached 
            if (currentNode == node_end):
                print("Reached goal ! \n")
                trajec = []
                curr = currentNode
                while curr is not None:
                    trajec.append(curr.pos)
                    curr = curr.parent
                return trajec[::-1] #Go backwards to find the path 
            
            children = []
            adj_square = [
                (0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1),(1, -1), (1, 1) # adjacent squares
                        ]
            #Get node position and check if is within range and on travel-able path 
            for new_pos in adj_square:
                node_pos = (currentNode.pos[0] + new_pos[0], currentNode.pos[1] + new_pos[1])
                if(node_pos[0] > len(graph)-1 or node_pos[0]<0 or
                   node_pos[1] > len(graph[len(graph)-1])-1 or node_pos[1] < 0):
                    continue
                if graph[node_pos[0]][node_pos[1]] != 0 :
                   continue
                
                #creat new node
                
                newNode = Node(currentNode,node_pos)
                children.append(newNode)
                
                #check if child is in closed list
                for kid in children:
                    for closedKid in closedList:
                        if kid == closedKid :
                            continue #continue the loop
                        
                    #Find f,g,h values
                    kid.g = currentNode.g+1
                    #Calculate the distance 
                    if(h_choice == "e" or h_choice =="E"):
                        kid.h = np.sqrt(((kid.pos[0] - node_end.pos[0])**2) + ((kid.pos[1] - node_end.pos[1])**2))
                    elif(h_choice == "m" or h_choice == "M"):
                        kid.h = np.abs(kid.pos[0] - node_end.pos[0]) + np.abs(kid.pos[1] - node_end.pos[1])
                    elif(h_choice == "d" or h_choice == "D"):
                        kid.h = max(np.abs(kid.pos[0] - node_end.pos[0]),np.abs(kid.pos[1] - node_end.pos[1]))
                    else:
                        print("\nThat heuristic choice is not available")
                        print("\nStarting Program once more...")
                        time.sleep(3)
                        os.system('clear')
                        main()
                    kid.f = kid.g + kid.h
                    
                    #check if child is in open list
                    for openNode in openList :
                        if(kid == openNode and kid.g > openNode.g):
                            continue #continue the loop
                        
                    #add child to open list 
                    openList.append(kid)
#Class defined to take input from user regarding starting and goal position
class user_input():
    
    def start_pos():
        
        start_pos = []
        x_axis_start = int(input("\nX-axis Starting position : "));
        if (x_axis_start  < 0 or x_axis_start  > 18): #checking if position is feasible on x-axis
            print("\n Position out of matrix")
            
            user_input.start_pos()
        else:
            start_pos.append(x_axis_start)
        y_axis_start  = int(input("Y-axis starting position : "));
        if (y_axis_start < 0 or y_axis_start > 18): #checking if position is feasible on y-axis
            print("\nPosition out of matrix")
        
            user_input.start_pos()
        else:
            start_pos.append(y_axis_start)
        start = (x_axis_start,y_axis_start)
        print( "\nStarting Position : ", start )
        print("\n-------------------------------------------------------- ")
        
        return start
    def goal_pos():
        
        goal_pos=[]
        x_axis_goal = int(input("\nX-axis goal position : "));
        if (x_axis_goal< 0 or x_axis_goal > 18): #checking if position is feasible on x-axis
            print("\nPosition out of matrix")
            
            user_input.goal_pos()
            
        else:
            goal_pos.append(x_axis_goal)
        y_axis_goal = int(input("Y-axis goal position : "));
        if (y_axis_goal< 0 or  y_axis_goal > 18):#checking if position is feasible on y-axis
            print("\nPosition out of matrix")
            
            user_input.goal_pos()
        else:
            goal_pos.append(y_axis_goal)
        end = (x_axis_goal),(y_axis_goal)
        print( "\nGoal Position :", end )
        print("\n-------------------------------------------------------- ")
        return end
        
    def repeat():
       ask_user = input("\nOne More Trial? (y/N)")
       if(ask_user == "y" or ask_user == "Y"):
           print("\nStarting Program....")
           time.sleep(4)
           os.system('clear')
           main()
       else:
           print("\nExiting...")
           exit()
        

def main():
   graph = [
        [0, 1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1, 0, 1, 0, 1, 0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1, 0, 1,0,0, 1,0,0,0,0,0,0,0,0,0,0,0,0],
        [1, 0, 1,0,0, 1, 0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0],
        [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0] ]
   
   start = user_input.start_pos()
   end = user_input.goal_pos()
   h_choice = input("\n Choice of Heuristic: \n\t(e/E) Euclidean? \n\t(m/M) Manhattan? \n\t(d/D) Diagonal? \n Enter Heuristic of Choice ---- ") #Heuristic choices available
   move_path = Node.Astar(graph,start,end,h_choice)
   print("\nPath from ", start , "to", end, "------")
   print(move_path)
   user_input.repeat()
if __name__ == '__main__':
    main()
