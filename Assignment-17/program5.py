"""5. Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}"""
firstset={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
firstset.update(secondset)
print(firstset)
