import dropbox
import os


class TransferData(object):
    def __init__(self, access_token):
        self.access_key = access_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_key)

        for root, dirs, files in os.walk(file_from):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

           
            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path,
                                 mode=dropbox.files.WriteMode('overwrite'))


def main():
    
    access_token = "sl.BHRfC4T4Kd_gkQaGrhQLRZ8kViV9R5RUfb8TKhFCqHjGlE1ni6Hxgv3JWjv7CN3GNiB64OyaoCCZ2F0XHzoSd_Ab4zi_E5d8GLrfc1hFLRhr9bdgth6kV2ooTarcJvPiZf4WmFk"
    transferdata = TransferData(access_token)

    file_from = input("Enter the source folder :")
    file_to = input("Enter the full path :")

    transferdata.upload_files(file_from, file_to)
    print("Your File/Folder is uploaded successfully")

main()
