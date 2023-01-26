# create_LD_FM

These graphs can be used to create the video RF FM signal that is similar to a 
Laserdisc and can be decoded with ld-decode.  The sources for this graph are 
created with ld-chroma-encoder and a suitable input file. HackTV could probably
also work, with some alterations. 

2 Version:
- cvbs.tbc version uses single input .tbc file, like laserdisc.  
- y.tbc and c.tbc version uses separate Luma and Chroma tbc files, like VHS style.

Initially it seemed the Y/C version worked better, but i think it just revealed the 
flaws better, and when i went back and updated the CVBS.tbc version parameters, it now
works well too. 


CVBS ffmpeg + ld-chroma encoder example:
`ffmpeg -i thx.avi -an -vf "scale=758:480,pad=758:486:0:3" -vcodec rawvideo -pix_fmt yuv444p16 -f rawvideo - | ld-chroma-encoder -p yuv -f NTSC - PADiceagethxCVBS.tbc`

Y/C ffmpeg + ld-chroma encoder example:
`ffmpeg -i thx.avi -an -vf "scale=758:480,pad=758:486:0:3" -vcodec rawvideo -pix_fmt yuv444p16 -f rawvideo - | ld-chroma-encoder -p yuv -f NTSC - PADiceagethx.tbc PADiceagethx_chroma.tbc`


The source in the examples are DVD (DVD is 480 verticle, so just pad 3 top and bottom to 
get 486 needed by encoder), but other video formats would work too. 1080i would be 
problematic, so yo would want to deinterlace first (due to scaling interlaced content=bad).

This graph is highly experimental and just for fun.  

After running the graph, you can decode the file like it was an LD RF capture: 

`ld-decode ldFM_YC_version.s16 out/ldFM_YC_version.s16 -f 40 --daa --noEFM`


Currently NTSC ONLY
