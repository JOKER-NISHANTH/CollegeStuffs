package threadClasses;

public class ThreadExample extends Thread {

	public static void main(String[] args) {

		A threadA = new A();
		B threadB = new B();
		C threadC = new C();
		
		threadA.setPriority(MIN_PRIORITY);
		threadB.setPriority(NORM_PRIORITY);
		threadC.setPriority(MAX_PRIORITY);
		
		threadA.start();
		threadB.start();
		threadC.start();
		
		System.out.println("Exit from Main");
		
	}

}
