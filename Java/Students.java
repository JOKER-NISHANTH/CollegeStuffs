package com.v1;

import java.util.Scanner;

public class Students {

	
	static Scanner scanner;
	public static void main(String[] args) {

		int  rollno;
		String dob,course,name,addr,fatherName,phone;
		float fee;
		scanner = new Scanner(System.in);
		System.out.print("Enter the Roll No : ");
		rollno = scanner.nextInt();
		
		scanner.nextLine();
		System.out.print("Enter the Name : ");		
		name = scanner.nextLine();
		System.out.print("Enter the Father Name : ");		
		fatherName = scanner.nextLine();
		System.out.print("Enter the Date of Birth : ");
		dob = scanner.nextLine();
		System.out.print("Enter the Course : ");
		course = scanner.nextLine();
		System.out.print("Enter the Fees  : ");
		fee = scanner.nextFloat();
		
		scanner.nextLine();
		System.out.print("Enter the Address : ");
		addr = scanner.nextLine();
		System.out.print("Enter the Phone Number : ");
		phone = scanner.nextLine();
			
		;
		
		System.out.print("\n	Enter the Option to Display \n  1 for Student BioData and 2 for Student Data : ");
		int choice = scanner.nextInt();
		
		switch (choice) {		
		case 1:
			Student stu1Bio = new Student(rollno,name,fatherName,dob,course,fee,addr,phone );
			stu1Bio.displayBioData();
			break;
		case 2:
			Student stu1Data = new Student(rollno,name,course,fee);
			stu1Data.displayData();
			break;
		default:
			System.out.println("Invaild Input");
			break;
			
		}		
	}

}
