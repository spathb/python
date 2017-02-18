import os
    
old = "test1/doc1.txt"
new = "test2/doc1.txt"

os.rename(old,new)
print(os.path.abspath(new))

old = "test1/doc2.txt"
new = "test2/doc2.txt"

os.rename(old,new)
print(os.path.abspath(new))

old = "test1/doc3.txt"
new = "test2/doc3.txt"

os.rename(old,new)
print(os.path.abspath(new))

old = "test1/doc4.txt"
new = "test2/doc4.txt"

os.rename(old,new)
print(os.path.abspath(new))

