import boto3

SOURCE_BUCKET_NAME = "myproduction-bucket"                   ## definition of source, target and extension to operate on 
SOURCE_DIRECTORY = "store/"
DESTINATION_BUCKET_NAME = "mytest-bucket"
EXTENSION_TO_COPY = ".mp4"

MAX_SIZE_TRANSFER = 3221225472   ### 3GB to be passed max
# - 1GB = 1,073,741,824 bytes (1024 × 1024 × 1024)
# - 3GB = 3 × 1,073,741,824 = 3,221,225,472 bytes

s3 = boto3.resource('s3')                                   ## initialization of S3 resource
bucket = s3.Bucket(SOURCE_BUCKET_NAME)                      ##

# Iterate over all objects in the bucket
already_coppied = 0
for obj in bucket.objects.filter(Prefix=SOURCE_DIRECTORY):   ## filtering only in desired Directory
    if obj.key.endswith(EXTENSION_TO_COPY):                  ## filtering only certain extension
        
        obj_metadata = obj.Object()
        if obj_metadata.storage_class not in ["DEEP_ARCHIVE", "GLACIER"]:     ## avoid slow storage
            #print(obj.key)                                                   ## this was used for debug purposes

            already_coppied = already_coppied + obj_metadata.content_length   ## limiting to max 3GB
            if already_coppied >= MAX_SIZE_TRANSFER:
                break  # Stop iteration

            copy_source = {'Bucket': SOURCE_BUCKET_NAME, 'Key': obj.key}      ## redefining rource as dictionary
            s3.Bucket(DESTINATION_BUCKET_NAME).copy(copy_source, obj.key)     ## execution of copy 

            print(f"Copied {obj.key} to {DESTINATION_BUCKET_NAME}")           ## printout only