# test_cxadc

This GNRC flowgraph can be used to test your CX card and show signal level, center offset, and verify you have a correct connection set up. The graph shows a readout of the signal and a Video display.  You can use the signal readout in conjuction with the cx parameters to adjust the amplitude (level) and DC offset (center_offset).

## Steps to use:

You'll need gnu radio companion packages installed and all dependencies: `sudo apt install gnuradio`

Open the flowgraph and look for the triangle "play" shaped button run the graph.


### Disconnected:
This is good to adjust the center_offset parameter. 

![pic1](https://raw.githubusercontent.com/tandersn/GNRC-Flowgraphs/main/z_images/disconnected.png)

### Active VHS signal:
Here, if you have the right vmux and good signal level, you should be able to make out the h_sync and v_sync pattern of the image. Often you can also see outlines of big objects in the scene.

![pic1](https://raw.githubusercontent.com/tandersn/GNRC-Flowgraphs/main/z_images/active.png)

