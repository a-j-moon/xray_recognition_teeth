# xray_recognition_teeth

This is a project on training a model using neural networking to identify carious lesions on dental X-rays, from a bioinformatics approach. The project is still currently ongoing, as scripts are being written.

There are two main datasets, one that contains panoramic X-rays of healthy teeth 'healthy', and another than contains panoramic X-rays that have at least one carious lesions 'carious'. Combined, there is approximately 400 images. To begin training the model, periapical (PA) X-rays are being used as a small sample to test the output. 

The neural network is constructed by inputing nodes, such as shadows, lights, and depth, to create different conditions. There will then be a hidden layer to add weight to some of the inputs, and then the output will categorize the image as 'healthy' or 'carious'. The first goal will be to create a model that recognizes the darker areas of the X-ray, then detect carious lesions, and an advanced output would be a model that shows where the carious lesions are. 

X-rays are crucial to dentistry. They allow the dentist to see through the teeth, between the teeth, and below the crown of the tooth. X-rays can be used to detect decay, bone loss, and map the patient's anatomy. This is the only way to fully get a picture of the state that the patient's teeth are in. Science has allowed for all of the technology used in dentistry to be possible. 
