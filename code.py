try:
  varlist=[]
  counter=0
  reader = csv.reader(file, 'excel-fr')
  for column in reader:
    varlist.append([])
    varlist[counter].append(column[X])
    varlist[counter].append(column[X+1])
    varlist[counter].append(column[X+2])
    varlist[counter].append(column[X+3])
    varlist[counter].append(column[X+4])
    varlist[counter].append(column[X+5])
    varlist[counter].append(column[X+6])
    counter+=1
finally:
    file.close()
    
    length=len(varlist)
    for var1 in range(length): #nb sous listes
      for var2 in range(7): #nb valeurs par sous listes
        varlist[var1][var2]=int(varlist[var1][var2])
    varlist_v1v0 #tri selon varlist[var1][0]
    for var3 in range(1,51): #Tri selon 51 premieres valeurs possible
      varlist_v1v0.append([])
      for var1 in range(length):
          if varlist[var1][0]==var3:
            varlist_v1v0[var3-1].append(varlist[var1])
