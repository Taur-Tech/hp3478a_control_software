# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainWindow
###########################################################################

class MainWindow ( wx.Frame ):

	def __init__( self, parent, hp_instr ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"HP3478A GPIB Control Software", pos = wx.DefaultPosition, size = wx.Size( 766,575 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar = wx.MenuBar( 0 )
		self.m_filemenu = wx.Menu()
		self.m_export = wx.MenuItem( self.m_filemenu, wx.ID_ANY, u"Export", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_filemenu.AppendItem( self.m_export )

		self.m_filemenu.AppendSeparator()

		self.m_exit = wx.MenuItem( self.m_filemenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_filemenu.AppendItem( self.m_exit )

		self.m_menubar.Append( self.m_filemenu, u"File" )

		self.m_helpmenu = wx.Menu()
		self.m_about = wx.MenuItem( self.m_helpmenu, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_helpmenu.AppendItem( self.m_about )

		self.m_help = wx.MenuItem( self.m_helpmenu, wx.ID_ANY, u"Help", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_helpmenu.AppendItem( self.m_help )

		self.m_menubar.Append( self.m_helpmenu, u"Help" )

		self.SetMenuBar( self.m_menubar )

		gbSizerMain = wx.GridBagSizer( 0, 0 )
		gbSizerMain.SetFlexibleDirection( wx.BOTH )
		gbSizerMain.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_instr_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerInstr = wx.BoxSizer( wx.VERTICAL )

		self.m_measure_select = wx.Panel( self.m_instr_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizerMeasSelect = wx.GridBagSizer( 0, 0 )
		gbSizerMeasSelect.SetFlexibleDirection( wx.BOTH )
		gbSizerMeasSelect.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_meas_label = wx.StaticText( self.m_measure_select, wx.ID_ANY, u"Measurement", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_meas_label.Wrap( -1 )
		gbSizerMeasSelect.Add( self.m_meas_label, wx.GBPosition( 0, 0 ), wx.GBSpan( 3, 1 ), wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_radioVoltage = wx.RadioButton( self.m_measure_select, wx.ID_ANY, u"Voltage", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizerMeasSelect.Add( self.m_radioVoltage, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_radioCurrent = wx.RadioButton( self.m_measure_select, wx.ID_ANY, u"Current", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizerMeasSelect.Add( self.m_radioCurrent, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_radioResistance = wx.RadioButton( self.m_measure_select, wx.ID_ANY, u"Resistance", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizerMeasSelect.Add( self.m_radioResistance, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.m_measure_select.SetSizer( gbSizerMeasSelect )
		self.m_measure_select.Layout()
		gbSizerMeasSelect.Fit( self.m_measure_select )
		bSizerInstr.Add( self.m_measure_select, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self.m_instr_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizerInstr.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_scaling = wx.Panel( self.m_instr_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_scale_label = wx.StaticText( self.m_scaling, wx.ID_ANY, u"Scaling Formula, f(x) =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_scale_label.Wrap( -1 )
		bSizer2.Add( self.m_scale_label, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_scaling, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_scale_panel = wx.Panel( self.m_scaling, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizerScalePanel = wx.BoxSizer( wx.HORIZONTAL )

		self.m_btn_scale_clear = wx.Button( self.m_scale_panel, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerScalePanel.Add( self.m_btn_scale_clear, 0, wx.ALIGN_LEFT|wx.ALL, 5 )

		self.m_btn_scale_apply = wx.Button( self.m_scale_panel, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizerScalePanel.Add( self.m_btn_scale_apply, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		self.m_scale_panel.SetSizer( bSizerScalePanel )
		self.m_scale_panel.Layout()
		bSizerScalePanel.Fit( self.m_scale_panel )
		bSizer2.Add( self.m_scale_panel, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_scaling.SetSizer( bSizer2 )
		self.m_scaling.Layout()
		bSizer2.Fit( self.m_scaling )
		bSizerInstr.Add( self.m_scaling, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticline2 = wx.StaticLine( self.m_instr_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizerInstr.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_command = wx.Panel( self.m_instr_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizerCommand = wx.GridBagSizer( 0, 0 )
		gbSizerCommand.SetFlexibleDirection( wx.BOTH )
		gbSizerCommand.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self.m_command, wx.ID_ANY, u"Interval [s]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gbSizerCommand.Add( self.m_staticText3, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_interval = wx.TextCtrl( self.m_command, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizerCommand.Add( self.m_interval, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_btn_go_single = wx.Button( self.m_command, wx.ID_ANY, u"Single", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btn_go_single.SetMinSize( wx.Size( 100,100 ) )

		gbSizerCommand.Add( self.m_btn_go_single, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_btn_go_run = wx.Button( self.m_command, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btn_go_run.SetMinSize( wx.Size( 100,100 ) )

		gbSizerCommand.Add( self.m_btn_go_run, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.m_command.SetSizer( gbSizerCommand )
		self.m_command.Layout()
		gbSizerCommand.Fit( self.m_command )
		bSizerInstr.Add( self.m_command, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_instr_panel.SetSizer( bSizerInstr )
		self.m_instr_panel.Layout()
		bSizerInstr.Fit( self.m_instr_panel )
		gbSizerMain.Add( self.m_instr_panel, wx.GBPosition( 0, 0 ), wx.GBSpan( 2, 1 ), wx.EXPAND |wx.ALL, 5 )

		self.m_measure_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.DOUBLE_BORDER|wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )
		self.m_measure_panel.SetMinSize( wx.Size( 500,-1 ) )

		gbSizerMeas = wx.GridBagSizer( 0, 0 )
		gbSizerMeas.SetFlexibleDirection( wx.BOTH )
		gbSizerMeas.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gbSizerMeas.SetMinSize( wx.Size( 500,-1 ) )
		self.m_meas_raw = wx.StaticText( self.m_measure_panel, wx.ID_ANY, u"0.00001", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_meas_raw.Wrap( -1 )
		self.m_meas_raw.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Courier" ) )
		self.m_meas_raw.SetMinSize( wx.Size( 400,-1 ) )

		gbSizerMeas.Add( self.m_meas_raw, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_meas_scaled = wx.StaticText( self.m_measure_panel, wx.ID_ANY, u"0.000001", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_meas_scaled.Wrap( -1 )
		self.m_meas_scaled.SetFont( wx.Font( 30, 70, 90, 90, False, "Courier" ) )
		self.m_meas_scaled.SetMinSize( wx.Size( 400,50 ) )

		gbSizerMeas.Add( self.m_meas_scaled, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_unit = wx.StaticText( self.m_measure_panel, wx.ID_ANY, u"mV", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_unit.Wrap( -1 )
		self.m_unit.SetFont( wx.Font( 30, 76, 90, 91, False, "Courier" ) )

		gbSizerMeas.Add( self.m_unit, wx.GBPosition( 0, 1 ), wx.GBSpan( 2, 1 ), wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self.m_meas_gauge = wx.Gauge( self.m_measure_panel, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_meas_gauge.SetValue( 0 )
		self.m_meas_gauge.SetMinSize( wx.Size( 500,10 ) )

		gbSizerMeas.Add( self.m_meas_gauge, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )


		self.m_measure_panel.SetSizer( gbSizerMeas )
		self.m_measure_panel.Layout()
		gbSizerMeas.Fit( self.m_measure_panel )
		gbSizerMain.Add( self.m_measure_panel, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_graph_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.DOUBLE_BORDER|wx.TAB_TRAVERSAL )
		gbSizerMain.Add( self.m_graph_panel, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( gbSizerMain )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_radioVoltage.Bind( wx.EVT_RADIOBUTTON, self.selectVoltage )
		self.m_radioCurrent.Bind( wx.EVT_RADIOBUTTON, self.selectCurrent )
		self.m_radioResistance.Bind( wx.EVT_RADIOBUTTON, self.selectResistance )
		self.m_btn_scale_clear.Bind( wx.EVT_BUTTON, self.scalingClear )
		self.m_btn_scale_apply.Bind( wx.EVT_BUTTON, self.scalingApply )
		self.m_btn_go_single.Bind( wx.EVT_BUTTON, self.goSingle )
		self.m_btn_go_run.Bind( wx.EVT_BUTTON, self.goRun )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def selectVoltage( self, event ):
		event.Skip()

	def selectCurrent( self, event ):
		event.Skip()

	def selectResistance( self, event ):
		event.Skip()

	def scalingClear( self, event ):
		event.Skip()

	def scalingApply( self, event ):
		event.Skip()

	def goSingle( self, event ):
		event.Skip()

	def goRun( self, event ):
		event.Skip()
