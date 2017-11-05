#running in python3
def hello(name):
    print ("Hello,%s" % name)

name = input("Please input your name ")
if name == "":
    name = "world"
hello(name)
