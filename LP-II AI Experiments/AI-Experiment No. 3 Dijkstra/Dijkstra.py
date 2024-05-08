graph={
    'A':{'B':2,'C':3},
    'B':{'D':3,'E':1},
    'C':{'F':2},
    'D':{},
    'E':{'F':1},
    'F':{}
	}

import heapq
def dijkstra(graph,node):
	distances={node:float('inf') for node in graph}
	print("distances::",distances)
	distances[node]=0
	previous={node:None for node in graph}
	queue=[(0,node)]
	print("Value of QUEUE ==> ",queue)
	
	while queue:
		current_distance,current_node=heapq.heappop(queue)
		print("Cureent Distance and Node ==> ",current_distance)
		print("Cureent Node ==> ",current_node)
		# relaxation
		for next_node,weight in graph[current_node].items():
			distance_temp=current_distance+weight
			if distance_temp<distances[next_node]:
				distances[next_node]=distance_temp
				previous[next_node]=current_node
				heapq.heappush(queue,(distance_temp,next_node))
			print("Distances::",distances)
	return distances,previous

#Driver Code
Node_distance, Path = dijkstra(graph,'A')
print(Node_distance)
print(Path)
