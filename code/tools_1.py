import numpy as np 

## Two commonly used stacking functions： vstack（vertical） 和 hstack（horizontal）

  


corr_matrix = lambda d: np.ma.corrcoef(np.ma.masked_invalid(np.array([np.array(m).flatten() for m in d]))).data
# code below is a more detailed version of the lambda function above 
def calculate_correlation_matrix(data_list):
    flattened_arrays = []
    for array in data_list:
        array = np.array(array)
        flattened = array.flatten()
        masked_array = np.ma.masked_invalid(flattened)
        flattened_arrays.append(masked_array)
    
    stacked_arrays = np.ma.vstack(flattened_arrays)
    correlation_matrix_masked = np.ma.corrcoef(stacked_arrays)
    correlation_matrix = correlation_matrix_masked.data
    return correlation_matrix
