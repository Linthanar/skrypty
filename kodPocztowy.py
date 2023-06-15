import re
# kod = input()
# XX-XXX
# X = {0-9}
# print(kod)

txt = "30-163"
x = re.search("[0-9]{2}-[0-9]{3}", txt)
if(txt==x):
    print('pasuje')
else: 
    print('nie pasuje')