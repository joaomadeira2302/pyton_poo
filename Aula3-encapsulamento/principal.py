from contaBancaria import Conta

minhaConta = Conta(123,"Ermenegildo Sousa",1000,500)

minhaConta.detalhes()

print(f"O limite atual é {minhaConta.getLimite()}")

minhaConta.setLimite(259)

print(f"O limite atual é{minhaConta.getLimite()}")

minhaConta.depositar(100)
minhaConta.detalhes()

minhaConta.sacar(500)
minhaConta.detalhes()