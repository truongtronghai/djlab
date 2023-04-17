# This version is Docker of lab for DRF but with changing setting folder to 'config' instead of project name as default
# When changing to config folder, we need to change all names of project in setting.py file to "config".
# Reading file Dockerfile to know how to change folder project name to config
# NOTE: after change the folder of settings, we MUST use env variable to pass env variable DJANGO_SETTINGS_MODULE (watching file .env for detail)

# Command to run docker: docker run -dp 80:8000 --name drflab --env-file .env --volume $(pwd):/drfapp drflabimg
