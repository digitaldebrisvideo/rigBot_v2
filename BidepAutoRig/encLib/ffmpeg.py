import os
import subprocess


def get_file_extensions(folder):
    """
    Given a folder of files, eturns a list of file extensions.
    :param folder: String - path to a directory on disk
    :return: List - of found file extensions
    """

    def test(f): return os.path.isfile(os.path.join(folder, f))

    extensions = [os.path.splitext(x)[-1].lower() for x in os.listdir(folder) if test(x)]
    extensions = list(set(extensions))
    return extensions


def make_quicktime(folder, output_path=None, extension=".jpg"):
    """
    Given a folder containing a JPG image sequence or an AVI, generate a Quicktime and return its path.

    :param folder: String - path to a directory on-disk.
    :param output_path: String - output path to a Quicktime movie on-disk. (ex: "C:\temp\movie.mov")
    :param extension: String - the extension to feed FFMPEG (ex: ".jpg")
    :return: None or String - path to a Quicktime file.
    """
    """ determine pattern -- AVI or JPG? """
    files = os.listdir(folder)
    extensions = get_file_extensions(folder)
    fmt = "-c:v mjpeg -qscale:v 1"
    """ build command """
    if ".avi" in extensions:
        avi = [x for x in files if x.lower().endswith(".avi")][0]
        mov = "{name}.mov".format(name=os.path.splitext(avi)[0])
        if output_path is None:
            out = os.path.join(folder, mov).replace("\\", "/")
        else:
            out = output_path.replace("\\", "/")
        cmd = "ffmpeg -i {avi} {fmt} {mov} -y".format(avi=os.path.join(folder, avi),
                                                      fmt=fmt,
                                                      mov=out)
    else:
        pattern = extension
        if ".jpeg" in extensions:
            pattern = ".jpeg"
        jpg_files = [x for x in files if x.lower().endswith(pattern)]
        jpg_files.sort()
        jpg = jpg_files[0]
        bits = jpg.rsplit(".", 2)
        prefix = bits[0]
        start = int(bits[1])
        ext = bits[-1]
        mov = "{name}.mov".format(name=prefix)
        if output_path is None:
            out = os.path.join(folder, mov).replace("\\", "/")
        else:
            out = output_path.replace("\\", "/")
        cmd_string = "ffmpeg -framerate 24 -f image2 -start_number {start} -i \"{prefix}.%04d.{ext}\" {fmt} {mov} -y"
        cmd = cmd_string.format(start=start,
                                prefix=os.path.join(folder, prefix).replace("\\", "/"),
                                ext=ext,
                                fmt=fmt,
                                mov=out)
    """ build Quicktime """
    print(cmd)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    msg = proc.communicate()
    print(msg[0])
    if os.path.exists(out):
        return out
    else:
        return None


def avi_to_jpeg(folder, output_folder=None, start_frame=101, prefix=None):
    """
    Given a folder containing an AVI file, generate a JPEG sequence to an output folder.

    :param folder: String - path to a directory on-disk.
    :param output_folder: String - output path to a Quicktime movie on-disk. (ex: "C:\temp\")
    :param start_frame: Integer - what the first JPG number should be.
    :param prefix: String - what the JPG filename should be before the number and extension
                           (ex: "001_0010_ani_audio-test_v0013")
    :return: None or String - path to a Quicktime file.
    """
    """ find the AVI """
    files = os.listdir(folder)
    extensions = get_file_extensions(folder)
    fmt = "-q:v 1 -start_number {0}".format(start_frame)
    """ build command """
    if ".avi" in extensions:
        avi = [x for x in files if x.lower().endswith(".avi")][0]
        if prefix:
            name = prefix
        else:
            name = os.path.splitext(avi)[0]
        jpg = "{name}.%04d.jpg".format(name=name)
        if output_folder is None:
            out = folder
        else:
            out = output_folder
        out = os.path.join(out, jpg).replace("\\", "/")
        cmd = "ffmpeg -i {avi} {fmt} {jpg} -y".format(avi=os.path.join(folder, avi),
                                                      fmt=fmt,
                                                      jpg=out)
    else:
        """ quit """
        return None
    """ build JPEGS """
    print(cmd)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    msg = proc.communicate()
    print(msg[0])
    if os.path.exists(out):
        return out
    else:
        return None


if __name__ == "__main__":
    src = r"C:\temp\test"
    dst = r"C:\temp\test\_jpg"
    avi_to_jpeg(src, output_folder=dst)
