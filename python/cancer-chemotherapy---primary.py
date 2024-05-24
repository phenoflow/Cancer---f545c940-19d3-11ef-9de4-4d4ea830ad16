# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"B03y.00","system":"readv2"},{"code":"B581.00","system":"readv2"},{"code":"B66yz00","system":"readv2"},{"code":"ByuGD00","system":"readv2"},{"code":"ByuG700","system":"readv2"},{"code":"ByuF300","system":"readv2"},{"code":"B33..00","system":"readv2"},{"code":"B49y.00","system":"readv2"},{"code":"ByuD000","system":"readv2"},{"code":"Byu4200","system":"readv2"},{"code":"B48..00","system":"readv2"},{"code":"B57y.00","system":"readv2"},{"code":"ByuD700","system":"readv2"},{"code":"ByuFA00","system":"readv2"},{"code":"ByuD400","system":"readv2"},{"code":"ByuG100","system":"readv2"},{"code":"ByuD600","system":"readv2"},{"code":"ByuGB00","system":"readv2"},{"code":"Byu4.00","system":"readv2"},{"code":"ByuFG00","system":"readv2"},{"code":"ByuD200","system":"readv2"},{"code":"ByuA300","system":"readv2"},{"code":"B2zy.00","system":"readv2"},{"code":"8CP1.00","system":"readv2"},{"code":"B1z..00","system":"readv2"},{"code":"B573.00","system":"readv2"},{"code":"B51yz00","system":"readv2"},{"code":"ByuF600","system":"readv2"},{"code":"B627B00","system":"readv2"},{"code":"B52W.00","system":"readv2"},{"code":"K9611","system":"readv2"},{"code":"Byu5B00","system":"readv2"},{"code":"B41yz00","system":"readv2"},{"code":"B02y.00","system":"readv2"},{"code":"B584.00","system":"readv2"},{"code":"B66y.00","system":"readv2"},{"code":"B591.00","system":"readv2"},{"code":"B16y.00","system":"readv2"},{"code":"B55z.00","system":"readv2"},{"code":"8BAD000","system":"readv2"},{"code":"B04y.00","system":"readv2"},{"code":"B24y.00","system":"readv2"},{"code":"B44..00","system":"readv2"},{"code":"B34yz00","system":"readv2"},{"code":"B31..00","system":"readv2"},{"code":"B48yz00","system":"readv2"},{"code":"B581z00","system":"readv2"},{"code":"B35z.00","system":"readv2"},{"code":"B62..00","system":"readv2"},{"code":"B55..00","system":"readv2"},{"code":"ByuC100","system":"readv2"},{"code":"Byu5000","system":"readv2"},{"code":"ByuD100","system":"readv2"},{"code":"B54..00","system":"readv2"},{"code":"8CL1.00","system":"readv2"},{"code":"ByuD500","system":"readv2"},{"code":"B48y.00","system":"readv2"},{"code":"B01y.00","system":"readv2"},{"code":"B34y.00","system":"readv2"},{"code":"B63y.00","system":"readv2"},{"code":"B48z.00","system":"readv2"},{"code":"B22y.00","system":"readv2"},{"code":"B20y.00","system":"readv2"},{"code":"B65yz00","system":"readv2"},{"code":"ByuB.00","system":"readv2"},{"code":"B64y.00","system":"readv2"},{"code":"B4Ay.00","system":"readv2"},{"code":"67G2.00","system":"readv2"},{"code":"B64yz00","system":"readv2"},{"code":"B51y.00","system":"readv2"},{"code":"B43y.00","system":"readv2"},{"code":"B41y.00","system":"readv2"},{"code":"B14y.00","system":"readv2"},{"code":"B44y.00","system":"readv2"},{"code":"B2z..00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cancer-chemotherapy---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cancer-chemotherapy---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cancer-chemotherapy---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
