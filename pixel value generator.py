from PIL import Image
import csv

#taking each image slice and extrating it's pixel values
im = Image.open("output_cropped0.bmp", "r")
pix_val = list(im.getdata())
#print(pix_val)
pix_val_flat = [x for sets in pix_val for x in sets]
#print(pix_val_flat)

#converting the list to csv file
with open('output_cropped0.csv', 'wt') as output_write:
    csvout = csv.writer(output_write, delimiter=',')
    for c in pix_val_flat:
         csvout.writerow([c])