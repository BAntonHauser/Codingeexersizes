#creating variables
rows, cols = 50, 50
arr = [[0 for _ in range(cols)] for _ in range(rows)]

temp = ""


i = 1
j = 1
while(i < cols):
    
    while(j < rows):
        if arr[i-1][j] == arr[i][j-1]:
            arr[i][j] = 1
          
        j += 1
    i += 1
    j= 1
#printing result  

for x in arr:
    temp = ""
    for y in x:

        if y == 0:
            temp += '_'
        elif y == 1:
            temp += '#'
        else:
            print("error vlaue is out of range")
    print(temp)
    
