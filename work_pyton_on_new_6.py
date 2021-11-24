str1 = input()
str2 = input()
 
if (('да' or 'нет') in (str1 and str2)):
    print('ВЕРНО')
elif (('нет' or 'да') in (str1 and str2)):
    print('ВЕРНО')
else:
    print('НЕВЕРНО')

