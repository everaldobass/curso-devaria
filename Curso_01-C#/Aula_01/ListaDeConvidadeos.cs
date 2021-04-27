// importar a biblioteca
using System;
//Serve para inportar os arquivos dentro de outo codigo
namespace ListaDeConvidados
{
    //Classe princiapal
    class Program
    {
        private static string[] ListaDeConvidado = {

            "Everaldo",
            "Edson",
            "Eduardo",
            "Eriberto",
            "Elias",
            "Henrique",

        };
        public static void Main(string[] args)
        {

            Console.WriteLine("Informe um nome: ");
            var nome = Console.ReadLine();

            if(nome == null || string.IsNullOrEmpty(nome))
            {
                Console.WriteLine("Nome não informado");
                return;
            }


            Console.WriteLine("Informe uma idade: ");
            var idadeString = Console.ReadLine();

            int idade;

            bool idadeInformada = int.TryParse(idadeString, out idade);

            if(idadeInformada == false)
            {
                Console.WriteLine("Idade não informada");
                return;
            }


        }
    }
    
}