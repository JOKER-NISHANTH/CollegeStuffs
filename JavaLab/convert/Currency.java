package convert;

import java.io.*;
import java.util.*;
import convert.*;

public class Currency {

	void getData() throws IOException {
		India ind = new India();
		USA us = new USA();
		UK uk = new UK();
		Japan jap = new Japan();
		
		Scanner in = new Scanner(System.in);
		
		int ch = 0;
		while(ch != 7) {
			
			System.out.println("Currency Conversation");
			System.out.println("1. Rupees to Dollar ");
			System.out.println("2. Dollar to Rupees ");
			System.out.println("3. Rupees to Pound ");
			System.out.println("4. Pound to Rupees ");
			System.out.println("5. Rupees to Euro");
			System.out.println("6. Euro to Rupees ");
			
			System.out.println("Enter the choice : ");
			ch = in.nextInt();
			
			if (ch == 1) {
				System.out.println("Enter the rupees value : ");
				float x = in.nextFloat();
				float n = ind.convertRupeesToDollar(x);
				System.out.println(x +"Rupees is "+n+"Dollar");
				
			}
			
			if (ch == 2) {
				System.out.println("Enter the dollar value : ");
				float x = in.nextFloat();
				float n = us.convertDollarTORupees(x);
				System.out.println(x+"Dollor is"+n+"Rupees");
			}
			
			if(ch ==3) {
				System.out.println("Enter the rupees value : ");
				float x = in.nextFloat();
				float n = ind.convertRupeesToPound(x);
				System.out.println(x +"Rupees is "+n+"Pound");
			}
			
			if(ch ==4) {
				System.out.println("Enter the pound value : ");
				float x = in.nextFloat();
				float n = uk.convertPoundToRupees(x);
				System.out.println(x +"Pound is "+n+"Rupees");
			}
			
			if (ch == 5) {
				
				System.out.println("Enter the rupees value : ");
				float x = in.nextFloat();
				float n = ind.convertRupeesToEuro(x);
				System.out.println(x+" rupees is "+n+"Euro");
				
			}
		
			if (ch == 6) {
				
				System.out.println("Enter the euro value : ");
				float x = in.nextFloat();
				float n = jap.convertEuroToRupees(x);
				System.out.println(x+" euro is "+n+"rupees");
				
			}
			
		}
	
	}

}
