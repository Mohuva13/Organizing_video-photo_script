# Organizing_video-photo_script

Python script for copy your videos and photos by year

# To use

1- Open your terminal

2- First enter directory of your media and then enter directory where you want the media to be copied ( between quotation )


* e.g.,

> $ python3 **Org_copy.py** \"\~/home/Documents\" \"\~/home/Travel Memories\"



# Befor and after using script:

```
src_folder
├── IMG_2235.jpg   [modified time: 2018/01/28]
├── travel_photos
│   ├── 2018-11-09_11-27-14.3gp
│   ├── IMG_20171017_052418.jpg
│   ├── 20180311_214539.JPG
│   ├── IMG_2237.jpg   [modified time: 2018/02/21]
│   └── note.txt
└── vid1
    ├── images
    │   └── IMG_2014-01-12.JPG
    └── VID_20170425_184731.mp4
```



```
dst_folder
├── 2014
│   └── photos
│       └── IMG_2014-01-12.JPG
├── 2017
│   ├── photos
│   │   └── IMG_20171017_052418.jpg
│   └── videos
│       └── VID_20170425_184731.mp4
└── 2018
    ├── photos
    │   ├── 20180311_214539.JPG
    │   ├── IMG_2235.jpg
    │   └── IMG_2237.jpg 
    └── videos
        └── 2018-11-09_11-27-14.3gp
```
