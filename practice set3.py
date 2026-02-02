# # # name = input("Enter your nme:")
# # # print(f"Good afternoon, {name} ")
# # letter = '''Dear <|Name|>,
# #          you are selected!
# #            <|Date|> '''
# # print(letter.replace("<|Name|>","Shivam").replace("<|Date|>","09 october 2025"))
# name = "Shivam  is  a  good  boy   "
# print(name.find("  "))

#Below the given code is LIST👇
friends = ["Apple","Orange","Mango",3.67,False,True,"Shivam","Satyam"]
print(friends[2])
friends[2] = "Roshan"
print(friends[2])
print(friends[0:4])
print(friends[0:])
friends.append("Roy")
print(friends)

li = [23,34,3,4,3,9]
# li.sort()
# li.reverse()
# li.insert(3,78)
# li.pop(2)
print(li.pop(2))
print(li)


#👇tuple
a = (1,5,6,8,45,63,34,34,"Shivam","Roshan")
print(a)
print(type(a))
#method of tuple
no = a.count(34)
print(no)

repeated = a*4
print(repeated)

print(2 in a)
print(6 in a)
print(len(a))#len stands for length of tuple




