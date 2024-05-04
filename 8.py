with (open("/Users/altanazambaldorzieva/Desktop/input.txt", "r") as input_file,
      open("/Users/altanazambaldorzieva/Desktop/output.txt", "w") as output_file):
    day = list(map(str.strip, input_file.readlines()))
    k = 0
    month = 0
    for i in range(12):
        if i % 2 == 0 and i != 2:
            for j in range(31):
                k += int(day[month])
                month += 1
            output_file.write(str(k / 31))
            output_file.write('\n')
            k = 0
        else:
            for j in range(30):
                k += int(day[month])
                month += 1
            output_file.write(str(k / 30))
            output_file.write('\n')
            k = 0
    print(month)

