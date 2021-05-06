/*
* -> Escrever um programa que recebe alguns produtos como argumento, - ok
* -> validar se esses produtos estão na lista de itens disponíveis do mercado. - ok
*
 -> Caso estejam, avisar o usuário quais produtos tem
 -> E quais não tem e
 *
 por último, exibir a lista de produtos disponíveis ordenados por ordem alfabética do mercado,
 para que o usuário possa pedir na próxima vez.
* */

fun main(argumentos: Array<String>){
    //Validar se os produtos dos argumentos
    if(argumentos.isEmpty()){
        println("Favor informar os produtos")
        return
    }

    val produtosDisponiveis = arrayOf("Pão", "Bolacha", "Biscoito", "Queijo", "Arroz", "Carnes")

    val produtosRequisitadosDisponiveis = argumentos.filter { produtoRequisitado ->
        produtosDisponiveis.contains(produtoRequisitado)
    }

    for(produtoRequisitadoDisponivel in produtosRequisitadosDisponiveis){
        println("Este produto nos temos: $produtoRequisitadoDisponivel")
    }

    val produtosRequisitadoNãoDisponiveis = argumentos.filter { produtoRequisitado ->
        !produtosDisponiveis.contains(produtoRequisitado)
    }


    produtosRequisitadoNãoDisponiveis.forEach { produtoNaoDisponivel ->
        println(" Este produto nos não temos: $produtoNaoDisponivel")
    }

    val produtosOrdenados = produtosDisponiveis.sortedBy { produto -> produto }
    produtosOrdenados.forEach { produto -> println("Confira os produtos disponiveis: $produto") }


}