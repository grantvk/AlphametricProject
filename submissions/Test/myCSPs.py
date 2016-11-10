import csp

startd = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]#'K']

domains = {
    'A': startd,
    'B': startd,
}

variables = domains.keys()

neighbors = {
    'A': ['B'],
    'B': ['A'],
}

def constraints(A, a, B, b):
    if A == B:      # e.g. NSW == NSW
        return True

    if a == b:      # e.g. WA = G and SA = G
        return False

    return valid(A,a,B,b)

def valid(A,a, B, b):
    if a + a == b:
        return True
    else:
        return False


alphaM = csp.CSP(variables, domains, neighbors, constraints)

myCSPs = [
    {
        'csp': alphaM,
     }
]