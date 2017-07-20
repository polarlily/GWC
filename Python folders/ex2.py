
target = "g"

def binarySearch(alist, item):
	    first = 0
	    last = len(alist)-1
	    found = False



	    while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True #and print("ok")

	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1

	    return found
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
alpha.append("y")
alpha.append("z")

print(binarySearch(alpha, "k"))
