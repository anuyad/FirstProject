#def print_something(name, age):
#    print("My name is " + name + " and my age is " + age)
#print_something("Anvit", 13)
#result-     print("My name is " + name + " and my age is " + age)
#TypeError: must be str, not int

#def print_something(name, age):
#    print("My name is " + name + " and my age is " + str(age))
#print_something("Anvit", 13)
#result - My name is Anvit and my age is 13

#def print_something(name, age):
#    print("My name is", name, "and my age is", age)
#print_something("Anvit", 13)
#result - My name is Anvit and my age is 13

#def print_something(name="something", age="unknown"):
#    print("My name is", name, "and my age is", age)
#print_something("Anvit")
#Result - My name is Anvit and my age is unknown

def print_something(name="something", age="unknown"):
    print("My name is", name, "and my age is", age)
print_something()
#result - My name is something and my age is unknown