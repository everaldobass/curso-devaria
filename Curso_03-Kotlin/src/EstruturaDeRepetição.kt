fun main(argumentos : Array<String>) {

    //for subindo
    for(indice in argumentos.indices){
        println(" Percorrendo os argumentos posição: $indice e valor ${argumentos[indice]}")
    }
    //for descendo
    for(indiceDecrescente in argumentos.size-1 downTo 0){
        println(" Percorrendo os argumentos de forma decrescente $indiceDecrescente" + " e valor : ${argumentos[indiceDecrescente]}")
    }
    //for each
    for (argumento in argumentos){
        println(" Percorrendo um foreach valor: $argumento")
    }
    //while
    var contadorArgumentoslido = 0
    while (contadorArgumentoslido < argumentos.size){
        println(" Percorrendo com while: ${++contadorArgumentoslido}" + " valor lido : ${argumentos[contadorArgumentoslido-1]}")
    }
    //do while
    var contadorloopsEfetuados = 0

    do{
        println(" Percorrendo os argumentos while, total loops : $contadorloopsEfetuados" +
                " Valor lido ${argumentos[contadorloopsEfetuados]}")
        contadorloopsEfetuados++
    }while (contadorloopsEfetuados < argumentos.size)



}