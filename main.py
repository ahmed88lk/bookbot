with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    
def number_of_characters(file_contents):
    return len(file_contents.split())       
    
def count_words(file_contents):
    dict = {}
    #file_contents.lower()
    words = file_contents.split()
    words = [word.lower() for word in words]
    text= ''.join(words)

    
    
    for char in text:
        if char in "abcdefghijklmnopqrstuvwxyz":
            if char in dict and char :
                 dict[char] += 1
            else:
                dict[char] = 1
                
    sorted_word_count = sorted(dict.items(), key=lambda item: item[1], reverse=True)       
    return sorted_word_count         

 







if __name__ == '__main__':


    print(count_words(file_contents))
    print(number_of_characters(file_contents))
    
    print('--- Begin report of books/frankenstein.txt ---')
    print('{}   words found in the document'.format(number_of_characters(file_contents)))
    for i in count_words(file_contents):
        print('The  {} character was found {} times'.format (i[0], i[1]))
    print('--- End of report ---')