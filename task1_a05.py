                          # Task 1: Create a Dictionary of Student Marks
dict = {'shubham':'44','pritikana':'94','pritshu':'69','bhamtika':'96','shubh':'41'}
userinput = input("enter the students name:")
if userinput in dict:
    print(f"{userinput}'s marks: {dict[userinput]}")
else:
    print("student name is not found")


# output
# enter the students name:shubh
# shubh's marks: 41
