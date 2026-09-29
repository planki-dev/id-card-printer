[app]

# (str) Title of your application
title = ID Card Falt-Drucker Pro

# (str) Package name
package.name = idcardfaltprinter

# (str) Package domain (needed for android packaging)
package.domain = org.idcardprinter

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,html

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3, kivy, flask, reportlab, jinja2, werkzeug, itsdangerous, click

# (str) Supported orientations (valid options are: landscape, portrait, portrait-reverse, landscape-reverse)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
#android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug and above)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
