package com.v1;

import java.util.Scanner;

public class Area {
	static Scanner scanner;
		public static void main(String[] args)
		{

			// Creating object of Shape class
			Shape obj = new Shape();

			scanner = new Scanner(System.in);
			float sqr;
			double radius;
			int length , width;
			
			System.out.println("Enter the choice to calculate \n"
					+ "\n 1 for Rectangle "+"\n 2 for Square "+"\n 3 for Circle ");
			while(true) {
				int choice = scanner.nextInt();
				
				switch (choice) {
				case 1:
					System.out.print("Enter the Length : ");
					length = scanner.nextInt();
					System.out.print("Enter the Width : ");
					width = scanner.nextInt();
					obj.Area(length, width);
					break;
				case 2:
					System.out.print("Enter the Side : ");
					sqr= scanner.nextInt();
					obj.Area(sqr);
					break;
				case 3:
					System.out.print("Enter the Radius  : ");
					radius= scanner.nextInt();
					obj.Area(radius);
					break;

				default:
					System.out.println("\n Invalid Input");
					break;
				}
			}
		}
}
