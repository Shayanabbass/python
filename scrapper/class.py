from base64 import decode
from fileinput import filename


class physicalfile:
    def __init__(self, filename , filesize,date):
        self.filename=filename
        self.filesize=filesize
        self.date=date


    def assignvalues(self) :
        print(self.filename, self.filesize,self.date)
    

p1=physicalfile("hxmhx",222,6666)
p1.assignvalues()



     
        

