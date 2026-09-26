A = float(input("Escreva o primeiro número: "))
B = float(input("Escreva o segundo número: "))
C = float(input("Escreva o terceiro número: "))

if A > B and A > C:
    print("O primeiro número é maior: {:.2f}" .format(A))
if A < B and A < C:
    print("O primeiro número é menor: {:.2f}" .format(A))
if B > A and B > C:
    print("O segundo número é maior: {:.2f}" .format(B))
if B < A and B < C:
    print("O segundo número é menor: {:.2f}" .format(B))
if C > A and C > B:
    print("O terceiro número é maior: {:.2f}" .format(C))
if C < A and C < B:
    print("O terceiro número é menor: {:.2f}" .format(C))