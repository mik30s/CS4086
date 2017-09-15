"""
Quesition 1
table with dictionaries representing each impact
"""
table = {
    100:{"ke":47,    "ie":38,    "cd":1.2,  "af":5200 },
    130:{"ke":103,   "ie":64.8,  "cd":2.0,  "af":11000 },
    150:{"ke":159,   "ie":71.5,  "cd":2.4,  "af":16000 },
    200:{"ke":376,   "ie":261,   "cd":3.0,  "af":36000 },
    250:{"ke":734,   "ie":598,   "cd":3.8,  "af":59000 },
    300:{"ke":1270,  "ie":1110,  "cd":4.6,  "af":73000 },
    400:{"ke":3010,  "ie":2800,  "cd":6.0,  "af":100000 },
    700:{"ke":16100, "ie":15700, "cd":10.0, "af":190000 },
    1000:{"ke":47000, "ie":46300, "cd":13.6, "af":440000 }
}

while True:
    diameter = input("Enter a diameter (meters): ")
    if not(100 <= diameter <= 1000): 
      print "Diameter %d out of bounds" % diameter
      continue
    else:
        entry = table.get(int(diameter))
        if entry == None: 
          print "Unknown impact diameter"
          continue
        else:
          print entry["af"]
          # sort the keys first
          keys = sorted(table.keys())
          for i in range(1, len(keys) + 1):
              if diameter in range(keys[i-1], keys[i]):
                  print "hi %d low: %d" % (keys[i-1], keys[i])
                  break
