from PyQt5 import QtCore 
from PyQt5.QtGui import QImage, QPixmap

from opencv_engine import opencv_engine
import ujson
import numpy as np
import os 
import math

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
        
        self.list_collect_points = []
        
        self.edit_mode_flag = False
        self.show_result_flag = False
        
        
        self.route_mode = False
        
        self.obstacle_scenario_mode = False
        
        self.previous_point = [-1,  -1]
        
        self.obstacle_scenario_result = []
        self.current_pos = None
        self.yaw = None
        
        
    def draw_rotated_bbox(self, pos, dx, dy, yaw):
        # yaw is degree 
        def rotate(origin, point, yaw):
            """
            Rotate a point counterclockwise by a given angle around a given origin.

            The angle should be given in radians.
            """
            angle = math.radians(yaw)
            ox, oy = origin
            px, py = point

            qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
            qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
            return int(qx), int(qy)
            
        x = pos[0]
        y = pos[1]
        
        x1, y1 = rotate((x, y), (x - dx/2, y - dy/2), yaw)
        x2, y2 = rotate((x, y), (x - dx/2, y + dy/2), yaw)
        x3, y3 = rotate((x, y), (x + dx/2, y - dy/2), yaw)
        x4, y4 = rotate((x, y), (x + dx/2, y + dy/2), yaw)
        
        return np.array([[x1, y1], [x3, y3],   [x4, y4], [x2, y2]]).astype(int)
        
    def add_obstacle(self):
        
        if self.obstacle_scenario_mode == False:
            return 0 
        
        # if self.current_pos != None:
        #     return 0
        
        data = {}
        data["obstacle_type"] = self.ui.obstacle_type_comboBox.currentText() # ex: trafficcone02
        data["pos"] = self.current_pos

        yaw = self.yaw
        if yaw == None:
            yaw = 0
        data["yaw"] = yaw
        
        self.obstacle_scenario_result.append(data)
        
        
        
        

        
        
        # draw on the  display
        
        pos = self.carla_to_pixel(np.array(self.current_pos))     
        
        if self.ui.obstacle_type_comboBox.currentText() == "trafficcone01":
        
            self.display_img = opencv_engine.draw_point(self.display_img, (pos[0], pos[1]), color = (125, 125, 0), point_size=7) 
        
        elif   self.ui.obstacle_type_comboBox.currentText() == "trafficcone02":
        
            self.display_img = opencv_engine.draw_point(self.display_img, (pos[0], pos[1]), color = (125, 125, 0), point_size=4) 
        
        elif   self.ui.obstacle_type_comboBox.currentText() == "streetbarrier":
            
            contours = self.draw_rotated_bbox(pos, dx=12, dy=6, yaw=yaw)
            self.display_img = opencv_engine.draw_fillpoly(self.display_img, contours, color = (125, 125, 0))
        
        elif   self.ui.obstacle_type_comboBox.currentText() == "trafficwarning":
            
            contours = self.draw_rotated_bbox(pos, dx=25, dy=15, yaw=yaw)
            self.display_img = opencv_engine.draw_fillpoly(self.display_img, contours, color = (125, 125, 0))
            
            
        elif   self.ui.obstacle_type_comboBox.currentText() == "illegal_parking":
            
            contours = self.draw_rotated_bbox(pos, dx=49, dy=20, yaw=yaw)
            self.display_img = opencv_engine.draw_fillpoly(self.display_img, contours, color = (125, 125, 0))

        self.__update_img()
        
    def save_obstacle_scenario(self):
        
        if self.obstacle_scenario_mode == False:
            return 0 

        self.file_path = f'./obstacle_scenarios/{self.ui.town_comboBox.currentText()}.pkl'
        if os.path.exists(self.file_path):
            old_ = self.load_dict(self.file_path)
            old_.append(self.obstacle_scenario_result)
            self.save_dict(old_, self.file_path)
        else:
            self.save_dict([self.obstacle_scenario_result], self.file_path)
        self.obstacle_scenario_result = []
        
        
    def show_all_obstacle_scenario(self):
        self.file_path = f'./obstacle_scenarios/{self.ui.town_comboBox.currentText()}.pkl'
        if os.path.exists(self.file_path):
            result = self.load_dict(self.file_path)
            
            # clean the image 
            self.clear()
            
            # draw on image
            
            
            for obstacle_scenario in result:
                
                
                random_color = tuple(np.random.random(size=3) * 256)
                
                for obstacle_info in obstacle_scenario: 
                    
                    obstacle_type = obstacle_info['obstacle_type']
                    pos = obstacle_info['pos']
                    yaw = obstacle_info['yaw']
        
                    pos = self.carla_to_pixel(np.array(pos))     
                    
                    if obstacle_type == "trafficcone01":
                    
                        self.display_img = opencv_engine.draw_point(self.display_img, (pos[0], pos[1]), color = random_color, point_size=7) 
                    
                    elif obstacle_type == "trafficcone02":
                    
                        self.display_img = opencv_engine.draw_point(self.display_img, (pos[0], pos[1]), color = random_color, point_size=4) 
                    
                    elif obstacle_type == "streetbarrier":
                        
                        contours = self.draw_rotated_bbox(pos, dx=12, dy=6, yaw=yaw)
                        self.display_img = opencv_engine.draw_fillpoly(self.display_img, contours, color = random_color)
                    
                    elif obstacle_type == "trafficwarning":
                        
                        contours = self.draw_rotated_bbox(pos, dx=25, dy=15, yaw=yaw)
                        self.display_img = opencv_engine.draw_fillpoly(self.display_img, contours, color = random_color)
                        
                        
                    elif obstacle_type == "illegal_parking":
                        
                        contours = self.draw_rotated_bbox(pos, dx=49, dy=20, yaw=yaw)
                        self.display_img = opencv_engine.draw_fillpoly(self.display_img, contours, color = random_color)
                    

        
                    

            self.__update_img()
    
        
    # def remove_obstacle(self)

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
        self.obstacle_scenario_result = []
        self.list_collect_points = []
        
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

    def __update_text_clicked_position(self, x, y, yaw):
        # give me qpixmap point
        self.ui.label_click_pos.setText(f"Clicked postion = ({x}, {y})")
        norm_x = x/self.qpixmap.width()
        norm_y = y/self.qpixmap.height()
        # print(f"(x, y) = ({x}, {y}), normalized (x, y) = ({norm_x}, {norm_y})")
        # self.ui.label_norm_pos.setText(f"Normalized postion = ({norm_x:.3f}, {norm_y:.3f})")

        cv_image_x = norm_x*self.origin_width
        cv_image_y = norm_y*self.origin_height
        image_pos = np.array([int(cv_image_x), int(cv_image_y)])
        carla_pos = self.pixel_to_carla(image_pos)

        self.ui.label_real_pos.setText(f"Carla Coordinate = ({carla_pos[0]:5.1f}, {carla_pos[1]:5.1f})")
        
        if yaw == -1:
            pass
        else:
            self.ui.label_yaw.setText(f"yaw= ({yaw:5.1f})")
        # label_yaw

