import time

def startCheck(f):
    locations = list()
    for i in range(len(f)):
        if f[i][0] == p[len(p) - 1]:
            locations.append(i)
    return locations

def checkFirst(f, counter, string):
    word = string
    locations = list()
    for i in range(len(f)):
        if f[i] == word:
            locations.append(i)
    return locations

def checkLast(l, locations, counter, d, f, string, misses):
    locs = list()
    newLocations = list()
    count = 0
    for i in locations:
        if l[i][0] != p[counter]:
            misses[count] += 1
            if misses[count] <= d:
                string = (l[i][0], l[i][1])
                newLocations = checkFirst(f, counter, string)
        else:
            string = (p[counter], l[i][1])
            newLocations = checkFirst(f, counter, string)
        if len(newLocations) != 0:
            locs.extend(newLocations)
        count += 1
    return (locs, string, misses)

print("Please enter T, P, then mismatch count. Each followed by a space.")
t, p, d = input().split()
d = int(d)
t += "$"

cols = list()
for i in range(len(t)):
    cols.append((t, i))
    temp = t
    t = t[1: len(t)]
    t += temp[0]
cols.sort(key = lambda x : x[0]) #sort by string
FlettCount = dict()
LlettCount = dict()
f = list()
l = list()
suffixArray = list()
for c in cols:
    if c[0][0] not in FlettCount.keys():
        FlettCount[c[0][0]] = 0
    else:
        FlettCount[c[0][0]] += 1
    if c[0][len(t) - 1] not in LlettCount.keys():
        LlettCount[c[0][len(t) - 1]] = 0
    else:
        LlettCount[c[0][len(t) - 1]] += 1
    f.append((c[0][0], FlettCount[c[0][0]]))
    l.append((c[0][len(t) - 1], LlettCount[c[0][len(t) - 1]]))
    suffixArray.append(c[1])
del cols
start = time.time() #starting timer here after table is set up
#searching through for matches
string = ("start", 0) #if a mismatch, pass in character, otherwise leave blank
locations = startCheck(f)
misses = [0] * (len(locations))


#repeat these len(p) - 1 times
for i in range(len(p) - 1):
    locations, string, misses = checkLast(l, locations, len(p) - 2 - i, d, f, string, misses)

end = time.time()
locations = set(locations)
print("Time:", end - start)
print(p, "allowing", d, "mismatches (" + str(len(locations)), "found)are at indexes:")
for l in locations:
    print(suffixArray[l] , t[suffixArray[l]: suffixArray[l] + len(p)])


