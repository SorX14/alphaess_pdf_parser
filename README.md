# Reader

Simple python script to extract register names and values from the AlphaESS PDF

PDF can be found here: https://www.alpha-ess.de/images/downloads/handbuecher/AlphaESS-Handbuch_SMILET30_ModBus_RTU_V123-DE.pdf

## Usage

Hopefully shouldn't be needed again, but just in case...

Open PDF in Word, copy table to Excel and save as CSV (probably easier ways to do it).

Name output CSV to `alpha csv.csv` and put in the same directory as `reader.py`.

Run `./reader.py` and copy resulting `registers.json`.

## Notes

Wasn't made to be particularly smart or to check errors, probably gets some registers wrong. Idea is
to massively speed up the time needed to parse the data out. You might need to manually fix the result.

Doesn't check for duplicates or if the units are sensible. Doesn't handle units/decimals that aren't
0.1, 0.01 etc. Some units are obviously wrong, e.g. `bmu20_version` which has `:BMU-HV/`. 

