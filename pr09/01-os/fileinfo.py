"""
Python 3 version of FileInfo Python 2 example from original Dive Into Python
"""
import os
import sys


def stripnulls(data):
    """
    strip whitespace and nulls
    """
    data = data.decode('utf-8')
    return data.replace("\00", " ").strip()


class FileInfo(dict):
    """
    store file metadata in dict like structure
    """

    def __init__(self, filename=None):
        super(FileInfo, self).__init__()
        self["name"] = filename


class MP3FileInfo(FileInfo):
    "store ID3v1.0 MP3 tags"
    tag_data_map = {"title": (3, 33, stripnulls),
                    "artist": (33, 63, stripnulls),
                    "album": (63, 93, stripnulls),
                    "year": (93, 97, stripnulls),
                    "comment": (97, 126, stripnulls),
                    "genre": (127, 128, ord)}

    def __parse(self, filename):
        """
        parse ID3v1.0 tags from MP3 file
        """
        self.clear()
        try:
            fsock = open(filename, "rb", 0)
            try:
                fsock.seek(-128, 2)
                tagdata = fsock.read(128)
            finally:
                fsock.close()

            if tagdata[:3] == b'TAG':
                for tag, (start, end, parsing_func) in self.tag_data_map.items():
                    self[tag] = parsing_func(tagdata[start:end])
        except IOError:
            pass

    def __setitem__(self, key, item):
        if key == "name" and item:
            self.__parse(item)

        super(MP3FileInfo, self).__setitem__(key, item)


def get_file_info_class(filename, module=sys.modules[FileInfo.__module__]):
    """
    get file info class from filename extension
    """
    subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
    return getattr(module, subclass) if hasattr(module, subclass) else FileInfo


def list_dir(directory, file_ext_list):
    """
    get list of file info objects for files of particular extensions
    """
    file_list = [os.path.normcase(f) for f in os.listdir(directory)]
    file_list = [os.path.join(directory, f) for f in file_list
                 if os.path.splitext(f)[1] in file_ext_list]

    return [get_file_info_class(f)(f) for f in file_list]

if __name__ == "__main__":
    for info in list_dir("/home/albert/data/fileinfo", [".mp3"]):
        print("\n".join(["%s=%s" % (k, v) for k, v in info.items()]))
