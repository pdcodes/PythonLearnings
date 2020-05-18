output_strings = []
final_message = ''

def sentence_maker(phrase):
    cap_phrase = phrase.capitalize()
    interrogatives = ("How", "What", "Why")
    if cap_phrase.startswith(interrogatives):
        return "{}?".format(cap_phrase)
    else:
        return "{}.".format(cap_phrase)

while True:
    input_string = input("Say something: ")
    if input_string == "\end":
        print(" ".join(output_strings))
        break
    else:
        output_strings.append(sentence_maker(input_string))
        continue