from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('João Pedro')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever()

# Relação de associação: Uma classe possui outra classe
# Realizando uma associação: Escritor possui uma caneta
escritor.ferramenta = caneta

escritor.ferramenta.escrever()
