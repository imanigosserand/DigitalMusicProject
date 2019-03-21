import csv
from array import *

# set size of matrix
w, h = 46, 46;

# create nodes matrix
nodes = [[0 for x in range(w)] for y in range(h)] 

# maps node names to numbers
node_keys = {}

# array to keep count of activities,
activities_count = [[0,0]]

with open("nodes.txt") as nodesFile:
  # content = lines of nodes text file
    content = nodesFile.readlines()

    # make 2D matrix with nodes as top row and first column
    # make dictionary and activities_count
    count = 1
    for x in content:
      nodes[count][0] = x.strip("\n")
      nodes[0][count] = x.strip("\n")
      node_keys[x.strip("\n")] = count
      activities_count.append([x.strip("\n"), 0])
      count += 1

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # activities + location for each person
    for row in csv_reader:
      activities = row[0]
      locations = row[1]
      al = [] # activity location combos
      
      for act in activities.split(": "):
        # special case for merchandise
        if(act == "buy merchandise"):
          activities_count[int(node_keys[act])][1] += 1
          continue

        # create list of acitivity location combos
        # increment activities_count if valid node
        for place in locations.split(": "):
          str = act + ", " + place
          if str in node_keys:
            activities_count[int(node_keys[str])][1] += 1
            al.append(str)

    # for each activity location combo, add 1 to count and relations
      for a in al:
        for b in al:
          nodes[node_keys[a]][node_keys[b]] = int(nodes[node_keys[a]][node_keys[b]]) + 1

# create csvfile with matrix
csvfile = "matrix.csv"   

with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(nodes)
