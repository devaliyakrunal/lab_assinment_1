account=int(input("ebter account marks:"))
physics=int(input("ebter physics marks:"))
science=int(input("ebter science marks:"))
maths=int(input("ebter maths marks:"))
economic=int(input("ebter economic marks:"))

total=account+physics+science+maths+economic
per=total/5

if per>=90:
  grade='A'

elif per>=80:
  grade='B'

elif per>=50:
  grade='C'

elif per>=35:
  grade='D'

else :grade='reappear'

print("total:",total)
print("percentage:",per)
print("grade:",grade)
