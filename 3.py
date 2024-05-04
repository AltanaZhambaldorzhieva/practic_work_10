with (open("/Users/altanazambaldorzieva/Desktop/input.txt", "r") as input_file,
      open("/Users/altanazambaldorzieva/Desktop/output.txt", "w") as output_file):
    word = ''
    for line in input_file:
        first_char = line[0]
        word += first_char
    output_file.write(word)


