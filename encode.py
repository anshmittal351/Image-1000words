from PIL import Image
import random

# ENCODE AN IMAGE INTO TEXT

def convert_image_to_binary(image_path):
    # opens the image and convert it to a large binary string
    with open(image_path, "rb") as image_file:
        raw_bytes = image_file.read()

    binary_string = "".join(format(byte, "08b") for byte in raw_bytes)

    return binary_string

def import_words_list():
    # imports the list of words in "words.txt"
    with open("words.txt", "r") as file:
        vocab_list = file.read().splitlines()

    vocab_list.sort()
    print(f"Successfully loaded {len(vocab_list)} words into the list!")
    return vocab_list

def convert_to_words(binary, words):
    # converts the binary string to words
    words_list = []
    list_13_digits = []
    num = 0
    count = 0
    for i in range(len(binary)):
        if count == 13:
            num = int("".join(list_13_digits), 2)
            words_list.append(words[num])
            list_13_digits = [binary[i]]
            count = 1
        else:
            list_13_digits.append(binary[i])
            count += 1
            if i == len(binary) - 1:
                list_13_digits.append(binary[i])
                count += 1
                num = int("".join(list_13_digits), 2)
                words_list.append(words[num])

    return words_list

def encode_image(path):
    final_list = []
    binary_image = convert_image_to_binary(path)
    vocab_list = import_words_list()
    words = convert_to_words(binary_image, vocab_list)
    remainder_len = len(binary_image) % 13


    final_list.append(vocab_list[len(words)])
    final_list.append(vocab_list[remainder_len])
    # the first 2 words of the text will be how many words the image takes up, and the number of bits in the final word

    final_list += words
    # next, the data from the words is added

    while len(final_list) < 1000:
        final_list.append(random.choice(vocab_list))

    final_string = " ".join(final_list)

    with open("1000_words.txt", "w") as file:
        file.write(final_string)

    print("image converted successfully!")

encode_image("ENCODE.zip") # input file format can be changed here