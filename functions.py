# -*- coding: latin-1 -*-
def area_tri(h,b): #definition of functions in python
	return h*b/2 #return the area of a triangle

hojd = int(input("Ange höjd: ")) #converts user input string -> int with int() and sets to variable
bredd = int(input("Ange bredd: "))

area = area_tri(hojd,bredd) #area is set to return value of the function

print("Triangelns area är",area)

#this also works, but makes it more unreadable
print("Triangelns area är",area_tri(int(input("Ange höjd: ")),int(input("Ange bredd: "))))
