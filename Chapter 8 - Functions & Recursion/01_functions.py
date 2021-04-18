def percent(marks):
    # return ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p
    
# marks = [45, 78, 86, 77]
# percentage1 = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100

# marks2= [75, 98, 88, 77]
# percentage2 = (sum(marks2)/400)*100

marks = [45, 78, 86, 77]
percentage1 = percent(marks)

marks2= [75, 98, 88, 77]
percentage2 =  percent(marks2)

print(percentage1, percentage2)

