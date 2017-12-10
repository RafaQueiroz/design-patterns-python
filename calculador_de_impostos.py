
class Calculador_de_impostos(object):
	
	def realiza_calculo(self, orcamento, imposto):
	
		imposto_calculado = imposto.calcula(orcamento)
		print imposto_calculado

# TESTES
# Design pattern strategy
# eh passado - como parametro - a estrategia a ser utilizada na funcao/metodo
# Exemplo: Calculo de imposto. Existem diversos tipos de impostos para calcularmos,
# cada um de um tipo diferente. 

if __name__ == '__main__':
	from orcamento import Orcamento
	from impostos import ISS, ICMS
	
	calculador = Calculador_de_impostos()

	orcamento = Orcamento(500)

	calculador.realiza_calculo(orcamento, ISS())
	calculador.realiza_calculo(orcamento, ICMS())

