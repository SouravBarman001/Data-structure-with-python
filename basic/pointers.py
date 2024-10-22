# For integer, value can not be updated

number1 = 11
number2 = number1

print("after updating number2")
number2 = 22

print("number 1 address",id(number1))
print("number 2 address",id(number2))

# But in dictionary, value of a key can be changed

dic1 = {
    'value':10
}

dic2 = dic1

# after updating dic2
dic2['value'] = 40

print('after updating, dic1 value',dic1)
print("dic1 1 address",id(dic1))
print("dic2 2 address",id(dic2))