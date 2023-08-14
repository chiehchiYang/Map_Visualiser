import numpy as np
import cv2
import json

import open3d as o3d

if __name__ == "__main__":
    
    Town_list = ["Town01", "Town02", "Town03", "Town04", "Town05", "Town05_highway", "Town06", "Town07", "Town10HD"]
    
    # Town_list = ["Town10HD"]

    with open("./maps/MapBoundaries.json", 'r') as f:
        data = json.load(f)
    for Town in Town_list:
        
        lane = cv2.imread(f"./maps/{Town}/mask_lane.png", cv2.IMREAD_GRAYSCALE)
        lane_line = cv2.imread(f"./maps/{Town}/mask_road_line.png", cv2.IMREAD_GRAYSCALE)
        
        
        
        min_x= data[Town]["min_x"]
        min_y= data[Town]["min_y"]
        max_x= data[Town]["max_x"]
        max_y= data[Town]["max_y"]
        
        min_point = np.array([min_x, min_y])
        
        lane = np.argwhere(lane > 0)

        tmp = lane.copy()
        lane[:,0] = tmp[:, 1]
        lane[:,1] = tmp[:, 0]
        
        lane = (lane /10.0) + min_point
        
        lane_line = np.argwhere(lane_line > 0)
        
        tmp = lane_line.copy()
        lane_line[:,0] = tmp[:, 1]
        lane_line[:,1] = tmp[:, 0]
        lane_line = (lane_line /10.0) + min_point
        
        np.save(f"./maps/{Town}/mask_road.npy", lane)
        np.save(f"./maps/{Town}/mask_road_line.npy", lane_line)
        
        if not(Town == "Town01" or Town == "Town02" or Town == "Town05_highway"):
            
            crosswalk = cv2.imread(f"./maps/{Town}/crosswalk.png", cv2.IMREAD_GRAYSCALE)
            crosswalk = np.argwhere(crosswalk > 0)
            
            tmp = crosswalk.copy()
            crosswalk[:,0] = tmp[:, 1]
            crosswalk[:,1] = tmp[:, 0]
            crosswalk = (crosswalk /10.0) + min_point
            np.save(f"./maps/{Town}/crosswalk.npy", crosswalk)