# S3_copy
### this short program suppose to copy data between two buckets

## prerequisities
 - s3 credentails in ~/.aws/credential
 - installed boto3 library '''pip install boto3'''
 - running within python virt. env ''' python -m venv .venv; source .venv/bin/activate '''

## variables
- SOURCE_BUCKET_NAME = "msrogoncikmail-test1"                   
- SOURCE_DIRECTORY = "store/"
- DESTINATION_BUCKET_NAME = "msrogoncikmail-test2"
- EXTENSION_TO_COPY = ".mp4"
- MAX_SIZE_TRANSFER = 3221225472  (3GB)
.. self-explanatory

## pools to avoit due to slowlynes:
 - "DEEP_ARCHIVE"
 - "GLACIER"


## example run: 
```
(.venv) msrogoncik@msrogoncik-dev-vm:~/repos/S3_copy$ /home/msrogoncik/repos/S3_copy/.venv/bin/python /home/msrogoncik/repos/S3_copy/S3_copy_mp4.py
Copied store/1.mp4 to msrogoncikmail-test2
Copied store/2.mp4 to msrogoncikmail-test2
Copied store/3.mp4 to msrogoncikmail-test2
Copied store/a.mp4 to msrogoncikmail-test2
Copied store/b.mp4 to msrogoncikmail-test2
Copied store/c.mp4 to msrogoncikmail-test2
(.venv) msrogoncik@msrogoncik-dev-vm:~/repos/S3_copy$ 
```

## summary
the program was built with focus on functionality only,
there is no additioanl error handling (as there was not closely specified whether for example 3TB should be trasferred, or destination is limited to max 3 TB, .. whether to overwrite files if they already exist, whether it should be considered as error when nothing has been found for transfer... )
also no security measurements has been taken into account (root key or app key to be used, target file ACL .. )

