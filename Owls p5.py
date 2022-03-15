text = input("Enter some text : ")
#print (text)
text = text.lower()
#print (text)
text_list = text.split()
#print (text_list)
counter = 0
for word in text_list:
    if "owl" in word:
        counter = counter + 1
print ("There were", counter, "words that contain owl") 
        
        
