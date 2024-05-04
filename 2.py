with (open("/Users/altanazambaldorzieva/Desktop/input.txt", "r") as input_file,
      open("/Users/altanazambaldorzieva/Desktop/output.txt", "w") as output_file):
    for line in input_file:
        if line.startswith('A') or line.startswith('a'):
            output_file.write(line)


