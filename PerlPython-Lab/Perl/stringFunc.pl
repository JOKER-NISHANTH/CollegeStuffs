sub upper{

	print("Uppercase for given string is : ",uc($str));

}
 
sub lower{

	print("Lowercase for given string is : ",lc($str));

}

sub substring{

	print("Enter the starting position : ");
	$off = <>;
	print("Enter the length : ");
	$len = <>;
	print("Substring in the given string is : ",substr($str,$off,$len));

}

sub replace {

	print("Enter the starting position : ");
	$off = <>;
	print("Enter the length : ");
	$len = <>;
	print("Enter the string to replace : ");	
	chomp($re=<>);
	substr($str,$off,$len,$re);
	print("Replace string for given string is : ",$str);

}

sub len{

	print("Length of the given string is : ",length($str));

}


sub concat {

	print("Enter the string to concatenation : ");
	chomp($str1=<>);
	print("The concatenation string is : ",$str.$str1);

}


print("\n Enter the string : ");
chomp($str=<>);


while(1){

	print("\n The String FUnction  ");
	print("\n ************************");
	print("\n 1. Uppercase \n 2.Lowercase \n 3. Substring \n 4.Replace String \n 5.Length \n 6. Concatenation \n 7.Exit");
	print("\n Enter the choice : ");
	$ch = <>;
	if($ch == 1) {
		upper();
	}
	elsif($ch == 2) {
		lower();
	}
	elsif($ch == 3){
		substring();
	}
	elsif($ch == 4){
		replace()
	}
	elsif($ch == 5){
		len();
	}
	
	elsif($ch == 6){
		concat();
	}
	elsif($ch == 7){
		exit();
	}

	
}





























