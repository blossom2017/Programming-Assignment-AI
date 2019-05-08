#MAITRI SHASTRI 2014B2A70220P


def createBayes(inputfile):
	fp=open(inputfile+'.txt','r')
	lines=fp.readlines()
	lines=lines[ :-2]
	graph={}
	#print(lines)
	for x in lines:
		y=x.split(">>")
		#print(y[1])
		y[1]=y[1][2:-2]
		if(y[1]):
			y[0]=y[0][:-1]
			ls=y[1].split(", ")
			#print(ls)
			graph[y[0]]=ls
	print(graph)	
	return graph

def markovblanket(graph,nodeA):
	mb=[]
	mb.append(nodeA)
	value=graph[nodeA]
	if(value):
		for x in value:
			mb.append(x)

	mb1=[]		
	for k,v in graph.items():
		if (nodeA in v):
			mb1.append(k)

	mb2=[]
	if(mb1):

		for i in mb1:
			mb.append(i)
			value=graph[i]
			if(value):
				for x in value:
					mb2.append(x)
					mb.append(x)

	mbwithoutdup=set(mb)			
	return mbwithoutdup				






if __name__=="__main__":

	inputfile=raw_input("Enter the name of input file")
	graph=createBayes(inputfile)
	nodeA=raw_input("Enter the name of node whose markov blanket is to be computed")
	mb=markovblanket(graph,nodeA)
	print(mb) 