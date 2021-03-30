import dropbox
import os

# Only works if folder has files in it. Doesn't work for sub folders. The path gets errorneous
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for file in files:
                local_path = os.path.join(root, file)
                #print(local_path)

                relative_path = os.path.relpath(local_path, file_from)
                #print(relative_path)
                
                #dropbox_path = os.path.join(file_to, relative_path)
                dropbox_path = "/"+file_to+'/'+relative_path
                print(dropbox_path)

                with open(local_path,'rb') as f:                    
                    dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)

def main():
    access_token = 'QbwFjG7FCJkAAAAAAAAAAY99SdB9T9qQMc1ZyyK-taHbz_jKqjYw_y6k4KDqd-uF'
    transferData = TransferData(access_token)

    file_from = input ("Enter the folder path to transfer: ")
    file_to = input("Enter the full path to upload to dropbox: ")

    #file_from = "C:/Users/banas/Desktop/WhiteHat_Classes/projects/sbsdbsd"
    #file_to="/BANA1" 

    transferData.upload_file(file_from, file_to)
    print("File has been uploaded!")


main()