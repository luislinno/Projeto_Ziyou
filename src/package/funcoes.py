import kagglehub
import os
import shutil



# Funçao que realiza o download dos arquivos
def downloadDataset(pathFile):
    try:
        path = kagglehub.dataset_download(pathFile)
    except ValueError as e:
        print(e)
        raise

# Verifica se o diretório existe
def VerifyPath(FilePathOrigin):
    return True if os.path.exists(FilePathOrigin) else False
            
# Move os arquivos entre pastas
def FileMove(FilePathOrigin, filePatchDestiny):
    validation = VerifyPath(FilePathOrigin)
    if validation:
        filesName = [filenames for dirpath, dirnames, filenames in os.walk(FilePathOrigin)]
        for fileName in filesName:
            for file in fileName:
                FilePathOriginComplete = FilePathOrigin + file
                filePatchDestinyComplete = filePatchDestiny + file
                shutil.move(FilePathOriginComplete, filePatchDestinyComplete)
        return 'Moved Files'
    else: 
        return "Path don't exist"
