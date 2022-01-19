open(Fh,"sub.txt");

while(my $line=<Fh>){

	
	
	if($line =~ /^Tamil/){
	
		$curpos = tell;
		
		print("The current byte position of $line is $curpos \n");		
	
	}
		
	
}

seek(Fh,$curpos,0);
@lines=(<Fh>);
print(@lines);

