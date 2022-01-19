open(Fh,"emp.txt");

while(<Fh>){

	($num,$name) = split(" ", $_, 2);
	
	$realid {$num} = $name;
	
}

close(Fh);


while(1){

	print("Choose the number from the list of name : ");
	
	chomp($num=<>);	
	
	last unless $num;
	
	print(" $realid{$num} \n");

}
