import os

# This will run as a system script so let's use absolute paths
app_root = '/srv/FamilyPhoto/'
content_root = app_root + 'content/'
video_path = content_root + 'video/'
image_path = content_root + 'image/'
trash_path = app_root + 'trash/'
log_path = app_root + 'log/'
store_path = app_root + 'store/'


# this will handle all of the uploading from store -> content
# content will be sep by type



# if dropoff has subfolders, digest them
# os.path.isfile("bob.txt") # Does bob.txt exist?  Is it a file, or a directory?
# os.path.isdir("bob")


# handle duplicate file name issue


# get all file info available: date, size etc
