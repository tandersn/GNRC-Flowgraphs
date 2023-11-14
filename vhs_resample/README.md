# Graphs to resample (and low pass filter) VHS captures to 16msps

NOTE:  16msps is ony enough for NTSC regular VHS.  For SVHS or PAL / SECAM you would need higher msps.  Most people are using sox to resample now, so these graphs haven't been updated for other formats. 

To use these graphs, you must put the source sample rate value in the corresponding block in the graph, along with INFILE and OUTFILE.

A few rounds of testing between Titan91 and I resulted in the creation of a flow graph to resample VHS captures (8 bit @ 40msps) to 8 bit @ 16msps with a low passfilter around 7.75mhz.

The versions of these graphs have been updated to work with any source file sample rate, and different graphs for signed 16 bit (raw scaled ddd output), usigned 8 bit (cx card 8 bit mode), and `any bit` .WAV or .FLAC file. 

Obviously, not every possible situation could be tested, so YMMV, but this is what we found worked well, and preserved quality, and allowed for best conservation of space (the output file is then flac compressed).

Our observations indicated that for CX card capturs, capturing at 8 bit crystal speed worked best, and then resampling after. This was with a modified card though. 


No promise of quality or financial gain is made with these graphs. Feedback would be nice though.


