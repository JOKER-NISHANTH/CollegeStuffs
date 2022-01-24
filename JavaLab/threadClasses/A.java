package threadClasses;

public class A extends Thread {

	
	public void run() {
		
		for(int i =1; i<6;i++) {
			
			if(i==1) 
				Thread.yield();			
			System.out.println("Value of i = "+i);
			
		}
		System.out.println("Exit from A");
		
	}
	
	
}
