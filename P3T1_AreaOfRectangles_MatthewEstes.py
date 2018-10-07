rectangle1Length = float( input( "Please enter the length of the first rectangle:") )
rectangle1Width = float( input ("Please enter the width of the first rectangle:") )
rectangle2Length = float( input("Please enter the length of the second rectangle:") )
rectangle2Width = float( input ("Please enter the width of the second rectangle:") )
rectangle1Area = rectangle1Length * rectangle1Width
rectangle2Area = rectangle2Length * rectangle2Width

if rectangle1Area > rectangle2Area:
    print("The first rectangle is larger than the second.")
elif rectangle2Area > rectangle1Area:
    print("The second rectangle is larger than the first.")
elif rectangle1Area == rectangle2Area:
    print("The rectangles are the same size.")
    
