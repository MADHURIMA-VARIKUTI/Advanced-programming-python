import re 

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
fo = open('madhu_email.txt', 'r')
lines = fo.readlines()
fo.close()

fo = open('madhu_validemail.txt', 'w');
for line in lines: 
    if re.match(regex, line):
        fo.write(line)
        print(line)
fo = open('madhu_invalidemail.txt', 'w');
for line in lines: 
    if not re.match(regex, line):
        fo.write(line)
        print(line)

fo.close()

# madhurima@gmail.com
# hi@ap@gmail.com
