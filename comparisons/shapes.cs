using System;

class ShapeCalcs {
    static void Main() {

        Console.Write("Enter rectangle width: ");
        int width = int.Parse(Console.ReadLine());
        Console.Write("Enter rectangle height: ");
        int height = int.Parse(Console.ReadLine());

        string choice = "";
        while (true) {
            Console.Write("Enter calculation: (Perimeter/Area: )");
            choice = Console.ReadLine();

            if (choice.ToLower() == "perimeter") {
                Console.WriteLine("Perimeter: " + Peri(width, height));
            }
            else if (choice.ToLower() == "area") {
                Console.WriteLine("Area: " + Area(width, height));
            }

            Console.Write("Display both? [y/n]: ");
            choice = Console.ReadLine();

            if (choice.ToLower() == "y") {
                CalcAll(width, height);
            }

            Console.WriteLine("Done.\n");
        }
    }

    private static int Peri(int width, int height) {
        return 2 * width + 2 * height;
    }

    private static int Area(int width, int height) {
        return width * height;
    }

    private static void CalcAll(int width, int height) {
        int localPerm = Peri(width, height);
        int localArea = Area(width, height);

        Console.WriteLine("Perimeter: " + localPerm);
        Console.WriteLine("Area: " + localArea);
    }
}