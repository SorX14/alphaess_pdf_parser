#!/usr/bin/env python3

from csv import reader
import json
import itertools

rows = []
with open('alpha csv.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        # Ignore rows with blanks in any of the first three columns
        if row[0] == '' or row[1].strip() == '' or row[2] == '':
            #print(f"IGNORING {row}")
            continue

        if not row[0].endswith('H'):
            continue

        rows.append(row)

print(f"Found {len(rows)} rows")
formattedRows = []
stop = None
#stop = 10

for row in itertools.islice(rows, 0, stop):
#for row in rows:

    # Trim, turn into underscores, lowercase
    name = row[1].lower().strip().replace("  ", " ").translate({ord(ch): "_" for ch in ' (-'}).translate({ord(ch): None for ch in ')'})
    
    # Convert HEX to INT
    address = int(f"0x{row[0][:-1]}", 16)

    #print(row)
    #print(f"[{row[3].replace('Belegt', '').strip()}]")

    # Determine length of register
    type = "register"
    if row[3].replace('Belegt', '').strip() == "4":
        type = "long"

    # If its signed or unsigned
    signed = True
    if "unsigned" in row[4]:
        signed = False
    
    # Basic check for decimals of resulting value
    decimals = 0
    if "0.1" in row[5]:
        decimals = 1
    elif "0.01" in row[5]:
        decimals = 2
    elif "0.001" in row[5]:
        decimals = 3
    
    # Do the bare minimum to extra the register unit type
    unitColumn = row[5]
    if unitColumn.lower().find("/bit") > -1:
        unitColumn = unitColumn[0:unitColumn.lower().find("/bit")]
    unitColumn = unitColumn.translate({ord(ch): None for ch in ' .0123456789'}).strip()

    # Conform some units to SI
    if unitColumn.lower() == "w":
        unitColumn = "W"

    if unitColumn.lower() == "kwh":
        unitColumn = "KWh" 

    units = unitColumn

    formatted = {
        "name": name,
        "address": address,
        "hex": f"0x{row[0][:-1]}",
        "type": type,
        "signed": signed,
        "decimals": decimals,
        "units": units
    }
    #print(formatted)
    formattedRows.append(formatted)

# Write JSON to file
filename = "alphaess_registers.json"
f = open("alphaess_registers.json", "w")
f.write(json.dumps(formattedRows, indent=4))
f.close()
print(f"Written output to {filename}")

