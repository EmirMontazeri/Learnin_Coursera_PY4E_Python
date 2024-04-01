# Use find and string slicing to extract the portion of the string after the colon
#charactar and then use float function to convert the extracted string into a
#floating point number

data = 'X-DSPAM-Confidence: 0.8475 '
startpoint = data.find(':')
endpoint = data.find(' ' , startpoint + 2)
slice = float(data[startpoint + 2 : endpoint])
print('Desired Data:',slice)