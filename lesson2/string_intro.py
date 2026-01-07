a="hello"
b='world'

print( "hello world")
name = input("Enter your name: ")
print("Hello, " + name + "!")   
print(f"Hello, {name}!")
print("Hello, {}".format(name)) 
print("Hello, %s!" % name)
print(a + " " + b)
print(a * 3)
print(len(a))
print(a[0])
print(a[1:4])
print(a.lower())
print(a.upper())
print(a.replace("h", "H"))
print(a.split("e"))
print("world" in b)
print("WORLD" not in b)
print(a.startswith("he"))
print(b.endswith("ld"))
print(a.find("l"))
print(a.count("l"))
print(a.isalpha())
print(a.isdigit())
print(a.strip())
print(a.center(20, '*'))
print(a.ljust(20, '-'))
print(b.rjust(20, '+'))
print(a.index("e"))
print(a.capitalize())
print(a.title())
print(a.swapcase())
print(a.encode())
print(b.format())
print(a.partition("l"))
print(b.rpartition("r"))
print(a.zfill(10))
print(b.islower())
print(a.isupper())
print(a.translate(str.maketrans("h", "H")))
print(b.replace("o", "0", 1))   
print(a.splitlines())
print(b.join(["Hello", "there"]))
print(a * 2 + " " + b * 2)
print(f"{a} {b}")
print("{} {}".format(a, b))
print("%s %s" % (a, b))
print(a + b == "helloworld")
print(a + b != "helloworld")
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)   
print(a != b)
print(a is b)   
print(a is not b)
print(id(a))
print(id(b))
print(type(a))
print(type(b))
print(isinstance(a, str))
print(isinstance(b, str))
print(isinstance(a, int))
print(isinstance(b, float))


name = "Alice"
age = 30
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")
print("Hello, my name is {name} and I am {age} years old.".format(name=name, age=age))
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")
print("My name is %s and I am %d years old." % (name, age))


name1 = "Bob"
name2 = "Charlie"
print(f"{name1:<10} -first name")
print(f"{name2:<10} -last name")










