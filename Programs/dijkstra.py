INT_MAX = 999

#This function calculates the closest vertex to visit next
def min_wt(nv, dist, vlist):
	min, min_index = INT_MAX, 0
	for i in range(nv):
		if vlist[i] == False and dist[i] < min:
			min = dist[i]
			min_index = i
	return min_index

#Performs Dijkstra's method to find SSSP
def dijkstra(nv, graph, src):
	dist = [INT_MAX] * nv
	vlist = [False] * nv

	dist[src] = 0

	for i in range(nv-1):
		u = min_wt(nv, dist, vlist)
		vlist[u] = True

		for v in range(nv):
			if graph[u][v] != INT_MAX and vlist[v] == False and dist[u] != INT_MAX and (dist[u] + graph[u][v]) < dist[v]:
				dist[v] = dist[u] + graph[u][v]
	for i in range(nv):
		if i != src: print("%d - %d = %d\n" % (src, i, dist[i]), end="")

#Main Block
nv = int(input("Enter the number of vertices in the graph: "))
graph = [0] * nv

print("Enter the adjacency matrix of the graph: ")
for i in range(nv):
	graph[i] = [0] * nv
	for j in range(nv):
		if i==j: graph[i][j] = INT_MAX
		else: graph[i][j] = int(input())

src = int(input("Select the source vertex (in INDEX notation): "))
dijkstra(nv, graph, src)
