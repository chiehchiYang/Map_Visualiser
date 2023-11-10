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
        
        
        # - traffic cone
        #     - static.prop.trafficcone01 
        #     - static.prop.trafficcone02
        # - street barrier 
        #     - static.prop.streetbarrier
        # - traffic warning
        #     - static.prop.trafficwarning
        # - illegal parking
        
        obstacle_type_list = ["trafficcone01", "constructioncone", "streetbarrier", "trafficwarning", "illegal_parking"]

        for obstacle_type in obstacle_type_list:
            self.ui.obstacle_type_comboBox.addItem(obstacle_type)
        

        Town_list = ["Town01", "Town02", "Town03", "Town04", "Town05", "Town05_highway", "Town06", "Town07", "Town10HD" ]
        
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

        self.ui.pushButton_save_route.clicked.connect(self.img_controller.save_route_points)
        
        self.ui.pushButton_create_scenario_mode.clicked.connect(self.change_to_create_obstacle_scenario_mode)
        self.ui.pushButton_add_obstacle.clicked.connect(self.img_controller.add_obstacle)
        self.ui.pushButton_add_detect_point.clicked.connect(self.img_controller.add_detect_point)
        self.ui.pushButton_save_obstacle_scenario.clicked.connect(self.img_controller.save_obstacle_scenario)
        self.ui.pushButton_show_all_obstacle_scenario.clicked.connect(self.img_controller.show_all_obstacle_scenario)
        
        self.ui.pushButton_clear_route.clicked.connect(self.img_controller.clear_route)
        
        
        
        self.ui.pushButton_select_scenario.clicked.connect(self.img_controller.select_scenario)
        self.ui.pushButton_remove_obstacle_scenario.clicked.connect(self.img_controller.remove_scenario)
        
        
        
         
        
        # save_obstacle_scenario
        

    def change_to_route_mode(self):
        self.img_controller.route_mode = not self.img_controller.route_mode
        if self.img_controller.route_mode:
            self.ui.pushButton_route_mode.setStyleSheet("color: red;")
        else:
            self.ui.pushButton_route_mode.setStyleSheet("color: white;")
            
    def change_to_create_obstacle_scenario_mode(self):
        
        if self.img_controller.obstacle_scenario_mode == False:
            
            self.img_controller.obstacle_scenario_mode = not self.img_controller.obstacle_scenario_mode
            if self.img_controller.obstacle_scenario_mode:
                self.ui.pushButton_create_scenario_mode.setStyleSheet("color: red;")
            else:
                self.ui.pushButton_create_scenario_mode.setStyleSheet("color: white;")
                



        

    def init_new_picture(self):
        self.ui.slider_zoom.setProperty("value", 20)
        self.file_path = f'./Maps/{self.ui.town_comboBox.currentText()}.png'
        self.img_controller.set_path(self.file_path, self.ui.town_comboBox.currentText())   
        self.getslidervalue()     


    def getslidervalue(self):        
        self.img_controller.set_slider_value(self.ui.slider_zoom.value()+1)
        # print(self.ui.slider_zoom.value()+1)



