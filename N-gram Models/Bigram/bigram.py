pair_dict = []
freq = []
print("Type stop the training to stop the training")
while True:
    sentence1 = input("Enter your sentence: ")
    if sentence1 == "stop the training":
        break
    sentence = list(map(str, sentence1.split()))

    
    

    # print(sentence)



    def making_list(sentence, pair_dict, freq):
        for i in range(len(sentence) - 1):
            pair = [sentence[i], sentence[i + 1]]
            if pair not in pair_dict:
                pair_dict.append(pair)
                freq.append(1)
            else:
                index = pair_dict.index(pair)
                freq[index] += 1
    making_list(sentence, pair_dict, freq)           
# print("Pairs:", pair_dict)
# print("Frequencies:", freq)

#taking user input
print("Type stop the program12 for terminating the programme")
while True:
    user_input1 = input("\nType some text below to autocomplete\n")
    if user_input1 == "stop the program12":
        break
    
    user_input = list(map(str, user_input1.split()))
    words = int(input("No of words for autocompletion:"))

    result = user_input[-1]

        
        
    for c in range(words):
        
        word_freq = []
        for j in range(len(pair_dict)):
            word_freq_pair = [pair_dict[j][1],freq[j]]
            
            if(pair_dict[j][0] == result): 
                word_freq.append(word_freq_pair)    
        
        
        word_count = word_freq[0][1]
        word = word_freq[0][0]       
        for d in range(len(word_freq) - 1):

            if(word_freq[d + 1][1]> word_count):
                word_count = word_freq[d+1][1]
                word = word_freq[d + 1][0]
                
            
                
        print(word, end = " ")
        result = word
        # word_index = word_freq.index(max(word_freq[:][1]))
        # result.append(word_freq[word_index][0])
            



                
