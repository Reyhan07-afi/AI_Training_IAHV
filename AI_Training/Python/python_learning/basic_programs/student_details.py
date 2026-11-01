def calculate_total(mark1,mark2,mark3):
    total = mark1+mark2+mark3
    return total
def avg_mark(mark1,mark2,mark3):
    avg = (mark1+mark2+mark3)/3
    return avg



#driver
rollno = int(input('Enter roll no: '))
sname = input('Enter student name: ')
m1=int(input('Enter m1: '))
m2=int(input('Enter m2: '))
m3=int(input('Enter m3: '))

total_marks = calculate_total(m1,m2,m3)
avg_marks = avg_mark(m1,m2,m3)

print(f'Roll.No:{rollno} \n Name:{sname} \n Total:{total_marks}')
print(f'Average marks:{avg_marks}')