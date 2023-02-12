# Import math Library
import math

def main():
    print("Hello World!")
    # nieuweVermogen = compoundInterestMaandelijksInleg(10, 100)
    # print("nieuwe vermogen na 10 jaar elke maand 100 euro inleg: " + str(nieuweVermogen))

    nieuweVermogen = compoundInterestEenmaligInleg(10, 1000)
    print("nieuwe vermogen na 10 jaar met eenmalige inleg van 1000 euro: " + str(nieuweVermogen))

def compoundInterestEenmaligInleg(aantalJaar, eenmaligeInleg):
    # print("aantal jaar: " + str(aantalJaar))
    # print("inleg: " + str(eenmaligeInleg))

    result = eenmaligeInleg * 1.07**aantalJaar
    return result











def compoundInterestMaandelijksInleg(aantalJaar, inlegMaandelijks):
    print(f"aantal jaar: {str(aantalJaar)}")
    print("inleg: " + str(inlegMaandelijks))
    sum = 0
    
    first = 0
    last = aantalJaar - 1

    for a in range(first, last + 1): 
        print(f"sum = {sum} + {inlegMaandelijks} * 1.07^{a}")
        print("wordt:")
        print(f"sum = {sum} + {inlegMaandelijks * 1.07**a}")
        print("wordt")
        print(f"sum = {sum + (inlegMaandelijks * (1.07**a))}")
        print()
        
        sum = sum + inlegMaandelijks * math.pow(1.07,a)
        
    
    return sum










if __name__ == "__main__":
    main()

