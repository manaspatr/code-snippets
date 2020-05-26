#assigning elements to different lists
#we can keep different types of elements in a list
names =['mkp','john','johny']
print(names)
#output of this will be ['mkp,'john','johny']
#elements in a list are always assigned in a square brackets with'='sign
#elements in list can be strings or integers
#we can have random lists,nested lists and also can have empty lists
random_list = [1,'ball',10.7]
nested_list =[1,[2.3],[4,5,6]]
empty_list =[]
#accssing elements from tuple
#tuple can be accessed by round brackets 
my_tuple =("c","c++","java")
print(my_tuple)
#out put will be ('c','c++','java')
#it also supports index-based access
print(my_tuple[1])
#output will be c++
#deleting elements from a dictionary
my_dict ={"c":"easy","c++":"moderate","java":"tough","python":"cool"}
del my_dict["c"]
print(my_dict)
#out put will be {'c++':'moderate','java':'tough','python':'cool'}
