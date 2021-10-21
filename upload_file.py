import dropbox

class transfer_data:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(filefrom,'rb')
        dbx.files_upload(f.read(),fileto)

def main():
    access_token = 'sl.A6y-dKzwNYG0BJDwrPGKMzR3dKq555dN2WHX5tVN2to5wl-tOSes8nqCBU9v_9vktHgF_ryMdct1j0ixtjiYj9Bwc3nH8r4jHMfLTbWdoJZ6ozQF3nh-rNPuuWmxcnRhEqbm5Yk'
    transferData = transfer_data(access_token)
    filefrom = input("Enter location of file ")
    fileto = input("Enter path to upload file ")
    transferData.upload_file(filefrom,fileto)
    print("Success")

main()
