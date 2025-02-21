#By Shardul Funde
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

arr = []
arr_for_graph = []
print("Type 'stp' to stop the training")
print("Type 'feature1', 'feature2' and 'label' below")
labels = []

while True:
    inp = input()
    if(inp == "stp"):
        break
    
    else:
        x,y,z = map(str, inp.split())
        x = int(x)
        y = int(y)
        if z not in labels:
            labels.append(z)
            new_data = [[x,y]]
            arr.append(new_data)
            arr_for_graph.append([x,y])
            
        else:
            z_index = labels.index(z)
            arr[z_index].append([x,y])
            arr_for_graph.append([x,y])

dataArr = np.array(arr_for_graph)           
xPoints = np.array(dataArr[:,0])
yPoints = np.array(dataArr[:,1])
plt.scatter(xPoints, yPoints,s = 5)
plt.show()
           
#calculating mean of every cluster
label_mean_x = []
label_mean_y = []

for i in range(len(labels)):
    cluster_array = np.array(arr[i])
    mean_x = np.mean(cluster_array[:, 0])
    mean_y = np.mean(cluster_array[:, 1])
    
    #appending every mean
    label_mean_x.append(mean_x)
    label_mean_y.append(mean_y)

#converting x and y means to array   
label_mean_x = np.array(label_mean_x)
label_mean_y = np.array(label_mean_y)

#adding dots to graph
plt.scatter(xPoints, yPoints,s = 5)
plt.scatter(label_mean_x, label_mean_y,color = 'hotpink',s = 10)

plt.show()

feat1, feat2 = map(int,input("Type feature1 and feature 2 for prediction: ").split())

shortest_dist = sqrt((feat1 - label_mean_x[0])**2 + (feat2 - label_mean_y[0])**2)
shortest_dist_index = 0
for j in range(1,len(labels)):
    dist = sqrt((feat1 - label_mean_x[j])**2 + (feat2 - label_mean_y[j])**2)
    
    if(dist < shortest_dist):
        shortest_dist = dist
        shortest_dist_index = j
        
plt.scatter(xPoints, yPoints,s = 5)
plt.scatter(label_mean_x, label_mean_y,color = 'hotpink',s = 10)
plt.scatter(feat1,feat2,color = 'red')

shortest_dist_x = np.array([label_mean_x[shortest_dist_index],feat1])
shortest_dist_y = np.array([label_mean_y[shortest_dist_index],feat2])

plt.plot(shortest_dist_x,shortest_dist_y,ls = ':')
plt.show()

print("The closest prediction would be",labels[shortest_dist_index])  



        
    
    
    







