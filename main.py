#
#
#
#
#
import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QCheckBox,QMessageBox,QFileDialog
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont,QRegExpValidator
from PyQt5.QtCore import Qt,QRegExp

import mainwin
import reverse

def PB_leftturnclicked():
    try:
        ls = hs.str2hex(ui.TE_source.toPlainText())
        for i in range(len(ls)):
            ls[i] = rev.reverse(ls[i],(ui.CB_bitreverse.checkState() == Qt.Checked),(ui.CB_bytereverse.checkState() == Qt.Checked))
        ui.TE_target.setPlainText(hs.hex2str(ls))  
    except:
        msg("warming","Please input hex")

def PB_rightturnclicked():
    try:
        ls = hs.str2hex(ui.TE_target.toPlainText())
        for i in range(len(ls)):
            ls[i] = rev.reverse(ls[i],(ui.CB_bitreverse.checkState() == Qt.Checked),(ui.CB_bytereverse.checkState() == Qt.Checked))
        ui.TE_source.setPlainText(hs.hex2str(ls))  
    except:
        msg("warming","Please input hex")

def msg(title,mess):  
    QMessageBox.information(w,title,  mess,  QMessageBox.Yes)

def PB_readsourcehandle():
    filename,filetype = QFileDialog.getOpenFileName(w,r"open file",os.getcwd(),r"Txt files(*.txt)")
    if filename!='':
        fp = open(filename,'r')
        ui.TE_source.setPlainText(fp.read())
        fp.close()

def PB_savetargethandle():
    filename,filetype = QFileDialog.getSaveFileName(w,r"save file",os.getcwd(),r"Txt files(*.txt)")
    if filename!='':
        fp = open(filename,'w')
        fp.write(ui.TE_target.toPlainText())
        fp.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainwin.Ui_MainWindow()
    w = QMainWindow()
    ui.setupUi(w)

    hs = reverse.hexstr()
    rev = reverse.reverse()

    ui.PB_leftturn.clicked.connect(PB_leftturnclicked)
    ui.PB_rightturn.clicked.connect(PB_rightturnclicked)
    ui.PB_readsource.clicked.connect(PB_readsourcehandle)
    ui.PB_savetarget.clicked.connect(PB_savetargethandle)

    w.show()

    sys.exit(app.exec_())