import os
__all__ = [i.strip().split(".")[0].strip() for i in os.listdir(os.getcwd()+"/src/textPrograms") if not i.startswith("__")]