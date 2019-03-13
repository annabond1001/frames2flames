import glob
import sys

frames_dir = sys.argv[1]
order_file = open('order.csv','w')
order_file.write("slides, duration, is_primary\n")
lines = []
for f in glob.glob('{}/*.jpg'.format(frames_dir)):
    lines.append("{}, {}, {}".format(f, 1, 0))
    lines.append("\n")
order_file.writelines(lines[:-1])
order_file.close()