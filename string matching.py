




def horspool(cstext,cspattern):
    
    lowertext = cstext.lower()
    lowerpattern = cspattern.lower()
    n = len(lowertext)
    m = len(lowerpattern)

    d =  {}

    distinct = set(lowertext+lowerpattern)

    dislist = list(distinct)

    for i in range(0,len(dislist)):
        d[dislist[i]] = m

    for i in range(0,m-1):
        d[lowerpattern[i]] = m-i-1  # 0 based index

    innercount = 0
    pos = 0

    while pos <= n-m:
        j = m-1 # 0 based index
        while j>= 0 and lowertext[pos+j] == lowerpattern[j]:
            j= j-1
        if j<0:
            innercount+=1
        pos = pos + d[lowertext[pos+m-1]] # 0 based index

    if innercount  > 0 :
        print (cstext)
    return innercount

cspattern = input("Enter a search string: ")

file = open("modules.txt","r")
lines =  file.readlines()

count = 0 

for line in lines:
    count += horspool(line[:-1],cspattern)

print("Number of matches: "+ str(count))
