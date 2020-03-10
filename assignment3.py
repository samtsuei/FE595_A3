# Processing first file
with open('Webscrp_company.txt', 'r') as f:
    x1 = f.readlines()

#print(x1)

s1 = str(x1)
s1 = s1.replace('",', '.')
s1 = s1.replace('":','.')
s1 = s1.replace('{','')
s1 = s1.replace('}','')
s1 = s1.replace('"','')
s1 = s1.replace('[\'','')
s1 = s1.replace('\']','')
#print(s1)

l1 = s1.split('.',100)
#print(l1)
n1 = l1[::2]
p1 = l1[1::2]
#print(n1)
#print(p1)

# process second file

with open('text_scrap.txt', 'r') as f:
    x2 = f.readlines()

s2 =str(x2)
#print(s2)

s2 = s2.replace('\',','.')
s2 = s2.replace('\'],','.')
s2 = s2.replace('[\'Name: ','')
s2 = s2.replace('\'Purpose: ','')
s2 = s2.replace('["[','')
s2 = s2.replace('\']]"]','')
#print(s2)

l2 = s2.split('.',100)
#print(l2)
n2 = l2[::2]
p2 = l2[1::2]
#print(n2)
#print(p2)


# open the third file
with open('result.txt', 'r') as f:
    x3 = f.readlines()

s3 = str(x3)
s3 = s3.replace('\\n\',','.')
s3 = s3.replace('\'Name: ','')
s3 = s3.replace('\'Purpose: ','')
s3 = s3.replace('[','')
s3 = s3.replace('\']','')
#print(s3)

l3 = s3.split('.',100)
#print(l3)
n3 = l3[::2]
p3 = l3[1::2]
#print(n3)
#print(p3)

# processing fourth file

with open('name_purpose.txt', 'r') as f:
    x4 = f.readlines()

s4=str(x4)
s4 =s4.replace(' \'\\n", " \'',' ')
s4 =s4.replace(')','')
s4 =s4.replace('(','')
s4 = s4.replace('\'\\n",','.')
#print(s4)
s4 = s4.replace('"\'Name: ','')
s4 = s4.replace('"\'Purpose: ','')
s4 = s4.replace('[','')
s4 = s4.replace('\'\\n"]','')
#print(s4)

l4 = s4.split('.',100)
#print(l4)
n4 = l4[::2]
p4 = l4[1::2]
#print(n4)
#print(p4)

# processing five files

with open('myfile.txt', 'r') as f:
    x5 = f.readlines()

s5 =str(x5)
s5 = s5.replace('\\n\', \'','. ')
s5 = s5.replace('Name: ','')
s5 = s5.replace('Purpose: ','')
s5 = s5.replace('[\'','')
s5 = s5.replace('\\n\']','')
#print(s5)

l5 = s5.split('.',100)
#print(l5)
n5 = l5[::2]
p5 = l5[1::2]
#print(n5)
#print(p5)

# processing sixth file
with open('Company.txt', 'r') as f:
    x6 = f.readlines()

s6 = str(x6)
s6=s6.replace('1','')
s6=s6.replace('2','')
s6=s6.replace('3','')
s6=s6.replace('0','')
s6=s6.replace('4','')
s6=s6.replace('5','')
s6=s6.replace('6','')
s6=s6.replace('7','')
s6=s6.replace('8','')
s6=s6.replace('9','')
s6=s6.replace(')','')
s6=s6.replace('\\n\', \'','. ')
s6=s6.replace('[\'','')
s6=s6.replace('\\n\']','')
#print(s6)

l6 = s6.split('.',100)
#print(l6)
n6 = l6[::2]
p6 = l6[1::2]
#print(n6)
#print(p6)

# processing seventh file

with open('Company Details', 'r') as f:
    x7 = f.readlines()


s7 =str(x7)

s7 = s7.replace('\'Pham-Robertson - A Flask Website\\n\', ','')
s7 =s7.replace('\\n\', \'','. ')
s7 =s7.replace('\'Company Details . ','')
s7 =s7.replace('Name: ','')
s7 =s7.replace('Purpose: ','')
s7 =s7.replace('[','')
s7=s7.replace('\\n\']','')

#print(s7)

l7 = s7.split('.',100)
#print(l7)
n7 = l7[::2]
p7 = l7[1::2]
#print(n7)
#print(p7)

# processing eighth file
with open('companies.txt', 'r') as f:
    x8 = f.readlines()

s8 =str(x8)
s8 =s8.replace('\\t','. ')
s8 =s8.replace('\\n\', \'','. ')
s8 =s8.replace('[\'Name. Purpose. ','')
s8= s8.replace('\\n\']','')
#print(s8)

l8 = s8.split('.',100)
#print(l8)
n8 = l8[::2]
p8 = l8[1::2]
#print(n8)
#print(p8)

# processing ninth file
with open('output_Webscrap_HW2.txt', 'r') as f:
    x9 = f.readlines()

s9 = str(x9)
s9=s9.replace('\\n\', \'Name: ','. ')
s9=s9.replace(',Purpose:','.')
s9=s9.replace('[\'Name: ','')
s9=s9.replace('\\n\', \'\\n\', \'\\n\']','')
#print(s9)

l9 = s9.split('.',100)
#print(l9)
n9 = l9[::2]
p9 = l9[1::2]
#print(n9)
#print(p9)

# processing tenth file
with open('595_HW2.txt', 'r') as f:
    x0 = f.readlines()

s0 = str(x0)
s0 =s0.replace('\\n\', \'Purpose: ','. ')
s0 =s0.replace('\\n\', \'\\n\', \'Name:', '.')
s0= s0.replace('[\'Name: ','')
s0 = s0.replace('\\n\', \'\\n\']','')
#print(s0)

l0 = s0.split('.',100)
#print(l0)
n0 = l0[::2]
p0 = l0[1::2]
#print(n0)
#print(p0)



#Combine purposes
n = n1+n2+n3+n4+n5+n6+n7+n8+n9+n0
p = p1+p2+p3+p4+p5+p6+p7+p8+p9+p0

# Convert purposes to String
#https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/

def listToString(p):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in p:
        str1 += ele + ". "
    # return string
    return str1

# http://rwet.decontextualize.com/book/textblob/

b = listToString(p)
from textblob import TextBlob
s = ""
blob = TextBlob(b)
for sentence in blob.sentences:
        s += str(sentence.sentiment.polarity) + ", "


s = s[:-2]
s = s.split(',',)


#print(len(n))
#print(len(p))
#print(len(s))

# find the top value reference   https://stackoverflow.com/questions/13070461/get-indices-of-the-top-n-values-of-a-list

top_ten = sorted(range(len(s)), key=lambda i: s[i], reverse=True)[1:11]

#print(top_ten)
#print(type(top_ten))

print('Top ten companies based on purpose sentiment')
for item in top_ten:
    print("    ")
    print("Name:"+n[item])
    print("Purpose:"+p[item])
    print(" Sentiment polarity is" + s[item])

bottom_ten = sorted(range(len(s)), key=lambda i: s[i], reverse=True)[490:499]

print("--------------------")
print('Bottom ten companies based on purpose sentiment')
for item in bottom_ten:
    print("    ")
    print("Name:"+n[item])
    print("Purpose:"+p[item])
    print(" Sentiment polarity is" + s[item])
