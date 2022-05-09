FROM python
# copy everything in this directory (that is what the dot represents) into the containter path of /usr/src/app
COPY .  /usr/src/app
# set working directory to /usr/src/app (similar to doing cd in terminal)
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
# run this command once everything has been installed    
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
