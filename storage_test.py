import json
from minio import Minio
from minio.error import ResponseError

with open('config.json') as config:
    config_file = json.load(config)

storageClient = Minio(config_file['server'],
                      access_key=config_file['access_key'],
                      secret_key=config_file['secret_key'],
                      secure=True)


def create_bucket(bucketName):
    try:
        storageClient.make_bucket(bucketName)
    except BucketAlreadyOwnedByYou as err:
        print(err)
    except BucketAlreadyExists as err:
        print(err)
    except ResponseError as err:
        raise


def upload_to_bucket(bucketName, objectName, objectPath):
    try:
        print(f'uploading object {objectName} to bucket {bucketName}')
        storageClient.fput_object(bucketName, objectName, objectPath)
    except ResponseError as err:
        print(err)
