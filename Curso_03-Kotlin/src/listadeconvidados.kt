fun main() {

    println("Informar o nome do convidado: ")
    val nome = readLine()

    if(nome.isNullOrEmpty() || nome.isNullOrBlank()){
        println(" Nome informado não é Valido: ")
        return
    }

    println(" Informar a idade: ")
    val idade = readLine()?.toIntOrNull()

    if(idade == null || idade <=0){
        println(" Idade informada invalida: ")
        return
    }

    var estaconvidado = false
    when(nome){
        "Everaldo" -> estaconvidado = true
        "Edson" -> estaconvidado = true
        "Eduardo" -> estaconvidado = true
        "Eriberto" -> estaconvidado = true
        else -> estaconvidado = false

    }

    if(estaconvidado && idade >= 18){
        println("Bem vindo")
    }else if(!estaconvidado) {
        println("Não está na lista: ")
    }else{
        println("Idade informada não valida: ")
    }
}