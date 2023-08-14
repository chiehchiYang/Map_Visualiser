import cv2

class opencv_engine(object):

    @staticmethod
    def point_float_to_int(point):
        return (int(point[0]), int(point[1]))

    @staticmethod
    def read_image(file_path):
        return cv2.imread(file_path)

    @staticmethod
    def draw_point(img, point=(0, 0), color = (0, 0, 255)): # red
        point = opencv_engine.point_float_to_int(point)
        print(f"get {point=}")
        point_size = 1
        thickness = 4
        return cv2.circle(img, point, point_size, color, thickness)

    @staticmethod
    def draw_line(img, start_point = (0, 0), end_point = (0, 0), color = (0, 255, 0)): # green
        start_point = opencv_engine.point_float_to_int(start_point)
        end_point = opencv_engine.point_float_to_int(end_point)
        thickness = 3 # width
        return cv2.line(img, start_point, end_point, color, thickness)

    @staticmethod
    def draw_rectangle_by_points(img, left_up=(0, 0), right_down=(0, 0), color = (0, 0, 255)): # red
        left_up = opencv_engine.point_float_to_int(left_up)
        right_down = opencv_engine.point_float_to_int(right_down)
        thickness = 2 # 寬度 (-1 表示填滿)
        return cv2.rectangle(img, left_up, right_down, color, thickness)

    @staticmethod
    def draw_rectangle_by_xywh(img, xywh=(0, 0, 0, 0), color = (0, 0, 255)): # red
        left_up = opencv_engine.point_float_to_int((xywh[0], xywh[1]))
        right_down = opencv_engine.point_float_to_int((xywh[0]+xywh[2], xywh[1]+xywh[3]))
        thickness = 2 # 寬度 (-1 表示填滿)
        return cv2.rectangle(img, left_up, right_down, color, thickness)
    
    @staticmethod
    def draw_fillpoly(img, contours, color = (0, 0, 255)): # red
               
        return cv2.fillPoly(img, pts = [contours], color =color)
    
    @staticmethod
    def draw_fillpoly_with_tag(img, contours, tag_name, color = (0, 0, 255)): # red
        
        # cv2.putText(影像, 文字, 座標, 字型, 大小, 顏色, 線條寬度, 線條種類)
        img = cv2.fillPoly(img, pts = [contours], color =color)
        middle_point = ((contours[3] + contours[1])/2).astype(int)
        middle_point [0] = contours[0][0]
        img = cv2.putText(img, tag_name,  middle_point, cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)
               
        return img