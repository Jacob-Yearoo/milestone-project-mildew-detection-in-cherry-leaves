# Project 5 - Mildew Detection in Cherry leaves

## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* I hypothesize that the differences in the cherry leaves, visually, should be indentifiable, if the ML model has enough data to train from
  it should be able to accurately predict if any given cherry leaf is infected or not.
    * this can be validated by designing a Tensorflow neural network to train the ML AI into recognizing the different characteristics of the leaves


## The rationale to map the business requirements to the Data Visualisations and ML tasks
* Business Requirement 1: Data Visualization
  * As a client I would want to display the mean and standard deviation images of cherry leaves that are healthy, and also ones that are infected, so I can visually differentiate the two.
  * As a client I would want to display the mean and standard deviation of a healthy cherry leaf when compared to a leaf infected with powdery mildew, so that I can better understand the visual differences between them.
  * As a client I would like to see an image montage of healthy cherry leaves and infected cherry leaves, so I can visually differentiate cherry leaves.
* Business Requirement 2: Data Prediction
  * As a client i would want to predict if a given cherry leaf is healthy, or if it infected with powdery mildew.
  * As a client I would want to build an ML model that can actually predict from a large dataset that can be provided with more images, that then generates reports on inputed data.


## ML Business Case

* An ML model that could predict any given cherry leaf image and determine if it's infected with  powdery mildew or healthy, based on historical image data.
* It would be a supervised-learning model, classed as a binary classifier.
* The ideal outcome of said model would be to provide a quick and efficient way to identify the health of Cherry Leaves, this could be utilised by environmental agencies and agriclutural bodies alike.
* The model success metrics are:
  * accuracy of at least 97% on the test set.
* Heuristics for identifying Powder Mildew on flora (In our case, specifically Cherry Leaves) may include visual inspection for the characteristic white, powdery growth on the surface of leaves, stems, and other plant parts. Other heuristics may include observation of typical symptoms such as leaf distortion, curling, and yellowing, this is often used in conjunction with labratory testing to confirm the presence of Powdery Mildew
* The training data used to fit the model was provided by the client which includes 4+ thousand images taken by them personally.


## Dashboard Design

### Page 1: Quick Project Summary

* Quick project summary
  * General Information
    * powdery mildew, plant disease of worldwide occurrence that causes a powdery growth on the surface of leaves, buds, young shoots, fruits, and flowers.
    * The white powdery appearance is due to large numbers of microscopic spores borne in chains. These wind-borne spores uniquely do not require free water for germination and infection.
    * If the disease is severe, the mildewed plant parts may be stunted and distorted. Leaves commonly turn yellow and wither, flowers are distorted or fewer in number, and fruit yield and quality are reduced.
  * Project Dataset
    * The available dataset contains 4208 images containing cherry leaves in varying shapes and sizes, half of these are mildew-parasitised and the other half are healthy.
  * Link to additional information
  * Business requirements
    * 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
    * 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

### Page 2: Leaf Visualization

* It will answer business requirement 1
  * Checkbox 1 - Difference between average and variability image
  * Checkbox 2 - Differences between average parasitised and average healthy leaves
  * Checkbox 3 - Image Montage

### Page 3: Mildew Detector

* Business requirement 2 information - "The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew."
* Link to download a set of parasitised and healthy leaf images for live prediction.
* User Interface with a file uploader widget. The user can upload multiple cherry leaf images. It will display the image and a prediction statement, indicating if the leaf is infected with mildew or not and the probability associated with this statement.
* Table with the image name and prediction results.
* Download button to download table.

### Page 4: Project Hypothesis and Validation

* We suspect mildew-infected leaves have clear differences that visually set them apart, typically with an infected leaf, you will see a white powdery fungus.
* An Image Montage shows that typically an infected leaf has white fungus on the surface layer. Average Image and Difference between Averages studies did reveal that healthy cherry leaves are a more vibrant colour and infected ones are more withered and dull.

### Page 5: ML Performance Metrics

* Label Frequencies for Train, Validation and Test Sets
* Model History - Accuracy and Losses
* Model evaluation result


## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Main Data Analysis and Machine Learning Libraries
* Below is a list of the modules and libraries that made the project possible:
  * Numpy
  * Pandas
  * Matplotlib
  * Seaborn
  * Plotly
  * Streamlit
  * Scikit
  * Tensorflow
  * Keras
  * Protobuf

## Credits 

* The Malaria Detector walkthrough project made by Code Institute (linked the project github page [here](https://github.com/Code-Institute-Solutions/WalkthroughProject01/blob/main/README.md)) was a big inspiration and guide for my project due to the general similarities in content.
  * **Any functions or extensive code that I haven't made myself I have commented next to the code snippet on the Jupyter Notebooks**
  * **The Streamlit foundations were not written by me but by the Code Institute team. I adapted the content to fit my requirements.**


### Content 

* The text for the general information on Powdery Mildew (provided on the summary page of the streamlit dashboard) was found on this website (<https://www.britannica.com/science/powdery-mildew>).

## Acknowledgements

* Thank you as always to the Code Institute team for the excellent walkthrough projects, and to the tutor team for their help.
