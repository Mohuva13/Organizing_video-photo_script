import os
import sys
import os.path, time
import subprocess
#Import os libraries

input_arg = sys.argv #Input first and second directory
def explore(type, path):
    count_dict = {}
    type = str(type)
    type = type.lower()
    for root, dirs, files in os.walk(str(path)):
        for file in files:
            file0 = file.lower()
            if file0.endswith(f".{type}"):
                if root in count_dict:
                    count_dict[root+'/'+str(file)] = type
                else:
                    count_dict[root+'/'+str(file)] = type
    return (count_dict)

#for photos
jpg = explore("jpg",input_arg[1])
png = explore("png",input_arg[1])
jpeg = explore("jpeg",input_arg[1])
#for videos
mov = explore("mov",input_arg[1])
wmv = explore("wmv",input_arg[1])
mkv = explore("mkv",input_arg[1])
mpeg = explore("mpeg",input_arg[1])
x3gp = explore("3gp",input_arg[1])
avi = explore("avi",input_arg[1])
mp4 = explore("mp4",input_arg[1])
all_type_list = [jpg, png, jpeg, mov, wmv, mkv, mpeg, x3gp, avi, mp4]
date_created = {}
for xc in all_type_list:
    if str(xc) != "{}":
        list_xc = list(xc.keys())
        for ty in list_xc:
            file_date = time.ctime(os.path.getctime(ty))
            file_date = str(file_date)
            date_created[ty] = int(file_date[-4:])

#mkdir folder and copy media
list_year = list(date_created.values())
list_year = list(set(list_year))
parent_dir = input_arg[2]
for make_folder_year in list_year:
    path_year = os.path.join(parent_dir, str(make_folder_year))
    os.mkdir(path_year)
    if str(png) != "{}" or str(jpg) != "{}" or str(jpeg) != "{}":
        path_photo = os.path.join(parent_dir, str(make_folder_year),"photos")
        os.mkdir(path_photo)
        list_pic = [png, jpeg,jpg]
        list_pic_file = []
        for ds in list_pic:
            if str(ds) != "{}":
                ds = list(ds.keys())
                for gf in ds:
                    list_pic_file.append(gf)
        for find_year_photos in list_pic_file:
            if date_created[find_year_photos] == make_folder_year:
                src = find_year_photos
                dst = path_photo
                cmd = 'cp -r "%s" "%s"' % (src, dst)
                subprocess.call(cmd, shell=True)

    if str(mov) != "{}" or str(wmv) != "{}" or str(mkv) != "{}" or str(mpeg) != "{}" or str(x3gp) != "{}" or str(avi) != "{}" or str(mp4) != "{}":
        path_movie = os.path.join(parent_dir, str(make_folder_year), "videos")
        os.mkdir(path_movie)
        list_movie = [mov, wmv, mkv, mpeg, x3gp, avi, mp4]
        list_movie_file = []
        for ms in list_movie:
            if str(ms) != "{}":
                ms = list(ms.keys())
                for bf in ms:
                    list_movie_file.append(bf)
        for find_year_movies in list_movie_file:
            if date_created[find_year_movies] == make_folder_year:
                src = find_year_movies
                dst = path_movie
                cmd = 'cp -r "%s" "%s"' % (src, dst)
                subprocess.call(cmd, shell=True)