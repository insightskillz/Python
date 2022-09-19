def main():
    print("This is the function's file")
    for i in inclusive_range(25):
        print(i, end='  ')


def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError("requires at least one argument")
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step =1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('Inclusive_range expected at most 3 arguments, got {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step


if __name__=="__main__":main()
                                    
