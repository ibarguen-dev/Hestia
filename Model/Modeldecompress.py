import os

class ModelDecompress:
    def __init__(self):
        pass
        
        

    def verfyFile(self, data:str):
        
        if data.endswith('.zip'):
            return 'zip'
        elif data.endswith(('.tar.gz', '.tgz', '.tar', '.tar.bz2', '.tar.xz')):
            return 'tar.gz'
        elif data.endswith('.tar'):
            return 'tar'
        elif data.endswith('.rar'):
            return 'rar'
        else:
            return 'unknown'
        
