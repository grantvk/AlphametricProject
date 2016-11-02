import csp

startd = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]#'K']

domains = {
    'E': startd,
    'L': startd,
    'F': startd,
    'O': startd,
}

variables = domains.keys()

neighbors = {
    'L': ['E', 'F', 'O'],
    'E': ['L', 'F', 'O'],
    'F': ['L', 'E', 'O'],
    'O': ['L', 'F', 'E']
}

def constraints(A, a, B, b):
    if A == B:      # e.g. NSW == NSW
        return True

    if a == b:      # e.g. WA = G and SA = G
        return False

    return True

alphaM = csp.CSP(variables, domains, neighbors, constraints)

myCSPs = [
    {
        'csp': alphaM,
     }
]