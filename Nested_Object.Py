#Solution of Nested Object value extraction using Python
#Extracts the list of keys of a Nested object along with the value of keys with object and keys passed into function


#Method for extracting list of keys of nested object
def get_key_list(dict_object):
     for key, value in dict_object.items():
         key_list.append(key)
         if type(value) is dict:            
             yield from get_key_list(value)
         else:             
             yield key_list
       
#Method for extracting the values corresponding to the given key
def get_nested_value(dict_object, key_list):

   for k in key_list:
         dict_object = dict_object.get(k, None)
         if dict_object is None:
             return None
   return dict_object

#Initialize empty list for storing the list of keys
key_list = []

#Initialize the nested object
Nested_Obj = {"a":{"b":{"c":1}}}

#Call the get_key_list function and print the value of key_list
for key in get_key_list(Nested_Obj):
     print(key)
     
   
#Some test cases by passing Nested object and different types of keys in the function get_nested_value

print(get_nested_value(Nested_Obj,key_list))    #1
print(get_nested_value(Nested_Obj,['bar','a'])) #None
print(get_nested_value(Nested_Obj,['a','b']))   #{'c': 1}
print(get_nested_value(Nested_Obj,['b','a']))   #None
print(get_nested_value(Nested_Obj,['a']))       #{'b': {'c': 1}}


        
        
       
     

