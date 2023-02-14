# Place code below to do the munging part of this assignment.
all_text = []
x = 0


f = open("data/nasa_data.txt", "r" )
all_text = f.readlines()


f = open("nasa_data.txt", "w")

for line_number, line_text in enumerate(all_text):
    if line_number == 8:
        if "***" in line_text:
            line_text.replace("***", " ") 
    elif line_number > 6 and line_number < 165:
        if "Year" not in line_text and line_text.strip(): 
            f.write(line_text)
        elif x == 0:
            f.write(line_text)
            x += 1


def celsius_to_farenheit():
    for line_number, line_text in enumerate(all_text): 
        for line_text in all_text: 
            if line_number > 0 and line_number < 145:
                data = line_number.split()
                text_to_int = int(line_text)
                farenheit = (text_to_int / 100)*1.8
                print("%.1f" % farenheit)
            else:
                break
        

celsius_to_farenheit()


    
    




   
 


        
        
   

    

    
        











f.close() 
    
