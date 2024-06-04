#!/usr/bin/python3

def new_student(name, age, course):
    list_sample.append({'Name': name, 'Age': age, 'Course': course})


list_sample = [
    {
        'Name': 'Suhas',
        'Age': 24,
        'Course': 'Basic'
    },
    {
        'Name': 'Amos',
        'Age': 28,
        'Course': 'Intermediate'
    },
    {
        'Name': 'John',
        'Age': 21,
        'Course': 'Advanced'
    }
]

new_student(age=18, name='Nelly', course='C++')

print(list_sample[len(list_sample)-1])
print(list_sample)
