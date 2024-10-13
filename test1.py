def draw_plot():
    width = 20  
    height = 19 
    
    graph = [["." for raws in range(width)] for columns in range(height)]  

    for i in range (height):
        graph[i][1]= "|"
        graph[height-2][i]="-"

    graph[-2][1] = "*"      #добавила точку с координатой [0;0]

    graph[-1][0]=" "        
  

    for i in range (-2, -12, -2):      #координаты по оси y
        graph[i][0] = str(-(i+2))
    
    for i in range (1, 11):           #координаты по оси x
        graph[-1][i] = str (i-1)


    for x in range(1, width):
        coord_y = 2 * x
        y = height - 1 - coord_y  # инверсия
        
        if 0 <= y <= height :
            graph[y+1][x] = "*"


    for row in graph:
        print("".join(row))


