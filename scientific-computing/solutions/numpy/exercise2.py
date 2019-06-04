a_col_max = a.max(axis=1)
print(a_col_max)
a_row_mean = a.mean(axis=0)
print(a_row_mean)
i_j_index_min = np.argwhere(a == a.min()) # Find index of the overall minimum
print(i_j_index_min)