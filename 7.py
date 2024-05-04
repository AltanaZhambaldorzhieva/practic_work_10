with (open("/Users/altanazambaldorzieva/Desktop/input.txt", "r") as input_file,
      open("/Users/altanazambaldorzieva/Desktop/output.txt", "w") as output_file):
    num = list(map(str.strip, input_file.readlines()))
    for _ in num:
        if _ != '100':
            output_file.write(_)
        else:
            output_file.write('\n')
