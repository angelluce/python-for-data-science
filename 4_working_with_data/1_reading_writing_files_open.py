fileRead = open("../resources/open.txt", "r")
fileWrite = open("../resources/write.txt", "w")

# code to read a file

txt = fileRead.read()

print(txt)

fileRead.close


# code to write a file

message = "Hola Mundo\nI'm writing a file with open method."

fileWrite.write(message)
