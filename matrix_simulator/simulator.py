import os
import math
import random

def generate_matrix_string(max_width):
    random_width = random.randint(max_width//3, max_width-3)
    choices = [chr(i) for i in range(0x3041, 0x3095)] #+ [chr(i) for i in range(48, 58)]
    random.shuffle(choices)
    #print(''.join(choices[:random_width]))
    return choices[:random_width]

def calc_velocities(max_width):
    velocities = []
    for i in range(0, max_width):
        velocities.append(random.randint(1, 10)/10)
    return velocities

def run():
    columns, rows = os.get_terminal_size(0)
    print(columns, rows)

    velocities = calc_velocities(columns)
    translation_matrix = [ 0 for i in range(0, columns) ]

    matrix_string = [ [' ']*columns for i in range(rows) ]
    string_colummns = [generate_matrix_string(rows) for i in range(columns)]

    while True:
    
        for i in range(0, columns):
            translation_matrix[i] = round(translation_matrix[i] + velocities[i]) % rows
        
        #print(translation_matrix)


    #print(string_colummns)
    
        


if __name__ == '__main__':
    run()