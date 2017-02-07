"'allan gogo 7/feb/2016"
def data_type(args):
    if isinstance(args, str): #checks ifg the input is a string
        return len(args)
    elif args is None:  #checks if the input is a blank,if blank it returns "no value"
        return 'no value'
    elif isinstance(args, bool):   #checks if the input is a a boolean,if boolean it returns the input value
        return args
    elif isinstance(args, int):  #checks if the inputted value is greater,lesser or equal to 100
        if args > 100:
            return 'more than 100'
        elif args < 100:
            return 'less than 100'
        else:
            return 'equal to 100'
    elif isinstance(args, list):
        if len(args) > 2:
            return args[2]
        else:
            return None
