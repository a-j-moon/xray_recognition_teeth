# xray_recognition_teeth

This is a project on training a model using convolutional neural networking to identify carious lesions on dental X-rays, from a bioinformatics approach. The project is still currently ongoing, as scripts are being written.

A dataset containing 2,158 periapical (PA) x-ray images was downloaded from the data science company 'Kaggle'. To set up the environment, the following packages were imported into Python3: datetime, pathlib, NumPy, pandas, matplotlib, and TensorFlow. Through Python3, a Jupyter notebook was created and the dataset was imported.

Before model training, two arrays were created 'cav_files' and 'no_cav_files'. Next, some transformations had to be done. All anterior x-ray images (which are taken vertically, not horizontally like the pre-molars and back) had to be rotated 90 degrees so that they would sit horizontally, and all images were resized to be 660x844. 

Next, to begin creating the model 'keras' was used. To begin training the model, a small sample of 10 images are used to test the output, and alterations are made as needed.

X-rays are crucial to dentistry. They allow the dentist to see through the teeth, between the teeth, and below the crown of the tooth. X-rays can be used to detect decay, bone loss, and map the patient's anatomy. This is the only way to fully get a picture of the state that the patient's teeth are in. Science has allowed for all of the technology used in dentistry to be possible. 
