
"""
import pandas as pd
import numpy as np

data = []

with open("MinedData.txt","r") as f:
    for line in f:
        data.append(line)


print(len(data))

"""
import numpy as np
import wikipedia

search = wikipedia.search("emperors" , results=200)
minedData = []



for x in search:
	
	try :
	    ny = wikipedia.page(title=x , auto_suggest=True , redirect=True)
	    minedData.append(ny.content)
	    print(x)
	except :
		pass

print(len(minedData))

thefile = open('MinedData.txt', 'w')
for item in minedData:
    thefile.write("%s" % item)
    
thefile.close()  
print("its done " , len(minedData))
