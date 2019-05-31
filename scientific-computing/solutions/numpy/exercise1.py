x = np.arange(25).reshape(5, 5)
x_yellow = x[4]
x_red = x[:, 1::2]
x_blue = x[1::2, 0:3:2]
print(f'x = \n{x} \nx_yellow = \n{x_yellow} \nx_red = \n{x_red} \nx_blue = \n{x_blue}')