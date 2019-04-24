import time

#finds lowerR from paper R(k) = min{index where k is a prefix of sa}
def lowerR(k, sa):
    i = 0 #the number of symbols in t that are lexographically smaller than k[0]
    for s in sa:
        if k == s[1][0 : len(k)]: #if string k is the first part of string s[1]
            return i
        else:
            i += 1
#find upperR from paper R(k) = max{index where k is prefix of sa}
def upperR(k, sa, lowerR):
    i = lowerR + 1
    for s in sa[i:]:
        if k == s[1][0 : len(k)]:
            i += 1
        else:
            return i - 1

            
#User gives T and P to be found in T
print("Please enter T followed by a space. Then enter P.")
t, p = input().split()
t += "$" #marks the end of the string

#setting up the suffix array used to find BWT(T)
suffixArray = list()
for i in range(len(t)):
    suffixArray.append([i, t])
    temp = t
    t = t[1: len(t)]
    t += temp[0]
suffixArray.sort(key = lambda x : str(x[1])) #sort by string

#Getting lowerR and upperR
start = time.time() #time take to find locations of p in t
r = lowerR(p, suffixArray) #will be set to none if p is not found at all
if r != None:
    R = upperR(p, suffixArray, r)

#PRINTING RESULTS
end = time.time()
print(20 * "=")
if r != None:
    print("Number of occurence:", (R + 1) - r, "\nEach substring occurs at: ")
    for s in suffixArray[r : R + 1]:
        print(s[0], end = " ")
else:
    print("String not found")
print("\nTime: ", end - start)
##print("BWT(T): ", end = "")
##for s in suffixArray:
##    print(s[1][len(s[1]) - 1], end = "")
