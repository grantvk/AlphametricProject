import csp

startd = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]#'K']
puzzle = [['E','L','F'],['E','L', 'F'],['F','O','O','L']]
domains = {
    'E': startd,
    'L': startd,
    'F': startd,
    'O': startd,
    'S1': [0,10],
    'S2': [0,10],
    'S3': [0,10],
    'C1': [0,1],
    'C2': [0,1],
    'C3': [0,1],
}
E= domains[0][0]
L= domains[1][0]
F= domains[2][0]
O= domains[3][0]


variables = domains.keys()
exp1= ((100*E)+ (10*L)+ F)
exp2=((100*E)+ (10*L)+ F)
exp3= ((F*1000) + (O*100) + (O*10) + L)

neighbors = {
    'L': ['E', 'F', 'O'],
    'E': ['L', 'F', 'O'],
    'F': ['L', 'E', 'O'],
    'O': ['L', 'F', 'E'],
    'S1': [],
    'S2': [],
    'S3': [],
    'C1': [],
    'C2': [],
    'C3': [],
}

def constraints(A, a, B, b):
    if A == B:      # e.g. NSW == NSW
        return True

    if a == b:      # e.g. WA = G and SA = G
        return False
    return valid()

'''
def valid():
    if 'F' + 'F' == 'L' + 'C1'*10:
        if 'C1' + 'L' + 'L' == 'O' + 'C2'*10:
            if 'C2' + 'E' + 'E' == 'O' + 'C3'*10:
                if 'C3' == 'F':
                    return True
    return False
'''
def valid():
    if exp1 + exp2 == exp3:
        return True
    else:
        return False

alphaM = csp.CSP(variables, domains, neighbors, constraints)

myCSPs = [
    {
        'csp': alphaM,
     }
]