arr = []
inp = open ("myfile.txt","r")
#read line into array 
for line in inp.readlines():
    # add a new sublist
    arr.append([])
    # loop over the elemets, split by whitespace
    for i in line.split():
        # convert to integer and append to the last
        # element of the list
        arr[-1].append(int(i))
