from six.moves import cPickle as pickle #for performance


def load_dict( filename_):
    with open(filename_, 'rb') as f:
        ret_di = pickle.load(f)
    return ret_di

result = load_dict("Town10HD.pkl")
scenario_obstacles = result[0]

for obstacle_info in scenario_obstacles:
    
    obstacle_type = obstacle_info['obstacle_type']
    pos = obstacle_info['pos']
    yaw = obstacle_info['yaw']
    
    
    print(obstacle_type, pos, yaw)
    
    
    
    