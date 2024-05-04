try:
    with (open("/Users/altanazambaldorzieva/Desktop/input.txt", "r") as input_file,
          open("/Users/altanazambaldorzieva/Desktop/output.txt", "w") as output_file):
        strok = list(map(str.strip, input_file.readlines()))
        if len(strok) - 1 == int(strok[0]):
            output_file.write('YES')
        else:
            output_file.write('NO')
except ValueError:
    output_file.write('Value error')
        