from PyQt5 import QtCore 
# from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog
# from PyQt5.QtCore import QThread, pyqtSignal

import time
import os


from UI import Ui_MainWindow
from img_controller import img_controller

# set: big change
# update: simple update for info, no calculation... (format: update_type_name)

# private function: We do NOT want user directly call this function 

class MainWindow_controller(QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        

        Town_list = ["Town01", "Town02", "Town03", "Town04", "Town05", "Town05_highway", "Town06", "Town07", "Town10HD", "hct"]
        
        for Town_name in Town_list:
            self.ui.town_comboBox.addItem(Town_name)
    

        self.file_path = f'./Maps/{self.ui.town_comboBox.currentText()}.png'
        self.img_controller = img_controller(img_path=self.file_path,
                                             ui=self.ui, Town=self.ui.town_comboBox.currentText())

        self.ui.btn_zoom_in.clicked.connect(self.img_controller.set_zoom_in)
        self.ui.btn_zoom_out.clicked.connect(self.img_controller.set_zoom_out)
        self.ui.slider_zoom.valueChanged.connect(self.getslidervalue)   
        self.ui.slider_zoom.setProperty("value", 20)
        self.getslidervalue()     
        
           
        self.ui.town_comboBox.currentIndexChanged.connect(self.init_new_picture)
        
        self.ui.pushButton_clear.clicked.connect(self.img_controller.clear)
        
        self.ui.pushButton_save_region.clicked.connect(self.img_controller.save_flag)


        self.ui.pushButton_show_results.clicked.connect(self.img_controller.show_results)
        
        self.ui.pushButton_show_point.clicked.connect(self.img_controller.show_point)
        
        
        self.ui.pushButton_route_mode.clicked.connect(self.change_to_route_mode)
        self.ui.pushButton_smooth_route.clicked.connect(self.img_controller.smooth_route)
        # def smooth_route(self):
        # 
        
        self.ui.pushButton_save_route.clicked.connect(self.img_controller.save_route_points)

    def change_to_route_mode(self):
        self.img_controller.route_mode = not self.img_controller.route_mode
        
        if self.img_controller.route_mode:
            self.ui.pushButton_route_mode.setStyleSheet("color: red;")
        else:
            self.ui.pushButton_route_mode.setStyleSheet("color: white;")
        


        

    def init_new_picture(self):
        self.ui.slider_zoom.setProperty("value", 20)
        self.file_path = f'./Maps/{self.ui.town_comboBox.currentText()}.png'
        self.img_controller.set_path(self.file_path, self.ui.town_comboBox.currentText())   
        self.getslidervalue()     


    def getslidervalue(self):        
        self.img_controller.set_slider_value(self.ui.slider_zoom.value()+1)
        # print(self.ui.slider_zoom.value()+1)



