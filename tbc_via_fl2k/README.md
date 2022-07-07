# TBC_VIA_FL2K

This GNRC flowgraph takes in a .tbc file from ld-decode or a combined vhs-decode tbc file,  and converts it to signed 8 bit and discards the extra line. I tried piping the flowgraph output direclty to fl2k_file but it couldn't keep up on the machine i was using. 

# VHS-TBC_VIA_FL2K

This GNRC flowgraph takes in the 2 .tbc files from vhs-decode and converts it to signed 8 bit and discards the extra line (credit to Itewreed#2179@discord who contributed to this).

## Steps to use:

You'll need osmo-fl2k and gnu radio companion packages installed and all dependencies

Open the flowgraph, edit the path field of 'file source block' and 'file sink block'

run the graph

use `fl2k_file -s 14318181 outfile.s8` to pipe the file out for NTSC, and `fl2k_file -s 17734475 outfile.s8` to pipe the file out for PAL


## Notes:

910 for NTSC, 1135 for PAL in the `line_length` variable block

525 for NTSC, 625 for PAL in the `lines_per_frame` variable block

fl2k_file only uses the `red` vga signal and ground. 

for the purposes of this flowgraph, the "sample_rate" doesn't do anything but determine how much compute resources are used. 

My tests with USB2 connection, indicate that there are some pretty big variances on how high you can acheive connected with 
USB2.0. My 1st machine was around 12mhz, 12.5mhz would not work. However my second machine, 14,318,181mhz worked, but PAL
~17,734,400 would not. The highest rate for USB2 + fl2k seems to vary.

## Troubleshooting:

The error about allocating the memory buffer is normal, just do what it says: 
	echo 0 > /sys/module/usbcore/parameters/usbfs_memory_mb

If you get an error like this:
	libusb: error [submit_bulk_transfer] submiturb failed error -1 errno=2

Then you need to `apt remove osmo-fl2k` and follow the directions on the osmo-fl2k wiki on how to build it yourself. I 
suspect it is a kernel headers issue? Link below.

If your device won't recognize the signal (or it isn't stable), you can try and use the `high gain` flowgraph. This graph
adjusts the values so the cvbs signal uses the full range of the DAC. This could have unintended side effects (clipping)
as the values were based on a particular TBC file I was using at the time.


## In action

NTSC https://www.youtube.com/watch?v=4cjxmLpXbyE

PAL https://www.youtube.com/watch?v=MPpJ179-ZC4

## Refrecnces

https://www.rtl-sdr.com/osmo-fl2k-a-tx-only-sdr-hacked-from-commodity-5-usb-to-vga-adapters-demos-available-for-transmitting-wbfm-gsm-umts-gps/

https://osmocom.org/projects/osmo-fl2k/wiki/Osmo-fl2k 
