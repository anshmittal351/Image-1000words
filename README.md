# Image-1000words
This is a program I've created in Python for my Youtube Channel: @Cobalt_Dev
It converts any image or file into a string of exactly 1000 words as long as the file is under 1.62kb.
If the file is any larger, the text will end up being more than a thousand words.

The "encode" script takes multiple steps to convert the input file into 1000 words:
1. It converts the file into binary
2. It separates it into chunks of 13 bits
3. Each chunk is converted to a word
4. Additional metadata is added and the text is saved as a file

To decode the text, another script performs these steps:
1. It separates the text into a list of words
2. Each word is converted into 13 bits using binary search
3. The final sequence of bits is converted back into a file

If you want to try it out, I've left a demo input image, which is 1.5kb in size.

I recommend you use Google's tool squoosh.app to compress your own images in AVIF format.

I've also left a challenge:
The first person to decode the text "challenge.txt" and comment the output on my Youtube video will get pinned and will recieve a shoutout in the next video!

VIDEO LINK: [not published yet]

This is my first piece of published code, so I apologize if any code is inefficient or contains confusing variable names.

CREDITS:
github.com/first20hours/google-10000-english/ - list of 10000 english words, I removed 2000 for my list of 8192 (2^13) words
https://www.pinterest.com/pin/56506170337246384/ - Sunset Image used as the demo input image
