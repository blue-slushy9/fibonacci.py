# Throughout this program, I use many print() statements to enhance legibility
# in the terminal, e.g. below;
print()
print("This program takes an integer as input and outputs the first numbers\n" 
        "in the Fibonacci sequence equal to the value of the integer.\n" 
        "Please enter your integer now...")
print()

num = int(input())
print()

####################### DEFINE FIBONACCI FUNCTION

# n is the number of values in the Fibonacci sequence the user wants to see,
# e.g. if they enter 100 then they should see the first 100 numbers of the 
# sequence;
def fibonacci(n):
    
    # The 0th number of the Fibonacci sequence doesn't exist, nor do -nth 
    # numbers thereof, so we get an error if the user enters such a value;
    if n <= 0:
        err_msg = print("Invalid input\n")
        return err_msg
    
    # The first number of the Fibonacci sequence, in this case, is 0;
    # in some representations, the first number is 1, but we start with 0;
    elif  n == 1:
        return 0
    
    # Anything beyond that and we actually need to calculate the sequence,
    # so we define a function that will do it; we do not know how many numbers
    # in the Fibonacci sequence the user will want to see, so we cannot define
    # it ahead of time---it must be done at run-time;
    else:

################### DEFINE GENERATOR FUNCTION

        # This is a special function called a generator function;
        def fib_gen(n):
            
            # We can calculate the Fibonacci sequence using only the first two
            # numbers therein, because the formula simply adds the last two 
            # numbers together to create the next value, and so on;
            seq = [0,1]
            
            # x is our variable we use to track where in the entire span (n)
            # of the Fibonacci sequence we currently are, ergo we start at 0
            # because seq is a list and we are counting its elements computer
            # style;
            x = 0
            
            # The thing about n is that it is a counter that is NOT in
            # computer-style, i.e. it starts counting at 1 rather than 0;
            # ergo we have to subtract 1 from n in order to get it and x at
            # the same numerical value;
            while x <= (n - 1):
                
                # If x is 0 or 1, we already have both those indexes in our
                # seq list, so we can simply output the element that lives at
                # that index, e.g. seq[0] == 0 and seq[1] == 1;
                if x <= 1:
                    
                    # Yield is used with generator functions (and others?) to
                    # return values WITHOUT breaking generator function
                    # execution---contrast with 'return', which DOES bring
                    # program execution to a stop;
                    yield seq[x]
                
                # Any x value greater than 1 and we do have to calculate new
                # values of the Fibonacci sequence, so we simply define the
                # formula below and run it as many times as needed;
                else:
                    
                    # As mentioned above, the formula for generating new 
                    # values in the Fibonacci sequence is very simple, it is
                    # merely the sum of the last two values;
                    new_entry = (seq[(x-2)] + seq[(x-1)])
                    seq.append(new_entry) 
                    yield new_entry
                
                # Our sequence counter goes up by one every time a new value
                # is generated, until it is equal to n-1, which is equal to 
                # the total number of values in the sequence the user want to
                # see, per their input;
                x += 1

######################### DEFINE THE GENERATOR-CALLER FUNCTION

        # Define the generator-caller function, which will be used to generate 
        # the values that make up the Fibonacci sequence;
        def gen_call(n):
            
            # i represents each individual value in the Fibonacci sequence,
            # ergo we print it every time a new value is generated;
            for i in fib_gen(n):
                print(i)
            
            # It seemed to be necessary to have some kind of return statement,
            # so I used one that returns nothing;
            return ''
        
        # This return statement was also needed;
        return gen_call(n)

############################### CALL THE FUNCTIONS

# Call the Fibonacci function, and its nested functions, as the argument to
# a print statement;
print(fibonacci(num))
print()
