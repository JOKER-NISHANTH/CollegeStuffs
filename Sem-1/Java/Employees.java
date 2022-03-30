package com.v1;

import java.io.IOException;

public class Employees {

	public static void main(String[] args) throws IOException {

		Employer e1 = new Employer();
		Employer e2 = new Employer();
		e1.getAndSetData();
		e1.displayData();
		
		e2.getAndSetData();
		e2.displayData();
			
	}

}
