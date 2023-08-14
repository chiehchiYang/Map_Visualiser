import cv2 
import numpy as np
from PIL import Image

Town_list = ["Town01", "Town02", "Town03", "Town04", "Town05", "Town05_highway", "Town06", "Town07", "Town10HD"]

for Town in Town_list:
    lane = cv2.imread(f"./{Town}/mask_lane.png", cv2.IMREAD_GRAYSCALE)
    lane_line = cv2.imread(f"./{Town}/mask_road_line.png", cv2.IMREAD_GRAYSCALE)
    mask = np.ones_like(lane)
    # print(lane.shape)
    # print(lane_line.shape)
    
    lane = np.argwhere(lane == 0)
    lane_line = np.argwhere(lane_line > 0)
    


    
    
    for x, y in lane:
        mask[x][y] = 0
        
        
    for x, y in lane_line:
        mask[x][y] = 0
        
        
    if not(Town == "Town01" or Town == "Town02" or Town == "Town05_highway"):
            
        crosswalk = cv2.imread(f"./{Town}/crosswalk.png", cv2.IMREAD_GRAYSCALE)
        crosswalk = np.argwhere(crosswalk > 0)
        
                
        for x, y in crosswalk:
            mask[x][y] = 0
                

        
    mask = 255 * mask 
    mask = mask.astype(np.uint8)
    Image.fromarray(mask).save(f"./{Town}.png")
    
        
    
    
