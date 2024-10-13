import os
import time
from decimal import Decimal

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
PINK = '\u001b[48;5;225m'
PEACH = '\u001b[48;5;216m'
END = '\u001b[0m'




def draw_flag():

    for x in range(12):                            #task 1, флаг Нидерландов
        if x < 4: print(f'{RED}{" " * 40}{END}')  
        elif x < 8: print(f'{WHITE}{" " * 40}{END}')
        else: print(f'{BLUE}{" " * 40}{END}')
    return 0


def draw_string(offset, distance, length):   #task 2, рисуем узор

    for height_of_square in range(2):
        print(f'{offset * " "}', f'{RED}{" " * 5}{END}{" " * distance}'*length)
    return 0    
        

def draw_plot():                              #task 3, график функции y = 2 * x
    width = 20  
    height = 19 
    
    graph = [["." for raws in range(width)] for columns in range(height)]  

    for i in range(height):
        graph[i][1] = "|"
        graph[height-2][i+1] = "-"

    graph[-2][1] = "*"      #добавила точку с координатой [0;0]
    graph[-1][0] = " "        
  

    for i in range(-2, -12, -2):      #координаты по оси y
        graph[i][0] = str(-(i+2))
    for i in range(1, 11):           #координаты по оси x
        graph[-1][i] = str(i-1)


    for x in range(1, width):
        coord_y = 2 * x
        y = height - 1 - coord_y  # инверсия   
        if 0 <= y <= height :
            graph[y+1][x] = "*"


    for row in graph:
        print("".join(row))





def count_seq(): 

    count_pos = 1
    nechetn = Decimal(0)
    chetn = Decimal(0)

    for num in open('sequence.txt'):
    
        if count_pos % 2 == 0:
            chetn += abs(Decimal(num.strip()))
        else:
            nechetn += abs(Decimal(num.strip()))
        count_pos += 1
    return print (
        f'Сумма чисел по модулю на четных позициях:  {chetn} {BLUE}{(round(chetn))//12*" "}{END}\n'
        f'Сумма чисел по модулю на нечетных позициях:{nechetn} {WHITE}{(round(nechetn))//12*" "}{END}'   
                )



# def animation():             # Допзадание анимация
#     tabul = "\t"
#     shots = []
#     for i in range (10,1, -1):
#         shots += [f"{PEACH}(つ✧ω✧)つ{i*tabul}{PINK}(•ᴥ• )́`́’́`́’⻍'{END}"]
#     for i in range (10):
#         shots += [f"{tabul*i}༼ つ ◕_◕ ༽つヽ༼ຈل͜ຈ༽ﾉ{END}"]


#     while True: 
#         for shot in shots:                         
#             os.system("clear")
#             print (shot)
#             time.sleep(0.5)
#         time.sleep(1)
#     return 0


if __name__ == "__main__":
    draw_flag()
  
    uzor = ((0, 15, 6), (5, 5, 11), (10, 15, 5), (5, 5, 11)) #task 2
    for height_of_pattern in range(2):
        for i in uzor:
            draw_string(i[0], i[1], i[2])
    
    draw_plot()
    
    count_seq()

    #animation()


