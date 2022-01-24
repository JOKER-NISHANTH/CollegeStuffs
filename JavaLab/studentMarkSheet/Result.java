package studentMarkSheet;

public class Result extends Test implements Sports{
	
	int total;
	
	public void putwt() {
		
		System.out.println("Sport weigtht : "+sportswt);
	}
	
	void display() {
		
		 total = sub1 + sub2 + sportswt;
		 putNo();
		 putMark();
		 
		 System.out.println("Total score : "+total);
		
	}

}
