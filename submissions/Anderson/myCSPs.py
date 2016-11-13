import csp

switch = False

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

#domains('A')
print(domains.values())
# domains('B')
# print(domains.values())

def constraints(C, c, D, d):
    if C == D:      # e.g. NSW == NSW
        return True

    if c == d:      # e.g. WA = G and SA = G
        return False

    return valid(C,c,D,d)

Top = 'A'
Bottom = 'B'

def valid(E,e, F, f):
    if Top == E and Bottom == F:
        if e + e == f:
            return True
        else:
            return False
    else:
        return True

alphaM = csp.CSP(variables, domains, neighbors, constraints)

myCSPs = [
    {
        'csp': alphaM,
     }
]