import itertools as it
G0, X = [], [chr(ord('1')+i) for i in range(8)]
for x in X: G0.extend([f'{x}{g}' for g in input(f'{x}: ')])
G1 = list(map(lambda g: ''.join(g), it.product(*G0)))
G2 = [''.join(sorted(set(g))) for g in G1]; G2.sort(key=lambda g: (len(g), g))
G3 = [g for i, g in enumerate(G2) if all(set(k)-set(g) or i<=j for j, k in enumerate(G2))]
print(f"({')*('.join('+'.join(g) for g in G0)})")
print('+'.join('*'.join(g) for g in G3))
print('\n'.join(' '.join(sorted(set(X)-set(g))) for g in G3))
print(max(8-len(g) for g in G3))
