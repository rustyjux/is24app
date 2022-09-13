def fizzbuzz(i):
    return ("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i)

def main():
    for i in range(1,101): # could add an exception for these lines if you were confident they were solid
        print(fizzbuzz(i))

if __name__ == '__main__': # pragma: no cover
    main()