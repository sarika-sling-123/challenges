from challenge4 import Fibonacci
from challenge4 import NumToWord

fb=Fibonacci.Fibonacci()
nw=NumToWord.NumToWord()

# Considering the fibonacci series starting from 0
# 0,1,1,2,3,5,8,13,21,34,...

class Challenge4:
    print(str(fb.getFibonacci(8))+" - "+nw.convertToWord(fb.getFibonacci(8)))

