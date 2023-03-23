import java.util.Scanner;

public class ShapeCalcs {
	public static void main(String arge[]) {
		Scanner in = new Scanner(System.in);
		
		System.out.println("Enter rectangle width: ");
		int width = in.nextInt();
		
		System.out.println("Enter rectangle height: ");
		int height = in.nextInt();
		
		String choice = "";
		while (true) {			
			System.out.println("Enter calculation: (Perimeter/Area: )");
			choice = in.next();
			
			System.out.println((choice.equalsIgnoreCase("perimeter") ?
					"Perimeter: " + peri(width, height) : "Area: " + area(width, height)));
			
			System.out.println("Display both? [y/n]");
			choice = in.next();
			
			if (choice.equalsIgnoreCase("y")) {
				calcAll(width, height);
			}
			
			System.out.println("Done.\n");
		}
	}

	private static int peri(int width, int height) {
		return 2*width + 2*height;
	}

	private static int area(int width, int height) {
		return width*height;
	}

	private static void calcAll(int width, int height) {
		int localPerm = peri(width, height);
		int localArea = area(width, height);
		
		System.out.println("Perimeter: " + localPerm);
		System.out.println("Area: " + localArea);
	}
}