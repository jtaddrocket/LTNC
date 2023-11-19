def sinTaylor(x):
    sinh = 0.0 
    term = x 
    n = 1 
    epsilon = 10e-16 
    while abs(term) >= epsilon:
        sinh += term 
        term *= (-1) * x * x / ((2 * n) * (2 * n + 1))
        n += 1
    return sinh 


def cosTaylor(x):
    cosh = 0.0 
    term = 1 
    n = 1 
    epsilon = 10e-16 
    while abs(term) >= epsilon:
        cosh += term 
        term *= (-1) * x * x / (2 * n * (2 * n - 1))
        n += 1 
    return cosh