letter=('''Dear,<NAME>
                Hope you are doing well.it is to inform you that you have been selected
                in BSSE program you can submit your fees till 11 jan
                                        Thanks
                date                        ''')
name=input("Enter your name\n")
date=input("enter date\n") 
print(letter.replace("<NAME>",name))                                       
#letter=letter.replace("<NAME>",name)  
#letter=letter.replace("date",date)
#ali=letter.endswith("thanksshayan")  
#print(ali)
#print(letter)