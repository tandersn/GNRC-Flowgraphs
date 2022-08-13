# VHS_FM_DMOD

DISCLAIMER:  Color is not yet supported.

vhs_fm_dmod.grc is a simplified version that can be used to see the VHS RF signal in real time from /dev/cxadc0, but can also read a .wav file.

vhs_fm_dmod_V3_AGC.grc is a more complex graph, which is used to generate an output file for FL2K or my `alignsyncs` script. 

These GNRC flowgraphs takes in an RF capture file from in .WAV or .FLAC formats (or directly from /dev/cxadc0 for simplified graph) and FM demodulates them. The graph will display a rough image of the vidoe as well.  

## Steps to use V3_AGC:

1. You'll need gnu radio companion packages installed and all dependencies

2. open the flowgraph, edit the following blocks:

   a. path field of 'file source block'
   b. path field of 'file sink block' 
   c. source_sample_rate (this is the capture sample rate of source file. DO NOT change the variable samp_rate)

3. run the graph 

4. You need to use the sliders to adjust the GAIN and OFFSET to create a "clamped" signal:
![pic1](https://raw.githubusercontent.com/tandersn/GNRC-Flowgraphs/main/z_images/adjust_gain_and_offset2.PNG)

5. Once you've achieved the best possible adjustment, annotate the values (screen shot, write down, etc. etc.)

6. stop the graph, and update `OFFSET Default Value` and `GAIN Default value` to the numbers from step 5

7. rerun the graph

##NOTES
1. for some captures, the FM Deemphasis parameter needs to be adjusted
2. for some captures, the sample rate you think it is, might be a little off, adjust it until the HSYNC in the image is as vertical as you can get it 
3. for some reason, the graph just stops after some amount of time
4. this is for testing, research, and development, please don't assume it is a finished product
5. there is most likely some things wrong



you can use something like:`ffplay -f rawvideo -pix_fmt gray8 -video_size 2542x525 -i /tmp/outfile.u8` to play the file (it will look pretty much like it does in the graph display)


