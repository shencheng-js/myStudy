age=13
if age>20:
    print('20')
elif age>15:
    print('15')
elif age>12:
    print('12')
elif age>11:
    print('11')

#不只是python，很多语言的elif都是从小范围到大范围

#elif是短路的，只要有一个新就行，而if完全不同，多个if他会按顺序往下走
