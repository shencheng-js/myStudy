from collections import OrderedDict

favourite_language = OrderedDict()

favourite_language['mao']='python'
favourite_language['zhou'] = 'C'
favourite_language['zhu'] = 'ruby'
favourite_language['peng'] = 'python'

for name,language in favourite_language.items():
    print(name+"'s favourite language is "+language.title()+".")