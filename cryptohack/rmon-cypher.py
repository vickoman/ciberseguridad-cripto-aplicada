alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
iterations = len(alphabet)
posibilities = []
def decoded_phrase(phrase, n):
    output = ""
    for char in phrase:
        if(char in alphabet):
            output += alphabet[(alphabet.index(char) - n) % len(alphabet)]
        else:
            output += " "
    return output

def decode_by_iteration(phrase):
    for i in range(iterations):
        phrase_decode = decoded_phrase(phrase, i)
        posibilities.append(phrase_decode)

    print_posibilities()

def print_posibilities():
    for i in posibilities:
        print(i)

# Encode Phrase
def encode_phrase(phrase, n):
    output = ""
    for char in phrase:
        if(char in alphabet):
            output += alphabet[(alphabet.index(char) + n) % len(alphabet)]
        else:
            output += " "
    return output


decode_by_iteration("KTQQTB YMJ WFGGNY MTQJ")
# ecoded = encode_phrase("FOLLOW THE RABBIT HOLE", 5); #KTQQTB YMJ WFGGNY MTQJ
# print(ecoded)