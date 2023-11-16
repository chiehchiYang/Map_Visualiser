# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'label.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1871, 1055)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_img_shape = QtWidgets.QLabel(self.centralwidget)
        self.label_img_shape.setGeometry(QtCore.QRect(1470, 970, 361, 41))
        self.label_img_shape.setObjectName("label_img_shape")
        self.label_file_name = QtWidgets.QLabel(self.centralwidget)
        self.label_file_name.setGeometry(QtCore.QRect(40, 910, 941, 31))
        self.label_file_name.setObjectName("label_file_name")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1461, 981))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        

        self.label_img = QtWidgets.QLabel()
        self.label_img.setGeometry(QtCore.QRect(0, 0, 1087, 797))
        self.label_img.setObjectName("label_img")
        self.scrollArea.setWidget(self.label_img)
        self.verticalLayout.addWidget(self.scrollArea) 
        
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, ccccccccccc))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.label_img = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.label_img.setGeometry(QtCore.QRect(0, 0, 981, 791))
        # self.label_img.setObjectName("label_img")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # self.verticalLayout.addWidget(self.scrollArea)
        
        
        
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1480, 720, 331, 66))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_real_pos = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_real_pos.setObjectName("label_real_pos")
        self.verticalLayout_2.addWidget(self.label_real_pos)
        self.label_click_pos = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_click_pos.setObjectName("label_click_pos")
        self.verticalLayout_2.addWidget(self.label_click_pos)
        self.label_yaw = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_yaw.setObjectName("label_yaw")
        self.verticalLayout_2.addWidget(self.label_yaw)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(1470, 560, 351, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_edit_mode = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_edit_mode.setObjectName("pushButton_edit_mode")
        self.gridLayout.addWidget(self.pushButton_edit_mode, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pushButton_show_results = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_show_results.setObjectName("pushButton_show_results")
        self.gridLayout.addWidget(self.pushButton_show_results, 0, 1, 1, 1)
        self.lineEdit_tag = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_tag.setObjectName("lineEdit_tag")
        self.gridLayout.addWidget(self.lineEdit_tag, 2, 1, 1, 1)
        self.pushButton_save_region = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_save_region.setObjectName("pushButton_save_region")
        self.gridLayout.addWidget(self.pushButton_save_region, 3, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(1470, 0, 341, 141))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.town_comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.town_comboBox.setObjectName("town_comboBox")
        self.horizontalLayout_2.addWidget(self.town_comboBox)
        self.slider_zoom = QtWidgets.QSlider(self.frame_2)
        self.slider_zoom.setGeometry(QtCore.QRect(10, 50, 321, 22))
        self.slider_zoom.setProperty("value", 50)
        self.slider_zoom.setOrientation(QtCore.Qt.Horizontal)
        self.slider_zoom.setObjectName("slider_zoom")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 321, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_zoom_in = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_zoom_in.setObjectName("btn_zoom_in")
        self.horizontalLayout.addWidget(self.btn_zoom_in)
        self.btn_zoom_out = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_zoom_out.setObjectName("btn_zoom_out")
        self.horizontalLayout.addWidget(self.btn_zoom_out)
        self.label_ratio = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ratio.setObjectName("label_ratio")
        self.horizontalLayout.addWidget(self.label_ratio)
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(1470, 460, 111, 41))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(1590, 460, 221, 95))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_x = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_x)
        self.lineEdit_y = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_y.setObjectName("lineEdit_y")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_y)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pushButton_show_point = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton_show_point.setObjectName("pushButton_show_point")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_show_point)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(1480, 790, 331, 181))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_route_mode = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_route_mode.setObjectName("pushButton_route_mode")
        self.gridLayout_2.addWidget(self.pushButton_route_mode, 0, 0, 1, 1)
        self.pushButton_smooth_route = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_smooth_route.setObjectName("pushButton_smooth_route")
        self.gridLayout_2.addWidget(self.pushButton_smooth_route, 1, 0, 1, 1)
        self.pushButton_save_route = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_save_route.setObjectName("pushButton_save_route")
        self.gridLayout_2.addWidget(self.pushButton_save_route, 3, 0, 1, 1)
        self.pushButton_modify_point = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_modify_point.setObjectName("pushButton_modify_point")
        self.gridLayout_2.addWidget(self.pushButton_modify_point, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(1470, 130, 341, 321))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame_3)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 321, 306))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_save_obstacle_scenario = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_save_obstacle_scenario.setObjectName("pushButton_save_obstacle_scenario")
        self.gridLayout_3.addWidget(self.pushButton_save_obstacle_scenario, 5, 0, 1, 1)
        self.obstacle_type_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.obstacle_type_comboBox.setObjectName("obstacle_type_comboBox")
        self.gridLayout_3.addWidget(self.obstacle_type_comboBox, 2, 0, 1, 1)
        self.pushButton_add_obstacle = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_add_obstacle.setObjectName("pushButton_add_obstacle")
        self.gridLayout_3.addWidget(self.pushButton_add_obstacle, 3, 0, 1, 1)
        self.pushButton_create_scenario_mode = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_create_scenario_mode.setObjectName("pushButton_create_scenario_mode")
        self.gridLayout_3.addWidget(self.pushButton_create_scenario_mode, 0, 0, 1, 1)
        self.pushButton_remove_obstacle_scenario = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_remove_obstacle_scenario.setObjectName("pushButton_remove_obstacle_scenario")
        self.gridLayout_3.addWidget(self.pushButton_remove_obstacle_scenario, 10, 0, 1, 1)
        self.pushButton_add_detect_point = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_add_detect_point.setObjectName("pushButton_add_detect_point")
        self.gridLayout_3.addWidget(self.pushButton_add_detect_point, 4, 0, 1, 1)
        self.pushButton_clear_route = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_clear_route.setObjectName("pushButton_clear_route")
        self.gridLayout_3.addWidget(self.pushButton_clear_route, 7, 0, 1, 1)
        self.pushButton_show_all_obstacle_scenario = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_show_all_obstacle_scenario.setObjectName("pushButton_show_all_obstacle_scenario")
        self.gridLayout_3.addWidget(self.pushButton_show_all_obstacle_scenario, 8, 0, 1, 1)
        self.pushButton_select_scenario = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_select_scenario.setObjectName("pushButton_select_scenario")
        self.gridLayout_3.addWidget(self.pushButton_select_scenario, 9, 0, 1, 1)
        self.pushButton_add_route = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_add_route.setObjectName("pushButton_add_route")
        self.gridLayout_3.addWidget(self.pushButton_add_route, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1871, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_img_shape.setText(_translate("MainWindow", "Current image shape: (0,0), Origin image shape: (0,0)"))
        self.label_file_name.setText(_translate("MainWindow", "file name:"))
        self.label_img.setText(_translate("MainWindow", "label_img"))
        self.label_real_pos.setText(_translate("MainWindow", "Carla  Coordinate = ( x, y )"))
        self.label_click_pos.setText(_translate("MainWindow", "Clicked position = ( x, y )"))
        self.label_yaw.setText(_translate("MainWindow", "yaw = "))
        self.pushButton_edit_mode.setText(_translate("MainWindow", "Edit Mode"))
        self.label_2.setText(_translate("MainWindow", "TAG"))
        self.pushButton_show_results.setText(_translate("MainWindow", "Show Results"))
        self.pushButton_save_region.setText(_translate("MainWindow", "Save Region"))
        self.label.setText(_translate("MainWindow", "Town : "))
        self.btn_zoom_in.setText(_translate("MainWindow", "zoom in"))
        self.btn_zoom_out.setText(_translate("MainWindow", "zoom out"))
        self.label_ratio.setText(_translate("MainWindow", "ratio: 100%"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.label_3.setText(_translate("MainWindow", "X :      "))
        self.pushButton_show_point.setText(_translate("MainWindow", "Show Point"))
        self.label_5.setText(_translate("MainWindow", "Y :      "))
        self.pushButton_route_mode.setText(_translate("MainWindow", "Route Mode"))
        self.pushButton_smooth_route.setText(_translate("MainWindow", "Smooth Route"))
        self.pushButton_save_route.setText(_translate("MainWindow", "Save Route"))
        self.pushButton_modify_point.setText(_translate("MainWindow", "Modify Point"))
        self.pushButton_save_obstacle_scenario.setText(_translate("MainWindow", "3. Save Obstacle Scenario"))
        self.pushButton_add_obstacle.setText(_translate("MainWindow", " 1. Add Obstacle"))
        self.pushButton_create_scenario_mode.setText(_translate("MainWindow", "Create Scenario Mode"))
        self.pushButton_remove_obstacle_scenario.setText(_translate("MainWindow", "Remove this scenario"))
        self.pushButton_add_detect_point.setText(_translate("MainWindow", "2. Add Detected Point"))
        self.pushButton_clear_route.setText(_translate("MainWindow", "Clear Route"))
        self.pushButton_show_all_obstacle_scenario.setText(_translate("MainWindow", "Show All Scenario"))
        self.pushButton_select_scenario.setText(_translate("MainWindow", "Select the scenario"))
        self.pushButton_add_route.setText(_translate("MainWindow", "4. Add Route"))
