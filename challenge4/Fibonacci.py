

# Considering the fibonacci series starting from 0
# 0,1,1,2,3,5,8,13,21,34,...

class Fibonacci(object):
    def getFibonacci(self,num):
        if(num==0):
            return 0
        elif(num==1):
            return 1
        else:
            return self.getFibonacci(num-1) + self.getFibonacci(num-2)