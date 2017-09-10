class AtomicFile(AtomicSinkFile):
    """
    Simple class
    """
    def move_to_final_destination(self):
        os.rename(self.__tmp_path , self.path)

    def generate_tmp_path(self , path):
        return os.path.join(tempfile.gettempdir(), 'sunny-tmp-%09d' % random.randrange(0, 1e10))

class LocalFileSystem(FileSystem):
    """
    Wrapper for access to the local file system
    """
    def remove(self, path , recursive = True , skip_trash = True):
        if recursive and self.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    def exists(self , path):
        return os.path.exists(path)

    def mkdir(self , path , parents = True , raise_if_exists = True):

        if self.exists(path):
            if raise_if_exists:
                return FileAlreadyExists()
            elif not self.isdir(path):
                raise NotADirectory()
            else:
                return
        if parents:
            os.makedirs(path)
        else:
            if not os.path.exists(os.path.dirname(path)):
                raise MissingParentDirectory()
            os.mkdir(path)
    def isdir(self, path):
        return os.path.isdir(path)

    def listdir(self,path):
        for dir_, _ , files in os.walk(path):
            assert dir_.startswith(path)
            for name in files:
                yield os.path.join(dir_, name)

    def move(self , path ,dest):
        os.rename(path , dest)

class LocalFileSink(FileSystemSink):
    fs = LocalFileSystem()

    def __init__(self , path = None , is_tmp = False):
        if not path:
            if not is_tmp:
                 raise Exception('path or is_tmp must be set')
            path = os.path.join(tempfile.gettempdir() , "sunny-tmp-%09d" % random.randint(0, 999999999))
        super(LocalFileSink , self).__init__(path)
        self.is_tmp = is_tmp

    def makedirs(self):
        """
        Create all the parents folder
        """
        normpath = os.path.normpath(self.path)
        parentfolder = os.path.dirname(normpath)
        if parentfolder:
            try:
                os.makedirs(parentfolder)
            except OSError:
                pass
    def open(self ,mode = 'r'):
        """
        This is used to open the file for read/write purpose
        """
        mode = mode.replace('b' , '').replace('t' , '')
        if mode == 'w':
            self.makedirs()
            #TODO:Create a writer object
        elif mode == 'r':
            #TODO:Create a reader object
            pass
    def move(self , new_path , raise_if_exists = False):
        self.fs.move(self.path , new_path , raise_if_exists)

    def remove(self):
        self.fs.remove(self.path)

    def __del__(self):
        if self.is_tmp and self.exists():
            self.remove()

