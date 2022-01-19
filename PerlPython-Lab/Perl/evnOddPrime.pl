print "\n 1 for Odd or Even \n 2 for Prime or Not \n Enter the choice : ";

my $choice = <>;

if ($choice == 1){

    print "\n Enter the number : ";

    my $num = <>;

    if ($num%2 == 0){

            print " Even";

    }else{

            print " Odd";

    }

}

elsif ($choice == 2){

    print "\n Enter the number : ";

	my $num = <>;

	my $isPrime = 1;

	    if ($num < 2){

		$isPrime = 0;
		
        

	     }
	     else{
	     
	        for (my $i=2;$i<=int($num/2);$i++){

        	    if($num%$i==0){

			$isPrime = 0;

                        break;

            }
        }
    }
    
    if ($isPrime == 0){
        print " Not a prime number ";
    }
    
    else{

            	print("Prime number");
    }

}
else{
    print "\n Invalid choice , \n please enter correct choice :)"
}
