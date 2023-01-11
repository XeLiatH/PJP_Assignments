import os
for root, dirs, files, rootfd in os.fwalk('/home/albert/data'):
    size = sum([os.stat(name, dir_fd=rootfd).st_size for name in files])
    print("{} consumes {} bytes in {} non-directory files".format(root, size, len(files)))
