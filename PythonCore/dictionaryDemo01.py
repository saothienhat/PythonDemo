dicto = {'Bookname' : 'Python', 'Price' : 210, 'Author': 'TutorialsCloud'}

print (dicto['Bookname'])
print (dicto['Price'])

# Create new Dict
newDict = {}
newDict['first'] = 10
newDict['second'] = 20
print("First element of newDict has value: ", newDict['first'])


#Adding new entries
newDict ['Author'] = 'TutorialsCloud' ;
newDict ['Discount']= '10 Percent';

#Updating an Entry
newDict ['Price']  = 200;


# Deleting Dictionary
del dicto['Price'];
# It deletes only the key with the name 'Price'

dicto.clear();
# The above code removes all entries in dictionary & makes the dictionary empty

del dicto
# The above code Deletes the entire dictionary
