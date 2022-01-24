package threadClasses;

public class C extends Thread{

	public void run() {
		
		
		for(int k=0;k<6;k++) {
			System.out.println("Value of k ="+k);
			if (k==1)
			try {
				sleep(1000);
			}
			catch(Exception e) {}
			
			System.out.println("Exit from C");
			
		}
		
		
	}
}
