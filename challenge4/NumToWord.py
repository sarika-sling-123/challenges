class NumToWord(object):
    def __init__(self):
        self.below20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]

    def convertToWord(self,num):
        if(num==0):
            return "Zero"
        ret=""
        for i in range(len(self.thousands)):
            if(num%1000)!=0:
                ret=self.helper(num%1000)+self.thousands[i]+" "+ret
            num=int(num/1000)
        return ret.strip()

    def helper(self,num):
        if(num==0):
            return ""
        elif(num<20):
            return self.below20[int(num)]+" "
        elif(num<100):
            return self.tens[int(num/10)]+" "+self.helper(int(num%10))
        else:
            return self.below20[int(num/100)]+ " Hundred "+self.helper(int(num%100))



