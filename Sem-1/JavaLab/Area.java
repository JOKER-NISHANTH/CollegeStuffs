
import java.io.IOException;
import java.util.Scanner;
public class Area {

	public static void main(String[] args) throws IOException {
		int sqr;
		double length,width,radi;
		
		Scanner scanner = new Scanner(System.in);
		System.out.println("Enter the Length : ");
		length = scanner.nextDouble();
		System.out.println("Enter the Width : ");
		width = scanner.nextDouble();
		System.out.println("Enter the Radius : ");
		radi = scanner.nextDouble();
		System.out.println("Enter the Side Unit : ");
		sqr = scanner.nextInt();
		
		Shape s = new Shape();
		System.out.println("Area of Reatangle "+s.area(length,width));
		System.out.println("Area of Radius "+s.area(radi));
		System.out.println("Area of Square "+s.area(sqr));
	}

}
