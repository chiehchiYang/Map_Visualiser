from six.moves import cPickle as pickle #for performance


def load_dict( filename_):
    with open(filename_, 'rb') as f:
        ret_di = pickle.load(f)
    return ret_di

result = load_dict("Town10HD.pkl")

for obstacle_info in result:
    
    detect_point = obstacle_info[0]
    obstacle_info = obstacle_info[1][0]
    obstacle_type = obstacle_info['obstacle_type']
    pos = obstacle_info['pos']
    yaw = obstacle_info['yaw']
    
    
    print(detect_point, obstacle_type, pos , yaw)
    break
    