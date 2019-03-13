import glob
import sys

frames_dir = sys.argv[1]
if len(sys.argv) > 2:
    outfile_name = sys.argv[2]
else:
    outfile_name = 'order.csv'
order_file = open(outfile_name,'w')
order_file.write("slides, duration, is_primary\n")
lines = []
for f in glob.glob('{}/*.jpg'.format(frames_dir)):
    lines.append("{}, {}, {}".format(f, 1, 0))
    lines.append("\n")
order_file.writelines(lines[:-1])
order_file.close()