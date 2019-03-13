import glob
import sys

frames_dir = sys.argv[1]
order_file = open('order.csv','w')
order_file.write("slides, duration, is_primary\n")
for f in glob.glob('{}/*.jpg'.format(frames_dir)):
    order_file.write("{}, {}, {}\n".format(f, 1, 0))
order_file.close()