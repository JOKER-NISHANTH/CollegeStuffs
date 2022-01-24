package studentMarkSheet;

import java.io.*;
import java.util.*;

public class Student {

	
	Scanner in = new Scanner(System.in);
	 int rollNo;
	 String name;
	public void getNo() throws IOException{
				
		System.out.println("Enter the rollno  : ");
		rollNo = in.nextInt();
		System.out.println("Enter the Name : ");
		in.nextLine();
		name = in.nextLine();
		
	}
	
public	void putNo() {
		System.out.println("Student Details");
		System.out.println("Roll No : "+this.rollNo);
		System.out.println("Name : "+this.name);
		
	}
	
}
