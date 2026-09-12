<<<<<<< HEAD
colors=["Yellow","Orange","Green","Blue","Black","200","567","65.5"]
print(colors)

lengths=[len(i) for i in colors]
print(lengths)
cap_colors=[ i.upper() for i in colors]
lwr_colors=[ i.lower() for i in colors]
print(cap_colors,lwr_colors)

numbers=[i.isdigit() for i in colors]
print(numbers)

marks=[35,50,74,24,39,21]
result=["pass" if m>35 else "Fail" for m in marks]
print(result)

print(["Good" if i>50 else "Fair" for i in  marks])

=======
colors=["Yellow","Orange","Green","Blue","Black","200","567","65.5"]
print(colors)

lengths=[len(i) for i in colors]
print(lengths)
cap_colors=[ i.upper() for i in colors]
lwr_colors=[ i.lower() for i in colors]
print(cap_colors,lwr_colors)

numbers=[i.isdigit() for i in colors]
print(numbers)

marks=[35,50,74,24,39,21]
result=["pass" if m>35 else "Fail" for m in marks]
print(result)

print(["Good" if i>50 else "Fair" for i in  marks])

>>>>>>> d9ee51f0cc5c114ccd731eff574942c21419d1af
print(["even" if n%2==0 else "odd" for n in marks])