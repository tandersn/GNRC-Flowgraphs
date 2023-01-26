# create_LD_FM

The YC version is the one to use. 

This graph can be used to create the video RF FM signal that is similar to a Laserdisc and can be decoded with ld-decode.  The sources for this graph are created with ld-chroma-decoder and a suitable input file.


Example:

`ffmpeg -i thx.avi -an -vf "scale=758:480,pad=758:486:0:3" -vcodec rawvideo -pix_fmt yuv444p16 -f rawvideo - | ld-chroma-encoder -p yuv -f NTSC - PADiceagethxY.tbc PADiceagethxC.tbc`

The source here is DVD, but most any video can be used.

This graph is highly experimental and just for fun.  

After running the graph, you can decode the file like it was an LD RF capture: 

`ld-decode ldFM_YC_version.wav out/ldFM_YC_version.wav -f 40 --daa --noEFM`


Currently NTSC ONLY
