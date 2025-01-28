
l = list(map(int, input("Enter integers separated by space: ").split()))
y = []

i = 0
while i < len(l) - 1:
    if(l[i] > l[i + 1]):
        y.append(l[i + 1])
        l.pop(i + 1) 
    else:
        i += 1
        
sorted_list = []

sorted_list = l.copy()
i = 0

while i < len(y):
    
    for c in range(len(sorted_list)):
        if(y[i] <= sorted_list[c]):
            sorted_list.insert(c, y[i])
            break
        
    i += 1
            
print(sorted_list)
        
        

