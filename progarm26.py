str=" Rahul is Drinking "
print(str)
# to remove statring space
str1=str.lstrip()
print(str1)
#to remove end space
str2=str.rstrip()
print(str2) #but left side will there only removed in right side

#to remove right and left space(staring and ending
str3=str.strip()
print(str3)
# remove space between text
str4="U M A"
print(str4)

str5=""
for i in str4:
    if i==" ":
        pass
    else:
        str5=str5+i
print(str5)
