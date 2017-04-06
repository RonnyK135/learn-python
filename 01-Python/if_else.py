# print absolute value of an integer:
a = 100
if a >= 0:
    print a
else:
    print -a

a = raw_input('Plz enter a number whose absloute value you want to get:')
if a < 0:
    a = a*(-1)
    print "the absloute value is:", a 
else:
    print "the absloute value iss:" ,a
