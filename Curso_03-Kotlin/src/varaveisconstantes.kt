fun main(argumentos: Array<String>){
    
    if(argumentos.isEmpty()){
        
        println(" informar um número: ")
        return
    }

    val numero = argumentos[0].toInt()
    println(" Numero digitado foi: $numero ")

    var soma = 0
    soma = numero + numero
    println(" A soma do numero: $numero ")
    
}