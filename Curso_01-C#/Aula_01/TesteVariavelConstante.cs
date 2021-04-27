using System;

namespace TesteVariavelConstante
{
    class Program
    {
        static void Main(string[] args)
        {
            //Comentário
            const string constante = "Constante não muda";

            if(argumentos.length == 0)
            {
                Console.WriteLine("Informar um número");
                return;
            }

            int inteiro;
            bool teste = int.TryParse(argumentos[0], out inteiro);

            if(teste == false){
                Console.WriteLine("Argumento informado não é um numero inteiro");
                return;
            }

            Console.WriteLine(constante);
            Console.WriteLine("Número informado: " + inteiro);

        }
    }
}