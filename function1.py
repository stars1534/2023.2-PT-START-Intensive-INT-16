###Required function###

def title(str_in):

    words_list = str_in.split(' ') #Create list of words divided by ' '
    words_list_mod = [] #Create empty list

    for i in range(len(words_list)):
        words = words_list[i] #Supporting variable
        if len(words) > 1: #Condition for words contain 2 or more letters
            words = words[0].upper() + words[1:] #Turn the first letter of each word in words_list uppercase
        else:
            words = words.upper() #Make the same operation for 1 letter words
        words_list_mod.append(words) #Put modified words in empty list

    str_out = words_list_mod[0] #Add first word or space to the new empty string for comfort computing in advance

    for i in range(1, len(words_list_mod)):
        words = words_list_mod[i] #Supporting variable
        str_out += ' ' + words #Add other left words or spaces

    return str_out

###Demo code###

#str_in = '    9hello mister  s   shmi%ster watching TV on the sOFA %^& '

str_mod = title(input())

print(str_mod) #Cheking the output string