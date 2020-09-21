from django.conf import LazySettings
from storages.backends.s3boto3 import S3Boto3Storage

settings = LazySettings()


class MediaStorage(S3Boto3Storage):
    location = ""
    bucket_name = settings.AWS_MEDIA_STORAGE_BUCKET_NAME
    access_key = settings.AWS_MEDIA_ACCESS_KEY_ID
    secret_key = settings.AWS_MEDIA_SECRET_ACCESS_KEY
    region_name = settings.AWS_MEDIA_S3_REGION_NAME
    custom_domain = settings.AWS_MEDIA_S3_CUSTOM_DOMAIN