try:
    from django.conf.urls import patterns, url
else:
    from django.urls import patterns, re_path as url

from ajaxuploader.views import AjaxFileUploader
from ajaxuploader.backends.default_storage import DefaultStorageUploadBackend


default_storage_uploader = AjaxFileUploader(backend=DefaultStorageUploadBackend)

urlpatterns = patterns('',
    url(r'^upload$', default_storage_uploader, name="ajax-upload-default-storage"),                
)
