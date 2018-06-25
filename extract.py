import re
def takeInput():
	srcList=[]
	destList=[]
	i=0
	loc="/media/sanjay/OS/CORONA/37/DS1025-1039DF037_a.tif.points"
	file=open(loc,'r')
	content=file.read()
	m=re.findall(r"[0-9]+\.[0-9]*",content)
	print(len(m))
	while(i<len(m)):
		destList.append((float(m[i]),float(m[i+1])))
		srcList.append((float(m[i+2]),float(m[i+3])))
		i=i+4
	return (srcList,destList)
