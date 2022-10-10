import hashlib


str = "GeeksforGeeks"


result = hashlib.sha256(str.encode())


print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())

print ("\r")


str = input("Enter the string")

result = hashlib.sha384(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA384 is : ")
print(result.hexdigest())

print ("\r")


str = input("Enter the string")


result = hashlib.sha224(str.encode())


print("The hexadecimal equivalent of SHA224 is : ")
print(result.hexdigest())

print ("\r")


str = input("Enter the string")

result = hashlib.sha512(str.encode())

print("The hexadecimal equivalent of SHA512 is : ")
print(result.hexdigest())

print ("\r")


str =input("Enter the string")


result = hashlib.sha1(str.encode())


print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
