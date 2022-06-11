# TBC_VIA_FL2K

This GNRC flowgraph takes in a .tbc file from ld-decode or vhs-decode (vhs-decode would need to have the Y+C combined version of the .tbc file) and converts it to signed 8 bit and discards the extra line. I tried piping the flowgraph output direclty to fl2k_file but it couldn't keep up on the machine i was using. 

## Steps to use:

You'll need osmo-fl2k and gnu radio companion packages installed and all dependencies

Open the flowgraph, edit the path field of 'file source block' and 'file sink block'

run the graph

use `fl2k_file -s 14318181 outfile.s8` to pipe the file out

## Notes:

910 for NTSC, 1135 for PAL in the `line_length` variable block

525 for NTSC, 625 for PAL in the `lines_per_frame` variable block

fl2k_file only uses the `red` vga signal and ground. 

for the purposes of this flowgraph, the "sample_rate" doesn't do anything but determine how much compute resources are used. 

## In action

NTSC https://www.youtube.com/watch?v=4cjxmLpXbyE

PAL https://www.youtube.com/watch?v=MPpJ179-ZC4

## Refrecnces

https://www.rtl-sdr.com/osmo-fl2k-a-tx-only-sdr-hacked-from-commodity-5-usb-to-vga-adapters-demos-available-for-transmitting-wbfm-gsm-umts-gps/

https://osmocom.org/projects/osmo-fl2k/wiki/Osmo-fl2k 
