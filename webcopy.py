from pywebcopy import save_website
import sys

kwargs = {'project_name': 'classcentral'}

print("starting")
save_website(
    url='https://shantoroy.com/security/website-cloning-and-rerunning-in-localhost/',
    project_folder='C://Users//KK//Dropbox//Dev//Projects//python//hindi//scrap',    
    **kwargs
)
print("Done")