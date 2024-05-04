with (open("/Users/altanazambaldorzieva/Desktop/input.txt", "r") as input_file,
      open("/Users/altanazambaldorzieva/Desktop/output.txt", "w") as output_file):
    text = input_file.read()
    upper_text = text.upper()
    output_file.write(upper_text)



