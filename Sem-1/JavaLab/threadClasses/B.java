package threadClasses;

public class B extends Thread {

	public void run() {
		
		for(int j = 1; j < 6; j++) {
			
			System.out.println("Value of j = "+j);
			if (j==3)
				stop();
			
		}
		System.out.println("Exit from B");
	}
	
}
