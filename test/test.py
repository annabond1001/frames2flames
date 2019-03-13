import sys
sys.path.insert(0, '../')
import wipe
import recast
#TODO make package

# wipe.animate(order_input_path='wipe_order.csv', video_output_path='wipe_output.mp4')
recast.animate(order_input_path='wipe_order.csv', video_output_path='recast_output.mp4')