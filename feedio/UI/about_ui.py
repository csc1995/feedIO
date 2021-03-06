# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Sun Jul  3 22:10:14 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.setWindowModality(QtCore.Qt.NonModal)
        About.resize(454, 410)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        About.setFont(font)
        About.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/feedIO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About.setWindowIcon(icon)
        self.lblUrl = QtGui.QLabel(About)
        self.lblUrl.setGeometry(QtCore.QRect(144, 325, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.lblUrl.setFont(font)
        self.lblUrl.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lblUrl.setFrameShape(QtGui.QFrame.NoFrame)
        self.lblUrl.setTextFormat(QtCore.Qt.RichText)
        self.lblUrl.setScaledContents(True)
        self.lblUrl.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUrl.setOpenExternalLinks(False)
        self.lblUrl.setObjectName("lblUrl")
        self.lblVersion = QtGui.QLabel(About)
        self.lblVersion.setGeometry(QtCore.QRect(160, 163, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(19)
        font.setWeight(75)
        font.setBold(True)
        self.lblVersion.setFont(font)
        self.lblVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblVersion.setObjectName("lblVersion")
        self.lblAbout = QtGui.QLabel(About)
        self.lblAbout.setGeometry(QtCore.QRect(-9, 201, 471, 91))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.lblAbout.setFont(font)
        self.lblAbout.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAbout.setWordWrap(True)
        self.lblAbout.setObjectName("lblAbout")
        self.lblCopyright = QtGui.QLabel(About)
        self.lblCopyright.setGeometry(QtCore.QRect(157, 292, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(7)
        self.lblCopyright.setFont(font)
        self.lblCopyright.setLineWidth(2)
        self.lblCopyright.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCopyright.setObjectName("lblCopyright")
        self.image = QtGui.QLabel(About)
        self.image.setGeometry(QtCore.QRect(-19, 0, 481, 171))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap(":/images/about.png"))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.btnCredits = QtGui.QPushButton(About)
        self.btnCredits.setGeometry(QtCore.QRect(21, 363, 85, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCredits.sizePolicy().hasHeightForWidth())
        self.btnCredits.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.btnCredits.setFont(font)
        self.btnCredits.setObjectName("btnCredits")
        self.btnLicense = QtGui.QPushButton(About)
        self.btnLicense.setGeometry(QtCore.QRect(141, 363, 85, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLicense.sizePolicy().hasHeightForWidth())
        self.btnLicense.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.btnLicense.setFont(font)
        self.btnLicense.setObjectName("btnLicense")
        self.btnClose = QtGui.QPushButton(About)
        self.btnClose.setGeometry(QtCore.QRect(325, 363, 85, 27))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtGui.QApplication.translate("About", "About feedIO", None, QtGui.QApplication.UnicodeUTF8))
        self.lblUrl.setText(QtGui.QApplication.translate("About", "http://www.feedio.org", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVersion.setText(QtGui.QApplication.translate("About", "feedIO", None, QtGui.QApplication.UnicodeUTF8))
        self.lblAbout.setText(QtGui.QApplication.translate("About", "feedIO is a feed aggregator that tracks the user\'s reading tastes and prioritizes the content from future feed updates according to the recorded user preferences.", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCopyright.setText(QtGui.QApplication.translate("About", "Copyright © 2011 SLIIT", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCredits.setText(QtGui.QApplication.translate("About", "C&redits", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLicense.setText(QtGui.QApplication.translate("About", "&License", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClose.setText(QtGui.QApplication.translate("About", "&Close", None, QtGui.QApplication.UnicodeUTF8))

import feedIOicons_rc
