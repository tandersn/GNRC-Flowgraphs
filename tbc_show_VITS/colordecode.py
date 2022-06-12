#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Extract VITS line
# GNU Radio version: 3.10.2.0

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

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import video_sdl



from gnuradio import qtgui

class colordecode(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Extract VITS line", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Extract VITS line")
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

        self.settings = Qt.QSettings("GNU Radio", "colordecode")

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
        self.disp_lines = disp_lines = 526
        self.disp_columns = disp_columns = 910
        self.view_lines = view_lines = 44
        self.start_line = start_line = 0
        self.samp_rate = samp_rate = 14318181
        self.repeat_times = repeat_times = 20
        self.PAL_xtra = PAL_xtra = int(disp_columns)+int(disp_lines/600)

        ##################################################
        # Blocks
        ##################################################
        self.video_sdl_sink_0_1_0 = video_sdl.sink_s(29.97, PAL_xtra, int(view_lines*repeat_times), PAL_xtra, int(view_lines*repeat_times))
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            2048, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1.1, 1.1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.blocks_vector_to_stream_1 = blocks.vector_to_stream(gr.sizeof_float*1, PAL_xtra)
        self.blocks_vector_to_stream_0_1 = blocks.vector_to_stream(gr.sizeof_float*PAL_xtra, round(disp_lines/2))
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_float*PAL_xtra, round(disp_lines/2))
        self.blocks_uchar_to_float_0 = blocks.uchar_to_float()
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, int(PAL_xtra*disp_lines/2))
        self.blocks_stream_to_streams_0 = blocks.stream_to_streams(gr.sizeof_float*int(PAL_xtra*disp_lines/2), 2)
        self.blocks_stream_mux_1 = blocks.stream_mux(gr.sizeof_float*1, (disp_columns, int(PAL_xtra-disp_columns)))
        self.blocks_stream_mux_0_0 = blocks.stream_mux(gr.sizeof_float*PAL_xtra, (1, 1))
        self.blocks_stream_demux_0 = blocks.stream_demux(gr.sizeof_float*PAL_xtra, (start_line,view_lines, int( disp_lines-view_lines-start_line)))
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*PAL_xtra, repeat_times)
        self.blocks_null_sink_2_0 = blocks.null_sink(gr.sizeof_float*PAL_xtra)
        self.blocks_null_sink_2 = blocks.null_sink(gr.sizeof_float*PAL_xtra)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(127)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(256)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(126)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, '/laserdisc/captures/movies_and_demos/out/4300D_rfTap_100IOTopa657_13+_grn54c2_16x33.75_bi50t_dxvx2_fan_50k150ciCXlvladj_critSe7enC47.u16.tbc', True, 0, 0)
        self.blocks_file_source_0_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/tmp/outfile.u8', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_deinterleave_0 = blocks.deinterleave(gr.sizeof_float*1, 1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_1 = blocks.add_const_ff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_ff(1)
        self.analog_rail_ff_2 = analog.rail_ff(1, 254)
        self.analog_rail_ff_1 = analog.rail_ff(-1, 1)
        self.analog_const_source_x_2 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_1 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 32768)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.analog_const_source_x_1, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.analog_const_source_x_2, 0), (self.blocks_stream_mux_1, 1))
        self.connect((self.analog_rail_ff_1, 0), (self.blocks_stream_mux_1, 0))
        self.connect((self.analog_rail_ff_2, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_deinterleave_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_deinterleave_0, 1), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_uchar_to_float_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.video_sdl_sink_0_1_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.analog_rail_ff_2, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_vector_to_stream_1, 0))
        self.connect((self.blocks_stream_demux_0, 2), (self.blocks_null_sink_2, 0))
        self.connect((self.blocks_stream_demux_0, 0), (self.blocks_null_sink_2_0, 0))
        self.connect((self.blocks_stream_demux_0, 1), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_stream_mux_0_0, 0), (self.blocks_stream_demux_0, 0))
        self.connect((self.blocks_stream_mux_1, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_stream_to_streams_0, 1), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.blocks_stream_to_streams_0, 0), (self.blocks_vector_to_stream_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_stream_to_streams_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.analog_rail_ff_1, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_divide_xx_0, 0))
        self.connect((self.blocks_uchar_to_float_0, 0), (self.blocks_deinterleave_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.blocks_stream_mux_0_0, 1))
        self.connect((self.blocks_vector_to_stream_0_1, 0), (self.blocks_stream_mux_0_0, 0))
        self.connect((self.blocks_vector_to_stream_1, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_vector_to_stream_1, 0), (self.blocks_add_const_vxx_1, 0))
        self.connect((self.blocks_vector_to_stream_1, 0), (self.qtgui_time_sink_x_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "colordecode")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_disp_lines(self):
        return self.disp_lines

    def set_disp_lines(self, disp_lines):
        self.disp_lines = disp_lines
        self.set_PAL_xtra(int(self.disp_columns)+int(self.disp_lines/600))

    def get_disp_columns(self):
        return self.disp_columns

    def set_disp_columns(self, disp_columns):
        self.disp_columns = disp_columns
        self.set_PAL_xtra(int(self.disp_columns)+int(self.disp_lines/600))

    def get_view_lines(self):
        return self.view_lines

    def set_view_lines(self, view_lines):
        self.view_lines = view_lines

    def get_start_line(self):
        return self.start_line

    def set_start_line(self, start_line):
        self.start_line = start_line

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)

    def get_repeat_times(self):
        return self.repeat_times

    def set_repeat_times(self, repeat_times):
        self.repeat_times = repeat_times
        self.blocks_repeat_0.set_interpolation(self.repeat_times)

    def get_PAL_xtra(self):
        return self.PAL_xtra

    def set_PAL_xtra(self, PAL_xtra):
        self.PAL_xtra = PAL_xtra




def main(top_block_cls=colordecode, options=None):

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
