data = {"Terrel Kennedy":
        {"Position": "Forward",
         "Height": "6 Ft. 7 In.",
         "Weight": "245 Lbs",
         "Lives": "Jackson, MS"},
        "Cordarly Campbell":
        {"Position": "Guard",
         "Height": "6 Ft. 3 In.",
         "Weight": "190 Lbs",
         "lives": "Rosedale, MS"},
        "Jamarcus Holt":
        {"Position": "Forward",
            "Height": "6 Ft. 8 In.",
            "Weight": "250 Lbs",
            "lives":"Cleveland, MS"}
        }
for x in dict(data):
    data[x]["Name"] = x 
SortedByHeight = []
SortedByHeight2 = []
c = 0
for x in data:
  if len(SortedByHeight2) == 0:
    SortedByHeight2.append(data[x]["Height"])
    SortedByHeight.append(data[x])
  else:
    q = False
    for y in range(len(SortedByHeight2)):
      if data[x]["Height"] > SortedByHeight2[y]:
        SortedByHeight2.insert(y, data[x]["Height"])
        SortedByHeight.insert(y, data[x])
        q = True
    if not q:
      SortedByHeight2.append(data[x]["Height"])
      SortedByHeight.append(data[x])
SortedByName = []
SortedByName2 = []
c = 0
for x in data:
  if len(SortedByName2) == 0:
    SortedByName2.append(data[x]["Name"])
    SortedByName.append(data[x])
  else:
    q = False
    for y in range(len(SortedByName2)):
      if data[x]["Name"] > SortedByName2[y]:
        SortedByName2.insert(y, data[x]["Name"])
        SortedByName.insert(y, data[x])
        q = True
    if not q:
      SortedByName2.append(data[x]["Name"])
      SortedByName.append(data[x])
SortedByPosition = []
SortedByPosition2 = []
c = 0
for x in data:
  if len(SortedByPosition2) == 0:
    SortedByPosition2.append(data[x]["Position"])
    SortedByPosition.append(data[x])
  else:
    q = False
    for y in range(len(SortedByPosition2)):
      if data[x]["Position"] > SortedByPosition2[y]:
        SortedByPosition2.insert(y, data[x]["Position"])
        SortedByPosition.insert(y, data[x])
        q = True
    if not q:
      SortedByPosition2.append(data[x]["Position"])
      SortedByPosition.append(data[x])
SortedByWeight = []
SortedByWeight2 = []
c = 0
for x in data:
  if len(SortedByWeight2) == 0:
    SortedByWeight2.append(data[x]["Weight"])
    SortedByWeight.append(data[x])
  else:
    q = False
    for y in range(len(SortedByWeight2)):
      if data[x]["Weight"] > SortedByWeight2[y]:
        SortedByWeight2.insert(y, data[x]["Weight"])
        SortedByWeight.insert(y, data[x])
        q = True
    if not q:
      SortedByWeight2.append(data[x]["Weight"])
      SortedByWeight.append(data[x])


print("var SortedByName =", SortedByName, end=";\n")
print("var SortedByPosition =", SortedByHeight, end=";\n")
print("var SortedByHeight =", SortedByHeight,end=";\n")
print("var SortedByWeight =", SortedByWeight,end=";\n")
