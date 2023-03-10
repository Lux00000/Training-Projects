using System;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string ez = Console.ReadLine();
            string[] words = ez.Split(" ");
            int a = Convert.ToInt32(words[0]);
            string c = Convert.ToString(words[1]);
            int b = Convert.ToInt32(words[2]);

            switch (c)
            {
                case "+":
                    Sum(a, b);
                    break;

                case "-":
                    Min(a, b);
                    break;
                
                case "*":
                    Ymn(a, b);
                    break;
                case "/":
                    Del(a, b);
                    break;

            }
            
  







        }
        static void Sum(int a, int b)
        {
            Console.WriteLine(a + b);
        }
        static void Min(int a, int b)
        {
            Console.WriteLine(a - b);
        }
        static void Del(int a, int b)
        {
            Console.WriteLine(a / b);
        }
        static void Ymn(int a, int b)
        {
            Console.WriteLine(a * b);
        }
    }
}