import sys, os
import re
import time
import argparse

# Get arguments from the command line
def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument("-i", "--infile", dest="infile", required=True,
                      help="required input file path")
    
    args = parser.parse_args()
    
    return args

def check_num_type(x):
    if x % 2 == 0: return 'even'
    else: return 'odd'

def get_center_index(garden, x_index, y_index):
    """
    Use nested for loop to get the index of the cell with maximum number of carrots.
    The nested for loop should be efficient since there are two elements at most in x_index and y_index
    """
    ret_x, ret_y = 0, 0
    max_ncarrots = 0
    for i in x_index:
        for j in y_index:
            if max_ncarrots < garden[i][j]: # ret_x, ret_y save the current index of cell with largest number of carrots
                ret_x, ret_y = i, j
                max_ncarrots = garden[i][j] # max_ncarrots save the current largest number of carrots
    return ret_x, ret_y

def find_center_cell(garden, N, M):
    # check if N and M are odd or even numbers
    N_type = check_num_type(N)
    M_type = check_num_type(M)
    
    # consider every combinations of odd and even numbers of N and M
    if N_type == 'odd' and M_type == 'odd':
        center_index = (int(N/2), int(M/2))
    elif N_type == 'even' and M_type == 'odd':
        N_index = [int(N/2)-1, int(N/2)]
        M_index = [int(M/2)]
        center_index = get_center_index(garden, N_index, M_index)
    elif N_type == 'odd' and M_type == 'even':
        N_index = [int(N/2)-1, int(N/2)]
        M_index = [int(M/2)]
        center_index = get_center_index(garden, N_index, M_index)
    elif N_type == 'even' and M_type == 'even':
        N_index = [int(N/2)-1, int(N/2)]
        M_index = [int(M/2)]
        center_index = get_center_index(garden, N_index, M_index)
    else:
        print ("Something is wrong!")
        sys.exit(1)

    return center_index

def get_next_center(garden, center_index, N, M):
    """
    The function use a hash to save the index as key and number of carrots in the four directions as value. The function considers bundary issues and 
    would not save cells with zero carrots.
    """
    index2count={}
    if center_index[0]-1 >= 0 and garden[center_index[0]-1][center_index[1]] != 0:
        index2count[(center_index[0]-1, center_index[1])] = garden[center_index[0]-1][center_index[1]]
    if center_index[1]-1 >= 0 and garden[center_index[0]][center_index[1]-1] != 0:
        index2count[(center_index[0], center_index[1]-1)] = garden[center_index[0]][center_index[1]-1]
    if center_index[0]+1 < N and garden[center_index[0]+1][center_index[1]] != 0:
        index2count[(center_index[0]+1, center_index[1])] = garden[center_index[0]+1][center_index[1]]
    if center_index[1]+1 < M and garden[center_index[0]][center_index[1]+1] != 0:
        index2count[(center_index[0], center_index[1]+1)] = garden[center_index[0]][center_index[1]+1]
    
    
    if len(index2count) == 0: return (-1,-1) # Sleep if no valid cells 
    else:
        # sort cells by number of carrots and retrun index of largest number of carrots for next step
        for k, v in sorted(index2count.items(), key=lambda x: x[1], reverse=True): 
            return k 
    
def eat(garden, center_index, N, M):
    ret = 0
    
    while center_index != (-1,-1):
        # add up number of carrots eaten
        ret += garden[center_index[0]][center_index[1]]
        # set number of carrots to zero after eating
        garden[center_index[0]][center_index[1]] = 0
        # funciton to get the index of next step
        center_index = get_next_center(garden, center_index, N, M)
    
    return ret
 
# Main routine
def main(start_time):
    # Get command line options
    args = parse_args()
    
    # Get garden matrix from file to process
    garden = []
    with open(args.infile) as fp:
        for line in fp:
            garden.append([int(i) for i in line.strip().split()])
    
    # Get the demension of the garden matrix
    N = len(garden)    # N is the number of rows
    M = len(garden[0]) # M is the number of columns
    
    # Find center cell
    center_index = find_center_cell(garden, N, M)
    print ("center index: ", center_index)
    
    # eat carrots
    total_carrots = eat(garden, center_index, N, M)
    print ("total carrot eaten: {}".format(total_carrots))
    
if __name__ == "__main__":
    start_time = time.time()
    main(start_time)
    print("---total time {} seconds ---".format(time.time() - start_time))
