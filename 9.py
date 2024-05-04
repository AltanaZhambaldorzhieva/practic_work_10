import os
with (open("/Users/altanazambaldorzieva/Desktop/input.txt", "r") as input_file,
      open("/Users/altanazambaldorzieva/Desktop/output.txt", "w") as output_file):
    if not os.path.exists('simple'):
        os.mkdir('simple')
        lines = input_file.readlines()
        for i, line in enumerate(lines):
            if i % 2 == 1:
                output_file.write(line)
