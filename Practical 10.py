fh = open("prac 10.txt",'w')
a=input('Enter Binary :') 
from_base=2 
answer=int(a,from_base) 
fh.write(str(answer))
fh.close()
