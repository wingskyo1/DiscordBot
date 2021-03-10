# count function 
def count(str1, str2):  
    set_string1 = set(str1) 
    set_string2 = set(str2) 
    matched_characters = set_string1 & set_string2 
    print("No. of matching characters are : " + str(len(matched_characters)) ) 
  
# Main function 
def main():  
    str1 ='3592' # first string 
    str2 ='1572' # second string 
    count(str1, str2) # calling count function  
  
# Driver Code 
if __name__=="__main__": 
    main() 