# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feedIO.ui'
#
# Created: Tue Aug  9 22:54:49 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_feedIO(object):
    def setupUi(self, feedIO):
        feedIO.setObjectName("feedIO")
        feedIO.resize(952, 600)
        feedIO.setMinimumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/feedIO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        feedIO.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(feedIO)
        font = QtGui.QFont()
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 26))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_3.setBaseSize(QtCore.QSize(0, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboFeed = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboFeed.sizePolicy().hasHeightForWidth())
        self.comboFeed.setSizePolicy(sizePolicy)
        self.comboFeed.setMinimumSize(QtCore.QSize(250, 26))
        self.comboFeed.setMaximumSize(QtCore.QSize(16777215, 28))
        self.comboFeed.setBaseSize(QtCore.QSize(250, 36))
        self.comboFeed.setMaxVisibleItems(100)
        self.comboFeed.setObjectName("comboFeed")
        self.horizontalLayout_2.addWidget(self.comboFeed)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 26))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_4.setBaseSize(QtCore.QSize(0, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.comboTopic = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboTopic.sizePolicy().hasHeightForWidth())
        self.comboTopic.setSizePolicy(sizePolicy)
        self.comboTopic.setMinimumSize(QtCore.QSize(250, 26))
        self.comboTopic.setMaximumSize(QtCore.QSize(16777215, 28))
        self.comboTopic.setBaseSize(QtCore.QSize(250, 36))
        self.comboTopic.setMaxVisibleItems(100)
        self.comboTopic.setObjectName("comboTopic")
        self.horizontalLayout.addWidget(self.comboTopic)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnUp = QtGui.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnUp.sizePolicy().hasHeightForWidth())
        self.btnUp.setSizePolicy(sizePolicy)
        self.btnUp.setMaximumSize(QtCore.QSize(120, 36))
        self.btnUp.setBaseSize(QtCore.QSize(0, 26))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/upVote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnUp.setIcon(icon1)
        self.btnUp.setObjectName("btnUp")
        self.horizontalLayout_3.addWidget(self.btnUp)
        self.btnDown = QtGui.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDown.sizePolicy().hasHeightForWidth())
        self.btnDown.setSizePolicy(sizePolicy)
        self.btnDown.setMaximumSize(QtCore.QSize(120, 36))
        self.btnDown.setBaseSize(QtCore.QSize(0, 26))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/downVote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDown.setIcon(icon2)
        self.btnDown.setObjectName("btnDown")
        self.horizontalLayout_3.addWidget(self.btnDown)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.listUnread = QtGui.QTreeWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listUnread.sizePolicy().hasHeightForWidth())
        self.listUnread.setSizePolicy(sizePolicy)
        self.listUnread.setMinimumSize(QtCore.QSize(0, 0))
        self.listUnread.setBaseSize(QtCore.QSize(300, 500))
        self.listUnread.setIndentation(-10)
        self.listUnread.setAnimated(True)
        self.listUnread.setObjectName("listUnread")
        self.listOld = QtGui.QTreeWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listOld.sizePolicy().hasHeightForWidth())
        self.listOld.setSizePolicy(sizePolicy)
        self.listOld.setMinimumSize(QtCore.QSize(0, 0))
        self.listOld.setMaximumSize(QtCore.QSize(16777215, 200))
        self.listOld.setBaseSize(QtCore.QSize(300, 200))
        self.listOld.setIndentation(-10)
        self.listOld.setObjectName("listOld")
        self.viewArticle = QtWebKit.QWebView(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewArticle.sizePolicy().hasHeightForWidth())
        self.viewArticle.setSizePolicy(sizePolicy)
        self.viewArticle.setMinimumSize(QtCore.QSize(0, 0))
        self.viewArticle.setBaseSize(QtCore.QSize(0, 0))
        self.viewArticle.setUrl(QtCore.QUrl("http://www.feedio.org/"))
        self.viewArticle.setObjectName("viewArticle")
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        feedIO.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(feedIO)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 952, 21))
        font = QtGui.QFont()
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuArticle = QtGui.QMenu(self.menubar)
        self.menuArticle.setObjectName("menuArticle")
        self.menuFeedIO = QtGui.QMenu(self.menubar)
        self.menuFeedIO.setObjectName("menuFeedIO")
        self.menuTopics = QtGui.QMenu(self.menubar)
        self.menuTopics.setObjectName("menuTopics")
        feedIO.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(feedIO)
        font = QtGui.QFont()
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        feedIO.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(feedIO)
        font = QtGui.QFont()
        font.setItalic(False)
        self.toolBar.setFont(font)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        feedIO.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.LeftToolBarArea), self.toolBar)
        self.actionAddFeed = QtGui.QAction(feedIO)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/addFeed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddFeed.setIcon(icon3)
        self.actionAddFeed.setIconVisibleInMenu(True)
        self.actionAddFeed.setObjectName("actionAddFeed")
        self.actionRemoveFeed = QtGui.QAction(feedIO)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/removeFeed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveFeed.setIcon(icon4)
        self.actionRemoveFeed.setIconVisibleInMenu(True)
        self.actionRemoveFeed.setObjectName("actionRemoveFeed")
        self.actionHelp = QtGui.QAction(feedIO)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtGui.QAction(feedIO)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setIconVisibleInMenu(True)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPreferences = QtGui.QAction(feedIO)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/preferences.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreferences.setIcon(icon5)
        self.actionPreferences.setIconVisibleInMenu(True)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionExit = QtGui.QAction(feedIO)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setIconVisibleInMenu(True)
        self.actionExit.setObjectName("actionExit")
        self.actionUpVote = QtGui.QAction(feedIO)
        self.actionUpVote.setIcon(icon1)
        self.actionUpVote.setIconVisibleInMenu(True)
        self.actionUpVote.setObjectName("actionUpVote")
        self.actionDownVote = QtGui.QAction(feedIO)
        self.actionDownVote.setIcon(icon2)
        self.actionDownVote.setIconVisibleInMenu(True)
        self.actionDownVote.setObjectName("actionDownVote")
        self.actionRead = QtGui.QAction(feedIO)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/read.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRead.setIcon(icon7)
        self.actionRead.setIconVisibleInMenu(True)
        self.actionRead.setObjectName("actionRead")
        self.actionFetchFeed = QtGui.QAction(feedIO)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/fetchFeed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFetchFeed.setIcon(icon8)
        self.actionFetchFeed.setIconVisibleInMenu(True)
        self.actionFetchFeed.setObjectName("actionFetchFeed")
        self.actionFetchAllFeeds = QtGui.QAction(feedIO)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/fetchAll.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFetchAllFeeds.setIcon(icon9)
        self.actionFetchAllFeeds.setIconVisibleInMenu(True)
        self.actionFetchAllFeeds.setObjectName("actionFetchAllFeeds")
        self.actionVisitPage = QtGui.QAction(feedIO)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/visitPage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVisitPage.setIcon(icon10)
        self.actionVisitPage.setIconVisibleInMenu(True)
        self.actionVisitPage.setObjectName("actionVisitPage")
        self.actionManageFeeds = QtGui.QAction(feedIO)
        self.actionManageFeeds.setObjectName("actionManageFeeds")
        self.actionManageTopics = QtGui.QAction(feedIO)
        self.actionManageTopics.setObjectName("actionManageTopics")
        self.actionAddTopic = QtGui.QAction(feedIO)
        self.actionAddTopic.setObjectName("actionAddTopic")
        self.actionRemoveTopic = QtGui.QAction(feedIO)
        self.actionRemoveTopic.setObjectName("actionRemoveTopic")
        self.actionMinimizeToTray = QtGui.QAction(feedIO)
        self.actionMinimizeToTray.setObjectName("actionMinimizeToTray")
        self.actionUnread = QtGui.QAction(feedIO)
        self.actionUnread.setObjectName("actionUnread")
        self.actionReCalculateScores = QtGui.QAction(feedIO)
        self.actionReCalculateScores.setObjectName("actionReCalculateScores")
        self.actionPostToTwitter = QtGui.QAction(feedIO)
        self.actionPostToTwitter.setObjectName("actionPostToTwitter")
        self.actionReCalculateTopicScores = QtGui.QAction(feedIO)
        self.actionReCalculateTopicScores.setObjectName("actionReCalculateTopicScores")
        self.actionReadItLater = QtGui.QAction(feedIO)
        self.actionReadItLater.setObjectName("actionReadItLater")
        self.actionFavorite = QtGui.QAction(feedIO)
        self.actionFavorite.setObjectName("actionFavorite")
        self.menuFile.addAction(self.actionAddFeed)
        self.menuFile.addAction(self.actionRemoveFeed)
        self.menuFile.addAction(self.actionFetchFeed)
        self.menuFile.addAction(self.actionFetchAllFeeds)
        self.menuFile.addAction(self.actionManageFeeds)
        self.menuTools.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuArticle.addAction(self.actionUpVote)
        self.menuArticle.addAction(self.actionDownVote)
        self.menuArticle.addAction(self.actionRead)
        self.menuArticle.addAction(self.actionVisitPage)
        self.menuArticle.addSeparator()
        self.menuArticle.addAction(self.actionUnread)
        self.menuArticle.addAction(self.actionFavorite)
        self.menuArticle.addSeparator()
        self.menuArticle.addAction(self.actionPostToTwitter)
        self.menuArticle.addAction(self.actionReadItLater)
        self.menuFeedIO.addAction(self.actionMinimizeToTray)
        self.menuFeedIO.addAction(self.actionExit)
        self.menuTopics.addAction(self.actionAddTopic)
        self.menuTopics.addAction(self.actionRemoveTopic)
        self.menuTopics.addAction(self.actionManageTopics)
        self.menuTopics.addSeparator()
        self.menuTopics.addAction(self.actionReCalculateScores)
        self.menuTopics.addAction(self.actionReCalculateTopicScores)
        self.menubar.addAction(self.menuFeedIO.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTopics.menuAction())
        self.menubar.addAction(self.menuArticle.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionAddFeed)
        self.toolBar.addAction(self.actionRemoveFeed)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFetchFeed)
        self.toolBar.addAction(self.actionFetchAllFeeds)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPreferences)
        self.toolBar.addAction(self.actionVisitPage)
        self.toolBar.addAction(self.actionRead)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUpVote)
        self.toolBar.addAction(self.actionDownVote)

        self.retranslateUi(feedIO)
        QtCore.QMetaObject.connectSlotsByName(feedIO)

    def retranslateUi(self, feedIO):
        feedIO.setWindowTitle(QtGui.QApplication.translate("feedIO", "feedIO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("feedIO", "Feed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("feedIO", "Interest", None, QtGui.QApplication.UnicodeUTF8))
        self.btnUp.setText(QtGui.QApplication.translate("feedIO", "&UP", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDown.setText(QtGui.QApplication.translate("feedIO", "&DOWN", None, QtGui.QApplication.UnicodeUTF8))
        self.listUnread.headerItem().setText(0, QtGui.QApplication.translate("feedIO", "Important & Unread", None, QtGui.QApplication.UnicodeUTF8))
        self.listOld.headerItem().setText(0, QtGui.QApplication.translate("feedIO", "Everything else", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("feedIO", "&Feeds", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("feedIO", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("feedIO", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArticle.setTitle(QtGui.QApplication.translate("feedIO", "&Article", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFeedIO.setTitle(QtGui.QApplication.translate("feedIO", "feedI&O", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTopics.setTitle(QtGui.QApplication.translate("feedIO", "&Interests", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("feedIO", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddFeed.setText(QtGui.QApplication.translate("feedIO", "&Add Feed", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddFeed.setShortcut(QtGui.QApplication.translate("feedIO", "Ins", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveFeed.setText(QtGui.QApplication.translate("feedIO", "&Remove Feed", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("feedIO", "FeedIO Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("feedIO", "&About feedIO", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("feedIO", "&Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("feedIO", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("feedIO", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpVote.setText(QtGui.QApplication.translate("feedIO", "&Up vote ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpVote.setShortcut(QtGui.QApplication.translate("feedIO", "U", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownVote.setText(QtGui.QApplication.translate("feedIO", "&Down Vote", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDownVote.setShortcut(QtGui.QApplication.translate("feedIO", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRead.setText(QtGui.QApplication.translate("feedIO", "&Read", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFetchFeed.setText(QtGui.QApplication.translate("feedIO", "&Fetch Feed", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFetchAllFeeds.setText(QtGui.QApplication.translate("feedIO", "Fetch &All Feeds", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFetchAllFeeds.setShortcut(QtGui.QApplication.translate("feedIO", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVisitPage.setText(QtGui.QApplication.translate("feedIO", "&Visit Page", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVisitPage.setShortcut(QtGui.QApplication.translate("feedIO", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManageFeeds.setText(QtGui.QApplication.translate("feedIO", "&Manage Feeds", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManageTopics.setText(QtGui.QApplication.translate("feedIO", "&Manage Topics", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddTopic.setText(QtGui.QApplication.translate("feedIO", "&Add Topic", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemoveTopic.setText(QtGui.QApplication.translate("feedIO", "&Remove Topic", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMinimizeToTray.setText(QtGui.QApplication.translate("feedIO", "Mi&nimize to tray", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnread.setText(QtGui.QApplication.translate("feedIO", "&Mark as Unread", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUnread.setShortcut(QtGui.QApplication.translate("feedIO", "M", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReCalculateScores.setText(QtGui.QApplication.translate("feedIO", "Recalculate All &Scores", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPostToTwitter.setText(QtGui.QApplication.translate("feedIO", "Share on &Twitter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReCalculateTopicScores.setText(QtGui.QApplication.translate("feedIO", "Recalculate &Current Topic Scores", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReadItLater.setText(QtGui.QApplication.translate("feedIO", "Mark to Read It Later", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFavorite.setText(QtGui.QApplication.translate("feedIO", "Mark as &Favorite", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
import feedIOicons_rc
