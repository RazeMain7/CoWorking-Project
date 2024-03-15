### Gram-Schmidt Implementation
#### The Algorithm:
'''
u1 = v1
Loop i = 2,3...,n
   Compute μij = vi ∙ uj / ||uj||2, 1 ≤ j < i.
   Set ui = vi - μij * uj (Sum over j for 1 ≤ j < i)
End Loop
'''

import numpy as np

def GramSchmidt(V):
    U = [V[0]]
    for i in range(1,len(V)):
        for j in range(0,i):
            mi = V[i].dot(U[j]) / U[j].dot(U[j])
        for j in range(0,i):
            U[i] = V[i] - (V[i].dot(U[j]) / np.sqrt(U[j].dot(U[j])) * U[j])
        
    print(U)    
      
v1 = [4,1,3,-1]
v2 = [2,1,-3,4] 
v3 = [1,0,-2,7]
v4 = [6, 2, 9, -5]
V = np.array([v1, v2, v3, v4])
GramSchmidt(V)

v = [
    np.array([4,1,3,-1]), 
    np.array([2,1,-3,4]), 
    np.array([1,0,-2,7]), 
    np.array([6,2,9,-5]),
]

"""
u1 = v1
Loop i = 2,3...,n
   Compute μij = vi ∙ uj / ||uj||2, 1 ≤ j < i.
   Set ui = vi - μij * uj (Sum over j for 1 ≤ j < i)
End Loop
"""
u = [v[0]]
for vi in v[1:]:
    mi = [np.dot(vi, uj) / np.dot(uj, uj) for uj in u]
    u += [vi - sum([mij * uj for (mij, uj) in zip(mi,u)])]

print(round(u[3][1], 5))