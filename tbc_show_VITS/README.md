# TBC_SHOW_VITS

This GNRC flowgraph takes in a .tbc file from ld-decode or vhs-decode and shows the VITS info you specify in the variables. It can also save the output to a file (unsigned 8) that can be further processed with ffmpeg/ffplay/etc. 

## Steps to use:

You'll need gnu radio companion packages installed and all dependencies

Open the flowgraph, edit the path field of 'file source block' and 'file sink block' (if you want to save a file)

run the graph

use something like:`ffplay -f rawvideo -pix_fmt gray8 -video_size 910x880 -i /tmp/outfile.u8`

where width is NTSC 910 and height is view_lines * repeat_times.

## Notes:

910 for NTSC, 1135 for PAL in the `disp_columns` variable block

526 for NTSC, 626 for PAL in the `disp_lines` variable block

****The output flie for PAL will be 1136 pixels wide****

for the purposes of this flowgraph, the "sample_rate" doesn't really do anything but determine how much compute resources are used. 


## Examples:

NTSC showing line 0 thru 44 repeated 20 times:

![pic1](https://raw.githubusercontent.com/tandersn/GNRC-Flowgraphs/main/z_images/VITS_0_THRU_44_x20.png)

NTSC showing line 25 thru 26 repeated 300 times:

![pic1](https://raw.githubusercontent.com/tandersn/GNRC-Flowgraphs/main/z_images/VITS_25_THRU_26_x300.png)

