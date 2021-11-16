package com.v1;

public class Student {

		private int  rollno;
		private String dob,course,name,addr,fatherName,phone;
		private float fee;
		
		public Student(int rollno, String name , String fatherName,String dob, String course, float fee,  String addr,  String phone)
				 {
	
			this.rollno = rollno;
			this.name = name;
			this.fatherName = fatherName;
			this.dob = dob;
			this.course = course;
			this.fee = fee;
			this.addr = addr;
			this.phone = phone;
		}

		public Student(int rollno,  String name,String course, float fee) {
			this.rollno = rollno;
			this.name = name;
			this.course = course;
			this.fee = fee;
		}
		
		void displayBioData() {
			System.out.println("---------------------------");
			System.out.println("     STUDENT BIODATA       ");
			System.out.println("---------------------------");
			System.out.println("\n Roll No : "+this.rollno);
			System.out.println("\n Name : "+ this.name);
			System.out.println("\n Date of Birth : "+this.dob);
			System.out.println("\n Course : "+this.course);
			System.out.println("\n Father Name : "+this.fatherName);
			System.out.println("\n Address : "+this.addr);
			System.out.println("\n Phone : "+this.phone);
			System.out.println("\n Fees : "+this.fee);				
		}
		void displayData() {
			System.out.println("---------------------------");
			System.out.println("     STUDENT  DATA       ");
			System.out.println("---------------------------");
			System.out.println("\n Roll No : "+this.rollno);
			System.out.println("\n Name : "+ this.name);
			System.out.println("\n Course : "+this.course);
			System.out.println("\n Fees : "+this.fee);				
		}
}
