import requests
import zipfile
import os

class Loader:
    '''
    Downloads the data and have the data prepared.
    '''

    def __init__(self, download_link='gs://uga-dsp/project3/'):
        '''
        Constructor for the Loader Class
            
        Args:
            download_link: The bucket url from which data is to be downloaded
        '''
        self.download_link = download_link
        self.train_path = self.get_train_path()
        self.test_path = self.get_test_path()
        if os.path.exists("data"):
            print('Data Folder is ready')
        else:
            self.download_data(download_link)


    def download_data(self, download_link):
        '''
        Downloads the zipped file data from the the location if  'data' folder 
        not present
        '''
        if os.path.exists('data'):
            self.extract_zip_data()
        else:
            os.makedirs('../data/download')
            print("==> Downloading data")
            os.system('gsutil -m cp -r'+download_link+'*'+' ../data/dowload/')
            self.extract_zip_data()


    def extract_zip_data(path):
        """
        Function to extract the data into test and train folders inside a
        data folder

        Args:
            path: The path of the folder where zip data is present
        """

        files = os.listdir(path)
        for file in files:
            print("Extracting "+file)
            filepath = path + file
            print(filepath)
            zip_ref = zipfile.ZipFile(filepath, 'r')
            print(zip_ref)
            # Checking if the file is testfile or train file
            if file[-8:] == 'test.zip':
                # if it is a test file extract that in test_path
                zip_ref.extractall(get_test_path(path))
            else:
                zip_ref.extractall(get_train_path(path))
            zip_ref.close()


    def get_train_path(self):
        """
        Function to get the train path where unzipped train files are present

        Returns:
            Path of the train files
        """
        self.train = "../data/train/"
        return self.train


    def get_test_path(self):
        """
        Function to get the train path where unzipped train files are present

        Returns:
            Path of the test files
        """
        self.test = "../data/test/"
        return self.test