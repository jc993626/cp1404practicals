# 1
#name = input("Enter your name:")

#out_file = open("name.txt", "w")
#out_file.writelines(name)
#out_file.close()

#2
#in_file = open("name.txt", "r")
#name = in_file.readline()
#print(name)
#in_file.close()

#3
#sum_of_numbers = 0
#with open("numbers.txt", "r") as in_file:
#    for i in range(1, 3):
#        sum_of_numbers += int(in_file.readline())

#    print(sum_of_numbers)

#4
sum_of_numbers = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        sum_of_numbers += int(line)

    print(sum_of_numbers)






