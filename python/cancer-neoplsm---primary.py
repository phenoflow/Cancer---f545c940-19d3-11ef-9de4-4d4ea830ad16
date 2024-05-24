# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"B25..00","system":"readv2"},{"code":"B576.00","system":"readv2"},{"code":"B575z00","system":"readv2"},{"code":"B57..00","system":"readv2"},{"code":"Byu1300","system":"readv2"},{"code":"B313z00","system":"readv2"},{"code":"B315100","system":"readv2"},{"code":"B524.00","system":"readv2"},{"code":"B332z00","system":"readv2"},{"code":"Byu2300","system":"readv2"},{"code":"B312z00","system":"readv2"},{"code":"B314000","system":"readv2"},{"code":"B576z00","system":"readv2"},{"code":"B3z..00","system":"readv2"},{"code":"B312200","system":"readv2"},{"code":"B20..00","system":"readv2"},{"code":"B57z.00","system":"readv2"},{"code":"B312300","system":"readv2"},{"code":"B2...00","system":"readv2"},{"code":"B3y..00","system":"readv2"},{"code":"B312.00","system":"readv2"},{"code":"B314z00","system":"readv2"},{"code":"B574z00","system":"readv2"},{"code":"B312100","system":"readv2"},{"code":"B304z00","system":"readv2"},{"code":"B3...00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cancer-neoplsm---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cancer-neoplsm---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cancer-neoplsm---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
