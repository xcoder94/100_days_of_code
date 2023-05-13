# Open file: first way
# my_file = open('my_file.txt')
# contents = my_file.read()
# print(contents)
# my_file.close()

# Open file: second way "with" keyword
# Only reading mode
# with open('my_file.txt') as f:
#     contents = f.read()
#     print(contents)

# Write mode with 'w' after file path. If file doesn't exist, will create file
# with open('newfile.txt', 'w') as f1:
#     # Delete all data in file and writes new data
#     f1.write('\nnew text line write mode')
#     print(f1)

# Append mode with 'a' after file path
with open('/home/epamanager/Desktop/my_file.txt', mode='a') as f2:
    f2.write('\nnew text line2 append mode')
    print(f2)




# Hello. My name is Xon. 
# I'm 30 years old.
# My favourite food is a bowl of hot noodles





