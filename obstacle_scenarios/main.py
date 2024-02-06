from six.moves import cPickle as pickle #for performance


def load_dict( filename_):
    with open(filename_, 'rb') as f:
        ret_di = pickle.load(f)
    return ret_di

# result = load_dict("Town05.pkl")


result = load_dict("Town03.pkl")


print(len(result))



# def save_dict( di_, filename_):
#     with open(filename_, 'wb') as f:
#         pickle.dump(di_, f)


# pop_result = result.pop(-1)

# print(pop_result)

# print(result)


# save_dict(result,"Town10HD.pkl")


# print(result[0])


# # print(result[-1])
# counter = 0
# for obstacle_info in result:
    
#     detect_point = obstacle_info[0]
    
#     obstacle_route = obstacle_info[2]
#     print(counter)
#     counter+=1
    
#     for obstacle_infos in obstacle_info[1]:
        
        
        
        
#         obstacle_type = obstacle_infos['obstacle_type']
#         pos = obstacle_infos['pos']
#         yaw = obstacle_infos['yaw']
#         # print(obstacle_type, pos , yaw)
        
        
#         print(f"blueprint = world.get_blueprint_library().find(f\"static.prop.{obstacle_type}\")")
#         print(f"obstacle_transform = carla.Transform(carla.Location(x={pos[0]}, y={pos[1]}, z=0), carla.Rotation(roll=0.0, pitch=0.0, yaw={yaw}))")
#         print("obstacle = client.get_world().spawn_actor(blueprint, obstacle_transform)")
#     print("")
        
        
    
    