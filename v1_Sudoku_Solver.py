#20/01/2021
#Sudoku problem solver
#version 1 
#no back track implemented



import numpy as np
import pandas as pd

#create testing data frame which is a 9x9
sudoku_test_df = pd.DataFrame([
    [1,np.nan,np.nan,8,np.nan,np.nan,np.nan,np.nan,2],
    [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],
    [np.nan,6,np.nan,np.nan,np.nan,np.nan,4,np.nan,np.nan],
    [np.nan,np.nan,np.nan,6,np.nan,np.nan,np.nan,np.nan,np.nan],
    [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],
    [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],
    [np.nan,np.nan,np.nan,np.nan,9,np.nan,np.nan,np.nan,np.nan],
    [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan],
    [np.nan,5,np.nan,np.nan,np.nan,np.nan,np.nan,7,np.nan]
    ])

#scan the horizontal. Return possible values
def x_scan(list_1to9, problem_row):
    return [x for x in list_1to9 if x not in problem_row]

def y_scan(list_1to9, problem_col):
    col_list = [x for x in problem_col]
    return [y for y in list_1to9 if y not in col_list]

def _3x3scan(list_1to9, problem_3x3):

    full_list = [list(x) for ind,x in problem_3x3.iterrows()]
    vals_list = [x for y in full_list for x in y]
    return [z for z in list_1to9 if z not in vals_list]

def find_square(row, col):
    if row in [0,1,2]:
        square_y = 'top'
    elif row in [3,4,5]:
        square_y = 'mid'
    else:
        square_y = 'bot'

    if col in [0,1,2]:
        square_x = 'left'
    elif col in [3,4,5]:
        square_x = 'center'
    else:
        square_x = 'right'
    return(square_y,square_x)

find_index_square = {
    ('top','left'): sudoku_test_df.loc[0:3,list(range(0,3))],
    ('top','center'): sudoku_test_df.loc[0:3,list(range(3,6))],
    ('top','right'): sudoku_test_df.loc[0:3,list(range(6,9))],
    ('mid','left'): sudoku_test_df.loc[3:6,list(range(0,3))],
    ('mid','center'): sudoku_test_df.loc[3:6,list(range(3,6))],
    ('mid','right'): sudoku_test_df.loc[3:6,list(range(6,9))],
    ('bot','left'): sudoku_test_df.loc[6:,list(range(0,3))],
    ('bot','center'): sudoku_test_df.loc[6:,list(range(3,6))],
    ('bot','right'): sudoku_test_df.loc[6:,list(range(6,9))],
}




list_1to9 = list(range(1,10))
for row_count, row in sudoku_test_df.iterrows():
    col_count = 0
    for col in row:
        x_ok_vals = x_scan(list_1to9, sudoku_test_df.iloc[row_count])
        y_ok_vals = y_scan(list_1to9, sudoku_test_df.iloc[:][col_count])
        square = find_index_square[find_square(row_count,col_count)]
        square_ok_vals = _3x3scan(list_1to9, square)

        list_to_use = x_ok_vals
        if len(list_to_use) < len(y_ok_vals):
            list_to_use = y_ok_vals
        if len(list_to_use) < len(square_ok_vals):
            list_to_use = square_ok_vals

        list1 = [x for x in list_to_use if x in y_ok_vals and x_ok_vals and square_ok_vals]  
        num = np.random.choice(list1, size =1)
        sudoku_test_df.at[row_count,col_count] = num
        col_count +=1
