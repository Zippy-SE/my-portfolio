NOMAINWIN
Parents = 2
Whacks = 20
MotherAxWhacks = Parents * Whacks
FatherAxWhacks = MotherAxWhacks + 1
FirstName$ = "Lizzie"
LastName$ = " Borden"
FullName$ = FirstName$ + LastName$
'An underscore at the end of a line means to continue the code on the next line
NOTICE FullName$ + " had an ax, gave her mother " _
+ chr$(13) + str$(MotherAxWhacks) + " whacks. When she saw what" _
+ chr$(13) + "she had done, she gave her father " _
+ str$(FatherAxWhacks) + "."
'chr(13) is a carriage return (new line)
'str$() converts a number to a string
END

