# Messy definition of linear, quadratic and cubic functions
def cubic_function(a=0, b=0, c=0, d=0):
    return lambda x : (a * pow(x, 3)) + (b * pow(x, 2)) + (c * x) + d

def simple_polynomial_to_str(*args):
    
    def power(of): # qyuck and dirty way
        if of == 2: return '²'  # to represent a²
        if of == 3: return '³'  # to represent a³
        if of == 4: return '⁴'  # to represent a⁴
        if of == 1: return ''   # to represent a¹ = a
        else: return f'^{of}'   # to represent a^n e.g. a^-10

    def multiplier(value):
        if value == 1: return '' # 1*x = x
        if value == -1: return '-' # -1*x = -x
        else: return value

    terms = []
    for index, item in enumerate(args):
        if item != 0:
            if index != len(args) - 1:
                terms.append(f'{multiplier(item)}x{power(len(args) - (index + 1) )}')
            else:
                terms.append(f'{multiplier(item)}') # the last item (n) is n * x⁰, that's the same as just n
    return '+'.join(terms).replace('+-', '-').replace('+', ' + ').replace('-', ' - ')

print(simple_polynomial_to_str(1, -3, 1, 0, -2, 10)) # x^5 - 3x⁴ + x³ - 2x + 2
    

def quadratic_function(a=0, b=0, c=0):
    return cubic_function(0, a, b, c)

def linear_function(a=0, b=0):
    return quadratic_function(0, 0, a, b)






# The derivative on a point for any function (smaller values of h means more precision)
def derivative(function, x, h=0.00001):
    '''
       lim    f(x + h) - f(x)
       h->0   ---------------
                    h 
    '''
    return (function(x + h) - function(x)) / h

def evaluate_guess(function, guess_x):
    '''
    The distance between a f(guess) and 0
    '''
    return abs( 0 - function(guess_x) ) # the distance from f(x) and x=0

def newthon_raphson_step(function, guess_x=0):
    '''
    If you want to find the roots for a function f(x) numerically, the Newton-Raphson's method says

    1. Choose an initial guess x0
    2. Calculate new guesses until convergence with

          			    f(x_n)
        x_n+1 = x_n	- ---------
        			   f'(x_n)	

    '''
    return guess_x - (function(guess_x) / derivative(function, guess_x) )


def newthon_raphson(function, x_0=0, precision=0.000001, max_iterations=1000):
    '''
    The execution of multiple steps of the Newthon-Raphson's method, it will repeat until the distance between the guess
    and x=0 is grather then 0.000001 or if this value isn't reached after 1000 iterations - we'll assume that the function
    is stuck, however, we aren't actively checking for that
    '''
    best_guess_x = x_0
    Δ = evaluate_guess(function, x_0)
    iteration = 0

    print(f'#0 iter | x={best_guess_x} | Δ={Δ} | f(x)={function(best_guess_x)}')

    while best_guess_x is not None and Δ > precision and iteration < max_iterations:
        iteration += 1

        best_guess_x = newthon_raphson_step(function, best_guess_x)
        Δ = evaluate_guess(function, best_guess_x)

        print(f'#{iteration} iter | x = {round(best_guess_x, 6):.6f} | f(x) = {round(function(best_guess_x), 6):.6f} | Δ = {round(Δ, 6):.6f}')

    print('\n')
    print('== Newthon-Raphson final result ==')
    print(f'Root found:             {evaluate_guess(function, best_guess_x) < precision}')
    print(f'Iterations:             {iteration}')
    print(f'Starting guess:         x = {x_0}')
    print(f'Best guess:             x = {round(best_guess_x, 10):.10f}')
    print(f'Solving for best guess: f({round(best_guess_x, 2):.2f}) = {round(best_guess_x, 10):.10f}')
    print(f'Error:                  Δ = {round(Δ, 10):.10f}')
    print('====================================')

    if iteration == max_iterations:
        print('''Maximum iterations reached - probably you reached a close loop, check for loops, try changing x_0 or increase the maximum iteration.''')
    return best_guess_x, Δ, iteration

#f = cubic_function(a=1, b=-5, c=3) # f(x) = x³ - 5x² + 3x
#newthon_raphson(f, 3.1)

