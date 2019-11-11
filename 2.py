#4-way formatting index
name=input('name:')
age=int(input('age:'))
job=input('job:')

info=''' ------------info of-----------
Name:{1}
Age:{0}
Job:{2}'''.format(age,name,job)

print(info)