import sys
import mmr_fetch
import csv

inFile = sys.argv[1]

##run file inline terminal 'python program.py data.csv'
with open(inFile, 'r') as csv_file:
	reader = csv.DictReader(csv_file)
	for row in reader:
		print(row['vin'], row['year'], row['make'], row['model'], row['trim'], row['mileage'])
		if len(row['vin'])==17:
			vin=row['vin']
			mileage=row['mileage']
			mmr_value=mmr_fetch.get_mmr(vin, mileage)
			with open('/Users/pxteam/Desktop/fetch_mmr/mmr_results.csv','a') as csv_outfile:
				fieldnames=['vin', 'mileage', 'mmr_value']
				writer=csv.DictWriter(csv_outfile, fieldnames=fieldnames)
				writer.writerow({'vin':vin, 'mileage':mileage, 'mmr_value':mmr_value})
			

	
	