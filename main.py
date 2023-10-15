print("hello python!")

# checking number is even or not
num = int(input("Enter a number:"))
if num % 2 == 0:
    print(num, "is even!")
else:
    print(num, "is not even!")

def is_even(num):
    if int(num) % 2 == 0:
        return "Even!"
    return "Not even!"

print(is_even(10))

# finding the biggest number
n1 = 85
n2 = 434
n3 = 98
max_n = 0
if n1 > n2:
    max_n = n1
else:
    max_n = n2
if n3 > max_n:
    max_n = n3
print(max_n)

# checking a country is included in saark
saarc = ["Afghanistan", "Bangladesh", "Bhutan", "India", "Nepal", "Pakistan", "Sri Lanka"]
country = input("Enter your country name:")
if country in saarc:
    print(country, "is a member of saark!")
else:
    print(country, "is not a member of saark!")
