from PyQt5 import QtCore 
from PyQt5.QtGui import QImage, QPixmap

from opencv_engine import opencv_engine
import ujson
import numpy as np
import os 

from six.moves import cPickle as pickle #for performance


class img_controller(object):
    def __init__(self, img_path, ui, Town):
        self.Town = Town
        with open("./Maps/MapBoundaries.json", 'r') as f:
            data = ujson.load(f)
            Town = self.Town
            min_x= data[Town]["min_x"]
            min_y= data[Town]["min_y"]
        self.min_point = np.array([min_x, min_y])
        
        self.img_path = img_path
        self.ui = ui
        self.ratio_value = 50
        self.read_file_and_init()
        
        
        # 
        self.point_counter = 0
        self.points = []
        
        self.edit_mode_flag = False
        self.show_result_flag = False
        
        self.edit_goals_mode = False
        
        
        self.goals_list = []
        self.current_color = ""
        
    def reverse_goals_flag(self):
        self.edit_goals_mode = not self.edit_goals_mode

    def read_file_and_init(self):
        self.origin_img = opencv_engine.read_image(self.img_path)
        self.origin_height, self.origin_width, self.origin_channel = self.origin_img.shape
        
        self.display_img = self.origin_img.copy()
        self.__update_text_file_path()
        self.ratio_value = 50 # re-init
        self.__update_img()
        
    def clear(self):
        self.display_img = self.origin_img.copy()
        self.__update_img()
        self.point_counter = 0
        self.points = []
        
    def set_path(self, img_path, Town):
        self.img_path = img_path
        self.read_file_and_init()
        self.Town = Town
        with open("./Maps/MapBoundaries.json", 'r') as f:
            data = ujson.load(f)
            Town = self.Town
            min_x= data[Town]["min_x"]
            min_y= data[Town]["min_y"]
        self.min_point = np.array([min_x, min_y])


    def __update_img_ratio(self):
        self.ratio_rate = pow(10, (self.ratio_value - 50)/50)
        qpixmap_height = self.origin_height * self.ratio_rate
        self.qpixmap = self.qpixmap.scaledToHeight(qpixmap_height)
        self.__update_text_ratio()
        self.__update_text_img_shape()

    def __update_img(self):       
        bytesPerline = 3 * self.origin_width
        qimg = QImage(self.display_img, self.origin_width, self.origin_height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.qpixmap = QPixmap.fromImage(qimg)
        self.__update_img_ratio()
        self.ui.label_img.setPixmap(self.qpixmap)
        self.ui.label_img.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.ui.label_img.mousePressEvent = self.set_clicked_position

    def __update_text_file_path(self):
        self.ui.label_file_name.setText(f"File path = {self.img_path}")

    def __update_text_ratio(self):
        self.ui.label_ratio.setText(f"{int(100*self.ratio_rate)} %")

    def __update_text_img_shape(self):
        current_text = f"Current img shape = ({self.qpixmap.width()}, {self.qpixmap.height()})"
        origin_text = f"Origin img shape = ({self.origin_width}, {self.origin_height})"
        self.ui.label_img_shape.setText(current_text+"\t"+origin_text)

    def __update_text_clicked_position(self, x, y):
        # give me qpixmap point
        self.ui.label_click_pos.setText(f"Clicked postion = ({x}, {y})")
        norm_x = x/self.qpixmap.width()
        norm_y = y/self.qpixmap.height()
        # print(f"(x, y) = ({x}, {y}), normalized (x, y) = ({norm_x}, {norm_y})")
        # self.ui.label_norm_pos.setText(f"Normalized postion = ({norm_x:.3f}, {norm_y:.3f})")
        self.ui.label_real_pos.setText(f"Carla Coordinate = ({int(norm_x*self.origin_width)}, {int(norm_y*self.origin_height)})")


    def set_zoom_in(self):
        self.ratio_value = min(100, self.ratio_value + 1)
        self.__update_img()

    def set_zoom_out(self):
        self.ratio_value = max(0, self.ratio_value - 1)
        self.__update_img()

    def set_slider_value(self, value):
        self.ratio_value = value
        self.__update_img()
        
    def save_goal(self):
        

        if len(self.goals_list) != 0:
            if os.path.exists(f'./Color2Goals/{self.ui.town_comboBox.currentText()}.pkl'):
                
                color_2_goals = self.load_dict(f'./Color2Goals/{self.ui.town_comboBox.currentText()}.pkl')
                # color_2_goals[tag_name] = self.pixel_to_carla(contours)
                
                color_2_goals[self.current_color] = self.goals_list

                
                self.save_dict(color_2_goals, f'./Color2Goals/{self.ui.town_comboBox.currentText()}.pkl')

            else:
                color_2_goals = {}
                
                color_2_goals[self.current_color] = self.goals_list

                self.save_dict(color_2_goals, f'./Color2Goals/{self.ui.town_comboBox.currentText()}.pkl')
        
            # empty goal list 
            self.goals_list = []
            self.current_color = ""
            
            self.clear()
                

    # event 
    def set_clicked_position(self, event):
        x = event.pos().x()
        y = event.pos().y()
        self.__update_text_clicked_position(x, y)
        norm_x = x/self.qpixmap.width()
        norm_y = y/self.qpixmap.height()
        # self.draw_point((norm_x, norm_y))
        # self.__update_text_point_roi((norm_x, norm_y))
        
        cv_image_x = norm_x*self.origin_width
        cv_image_y = norm_y*self.origin_height
        image_pos = np.array([int(cv_image_x), int(cv_image_y)])
        
        
        
        if self.edit_goals_mode:
            
            
            
            selected_x = image_pos[0]
            selected_y = image_pos[1]
            
            
            if event.button() == 1: # right clicked
                
                if self.current_color !=  "":
                    self.goals_list.append([selected_x, selected_y])
                    
                    print("add Goal: ", selected_x, selected_y)
                    
                    self.draw_point((norm_x, norm_y))
                    
                
                # select goal points                 
            elif event.button() == 2: # left clicked
                # color 
                
                print('B, G, R: ')
                B, G, R = self.origin_img[selected_y][selected_x]
                print(B, G, R)
                
                self.current_color = f"{B}_{G}_{R}"
                
                
                
            
            
        else:
            if event.button() == 1: # right clicked
                if self.point_counter != 4:
                    self.point_counter+=1
                    self.points.append(image_pos)
                    
                    self.draw_point((norm_x, norm_y))
                    if self.point_counter == 4:
                        self.points = self.order_points(np.array( self.points) )
                        # print(self.points)
            elif event.button() == 2: # left clicked
                
                if self.point_counter == 4:
                    
                    coor_list = []
                    for point in self.points:
                        # coor_list.append(self.carla_to_pixel( point ))
                        coor_list.append(( point ))
                    contours = np.array(coor_list)
                    self.draw_poly(self.carla_to_pixel(self.pixel_to_carla(contours)))
                
                
    
    
    def show_selected_color_area(self):
        if self.current_color != "":
            
            color = self.current_color.split("_")
            
            B = int(color[0])
            G = int(color[1])
            R = int(color[2])
            self.current_color = f"{B}_{G}_{R}"
            idx = np.where(np.any(self.origin_img != [B, G, R], axis=-1)) # any instead of all
            self.display_img[idx[0], idx[1], :] = [0, 0, 0]
            self.__update_img()
            
            
    def show_goals(self):
        # clear
        
        
        # show goals 
        self.clear()
        
        if os.path.exists(f'./Color2Goals/{self.ui.town_comboBox.currentText()}.pkl'):
            color2goals = self.load_dict(f'./Color2Goals/{self.ui.town_comboBox.currentText()}.pkl')
           
            colors = list(color2goals.keys())
            # draw on image with tag 
            for color in colors:
                print(color)
                # B G R
                
                goal_list = color2goals[color]
                for goal in goal_list:
 
                   
                    
                    self.display_img = opencv_engine.draw_point(self.display_img, (goal[0], goal[1]))
                
                
            self.__update_img()
                
                
                #contours = self.carla_to_pixel(tags[tag])
                # self.display_img = opencv_engine.draw_fillpoly_with_tag(self.display_img, contours, tag, color = (125, 255, 0))
            #self.__update_img()
            
            
            # color_2_goals = self.load_dict(f'./Color2Goals/{self.ui.town_comboBox.currentText()}.pkl')
            # # color_2_goals[tag_name] = self.pixel_to_carla(contours)
                
            # color_2_goals[self.current_color] = self.goals_list

            
            # self.save_dict(color_2_goals, f'./Color2Goals/{self.ui.town_comboBox.currentText()}.pkl')
            
        else:
            print("NO tag")
            
            
                
        
                
                


    # order points 
    def order_points(self, pts):
        

        # sort the points based on their x-coordinates
        xSorted = pts[np.argsort(pts[:, 0]), :]

        # grab the left-most and right-most points from the sorted
        # x-roodinate points
        leftMost = xSorted[:2, :]
        rightMost = xSorted[2:, :]
        # now, sort the left-most coordinates according to their
        # y-coordinates so we can grab the top-left and bottom-left
        # points, respectively
        leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
        (tl, bl) = leftMost
        # if use Euclidean distance, it will run in error when the object
        # is trapezoid. So we should use the same simple y-coordinates order method.

        # now, sort the right-most coordinates according to their
        # y-coordinates so we can grab the top-right and bottom-right
        # points, respectively
        rightMost = rightMost[np.argsort(rightMost[:, 1]), :]
        (tr, br) = rightMost
        # return the coordinates in top-left, top-right,
        # bottom-right, and bottom-left order
        
        #return np.array([self.pixel_to_carla(tl), self.pixel_to_carla(tr), self.pixel_to_carla(br), self.pixel_to_carla(bl)], dtype="float32")
        return np.array([tl, tr, br, bl])
       
    def draw_poly(self, contours):
        self.display_img = opencv_engine.draw_fillpoly(self.display_img, contours)
        self.__update_img()

    def draw_point(self, point):
        # give me normalized point, i will help you to transform to origin cv image position
        cv_image_x = point[0]*self.origin_width
        cv_image_y = point[1]*self.origin_height
        self.display_img = opencv_engine.draw_point(self.display_img, (cv_image_x, cv_image_y))
        self.__update_img()
        
    def pixel_to_carla(self, image_pos):
        world_pos = (image_pos /10.0) + self.min_point
        return world_pos
    
    
    def carla_to_pixel(self, world_pos):
        image_pos = ((world_pos - self.min_point)*10.0).astype(int)
        return image_pos
    
    def save_dict(self, di_, filename_):
        with open(filename_, 'wb') as f:
            pickle.dump(di_, f)

    def load_dict(self, filename_):
        with open(filename_, 'rb') as f:
            ret_di = pickle.load(f)
        return ret_di
    
    
    def show_results(self):
        
        if os.path.exists(f'./Region_tags/{self.ui.town_comboBox.currentText()}.pkl'):
            tags = self.load_dict(f'./Region_tags/{self.ui.town_comboBox.currentText()}.pkl')
           
            tag_list = list(tags.keys())
            # draw on image with tag 
            for tag in tag_list:
                contours = self.carla_to_pixel(tags[tag])
                self.display_img = opencv_engine.draw_fillpoly_with_tag(self.display_img, contours, tag, color = (125, 255, 0))
            self.__update_img()
            
        else:
            print("NO tag")
    

    
    def save_flag(self):
        if self.point_counter == 4:
            coor_list = []
            for point in self.points:
                coor_list.append(( point ))
            contours = np.array(coor_list)
                
                
            # self.draw_poly(contours)
            # self.draw_poly(self.carla_to_pixel(self.pixel_to_carla(contours)))
            tag_name = self.ui.lineEdit_tag.text()
            if tag_name == "":
                return
            
            # check json file exist ?
            
            if os.path.exists(f'./Region_tags/{self.ui.town_comboBox.currentText()}.pkl'):
                
                tags = self.load_dict(f'./Region_tags/{self.ui.town_comboBox.currentText()}.pkl')
                tags[tag_name] = self.pixel_to_carla(contours)
                self.save_dict(tags, f'./Region_tags/{self.ui.town_comboBox.currentText()}.pkl')

            else:
                tags = {}
                tags[tag_name] = self.pixel_to_carla(contours)
                self.save_dict(tags, f'./Region_tags/{self.ui.town_comboBox.currentText()}.pkl')
                
            self.clear()
            self.ui.lineEdit_tag.clear()
                
            
            
        
        
    def show_point(self):
        
        if self.ui.lineEdit_x.text() != "" and self.ui.lineEdit_y.text() != "":
            x = float(self.ui.lineEdit_x.text())
            y = float(self.ui.lineEdit_y.text())
            pos = self.carla_to_pixel(np.array([x, y]))
            
            self.display_img = opencv_engine.draw_point(self.display_img, (pos[0], pos[1]), color = (0, 0, 255), point_size = 50, thickness = 5)
            
            # print(pos)
            self.__update_img()
            
            
            # img, point=(0, 0), color = (0, 0, 255), point_size = 1 
            