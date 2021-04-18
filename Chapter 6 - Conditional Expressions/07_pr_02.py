#Find out weather a student is pass or fail, if it requires 40% and atleast 33% in each subject to pass. Assume 3 subjects and marks as input from the user

sub1 = int(input("Enter first sub marks\n"))
sub2 = int(input("Enter second sub marks\n"))
sub3 = int(input("Enter third sub marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")

elif(sub1+sub2+sub3)/3 <40:
    print("You are fail due to total percentage less than 40")

else:
    print("You passed the test")