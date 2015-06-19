def main():
	f=open("a1.txt",'r')
	cnt=int(f.readline())
	length=len(open("a1.txt").readlines())-1
	maxi=float(cnt*(cnt-1)/2)
	threshold=float(length/maxi)
	if(threshold > 0.6):
		print "here"
		adgraph(f,cnt)
	else:
		print "bye"
		adlist(f,cnt)
def adgraph(f,n):
	temp=[0,0,0];
	matrix = [[999 for x in range(n)] for x in range(n)]
	
	for line in f:
		print "hello"
		i=0;
		for node in line.split():
			temp[i]=int(node)
			i=i+1
		matrix[temp[0]-1][temp[1]-1]=temp[2]
		matrix[temp[1]-1][temp[0]-1]=temp[2]
	print matrix

def adlist(f,n):
main()
		
