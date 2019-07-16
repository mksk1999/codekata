n=input()
n.lower()
if(n=='a'or n=='e' or n=='i' or n=='o' or n=='u'):
    print("Vowel")
elif(n>='b' and n<='z' and n!='e' and n!='i' and n!='o' and n!='u'):
    print("Consonant")
else:
    print("invalid")
