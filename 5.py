try:
    with (open("/Users/altanazambaldorzieva/Desktop/input.txt", "r") as input_file,
          open("/Users/altanazambaldorzieva/Desktop/output.txt", "w") as output_file):
        num1, num2, num3 = map(int, input_file.readline().split('\n'))
        result = num1 / num2 + num3
    output_file.write(str(result))

except ZeroDivisionError:
    output_file.write('division dy 0')
except ValueError:
    output_file.write('Data error')





