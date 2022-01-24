package studentMarkSheet;

import java.io.*;
import java.util.*;
public class Test extends Student{

	 int sub1, sub2 , m1,m2;
	
	Scanner in = new Scanner(System.in);
	void getMark() throws IOException{
		
		System.out.println("Enter the mark 1 : ");
		m1 = in.nextInt();
		System.out.println("Enter the mark 2 : ");
		m2 = in.nextInt();
		
		sub1 = m1;
		sub2 = m2;
		
	}
	
	void putMark() {
		
		System.out.println("Mark Obtained");
		System.out.println("Subject one : "+sub1);
		System.out.println("Subject tho : "+sub2);
	}
	
}
