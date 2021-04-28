const listaPessoas = ["Everaldo", "Edson", "Eduardo"];

const nome = process.argv[2];
const idade = parseInt(process.argv[3]);

if(!listaPessoas.includes(nome)){
    console.log("Não foi convidado!" );
    return;

}

if(idade < 18){
    console.log("Apenas maior de idade: ");
    return;

}