def isReachable(x1, y1, x2, y2):
 
    while(x2 > x1 and y2 > y1):
 
        # Reduce x2 by y2 until it is
        # less than or equal to x1
        if(x2 > y2):
            x2 %= y2
 
        # Reduce y2 by x2 until it is
        # less than or equal to y1
        else:
            y2 %= x2
 
    # If x2 is reduced to x1
    if(x2 == x1):
 
        # Check if y2 can be
        # reduced to y1 or not
        return (y2 - y1) >= 0 and (
                y2 - y1) % x1 == 0
 
    # If y2 is reduced to y1
    elif(y2 == y1):
 
        # Check if x2 can be
        # reduced to x1 or not 
        return (x2 - x1) >= 0 and (
                x2 - x1) % y1 == 0
    else:
        return 0
def reachDestination(sx,sy,dx,dy):
    if isReachable(sx,sy,dx,dy):
        return True
    else:
        return False

    
    
source_x, source_y = 1,1
dest_x, dest_y = 2,2
if (reachDestination(source_x, source_y, dest_x, dest_y)):
    print("True")
else:
    print("False")
    
    
    
    
    
    
    
    
    
    
