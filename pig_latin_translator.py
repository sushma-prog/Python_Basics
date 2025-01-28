##get sentence from user

original=input("please enter a sentence:").lower().strip()

##split sentence into words # we will use a string method called slpit

words= original.split()#.split() will convert the original sentence into list of words of sentence 

##loop through words and convert to pig latin

new_words=[]#we will store new pig latin words in this list

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"#this will add the "yay" to the word
        new_words.append(new_word)#this will add new word to the end of the list new_words
    else:
    #we will need to loop through each letter of each word(words that do not start with vowel) to find out the consonent cluster inside each word.     
        vowel_position=0    #we will use new veriable to lopp
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else:
                break    #it will break loop after vowel is found in each word
        consonent= word[:vowel_position]    #we will slice out consonent cluster in word prom 0th index to the index of vowel_position
        the_rest= word[vowel_position:]     #we will slice out the letters from index of vowel_position till the end
        new_word=the_rest + consonent + "ay" #now new word will be the rest part then the consonent part then "ay" at last 
        new_words.append(new_word)


##stick modified words back together into a sentence

output=" ".join(new_words)#we used string method called join to stick together words as a sentence(" " is used to give space between each word)

##output the final string

print(output)
