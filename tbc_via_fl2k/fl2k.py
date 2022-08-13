#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Y and UV TBC streams to s8
# GNU Radio version: 3.10.3.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import video_sdl



from gnuradio import qtgui

class fl2k(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Y and UV TBC streams to s8", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Y and UV TBC streams to s8")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "fl2k")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100e6
        self.lines_per_frame_discard = lines_per_frame_discard = 1
        self.lines_per_frame = lines_per_frame = 525
        self.line_length = line_length = 910

        ##################################################
        # Blocks
        ##################################################
        self.video_sdl_sink_0_0_0_0 = video_sdl.sink_uc(0, line_length, lines_per_frame, line_length, lines_per_frame)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_float*1, line_length)
        self.blocks_uchar_to_float_0_0_1 = blocks.uchar_to_float()
        self.blocks_uchar_to_float_0_0 = blocks.uchar_to_float()
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, line_length)
        self.blocks_stream_demux_0 = blocks.stream_demux(gr.sizeof_float*line_length, (lines_per_frame, lines_per_frame_discard))
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*line_length)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(256)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(256)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_source_0_0_0 = blocks.file_source(gr.sizeof_char*1, 'infile_chroma.tbc', False, 0, 0)
        self.blocks_file_source_0_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, 'infile.tbc', False, 0, 0)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_deinterleave_0_1 = blocks.deinterleave(gr.sizeof_float*1, 1)
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_float*1, 1)
        self.blocks_add_xx_2_0_1 = blocks.add_vff(1)
        self.blocks_add_xx_2_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_rail_ff_0 = analog.rail_ff((-127), 127)
        self.analog_const_source_x_5_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 127)
        self.analog_const_source_x_0_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 255)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0_1, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.analog_const_source_x_5_0, 0), (self.blocks_add_xx_2_0_0, 1))
        self.connect((self.analog_rail_ff_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_add_xx_2_0_1, 0))
        self.connect((self.blocks_add_xx_0_1, 0), (self.blocks_add_xx_2_0_1, 1))
        self.connect((self.blocks_add_xx_2_0_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_add_xx_2_0_1, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_deinterleave_0_1, 0), (self.blocks_add_xx_0_1, 0))
        self.connect((self.blocks_deinterleave_0_1, 1), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_divide_xx_0, 0), (self.analog_rail_ff_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_uchar_to_float_0_0, 0))
        self.connect((self.blocks_file_source_0_0_0, 0), (self.blocks_uchar_to_float_0_0_1, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.video_sdl_sink_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0_1, 1))
        self.connect((self.blocks_stream_demux_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_stream_demux_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_stream_demux_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_divide_xx_0, 0))
        self.connect((self.blocks_uchar_to_float_0_0, 0), (self.blocks_deinterleave_0, 0))
        self.connect((self.blocks_uchar_to_float_0_0_1, 0), (self.blocks_deinterleave_0_1, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_add_xx_2_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fl2k")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

    def get_lines_per_frame_discard(self):
        return self.lines_per_frame_discard

    def set_lines_per_frame_discard(self, lines_per_frame_discard):
        self.lines_per_frame_discard = lines_per_frame_discard

    def get_lines_per_frame(self):
        return self.lines_per_frame

    def set_lines_per_frame(self, lines_per_frame):
        self.lines_per_frame = lines_per_frame

    def get_line_length(self):
        return self.line_length

    def set_line_length(self, line_length):
        self.line_length = line_length




def main(top_block_cls=fl2k, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
