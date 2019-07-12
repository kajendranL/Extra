#even string

def evenstr(str):
    for i in range(0, len(str), 2):
        print("index [",i,"] is: ",str[i])
inputstr=input("Enter a string:")
print("The original string is:", inputstr)

print("The even strings are:")
evenstr(inputstr)


print()

#Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

def findDivisible(numlist):
    for num in numlist:
        if (num % 5 ==0):
            print(num)
numberlist=[12,56, 53 ,56 ,95 ,687,94,65]
print("Find the numbers that are divisible by 5 below")
findDivisible(numberlist)

print()
#Question 7: Return the number of times that the string “Emma” appears anywhere in the given string

def count_word(pharse):
    count=0
    for i in range(len(pharse)-1):
        count+=pharse[i:i+4] == 'yazh'
        return count
count = count_word("yazh is my daughter. yazh went to school now. yazh  is sister of Epifano")
print("The word 'yazh' appeared", count, "times")
# The word 'yazhini' appeared 1 times??????????????????????????????????????