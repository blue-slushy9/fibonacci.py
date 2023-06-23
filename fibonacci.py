print("This program takes an integer as input and outputs the first numbers in the Fibonacci sequence equal to the value of the integer. Please enter your integer now...")

num = int(input())
print()

def fibonacci(n):
    if n <= 0:
        err_msg = print("Invalid input")
        return err_msg

    elif  n == 1:
        return 0

    else:
        def fib_gen(n):
            seq = [0,1]
            x = 0
            while x <= (n - 1):
                if x <= 1:
                    yield seq[x]
                
                else:
                    new_entry = (seq[(x-2)] + seq[(x-1)])
                    seq.append(new_entry) 
                    yield new_entry
                x += 1

        def gen_call(n):
            for i in fib_gen(n):
                print(i)
            return ''

        return gen_call(n)

print(fibonacci(num))
