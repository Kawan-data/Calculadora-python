n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("insira a operação:")
if op == "+":
        print(n1, op, n2, "=", n1 + n2)
elif op == "-":
        print(n1, op, n2, "=", n1 - n2)
elif op == "*":
        print(n1, op, n2, "=", n1 * n2)
elif op == "/":
        print(n1, op, n2, "=", n1 / n2)
else:
        print("Operação inválida")
