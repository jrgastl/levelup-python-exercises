'''
Author Notes:
Here I applied what I learned in the JSON chapter of the Python Essential Training course, also part of this certificate.
The instructor used a different approach, using the pickle module.
'''
import json
#Function to take a python dictionary object to file.
def save(py_dict,path):
    with open(path,'w') as f:
        f.write(json.dumps(py_dict))

#Function to load the saved dictionary back to python.
def  load(path):
    with open(path, 'r') as f:
        return json.loads(f.read())



# Please, uncomment the lines below to execute the code with the example given

# my_dict = {'a':1,'b':2,'c':3}
# save(my_dict,'./dictionaries/PythonDictionary.txt')
# recovered = load('./dictionaries/PythonDictionary.txt')
# print(recovered)