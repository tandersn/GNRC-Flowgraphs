low_overhead_rtlsdr_hifi.grc creates a 8.192msps integer resampled file to use with hifi-decode and the -f 8.192 parameter. This graph uses less compute power than the fractional resamling graph that creates 8msps even files. 

rtlsdr_to_file and rtlsdr_decode_file work together in a 2 step process to create an "extremely low overhead" capture. The first graph (rtlsdr_to_file) just pipes the samples directly from the SDR to a file for later processing. You then can use rtlsdr_decode_file_cap.grc to convert that file from complex.short to a hifi-decode compatible file.

The output of rtlsdr_to_file is the input for rtlsdr_decode_file
