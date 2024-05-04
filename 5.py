try:
    with (open("/Users/altanazambaldorzieva/Desktop/input.txt", "r") as input_file,
          open("/Users/altanazambaldorzieva/Desktop/output.txt", "w") as output_file):
        num = list(map(str.strip, input_file.readlines()))
        result = int(num[0]) / int(num[1]) + int(num[2])
    output_file.write(str(result))
except ZeroDivisionError:
    output_file.write('division dy 0')
except ValueError:
    output_file.write('Data error')





