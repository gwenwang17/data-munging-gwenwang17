import csv

sum = 0
averages = []
decades = []
with open('clean_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=' ')
    line_count = 0
    final_year = None
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        else:
            # J-D or average is the 13th element
            yr_average = float(row[13])
            sum += yr_average

            yr = int(row[0])

            if yr % 10 == 0:
                decades.append(yr)
            if yr % 10 == 9:
                average = sum/10.0
                averages.append("{:.1f}".format(average))
                sum = 0

            line_count += 1
            final_year = yr
    # need to consider the case for the last decade (2020-2022) where 2022%10 != 9
    # we divide by the number of years in the decade which is final_year % 10 + 1
    num_years = int(final_year) % 10 + 1
    average = sum/num_years
    averages.append("{:.1f}".format(average))

print(decades)
print(averages)
