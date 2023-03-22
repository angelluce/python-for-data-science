# Python Programming Fundamentals

## Glossary

| Term       | Definition |
| ---------- | ---------- |
| Data Frame | A data structure comprising rows and columns much like a spreadsheet. A data frame can be created from a dictionary. The keys correspond to column labels. The values or lists correspond to the rows. A data frame is one of the most popular data structures used in data analytics. |
| Hadamard Product | The product of two arrays. Multiplication of two arrays corresponds to an element-wise product. The number of columns of the first array must equal the number of rows in the second in order to multiply them. |
| ndim | An attribute that obtains the number of dimensions of a NumPy array. It can be thought of as the number of nested lists in the array. |
| NumPy | A Python library for scientific computing. |
| NumPy Array | An array that is similar to a list and usually fixed in size. Each element is of the same type. |
| Pandas | A popular Python library for data analysis. |


## Cheatsheet

| Class or Method | Description | Example     |
| --------------- | ----------- | ----------- |
| `close()` | Closes a file. | `file1.close()` |
| `dot` | Calculate the dot product from two NumPy arrays. | `np.dot(U, V)` |
| `dtype` | Check the type of values stored in a NumPy array. | `myArray.dtype` |
| `linspace()` | Returns evenly spaced numbers over a specified interval. |
| `matplotlib.pyplot` | A library of functions that make matplotlib behave similar to MATLAB. | `import matplotlib.pyplot as plt` </br> `plt.plot([1, 2, 3, 4])` </br> `plt.xlabel("time")` </br> `pltylabel("distance")` </br> `plt.show()` |
| `max` | Get the largest value from a NumPy array. | `myArray.max` |
| `mean` | Get the mean of a NumPy array. | `myArray.mean` |
| `ndim` | Get the number of dimensions of a NumPy array. | `myArray.ndim` |
| `numPy` | A library used for working with arrays as well as functions for working with linear algebra, matrices, and Fourier transform. | `import numpy as np` |
| `open()` | Opens a file. | `file1=open(example1, "r")` |
| `pi` | The value of pi. | `np.pi` |
| `read()` | Reads a file. | `FileContent=file1.read()` |
| `readline()` | Reads the first line of the file. | `with open(example1, "r") as file1:` </br> `print("first line: " + file1.readline())` |
| `shape` | A tuple of integers that indicates the size of a NumPy array in each dimension. | `myArray.shape` |
| `sin()` | Calculate the sine of all elements in a NumPy array. | `y=np.sin(x)` |
| `size` | Get the size of a NumPy array. | `myArray.size` |
| `std` | Get the standard deviation of a NumPy array. | `myArray.std` |
| `T` | Transpose a NumPy array. | `my2DArray.T` |
| `with open() as` | Opening a file using the keyword “with” automatically closes the file after the code in the with statement is executed. | `with open(example1, "r") as file1:` </br> `FileContent = file1.read()` </br> `print(FileContent)` |
| `write()` | Writes a line to a file. write() takes two arguments, the pathname/URL and a mode. Passing the parameter ‘w’ as the mode overwrites all existing data. Passing ‘a’ as the mode appends the data. | `exmp2 = '/resources/data/Example2.txt'` </br> `with open(exmp2, 'w') as writefile:` </br> `writefile.write("This is line A")` |
