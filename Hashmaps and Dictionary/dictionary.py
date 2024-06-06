#ceating a dictionary
temp_dict={
    "Sam":10,
    "Harry":20,
    "Annie":30
}

#printing a dictionary
for key in temp_dict:
    print("marks of ",key," = ",temp_dict[key])

#to update dictionary
temp_dict.update([("Sasha",15),("Ruth",24)])
print(temp_dict.keys())

#delete any element 
marks=temp_dict.pop("Harry") #stores the deleted value
del(temp_dict["Annie"]) #doesn't store the deleted value
print(marks)
temp_dict.clear() #clears all the elements from dictionary
print(temp_dict)
