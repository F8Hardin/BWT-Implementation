import time

print("Please enter T followed by a space. Then enter P.")
t, p = input().split()
count = 0

start = time.time()
for i in range(len(t)):
    if t[i : len(p) + i] == p:
        count += 1
end = time.time()

print(end - start)
print(count)
