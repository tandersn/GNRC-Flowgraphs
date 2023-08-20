# GNRC-Flowgraphs
A repository for me to store my GNRC flowgraphs.

## MUSE
`Complexity Level: High`

Designed to FM demodulate an RF captured MUSE signal. The baseband signal has been succesfully decoded by others. Special hardware is required to capture this signal, I have used a 54mhz modified cx23881 card (so far, only cx23881 is capable of going this high, but cx25800 is untested) in conjunction with a ~25mhz low pass filter from mini-circuits. Adjustment of graph variable values required.

## GNRC Tutorial
`Complexity Level: Begginer to intermediate`

An attempt at making material to help familiarize people with how to use GNRC and explain fundimental concepts. This material is intentially geared towards the vhs-decode and ld-decode projects.

I would consider this an incomplete project.

## LD FM Dmod
`Complexity Level: High`

Designed to FM demodulate an RF captured Laserdisc signal. Video only (no audio or EFM). Useful for troubleshooting and illustrating what the signal looks like in an intermediate form (after demodulation, but before time base correction). Adjustment of graph variable values required.

## Low Overhead RTL-SDR hifi 
`Complexity Level: Beginner`

For systems short on resources (middle aged laptpo), these flowgraphs can substitute for the compute intensive flowgraphs for capturing hifi with an RTL-SDR dongle. There are 2 sets. The first is a single graph that captures, and then integer resamples to 8.192msps (must use -f 8.192 with hifi-decode) instead of the compute intensive fractional resampler. It also does not provide any real-time decoding of the hifi.  

For even more resource strained computers, the second option is a set of 2 graphs, one that simply captures and saves to a tmp file, and then a second that converts that file to one hifi decode can use, after capture is complete.  

## TBC Show VITS
`Complexity Level: Intermediate`

Can be used to expand and show the VITS lines of an ld-decoded laserdisc capture. You must be able to adjust the variables in the graph to extract the information you wish to see. It is useful mainly for quality assessment of RF captures. 

## TBC via fl2k
`Complexity Level: Intermediate to High`

Use to convert a TBC file to a format that can be output by the FL2K dongle for external decoding of signal by conventional composite devices. It removes the extra lines and can adjust the levels. Editing variable block values is required, as well as assessing signal levels and conformancy. Adjustment of graph variable values required.

## Test CXADC
`Complexity Level: Beginner`

Use to assess whether /dev/cxadc0 is working and configured properly. It is mainly a type conversion and then displaying the results. Can be used instead of ffplay to verify setup, adjust DC offset (center_offset), and amplitude. 

## U16 conversions
`Complexity Level: Intermediate`

GNRC does not support the u16 (unsigned 16 bit integer) data type natively. This is the data type used by the .TBC files and the 16 bit sampling mode of the CX card. This graph details how to read in, and write out, u16 files with GNRC. Mainly just a reference for myself. 

## VHS FM Demodulation
`Complexity Level: High`

Use to FM demodulate a VHS RF capture. Luma only. Useful in diagnosis and comparrison. It will show you the complete luma signal from a VHS capture. Adjustment of graph variable values required. Color not supported. 

## VHS Resample
`Complexity Level: Beginner to Intermediate`

VHS captures generally are made with more bandwidth than needed for storage. This graph can be used to "down-sample" high msps captures to a lower rate.

NOTE: The filter on the cx card is not very strong, and capturing at a lower rate initially can cause aliasing (signal degredation). I've seen aliasing even when capturing NTSC VHS at 17.8msps.  It is recommended to capture at crystal rate and then down-sample to avoid this. 

## Z Images

Just where i stored the images for the other READMEs and wiki. 
wiki https://github.com/tandersn/GNRC-Flowgraphs/wiki
