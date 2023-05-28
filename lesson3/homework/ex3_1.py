instring=input("type your name: ")
strlist=[x.center(3) for x in instring]
strlist.append("")
strlist.insert(0,"")
strlist_joined="|".join(strlist)


line="+---" * len(instring)+"+"

print(line)
print(strlist_joined)
print(line)
