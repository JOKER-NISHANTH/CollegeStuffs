package com.v1;

import java.io.*;
import java.util.Scanner;

public class Employer {

	private int id;
	private String name;
	private double salary;
	
	static Scanner scanner;
	
	void getAndSetData() throws IOException {
	 scanner = new Scanner(System.in);
	
	 	System.out.print("\n Enter the ID : ");
	 	this.id = scanner.nextInt();
	 	System.out.print("\n Enter the Name : ");
	 	scanner.nextLine();
	 	this.name = scanner.nextLine();
	 	System.out.print("\n Enter the Salary : ");
	 	this.salary = scanner.nextDouble();
	}
	
	void displayData () {
		System.out.print("--------------------------------");
		System.out.println("\n Id : "+this.id+"\n Name : "+this.name+"\n Salary : "+this.salary);
		System.out.print("--------------------------------");
	}
	
}
