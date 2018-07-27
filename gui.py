#
# Copyright 2018 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.logger_window = QtWidgets.QTextEdit(self.centralwidget)
        self.logger_window.setObjectName("logger_window")
        self.gridLayout.addWidget(self.logger_window, 4, 1, 1, 2)
        self.commands = QtWidgets.QTabWidget(self.centralwidget)
        self.commands.setMinimumSize(QtCore.QSize(0, 484))
        self.commands.setObjectName("commands")
        self.newmod = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.newmod.setFont(font)
        self.newmod.setObjectName("newmod")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.newmod)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.newmod_options = QtWidgets.QGroupBox(self.newmod)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.newmod_options.setFont(font)
        self.newmod_options.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.newmod_options.setObjectName("newmod_options")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.newmod_options)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_newmod_modname = QtWidgets.QLabel(self.newmod_options)
        self.label_newmod_modname.setObjectName("label_newmod_modname")
        self.gridLayout_3.addWidget(self.label_newmod_modname, 0, 0, 1, 1)
        self.newmod_run = QtWidgets.QPushButton(self.newmod_options)
        self.newmod_run.setToolTip("")
        self.newmod_run.setDefault(False)
        self.newmod_run.setFlat(False)
        self.newmod_run.setObjectName("newmod_run")
        self.gridLayout_3.addWidget(self.newmod_run, 1, 0, 1, 1)
        self.newmod_modname = QtWidgets.QLineEdit(self.newmod_options)
        self.newmod_modname.setObjectName("newmod_modname")
        self.gridLayout_3.addWidget(self.newmod_modname, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.newmod_options, 0, 1, 1, 1)
        self.commands.addTab(self.newmod, "")
        self.add = QtWidgets.QWidget()
        self.add.setObjectName("add")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.add)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.add_candidates = QtWidgets.QGroupBox(self.add)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.add_candidates.setFont(font)
        self.add_candidates.setObjectName("add_candidates")
        self.gridLayout_5.addWidget(self.add_candidates, 0, 1, 1, 1)
        self.add_options = QtWidgets.QGroupBox(self.add)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.add_options.setFont(font)
        self.add_options.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.add_options.setObjectName("add_options")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.add_options)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.add_blockname = QtWidgets.QLineEdit(self.add_options)
        self.add_blockname.setObjectName("add_blockname")
        self.gridLayout_4.addWidget(self.add_blockname, 0, 2, 1, 1)
        self.add_run = QtWidgets.QPushButton(self.add_options)
        self.add_run.setToolTip("")
        self.add_run.setDefault(False)
        self.add_run.setFlat(False)
        self.add_run.setObjectName("add_run")
        self.gridLayout_4.addWidget(self.add_run, 8, 0, 1, 1)
        self.label_add_blocktype = QtWidgets.QLabel(self.add_options)
        self.label_add_blocktype.setObjectName("label_add_blocktype")
        self.gridLayout_4.addWidget(self.label_add_blocktype, 1, 0, 1, 1)
        self.label_add_blockname = QtWidgets.QLabel(self.add_options)
        self.label_add_blockname.setObjectName("label_add_blockname")
        self.gridLayout_4.addWidget(self.label_add_blockname, 0, 0, 1, 1)
        self.label_add_copyright = QtWidgets.QLabel(self.add_options)
        self.label_add_copyright.setObjectName("label_add_copyright")
        self.gridLayout_4.addWidget(self.label_add_copyright, 3, 0, 1, 1)
        self.add_blocktype = QtWidgets.QComboBox(self.add_options)
        self.add_blocktype.setObjectName("add_blocktype")
        self.add_blocktype.addItem("")
        self.add_blocktype.addItem("")
        self.add_blocktype.addItem("")
        self.add_blocktype.addItem("")
        self.add_blocktype.addItem("")
        self.add_blocktype.addItem("")
        self.add_blocktype.addItem("")
        self.add_blocktype.addItem("")
        self.add_blocktype.addItem("")
        self.gridLayout_4.addWidget(self.add_blocktype, 1, 2, 1, 1)
        self.label_add_arglist = QtWidgets.QLabel(self.add_options)
        self.label_add_arglist.setObjectName("label_add_arglist")
        self.gridLayout_4.addWidget(self.label_add_arglist, 4, 0, 1, 1)
        self.label_add_lang = QtWidgets.QLabel(self.add_options)
        self.label_add_lang.setObjectName("label_add_lang")
        self.gridLayout_4.addWidget(self.label_add_lang, 2, 0, 1, 1)
        self.add_copyright = QtWidgets.QLineEdit(self.add_options)
        self.add_copyright.setObjectName("add_copyright")
        self.gridLayout_4.addWidget(self.add_copyright, 3, 2, 1, 1)
        self.add_py_qa = QtWidgets.QCheckBox(self.add_options)
        self.add_py_qa.setObjectName("add_py_qa")
        self.gridLayout_4.addWidget(self.add_py_qa, 5, 2, 1, 1)
        self.add_lang = QtWidgets.QComboBox(self.add_options)
        self.add_lang.setObjectName("add_lang")
        self.add_lang.addItem("")
        self.add_lang.addItem("")
        self.gridLayout_4.addWidget(self.add_lang, 2, 2, 1, 1)
        self.add_arglist = QtWidgets.QLineEdit(self.add_options)
        self.add_arglist.setObjectName("add_arglist")
        self.gridLayout_4.addWidget(self.add_arglist, 4, 2, 1, 1)
        self.add_cpp_qa = QtWidgets.QCheckBox(self.add_options)
        self.add_cpp_qa.setObjectName("add_cpp_qa")
        self.gridLayout_4.addWidget(self.add_cpp_qa, 6, 2, 1, 1)
        self.label_qa = QtWidgets.QLabel(self.add_options)
        self.label_qa.setObjectName("label_qa")
        self.gridLayout_4.addWidget(self.label_qa, 5, 0, 1, 1)
        self.gridLayout_5.addWidget(self.add_options, 0, 0, 1, 1)
        self.commands.addTab(self.add, "")
        self.disable = QtWidgets.QWidget()
        self.disable.setObjectName("disable")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.disable)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.disable_options = QtWidgets.QGroupBox(self.disable)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.disable_options.setFont(font)
        self.disable_options.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.disable_options.setObjectName("disable_options")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.disable_options)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.disable_run = QtWidgets.QPushButton(self.disable_options)
        self.disable_run.setToolTip("")
        self.disable_run.setDefault(False)
        self.disable_run.setFlat(False)
        self.disable_run.setObjectName("disable_run")
        self.gridLayout_6.addWidget(self.disable_run, 2, 0, 1, 1)
        self.label_disable_blockname = QtWidgets.QLabel(self.disable_options)
        self.label_disable_blockname.setObjectName("label_disable_blockname")
        self.gridLayout_6.addWidget(self.label_disable_blockname, 0, 0, 1, 1)
        self.disable_blockname = QtWidgets.QLineEdit(self.disable_options)
        self.disable_blockname.setObjectName("disable_blockname")
        self.gridLayout_6.addWidget(self.disable_blockname, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.disable_options, 0, 0, 1, 1)
        self.disable_candidates = QtWidgets.QGroupBox(self.disable)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.disable_candidates.setFont(font)
        self.disable_candidates.setObjectName("disable_candidates")
        self.gridLayout_7.addWidget(self.disable_candidates, 0, 1, 1, 1)
        self.commands.addTab(self.disable, "")
        self.makeyaml = QtWidgets.QWidget()
        self.makeyaml.setObjectName("makeyaml")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.makeyaml)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.makeyaml_options = QtWidgets.QGroupBox(self.makeyaml)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.makeyaml_options.setFont(font)
        self.makeyaml_options.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.makeyaml_options.setObjectName("makeyaml_options")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.makeyaml_options)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.makeyaml_blockname = QtWidgets.QLineEdit(self.makeyaml_options)
        self.makeyaml_blockname.setObjectName("makeyaml_blockname")
        self.gridLayout_8.addWidget(self.makeyaml_blockname, 0, 2, 1, 1)
        self.label_makeyaml_blockname = QtWidgets.QLabel(self.makeyaml_options)
        self.label_makeyaml_blockname.setObjectName("label_makeyaml_blockname")
        self.gridLayout_8.addWidget(self.label_makeyaml_blockname, 0, 0, 1, 1)
        self.makeyaml_run = QtWidgets.QPushButton(self.makeyaml_options)
        self.makeyaml_run.setToolTip("")
        self.makeyaml_run.setDefault(False)
        self.makeyaml_run.setFlat(False)
        self.makeyaml_run.setObjectName("makeyaml_run")
        self.gridLayout_8.addWidget(self.makeyaml_run, 2, 0, 1, 1)
        self.gridLayout_9.addWidget(self.makeyaml_options, 0, 0, 1, 1)
        self.makeyaml_candidates = QtWidgets.QGroupBox(self.makeyaml)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.makeyaml_candidates.setFont(font)
        self.makeyaml_candidates.setObjectName("makeyaml_candidates")
        self.gridLayout_9.addWidget(self.makeyaml_candidates, 0, 1, 1, 1)
        self.commands.addTab(self.makeyaml, "")
        self.rename = QtWidgets.QWidget()
        self.rename.setObjectName("rename")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.rename)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.rename_options = QtWidgets.QGroupBox(self.rename)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rename_options.setFont(font)
        self.rename_options.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rename_options.setObjectName("rename_options")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.rename_options)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_rename_oldname = QtWidgets.QLabel(self.rename_options)
        self.label_rename_oldname.setObjectName("label_rename_oldname")
        self.gridLayout_10.addWidget(self.label_rename_oldname, 0, 0, 1, 1)
        self.rename_oldname = QtWidgets.QLineEdit(self.rename_options)
        self.rename_oldname.setObjectName("rename_oldname")
        self.gridLayout_10.addWidget(self.rename_oldname, 0, 2, 1, 1)
        self.rename_run = QtWidgets.QPushButton(self.rename_options)
        self.rename_run.setToolTip("")
        self.rename_run.setDefault(False)
        self.rename_run.setFlat(False)
        self.rename_run.setObjectName("rename_run")
        self.gridLayout_10.addWidget(self.rename_run, 3, 0, 1, 1)
        self.rename_newname = QtWidgets.QLineEdit(self.rename_options)
        self.rename_newname.setObjectName("rename_newname")
        self.gridLayout_10.addWidget(self.rename_newname, 1, 2, 1, 1)
        self.label_rename_newname = QtWidgets.QLabel(self.rename_options)
        self.label_rename_newname.setObjectName("label_rename_newname")
        self.gridLayout_10.addWidget(self.label_rename_newname, 1, 0, 1, 1)
        self.gridLayout_11.addWidget(self.rename_options, 0, 0, 1, 1)
        self.rename_candidates = QtWidgets.QGroupBox(self.rename)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rename_candidates.setFont(font)
        self.rename_candidates.setObjectName("rename_candidates")
        self.gridLayout_11.addWidget(self.rename_candidates, 0, 1, 1, 1)
        self.commands.addTab(self.rename, "")
        self.rm = QtWidgets.QWidget()
        self.rm.setObjectName("rm")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.rm)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.remove_options = QtWidgets.QGroupBox(self.rm)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.remove_options.setFont(font)
        self.remove_options.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.remove_options.setObjectName("remove_options")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.remove_options)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.remove_blockname = QtWidgets.QLineEdit(self.remove_options)
        self.remove_blockname.setObjectName("remove_blockname")
        self.gridLayout_12.addWidget(self.remove_blockname, 0, 2, 1, 1)
        self.label_remove_blockname = QtWidgets.QLabel(self.remove_options)
        self.label_remove_blockname.setObjectName("label_remove_blockname")
        self.gridLayout_12.addWidget(self.label_remove_blockname, 0, 0, 1, 1)
        self.remove_run = QtWidgets.QPushButton(self.remove_options)
        self.remove_run.setToolTip("")
        self.remove_run.setDefault(False)
        self.remove_run.setFlat(False)
        self.remove_run.setObjectName("remove_run")
        self.gridLayout_12.addWidget(self.remove_run, 2, 0, 1, 1)
        self.gridLayout_13.addWidget(self.remove_options, 0, 0, 1, 1)
        self.remove_candidates = QtWidgets.QGroupBox(self.rm)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.remove_candidates.setFont(font)
        self.remove_candidates.setObjectName("remove_candidates")
        self.gridLayout_13.addWidget(self.remove_candidates, 0, 1, 1, 1)
        self.commands.addTab(self.rm, "")
        self.update = QtWidgets.QWidget()
        self.update.setObjectName("update")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.update)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.update_candidates = QtWidgets.QGroupBox(self.update)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.update_candidates.setFont(font)
        self.update_candidates.setObjectName("update_candidates")
        self.gridLayout_17.addWidget(self.update_candidates, 0, 1, 1, 1)
        self.update_options = QtWidgets.QGroupBox(self.update)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.update_options.setFont(font)
        self.update_options.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.update_options.setObjectName("update_options")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.update_options)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_update_blockname = QtWidgets.QLabel(self.update_options)
        self.label_update_blockname.setObjectName("label_update_blockname")
        self.gridLayout_16.addWidget(self.label_update_blockname, 0, 0, 1, 1)
        self.update_run = QtWidgets.QPushButton(self.update_options)
        self.update_run.setToolTip("")
        self.update_run.setDefault(False)
        self.update_run.setFlat(False)
        self.update_run.setObjectName("update_run")
        self.gridLayout_16.addWidget(self.update_run, 3, 0, 1, 1)
        self.update_blockname = QtWidgets.QLineEdit(self.update_options)
        self.update_blockname.setObjectName("update_blockname")
        self.gridLayout_16.addWidget(self.update_blockname, 0, 2, 1, 1)
        self.update_all = QtWidgets.QCheckBox(self.update_options)
        self.update_all.setObjectName("update_all")
        self.gridLayout_16.addWidget(self.update_all, 1, 0, 1, 1)
        self.gridLayout_17.addWidget(self.update_options, 0, 0, 1, 1)
        self.commands.addTab(self.update, "")
        self.common_params = QtWidgets.QWidget()
        self.common_params.setObjectName("common_params")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.common_params)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.common_options = QtWidgets.QGroupBox(self.common_params)
        font = QtGui.QFont()
        font.setFamily("Carlito")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.common_options.setFont(font)
        self.common_options.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.common_options.setObjectName("common_options")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.common_options)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.directory = QtWidgets.QLineEdit(self.common_options)
        self.directory.setObjectName("directory")
        self.gridLayout_14.addWidget(self.directory, 0, 1, 1, 1)
        self.skip_swig = QtWidgets.QCheckBox(self.common_options)
        self.skip_swig.setObjectName("skip_swig")
        self.gridLayout_14.addWidget(self.skip_swig, 2, 1, 1, 1)
        self.label_directory = QtWidgets.QLabel(self.common_options)
        self.label_directory.setObjectName("label_directory")
        self.gridLayout_14.addWidget(self.label_directory, 0, 0, 1, 1)
        self.skip_lib = QtWidgets.QCheckBox(self.common_options)
        self.skip_lib.setObjectName("skip_lib")
        self.gridLayout_14.addWidget(self.skip_lib, 1, 1, 1, 1)
        self.label_skip_dir = QtWidgets.QLabel(self.common_options)
        self.label_skip_dir.setObjectName("label_skip_dir")
        self.gridLayout_14.addWidget(self.label_skip_dir, 1, 0, 1, 1)
        self.skip_python = QtWidgets.QCheckBox(self.common_options)
        self.skip_python.setObjectName("skip_python")
        self.gridLayout_14.addWidget(self.skip_python, 3, 1, 1, 1)
        self.skip_grc = QtWidgets.QCheckBox(self.common_options)
        self.skip_grc.setObjectName("skip_grc")
        self.gridLayout_14.addWidget(self.skip_grc, 4, 1, 1, 1)
        self.scm_mode = QtWidgets.QComboBox(self.common_options)
        self.scm_mode.setObjectName("scm_mode")
        self.scm_mode.addItem("")
        self.scm_mode.addItem("")
        self.scm_mode.addItem("")
        self.gridLayout_14.addWidget(self.scm_mode, 5, 1, 1, 1)
        self.label_scm_mode = QtWidgets.QLabel(self.common_options)
        self.label_scm_mode.setObjectName("label_scm_mode")
        self.gridLayout_14.addWidget(self.label_scm_mode, 5, 0, 1, 1)
        self.gridLayout_15.addWidget(self.common_options, 0, 0, 1, 1)
        self.commands.addTab(self.common_params, "")
        self.gridLayout.addWidget(self.commands, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.commands.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "gr-modtool"))
        self.newmod_options.setTitle(_translate("MainWindow", "Options"))
        self.label_newmod_modname.setText(_translate("MainWindow", "Module Name :"))
        self.newmod_run.setText(_translate("MainWindow", "run"))
        self.commands.setTabText(self.commands.indexOf(self.newmod), _translate("MainWindow", "newmod"))
        self.add_candidates.setTitle(_translate("MainWindow", "Candidates"))
        self.add_options.setTitle(_translate("MainWindow", "Options"))
        self.add_run.setText(_translate("MainWindow", "run"))
        self.label_add_blocktype.setText(_translate("MainWindow", "BlockType"))
        self.label_add_blockname.setText(_translate("MainWindow", "Blockname"))
        self.label_add_copyright.setText(_translate("MainWindow", "Copyright"))
        self.add_blocktype.setItemText(0, _translate("MainWindow", "general"))
        self.add_blocktype.setItemText(1, _translate("MainWindow", "sink"))
        self.add_blocktype.setItemText(2, _translate("MainWindow", "source"))
        self.add_blocktype.setItemText(3, _translate("MainWindow", "sync"))
        self.add_blocktype.setItemText(4, _translate("MainWindow", "decimator"))
        self.add_blocktype.setItemText(5, _translate("MainWindow", "interpolator"))
        self.add_blocktype.setItemText(6, _translate("MainWindow", "tagged_stream"))
        self.add_blocktype.setItemText(7, _translate("MainWindow", "hier"))
        self.add_blocktype.setItemText(8, _translate("MainWindow", "noblock"))
        self.label_add_arglist.setText(_translate("MainWindow", "Argument List"))
        self.label_add_lang.setText(_translate("MainWindow", "Language"))
        self.add_py_qa.setText(_translate("MainWindow", "add_python_qa"))
        self.add_lang.setItemText(0, _translate("MainWindow", "cpp"))
        self.add_lang.setItemText(1, _translate("MainWindow", "python"))
        self.add_cpp_qa.setText(_translate("MainWindow", "add_cpp_qa"))
        self.label_qa.setText(_translate("MainWindow", "QA"))
        self.commands.setTabText(self.commands.indexOf(self.add), _translate("MainWindow", "add"))
        self.disable_options.setTitle(_translate("MainWindow", "Options"))
        self.disable_run.setText(_translate("MainWindow", "run"))
        self.label_disable_blockname.setText(_translate("MainWindow", "Blockname"))
        self.disable_candidates.setTitle(_translate("MainWindow", "Candidates"))
        self.commands.setTabText(self.commands.indexOf(self.disable), _translate("MainWindow", "disable"))
        self.makeyaml_options.setTitle(_translate("MainWindow", "Options"))
        self.label_makeyaml_blockname.setText(_translate("MainWindow", "Blockname"))
        self.makeyaml_run.setText(_translate("MainWindow", "run"))
        self.makeyaml_candidates.setTitle(_translate("MainWindow", "Candidates"))
        self.commands.setTabText(self.commands.indexOf(self.makeyaml), _translate("MainWindow", "makeyaml"))
        self.rename_options.setTitle(_translate("MainWindow", "Options"))
        self.label_rename_oldname.setText(_translate("MainWindow", "Old Blockname"))
        self.rename_run.setText(_translate("MainWindow", "run"))
        self.label_rename_newname.setText(_translate("MainWindow", "New Blockname"))
        self.rename_candidates.setTitle(_translate("MainWindow", "Candidates"))
        self.commands.setTabText(self.commands.indexOf(self.rename), _translate("MainWindow", "rename"))
        self.remove_options.setTitle(_translate("MainWindow", "Options"))
        self.label_remove_blockname.setText(_translate("MainWindow", "Blockname"))
        self.remove_run.setText(_translate("MainWindow", "run"))
        self.remove_candidates.setTitle(_translate("MainWindow", "Candidates"))
        self.commands.setTabText(self.commands.indexOf(self.rm), _translate("MainWindow", "remove"))
        self.update_candidates.setTitle(_translate("MainWindow", "Candidates"))
        self.update_options.setTitle(_translate("MainWindow", "Options"))
        self.label_update_blockname.setText(_translate("MainWindow", "Blockname"))
        self.update_run.setText(_translate("MainWindow", "run"))
        self.update_all.setText(_translate("MainWindow", " Update All Blocks"))
        self.commands.setTabText(self.commands.indexOf(self.update), _translate("MainWindow", "update"))
        self.common_options.setTitle(_translate("MainWindow", "Options"))
        self.directory.setPlaceholderText(_translate("MainWindow", "directory for commands execution (defaults to current directory)"))
        self.skip_swig.setText(_translate("MainWindow", "skip-swig"))
        self.label_directory.setText(_translate("MainWindow", "Directory"))
        self.skip_lib.setText(_translate("MainWindow", "skip-lib"))
        self.label_skip_dir.setText(_translate("MainWindow", "Skip Directories"))
        self.skip_python.setText(_translate("MainWindow", "skip-python"))
        self.skip_grc.setText(_translate("MainWindow", "skip-grc"))
        self.scm_mode.setItemText(0, _translate("MainWindow", "yes"))
        self.scm_mode.setItemText(1, _translate("MainWindow", "no"))
        self.scm_mode.setItemText(2, _translate("MainWindow", "auto"))
        self.label_scm_mode.setText(_translate("MainWindow", "scm-mode"))
        self.commands.setTabText(self.commands.indexOf(self.common_params), _translate("MainWindow", "common"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
