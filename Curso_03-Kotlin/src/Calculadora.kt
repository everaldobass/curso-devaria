import java.math.BigDecimal
fun calculaOperacao(primeiroNumero: BigDecimal, operador: String, segundoNumero: BigDecimal): BigDecimal {
    when(operador){
        "+" -> return primeiroNumero + segundoNumero
        "-" -> return primeiroNumero - segundoNumero
        "*" -> return primeiroNumero * segundoNumero
        "/" -> return primeiroNumero / segundoNumero
        "%" -> return primeiroNumero % segundoNumero
        else -> return BigDecimal.ZERO

    }
}

fun main() {
    println(" Digite um número: ")
    val primeiroNumero = readLine()?.toBigDecimalOrNull()

    if(primeiroNumero == null){
        println("Primeiro numero invalido: ")
        return
    }

    println("Digite o operador +, -, *, /, % :")
    val operador = readLine()
    if(operador.isNullOrEmpty() || operador.isNullOrBlank() ||
        (operador !="+" && operador !="-" && operador !="*" && operador !="/" && operador !="%")){
        println("Operador invalido: ")
        return
    }

    println(" Digite o Segundo número: ")
    val segundoNumero = readLine()?.toBigDecimalOrNull()

    if(segundoNumero == null){
        println(" Segundo numero invalido: ")
        return
    }

    val resultado = calculaOperacao(primeiroNumero, operador, segundoNumero)
    println("O Resultado da sua operação foi: $resultado ")
}