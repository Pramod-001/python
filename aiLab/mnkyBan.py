def monkey():
    ban = 'middle'
    mon = "door"
    box = "window"
    banana = False
    onbox = False 
    
    print("Monkey starts at the door ")
    
    mon = box
    print("Monkey is at the box ")
    
    box = ban
    mon = ban
    print("Monkey pushes the box into middle ")
    
    onbox = True
    print("Monkey climbs the box ")
    
    if mon == ban and box == ban and onbox:
        banana = True 
        print("Mokey grabs the banana")
    
    if banana : 
        print("Success")
    else :
        print("Fail")
        
monkey()