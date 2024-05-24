# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2024.

import sys, csv, re

codes = [{"code":"B116.00","system":"readv2"},{"code":"B621000","system":"readv2"},{"code":"B004.00","system":"readv2"},{"code":"B562100","system":"readv2"},{"code":"B4A..00","system":"readv2"},{"code":"B05..00","system":"readv2"},{"code":"ByuB100","system":"readv2"},{"code":"B335z00","system":"readv2"},{"code":"B67y.00","system":"readv2"},{"code":"B23y.00","system":"readv2"},{"code":"B561000","system":"readv2"},{"code":"B58yz00","system":"readv2"},{"code":"B5...11","system":"readv2"},{"code":"B561400","system":"readv2"},{"code":"B62x.00","system":"readv2"},{"code":"B18yz00","system":"readv2"},{"code":"Byu4000","system":"readv2"},{"code":"B05y.00","system":"readv2"},{"code":"B13y.00","system":"readv2"},{"code":"B143.00","system":"readv2"},{"code":"B563z00","system":"readv2"},{"code":"Byu1100","system":"readv2"},{"code":"B563.00","system":"readv2"},{"code":"B55y100","system":"readv2"},{"code":"B31y.00","system":"readv2"},{"code":"B62z800","system":"readv2"},{"code":"B00z000","system":"readv2"},{"code":"B560600","system":"readv2"},{"code":"B17y.00","system":"readv2"},{"code":"ByuDE00","system":"readv2"},{"code":"ByuC700","system":"readv2"},{"code":"B560500","system":"readv2"},{"code":"ByuG000","system":"readv2"},{"code":"B2z0.00","system":"readv2"},{"code":"B014.00","system":"readv2"},{"code":"B055.00","system":"readv2"},{"code":"B561800","system":"readv2"},{"code":"B560700","system":"readv2"},{"code":"B62z500","system":"readv2"},{"code":"B561500","system":"readv2"},{"code":"B08y.00","system":"readv2"},{"code":"B06yz00","system":"readv2"},{"code":"B563000","system":"readv2"},{"code":"B58y.00","system":"readv2"},{"code":"B24X.00","system":"readv2"},{"code":"B601000","system":"readv2"},{"code":"B626000","system":"readv2"},{"code":"ByuF900","system":"readv2"},{"code":"B1z0.00","system":"readv2"},{"code":"B62y000","system":"readv2"},{"code":"B561600","system":"readv2"},{"code":"Byu2500","system":"readv2"},{"code":"ByuGN00","system":"readv2"},{"code":"B623000","system":"readv2"},{"code":"B561z00","system":"readv2"},{"code":"B004000","system":"readv2"},{"code":"B627X00","system":"readv2"},{"code":"ByuDC00","system":"readv2"},{"code":"B565z00","system":"readv2"},{"code":"B333z00","system":"readv2"},{"code":"Byu2000","system":"readv2"},{"code":"B563200","system":"readv2"},{"code":"B625000","system":"readv2"},{"code":"B5...00","system":"readv2"},{"code":"ByuGA00","system":"readv2"},{"code":"ByuC600","system":"readv2"},{"code":"B62z200","system":"readv2"},{"code":"B68..00","system":"readv2"},{"code":"ByuA100","system":"readv2"},{"code":"B58..00","system":"readv2"},{"code":"ByuC500","system":"readv2"},{"code":"B1zy.00","system":"readv2"},{"code":"B33y.00","system":"readv2"},{"code":"B627W00","system":"readv2"},{"code":"B56y.00","system":"readv2"},{"code":"B67z.00","system":"readv2"},{"code":"B59..00","system":"readv2"},{"code":"B61z000","system":"readv2"},{"code":"Byu8200","system":"readv2"},{"code":"Byu4300","system":"readv2"},{"code":"B62z300","system":"readv2"},{"code":"B057.00","system":"readv2"},{"code":"B325z00","system":"readv2"},{"code":"B40..00","system":"readv2"},{"code":"B563300","system":"readv2"},{"code":"B17yz00","system":"readv2"},{"code":"B60y.00","system":"readv2"},{"code":"ByuFF00","system":"readv2"},{"code":"ByuC000","system":"readv2"},{"code":"B62xX00","system":"readv2"},{"code":"B45..00","system":"readv2"},{"code":"B483.00","system":"readv2"},{"code":"B67yz00","system":"readv2"},{"code":"B5z..00","system":"readv2"},{"code":"B152.00","system":"readv2"},{"code":"B614000","system":"readv2"},{"code":"Byu5100","system":"readv2"},{"code":"B564z00","system":"readv2"},{"code":"ByuC.00","system":"readv2"},{"code":"B18y.00","system":"readv2"},{"code":"B56z.00","system":"readv2"},{"code":"Byu3300","system":"readv2"},{"code":"B52X.00","system":"readv2"},{"code":"B11yz00","system":"readv2"},{"code":"B564000","system":"readv2"},{"code":"B560400","system":"readv2"},{"code":"B561700","system":"readv2"},{"code":"B565000","system":"readv2"},{"code":"B00z100","system":"readv2"},{"code":"B54y.00","system":"readv2"},{"code":"B5y..00","system":"readv2"},{"code":"B52y.00","system":"readv2"},{"code":"B565300","system":"readv2"},{"code":"B560900","system":"readv2"},{"code":"B560800","system":"readv2"},{"code":"B564100","system":"readv2"},{"code":"B561900","system":"readv2"},{"code":"B620000","system":"readv2"},{"code":"B12y.00","system":"readv2"},{"code":"ByuGC00","system":"readv2"},{"code":"Byu4100","system":"readv2"},{"code":"B560300","system":"readv2"},{"code":"B562400","system":"readv2"},{"code":"B56..00","system":"readv2"},{"code":"Byu5300","system":"readv2"},{"code":"B562z00","system":"readv2"},{"code":"B562.00","system":"readv2"},{"code":"B004200","system":"readv2"},{"code":"B560.00","system":"readv2"},{"code":"Byu7100","system":"readv2"},{"code":"B561200","system":"readv2"},{"code":"B67..00","system":"readv2"},{"code":"B45y.00","system":"readv2"},{"code":"ByuD900","system":"readv2"},{"code":"ByuA000","system":"readv2"},{"code":"B11y.00","system":"readv2"},{"code":"ByuF100","system":"readv2"},{"code":"Byu5700","system":"readv2"},{"code":"Byu1200","system":"readv2"},{"code":"B55y.00","system":"readv2"},{"code":"B59z.00","system":"readv2"},{"code":"B115.00","system":"readv2"},{"code":"B562200","system":"readv2"},{"code":"B06y.00","system":"readv2"},{"code":"B59zX00","system":"readv2"},{"code":"Byu5400","system":"readv2"},{"code":"B565200","system":"readv2"},{"code":"B561300","system":"readv2"},{"code":"B32y.00","system":"readv2"},{"code":"B565.00","system":"readv2"},{"code":"B21y.00","system":"readv2"},{"code":"B454.00","system":"readv2"},{"code":"ByuG900","system":"readv2"},{"code":"Byu7300","system":"readv2"},{"code":"B335.00","system":"readv2"},{"code":"ByuD800","system":"readv2"},{"code":"B58..11","system":"readv2"},{"code":"B582300","system":"readv2"},{"code":"B323.00","system":"readv2"},{"code":"B10y.00","system":"readv2"},{"code":"B560200","system":"readv2"},{"code":"Byu9000","system":"readv2"},{"code":"B624000","system":"readv2"},{"code":"B325.00","system":"readv2"},{"code":"ByuDF00","system":"readv2"},{"code":"ByuD300","system":"readv2"},{"code":"B563100","system":"readv2"},{"code":"ByuHD00","system":"readv2"},{"code":"ByuGH00","system":"readv2"},{"code":"B333.00","system":"readv2"},{"code":"B615000","system":"readv2"},{"code":"B58z.00","system":"readv2"},{"code":"B560000","system":"readv2"},{"code":"B613000","system":"readv2"},{"code":"B562000","system":"readv2"},{"code":"B52..00","system":"readv2"},{"code":"B600000","system":"readv2"},{"code":"B68y.00","system":"readv2"},{"code":"B007.00","system":"readv2"},{"code":"B62z100","system":"readv2"},{"code":"By...00","system":"readv2"},{"code":"ByuA200","system":"readv2"},{"code":"B55yz00","system":"readv2"},{"code":"B562300","system":"readv2"},{"code":"Byu5800","system":"readv2"},{"code":"B07y.00","system":"readv2"},{"code":"B616000","system":"readv2"},{"code":"B560z00","system":"readv2"},{"code":"B560100","system":"readv2"},{"code":"B564.00","system":"readv2"},{"code":"Byu8000","system":"readv2"},{"code":"Byu7000","system":"readv2"},{"code":"B316.00","system":"readv2"},{"code":"B561.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cancer-trunkunspecified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cancer-trunkunspecified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cancer-trunkunspecified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