# for numbers in list:
#     print(f'{numbers:9.3f}')

    def set_zoom_in(self):
        self.ratio_value = min(100, self.ratio_value + 1)
        self.__update_img()

    def set_zoom_out(self):
        self.ratio_value = max(0, self.ratio_value - 1)
        self.__update_img()

    def set_slider_value(self, value):
        self.ratio_value = value
        self.__update_img()

    # event 
    def set_clicked_position(self, event):
        x = event.pos().x()
        y = event.pos().y()
        
        norm_x = x/self.qpixmap.width()
        norm_y = y/self.qpixmap.height()
        # self.draw_point((norm_x, norm_y))
        # self.__update_text_point_roi((norm_x, norm_y))
        
        cv_image_x = norm_x*self.origin_width
        cv_image_y = norm_y*self.origin_height
        image_pos = np.array([int(cv_image_x), int(cv_image_y)])
        
        
        # get yaw     
        yaw = -1
        current_pos = self.pixel_to_carla(image_pos)     
        
        if self.previous_point[0] != -1:
            
            
            yaw_vector = (current_pos - self.previous_point)

            vector = [1, 0]

            unit_vector_1 = yaw_vector / np.linalg.norm(yaw_vector)
            unit_vector_2 = vector / np.linalg.norm(vector)
            
            
            dot_product = np.dot(unit_vector_1, unit_vector_2)
            
            angle = np.arccos(dot_product)
            import math
            
            if yaw_vector[1] < 0:
                yaw = -math.degrees(angle)
            else:
                yaw = math.degrees(angle)

            
            # change yaw yaw_vector to yaw
        self.__update_text_clicked_position(x, y, yaw)
        
        self.current_pos = current_pos
        self.yaw = yaw
            
        
        self.previous_point = current_pos

        
        

        if event.button() == 1: # left clicked
            
            if self.obstacle_scenario_mode:
                self.draw_point((norm_x, norm_y))
            
            if not self.route_mode:
                if self.point_counter < 4:
                    self.point_counter+=1
                    self.points.append(image_pos)        
                    if self.point_counter == 4:
                        self.points = self.order_points(np.array( self.points) )
                    self.draw_point((norm_x, norm_y))
                    
                
            else:
                
                carla_pos = self.pixel_to_carla(image_pos)
                self.list_collect_points.append(carla_pos)
                self.draw_point((norm_x, norm_y))
                
                                        
                                        
                        

        elif event.button() == 2: # right clicked
            if self.obstacle_scenario_mode:
                self.draw_point((norm_x, norm_y))
                
            if not self.route_mode:
                if self.point_counter == 4:
                    
                    coor_list = []
                    for point in self.points:
                        # coor_list.append(self.carla_to_pixel( point ))
                        coor_list.append(( point ))
                    
                    contours = np.array(coor_list)
                    
                    
                    # self.draw_poly(contours)
                    self.draw_poly(self.carla_to_pixel(self.pixel_to_carla(contours)))
                    
            else:
                pass
                    
                
                
                
                
                
                
                # draw fillPoly

                # cv2.fillPoly(self.current_top_img, pts = [contours], color =(255,0,0))
                
    def getEquidistantPoints(self, p1, p2, parts):
        return zip(np.linspace(p1[0], p2[0], parts+1),
                np.linspace(p1[1], p2[1], parts+1))
        
        
    ## smoothing    
    def smooth_route(self):
        
        if len(self.list_collect_points) > 0:
            import math
            import cv2 

            total_distance = 0
            route = []
            prev_x = 0
            prev_y = 0
                    

            for index in range(len(self.list_collect_points)):

                x = self.list_collect_points[index][0]
                y = self.list_collect_points[index][1]
                # coordinate in pixel
                coordinate = self.carla_to_pixel(np.array([x, y]))
                
                x = coordinate[0]
                y = coordinate[1]

                if index !=0:
                    distance = math.sqrt( (x-prev_x)**2 + (y-prev_y)**2)
                    total_distance+=distance
                route.append( (x, y))
                prev_x = x
                prev_y = y

            route = np.array(route)

            poly = cv2.approxPolyDP(route, 0.004 * total_distance, False)
            
            new_route = []
            for p in poly:
                new_route.append(self.pixel_to_carla (p[0]) )

            # getEquidistantPoints
            final_route = []
            prev_x = 0
            prev_y = 0
            for index in range(len(new_route)):
                x = new_route[index][0]
                y = new_route[index][1]

                if index !=0:
                    distance = math.sqrt( (x-prev_x)**2 + (y-prev_y)**2)
                    final_route+= list(self.getEquidistantPoints((prev_x, prev_y), (x,y), int(distance)))
                prev_x = x
                prev_y = y

            self.list_collect_points = final_route
            
            # draw on image 

            self.display_img = self.origin_img.copy()
            
            color_counter = 0
            for position in final_route:
                color_counter+=3
                
                pos = self.carla_to_pixel(np.array(position))
                
                self.display_img = opencv_engine.draw_point(self.display_img, (pos[0], pos[1]), color = (0, 255 - color_counter%255, color_counter%255)) 

            self.__update_img()
        
        
    def save_route_points(self):
        if self.route_mode and len(self.list_collect_points) > 0:
            np.save("./route.npy", np.array(self.list_collect_points))
        
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
            
            
            # ({self.origin_width}, {self.origin_height})"
            
            
            
            
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
            