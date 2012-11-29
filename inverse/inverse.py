from second_code import Bars
from third_code  import decode_morse

bs = first = Bars("ITT TI I T TIii")

for i in range(50000):
    print str(bs)+"         answer: " + decode_morse(str(bs))
    bs.next()
    if str(bs) == "ITT TI I T TIii":
        break