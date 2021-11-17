my @oneLetter = ();
my @twoLetter = ();
my @threeLetter = ();
my @fourLetter = ();
my @fiveLetter = ();
my @sixLetter = ();
my @sevenLetter = ();
my @eightLetter = ();
my @nineLetter = ();
my @tenLetter = ();
my @moreThenTenLetter = ();

print "\n Enter the sentence : ";
chomp($sentence = <STDIN>);
$sentence = lc($sentence);

# using split() function
my @wordList = split(' ', $sentence);

for my $word (@wordList)
{
   $len = length($word);

    if ($len == 1) {
          push(@oneLetter,"$word , ");
    }
    elsif ($len == 2) {
        push(@twoLetter,"$word , ");
    }
      elsif ($len == 3) {
        push(@threeLetter,"$word , ");
    }
      elsif ($len == 4) {
        push(@fourLetter, "$word , ");
    }
      elsif ($len == 5) {
        push(@fiveLetter,"$word , ");
    }
      elsif ($len == 6) {
        push(@sixLetter, "$word , ");
    }
      elsif ($len == 7) {
        push(@sevenLetter, "$word , ");
    }
      elsif ($len == 8) {
        push(@eightLetter,"$word , ");
    }
      elsif ($len == 9) {
        push(@nineLetter, "$word , ");
    }
      elsif ($len == 10) {
        push(@tenLetter, "$word , ");
    }
    else {
        push(@moreThenTenLetter,"$word , ")   ;
    }
}

print "[ @oneLetter  ]\n";
print "[ @twoLetter ]\n";
print "[ @threeLetter ]\n";
print "[ @fourLetter ]\n";
print "[ @fiveLetter ]\n";
print "[ @sixLetter ]\n";
print "[ @sevenLetter ]\n";
print "[ @eightLetter ]\n";
print "[ @nineLetter ]\n";
print "[ @tenLetter ]\n";
print "[ @moreThenTenLetter ]\n";