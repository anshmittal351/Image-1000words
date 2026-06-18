from PIL import Image

def import_words_list():
    # imports the list of words in "words.txt"
    with open("words.txt", "r") as file:
        vocab_list = file.read().splitlines()

    vocab_list.sort() # for binary search
    print(f"Successfully loaded {len(vocab_list)} words into the list!")
    return vocab_list

def import_1000_words(path):
    with open(path, "r") as file:
        return file.read()

def binary_search(list, word):
    current_word = ""
    current_index = 0
    min_index = 0
    max_index = len(list) - 1

    while not current_word == word:
        # repeats this loop until the word has been reached
        current_index = (max_index + min_index)//2
        current_word = list[current_index]

        # alphabetically checks if the current word is before or after the target word
        if current_word > word:
            max_index = current_index - 1
        elif current_word < word:
            min_index = current_index + 1
    
    return current_index

def convert_words_to_binary(list, words):
    word_amount = binary_search(list, words[0])
    remainder_bits = binary_search(list, words[1])
    binary_list = []
    for i in range(word_amount):
        int_value = binary_search(list, words[i+2])
        binary_value = format(int_value, '013b')
        if i == word_amount - 1 and remainder_bits > 0:
            binary_value = binary_value[-remainder_bits:]
        binary_list.append(binary_value)
    
    binary_text = "".join(binary_list)
    return binary_text

def convert_bits_to_bytes(binary):
    bytes_list = []
    for i in range(0, len(binary), 8):
        byte = binary[i : i + 8]
        bytes_list.append(int(byte, 2))
    
    return bytes(bytes_list)



def decode_image(path):
    str_1000_words = import_1000_words(path)
    vocab_list = import_words_list()
    words_list = str_1000_words.split(" ")
    print('step 1 complete!')
    binary_text = convert_words_to_binary(vocab_list, words_list)
    print('step 2 complete!')
    converted_bytes = convert_bits_to_bytes(binary_text)
    print('step 3 complete!')

    with open("output.avif", "wb") as output_file: # output file format can be changed here
        output_file.write(converted_bytes)
    
    print("The image has been successfully restored!")


decode_image("1000_words.txt")
