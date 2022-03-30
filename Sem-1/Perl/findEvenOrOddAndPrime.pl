# InComplete - | -

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
elsif (choice == 2){
    print "\n Enter the number : ";
    my $num = <>;
    if ($num > 1){
        for (my $i=2;$i<=($num/2);$i++){
            if($num%$i==0){
                print "not a prime";
                        break;
            }
        }else{
            print " prime";
        }
    }
    else{
        print " not a prime";
    }
}
else{
    print "\n Invalid choice , \n please enter correct choice :)"
}
