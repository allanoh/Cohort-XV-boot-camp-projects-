"""allan gogo 7/2/2017"""
def fizz_buzz(args):
    """ Checking if the number is divisible by both 3 and 5"""
    if args % 3 == 0 and args % 5 == 0:
        return "FizzBuzz"
    elif args % 3 == 0:
        return 'Fizz'
    elif args % 5 == 0:
        return 'Buzz'
    else:
        return args
