# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"B311.00","system":"readv2"},{"code":"B336z00","system":"readv2"},{"code":"B621400","system":"readv2"},{"code":"B337z00","system":"readv2"},{"code":"B326.00","system":"readv2"},{"code":"B555.00","system":"readv2"},{"code":"B337.00","system":"readv2"},{"code":"B612400","system":"readv2"},{"code":"Byu3100","system":"readv2"},{"code":"B326z00","system":"readv2"},{"code":"B327.00","system":"readv2"},{"code":"B336.00","system":"readv2"},{"code":"B554.00","system":"readv2"},{"code":"B30X.00","system":"readv2"},{"code":"B327z00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cancer-limbunspfd---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cancer-limbunspfd---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cancer-limbunspfd---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
