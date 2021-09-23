from os import access
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token) :
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():   
     access_token ='Q71u22lbKiUAAAAAAAAAAfL05D1EZpwzXzz8fTl4NqTsKVYpQQLVpvZSGM9pVKRw'
     transferData = TransferData(access_token)

     file_from = input('Enter The file path to transfer :-')
     file_to = input('Enter the path to upload to drop box :-')
     
     transferData.upload_file(file_from,file_to)
     print('file has been moved ')

main()


