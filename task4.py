import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

headings=[f'Task{i}' for i in range(1,5)]
cls_rep=pd.read_csv('.\media\Task2\classification_report.csv',index_col='Unnamed: 0')
activity=pd.read_csv('.\media\Task3\Activity.csv')
duration=pd.read_csv('.\media\Task3\duration.csv')


st.title('ResoluteAI Assignment Reports')

st.html(f'<h2>{headings[0]}</h2>')
st.html('<h4>Clustering Task</h4>')
st.write('''
         Scaled the dataset and then 
         performed PCA over the dataset. 
         The following results were obtained.
         ''')
st.image(".\media\Task1\pca.png")
st.html('''
        <p>
          <i>Insights</i>: 
          We need a minimum of 1 column to get a maximum 
          silhouette score and maximum of 15 columns to get 
          a minimum silhouette score and maximum variance.              
        </p>
        ''')
st.html('<br/>')
st.html('''
        <p>
        So I decided to select 3 columns and it gave a 
        silhouette score of 37 percentage for a k value of 5 
        which was observed from the image below.
        </p>
        ''')
st.image('.\media\Task1\download.png')
st.html('''
         <p>
          <i>Observation</i>:
          It was observed that when the first column had a 
          negative value it classified it as a 3rd cluster,
          while a negative value at first column and 
          last column was given as 1st cluster.
          Negative value at second and last became 2nd cluster.
        </p>
        ''')
st.html('<br/><br/>')


st.html(f'<h2>{headings[1]}</h2>')
st.html('<h4>Classification Task</h4>')
st.html('''
         <p>
         In the classification task the target column was chosen
         as the target variable .
         Since there were 34 unique variables both of which were 
         having either A or B followed by nymerical value.
         I decided to make it a binary classification problem
         by eliminating the numbers and kept the alphabets A and B 
         respectively. 
        This was done to avoid overfitting.
         </p>
''')
st.html('<br/>')
st.html('''
        <p>
        The classification model that was chosen for this task was
        Random Forest as Decision Tree is vulnerable to overfitting 
        and it uses Bagging technique which is an ensemnle model
        which is used to reduce variance in a noisy dataset, as 
        outlier removal wasn't done on it
        </p>
''')
st.html('<br/>')
st.html('''<p>
        With the help of GridSearchCV Hyperparameter tuning
        model, it was observed that :
        <ul>
        <li>'max_depth': None</li> 
        <li>'min_samples_leaf': 1</li> 
        <li>'min_samples_split': 5</li> 
        <li>'n_estimators': 200</li>
        </ul>
        The above hyperparameter gave an accuracy of 99.4 percent.
        (Further details can be found in images below.)
        </p>''')
st.html('<h3>Classification Report for Random Forest Classification</h3>')
st.dataframe(cls_rep)
st.html('<h3>Confusion Matrix for Random Forest Classification</h3>')
st.image('.\media\Task2\confusion_matrix.png')
st.html('<br/><br/>')


st.html(f'<h2>{headings[2]}</h2>')
st.html('<h4>Activity Task</h4>')
st.html('<p>Used raw data to:</p>')
st.html('''<p>
            Generate Datewise total duration for each inside and outside
        </p>''')
st.image('./media/Task3/duration.png')
st.dataframe(duration)
st.html('''<p>
            Generate Datewise number of picking and placing activity done.
        </p>''')
st.image('./media/Task3/duration.png')
st.dataframe(activity)
st.html('<br/><br/>')

st.html(f'<h2>{headings[3]}</h2>')
st.html('''
        <p>
        <b>All of these were created using Streamlit.
        You can find the codes in my Github repo.
        <b>
        </p>''')