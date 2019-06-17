INT_MAX = 999

#This function calculates the closest vertex to visit next
def min_wt(nv, evalues, vlist):
	min, min_index = INT_MAX, 0
	for i in range(nv):
		if vlist[i] == False and evalues[i] < min:
			min = evalues[i]
			min_index = i
	return min_index

#Performs Prims' method for finding MCST
def prims(nv, graph):
	parent = [0] * nv
	vlist = [False] * nv
	evalues = [INT_MAX] * nv

	parent[0] = -1
	for i in range(nv-1):
		u = min_wt(nv, evalues, vlist)
		vlist[u] = True

		for v in range(nv):
			if graph[u][v] != INT_MAX and vlist[v] == False and graph[u][v] < evalues[v]:
				evalues[v] = graph[u][v]
				parent[v] = u

	cost = 0
	for i in range(1, nv):
		#print("%d - %d = %d\n" % (parent[i]+1, i+1, evalues[i]))
		outhand.write("%d - %d = %d\n" % (parent[i]+1, i+1, evalues[i]))
		cost += evalues[i]
	#print("The cost is %d" % cost)
	outhand.write("The cost is %d" % cost)

#Main block
#nv = int(input("Enter the number of vertices: "))
inhand = open('input_file_name_here')
outhand = open('output_file_name_here', 'w')
nv = int(inhand.readline())
graph = [0] * nv
#print("Enter the matrix: ")

for i in range(nv):
	graph[i] = [0] * nv
	for j in range(nv):
		if i == j: graph[i][j] = 999
		#else: graph[i][j] = int(input())
		else: graph[i][j] = int(inhand.readline())

prims(nv, graph)
