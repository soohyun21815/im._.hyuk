a = "Life is too short, You need python"

print(a[-1])
print(a[:7:1]) # a[이상:미만:간격]

a = "I eat %s apples. So I was sick for %s days." %(1.2, 5)
print(a)



b = "My name is {name}, {age} years old".format(name="ljh",age=26)
print(b)

name = 'ljh'
age = 26
c = f"My name is {name}, {age} years old"
print(c)
