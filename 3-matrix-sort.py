
# # matrix = read_matrix('testmatrix0.txt')
# print(read_matrix('testmatrix0.txt'))

from starter import read_matrix


first_matrix = [   
                 [10, 5, 4, 20],
                 [9, 33, 27, 16],
                 [11, 6, 55, 3]     ]


def matrix_row_sums(matrix):
    """ finds the row sums """
    sum_list = [sum(each_list) for each_list in matrix]
    sum_string = "Row Sums: " + " ".join(str(i) for i in sum_list)
    return sum_string

print(matrix_row_sums(first_matrix))
 

def matrix_column_sums(matrix):
    """ finds the column sums """
    sum_list = []
    length_of_matrix = len(matrix)
    for i in range(length_of_matrix):
        total = 0
        for each_list in matrix: 
            total += each_list[i]
        sum_list.append(total)
    sum_string = "Column Sums: " + " ".join(str(i) for i in sum_list) 
    return sum_string

print(matrix_column_sums(first_matrix))

#### the two above work perfectly on their own here...
#### might need to alter to use the key=function sorting method for the second part

def matrix_sort(matrix):
    my_dict = {}
    for i in 
    for i in (matrix_row_sums(matrix))










# def short_matrix_row_sums(matrix, key):
#     """ finds the row sums quickly"""
#     my_sum = sum(matrix[key])
#     return my_sum


print(sorted(first_matrix, key=short_matrix_row_sums))
print(sorted(first_matrix, key=short_matrix_column_sums))



# print(matrix_sort_rows(matrix))
# print(matrix_sort_columns(matrix))



    

