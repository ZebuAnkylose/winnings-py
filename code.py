try:
  list=[]
  counter=0
  reader = csv.reader(file, 'excel-fr')
  for column in reader:
    list.append([])
    list[counter].append(column[X])
    list[counter].append(column[X+1])
    list[counter].append(column[X+2])
    list[counter].append(column[X+3])
    list[counter].append(column[X+4])
    list[counter].append(column[X+5])
    list[counter].append(column[X+6])
    counter+=1
