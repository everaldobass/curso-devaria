const valido = true;
const nome = "Everaldo";
let idade = 25;

// Operador &&
if(valido && idade >= 25){
    console.log("Expressão valida");
}else{
    console.log("Expressão não valida")
}

// Operador ||
if(valido || idade <= 25){
    console.log("Expressão valida");
}else{
    console.log("Expressão não valida")
}