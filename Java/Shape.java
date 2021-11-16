package com.v1;

public class Shape {
	
		static final double PI = Math.PI;

		// Overloaded Area() function to
		// calculate the area of the square
		// It takes one float parameter
		void Area(float a)
		{
			float A = a * a;
			System.out.println("Area of the Square: " + A);
		}

		// Overloaded Area() function to
		// calculate the area of the circle
		// It takes one double parameter
		void Area(double r)
		{
			double A = PI * r * r;
			System.out.println("Area of the Circle: " + A);
		}

		// Overloaded Area() function to
		// calculate the area of the rectangle
		// It takes two int parameters
		void Area(int l, int w)
		{
			int A = l * w;
			System.out.println("Area of the Rectangle: " + A);
		}	
}
