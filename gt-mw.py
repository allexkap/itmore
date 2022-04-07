import itertools as it
n, p = int(input('n: ')), ord('a')

def DNF(G):
    D = sorted([sorted(set(g)) for g in it.product(*G)], key=lambda l: (len(l), l))
    return list(d for i, d in enumerate(D) if all(set(b)-set(d) or i<=j for j, b in enumerate(D)))
E, V, S = [], [chr(p+i) for i in range(n)], set(range(n))
for i in range(n-1): E.extend([i, V.index(v)] for v in input(f'{V[i]}: '))
K = DNF(E)
F = [sorted(S-set(k)) for k in K]
C = [[j for j, f in enumerate(F) if i in f] for i in range(n)]
X = DNF(C)

show = lambda s, l: s.join(V[i] for i in l)
print('*'.join(f"({show('+', e)})" for e in E))
print('+'.join('*'.join(show('', k)) for k in K))
print(' '.join(f"{show('', f)}{('✓', '')[len(f)<len(F[0])]}" for f in F), len(F[0]), sep=' | ')
print('*'.join(f"({'+'.join(f'F{i+1}' for i in c)})" for c in C))
print('+'.join('*'.join(f'F{i+1}' for i in c) for c in X))
print(' '.join(show('', F[x]) for x in X[0]), len(X[0]), sep=' | ')
