# ImageTool #


- Prerequest : conda environment with Keras
- Upload a picture and use programe in project 'Image Retrieval Engine Based on Keras'  to rank picture.

## references ##
- [Image Retrieval Engine Based on Keras](https://github.com/willard-yuan/flask-keras-cnn-image-retrieval)  
- [How to build flask server in Windows](https://gama79530.github.io/whole_page_ver/Flask.html)

## Note ##
You may run 'ImageTool' flask app and 'Image Retrieval Engine Based on Keras' app in <font color="red" >**different**</font> enviornment. You should prepare an enviornment in which 'Image Retrieval Engine Based on Keras' app can execute by yourself. Then modify the following config.

Config Needed to modified : ImageTool/ImageTool/\_\_init\_\_.py  
(The default setting execute 'Image Retrieval Engine Based on Keras' app in conda enviornment called ImageTool)
	
	# Modifiy this to fit your computer setting
	CONDA_ACTIVATE = 'C:\\Python\\Anaconda-3.7\\Scripts\\activate ImageTool'  


## How to start flask server ##
I've uploaded a venv in project. The following shows **'How to execute ImageTool flask app in this venv'**  
(This venv may not work on your server, but you can create a venv with flask by using python and pip easily) 

	cd "project_dir"
	venv/Scripts/activate
	set FLASK_APP=ImageTool
	set FLASK_ENV=development 

	REM How to build index
	python -m flask init-img-db

	REM How to start dev server
	python -m flask run  --host=0.0.0.0 --port=5000

## Test link(you should change server ip and port number in url) : ##
 
http://_server\_ip_**:**_port\_num_  
or  
http://localhost:_port\_num_