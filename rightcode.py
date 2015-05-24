try:
  varlist=[]
  counter=0
  reader = csv.reader(file, 'excel-fr')
  for raw in reader:
    varlist.append([])
    varlist[counter].append(raw[X+5])
    varlist[counter].append(raw[X+6])
    counter+=1
finally:
    file.close()
    
length=len(varlist) #nb sous listes
for var1 in range(length):
  for var2 in range(2): #2 --> nb valeurs par sous listes
    varlist[var1][var2]=int(varlist[var1][var2])
varlist_v1v0=[] #tri selon varlist[var1][0]
for var3 in range(1,12): #11 --> nb valeurs pour var2
  varlist_v1v0.append([])
  for var1 in range(length):
    if varlist[var1][0]==var3:
      varlist_v1v0[var3-1].append(varlist[var1])
