print('Hi! Welcome to the Grade Analysis.')
print("Let's start!")

print()

grade1 = int(input('Enter your first grade: '))
grade2 = int(input('Enter your second grade: '))
grade3 = int(input('Enter your third grade: '))
grade4 = int(input('Enter your fourth grade: '))
grade5 = int(input('Enter your fifth grade: '))

grades = []

grades.append(grade1)
grades.append(grade2)
grades.append(grade3)
grades.append(grade4)
grades.append(grade5)

highest = grades[0]
lowest = grades[0]

total = 0
for grade in grades:
    total += grade

average = total/len(grades)
rate = ''

if average >= 90:
    rate = 'Excellent!'
elif average >= 75:
    rate = 'Good!'
elif average >= 50:
    rate = 'Pass'
else:
    rate = 'Fail'

for grade in grades:
    if grade > highest:
        highest = grade
    elif grade < lowest:
        lowest = grade

print()

print("The highest grade is:", highest)
print("The smallest grade is:", lowest)
print("The sum of the grades:", total)
print("Average grade:", average, '—',rate)
