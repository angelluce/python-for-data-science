# Python Basics for Data Science

## Glossary

| Term       | Definition |
| ---------- | ---------- |
| Argument | The input to a function. Same as “parameter.” |
| Class | A template that defines a data structure’s behavior (methods) and attributes. |
| Comparison Operator | An operator that compares two operands and produces a Boolean value. |
| Constructor | A method that is used to instantiate an object. |
| elif | A statement short for “else if” that checks additional conditions if the preceding condition is false. |
| Exception Handling | The encasing of code within a function so the program knows how to handle an anomalous condition. |
| Finally Statement | A block of code that executes if no other previous conditions are met. |
| Function | A procedure that takes an input and transforms it to produce an output. |
| Global Variable | A variable that is accessible in any part of a program. |
| Local Variable | A variable that is only accessible to a particular function. |
| Loop | An instruction that performs a task over and over until an exit condition is met. |
| Object | An instance of a class. Objects can be passed as arguments to functions. |
| Parameter | The input to a function. Same as “argument.” |
| Scope | The part of a program where a particular variable is accessible. |
| Variadic Function | A function that takes a variable number of arguments. |



## Cheatsheet

| Operators/Keywords/Statements | Description | Example |
| ----------------------------- | ----------- | ------- |
| ```==, !=, >, <, >=, <=``` | Comparison operators. Return a Boolean. | a = 5 </br></br> #b is false </br></br> b=a==6 |
| ```if <comparison>: <code runs when comparison is true>``` | Runs code based on true evaluation of the if argument. | #expression that can be true or false </br></br> if age > 18: </br></br> #within an indent, we have the expression that is run if the condition is #true </br></br> print("you can enter") </br></br> #The statements after the if statement will run regardless if the condition is true or false  </br></br> print("move on") |
| ```if <comparison>: <code that runs when comparison is true> else: <code that runs when comparison is false>``` | Runs code based on evaluation of the if argument. If the argument is false runs the code that follows the else statement. | # if=else statement example weather = “sunny” </br></br> # weather = “cloudy” </br></br> if weather == “sunny”: </br></br> print("The sun is out today") </br></br> else: </br></br> print("Looks like it might rain")
| ```elif``` | Similar to else if but allows for else if statements as well. | # If-elif statement example </br></br> age = 18 </br></br> if age > 18: </br></br> print("you can enter") </br></br> elif age == 18: </br></br> print("go see Pink Floyd") </br></br> else: </br></br> print("go see Meat Loaf") |
| ```for loop``` | Continue to do something while iterating through a list. | dates = [1982,1980,1973] </br></br> for year in dates: </br></br> print(year) |
| ```while loop``` | Continue to do something as long as while statement is true. | # While Loop Example </br></br> dates = [1982, 1980, 1973, 2000] </br></br> i = 0 </br></br> year = dates[0] </br></br> while year != 1973: </br></br> print(year) </br></br> i = i + 1 </br></br> year = dates[i] </br></br> print("It took ", i ,"repetitions to get out of
loop.") |
