from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):

	def calcula(self, orcamento):
		
		desconto = Desconto_por_cinco_itens(
			Desconto_por_mais_de_quinhentos_reais(
				Sem_desconto()
			)
		).calcula(orcamento)

		return desconto


if __name__ == '__main__':
	from orcamento import Orcamento, Item


	orcamento = Orcamento()

	orcamento.adiciona_item(Item('ITEM - 1', 100))
	orcamento.adiciona_item(Item('ITEM - 2', 200))
	orcamento.adiciona_item(Item('ITEM - 3', 101))


	calculador = Calculador_de_descontos()

	desconto = calculador.calcula(orcamento)

	print 'desconto %s' % desconto
