{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "331350c3-32c4-469d-a0e3-c3fbe4c55bf6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0e0b27dd-19ae-4407-b3bd-505997ba5d13",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>job</th>\n",
       "      <th>marital</th>\n",
       "      <th>education</th>\n",
       "      <th>default</th>\n",
       "      <th>balance</th>\n",
       "      <th>housing</th>\n",
       "      <th>loan</th>\n",
       "      <th>contact</th>\n",
       "      <th>day</th>\n",
       "      <th>month</th>\n",
       "      <th>duration</th>\n",
       "      <th>campaign</th>\n",
       "      <th>pdays</th>\n",
       "      <th>previous</th>\n",
       "      <th>poutcome</th>\n",
       "      <th>y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>30</td>\n",
       "      <td>unemployed</td>\n",
       "      <td>married</td>\n",
       "      <td>primary</td>\n",
       "      <td>no</td>\n",
       "      <td>1787</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>cellular</td>\n",
       "      <td>19</td>\n",
       "      <td>oct</td>\n",
       "      <td>79</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>33</td>\n",
       "      <td>services</td>\n",
       "      <td>married</td>\n",
       "      <td>secondary</td>\n",
       "      <td>no</td>\n",
       "      <td>4789</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>cellular</td>\n",
       "      <td>11</td>\n",
       "      <td>may</td>\n",
       "      <td>220</td>\n",
       "      <td>1</td>\n",
       "      <td>339</td>\n",
       "      <td>4</td>\n",
       "      <td>failure</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>35</td>\n",
       "      <td>management</td>\n",
       "      <td>single</td>\n",
       "      <td>tertiary</td>\n",
       "      <td>no</td>\n",
       "      <td>1350</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>cellular</td>\n",
       "      <td>16</td>\n",
       "      <td>apr</td>\n",
       "      <td>185</td>\n",
       "      <td>1</td>\n",
       "      <td>330</td>\n",
       "      <td>1</td>\n",
       "      <td>failure</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>30</td>\n",
       "      <td>management</td>\n",
       "      <td>married</td>\n",
       "      <td>tertiary</td>\n",
       "      <td>no</td>\n",
       "      <td>1476</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>unknown</td>\n",
       "      <td>3</td>\n",
       "      <td>jun</td>\n",
       "      <td>199</td>\n",
       "      <td>4</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>59</td>\n",
       "      <td>blue-collar</td>\n",
       "      <td>married</td>\n",
       "      <td>secondary</td>\n",
       "      <td>no</td>\n",
       "      <td>0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>unknown</td>\n",
       "      <td>5</td>\n",
       "      <td>may</td>\n",
       "      <td>226</td>\n",
       "      <td>1</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "      <td>unknown</td>\n",
       "      <td>no</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age          job  marital  education default  balance housing loan  \\\n",
       "0   30   unemployed  married    primary      no     1787      no   no   \n",
       "1   33     services  married  secondary      no     4789     yes  yes   \n",
       "2   35   management   single   tertiary      no     1350     yes   no   \n",
       "3   30   management  married   tertiary      no     1476     yes  yes   \n",
       "4   59  blue-collar  married  secondary      no        0     yes   no   \n",
       "\n",
       "    contact  day month  duration  campaign  pdays  previous poutcome   y  \n",
       "0  cellular   19   oct        79         1     -1         0  unknown  no  \n",
       "1  cellular   11   may       220         1    339         4  failure  no  \n",
       "2  cellular   16   apr       185         1    330         1  failure  no  \n",
       "3   unknown    3   jun       199         4     -1         0  unknown  no  \n",
       "4   unknown    5   may       226         1     -1         0  unknown  no  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv(\"C:/Users/mamun/OneDrive/Desktop/Data_science_project/ML Zoomcamp/bank.csv\",sep=',')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "630a1b05-3144-4db5-8428-819a21a02684",
   "metadata": {},
   "source": [
    "### Question 1\n",
    "* Install Pipenv\n",
    "* What's the version of pipenv you installed?\n",
    "* Use --version to find out"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d68a192c-c356-479a-8d28-342dda9fe612",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pipenv, version 2023.10.3\n"
     ]
    }
   ],
   "source": [
    "!pipenv --version"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6acf6642-9b03-47fd-8a64-24f3256fd45b",
   "metadata": {},
   "source": [
    "### Question 2\n",
    "* Use Pipenv to install Scikit-Learn version 1.3.1\n",
    "* What's the first hash for scikit-learn you get in Pipfile.lock?\n",
    "* Note: you should create an empty folder for homework and do it there."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a2032c78-574c-405b-8945-eb324acfe217",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Installing scikit-learn==1.3.1...\n",
      "Resolving scikit-learn==1.3.1...\n",
      "[    ] Installing...\n",
      "Installation Succeeded\n",
      "[    ] Installing scikit-learn...\n",
      "[    ] Installing scikit-learn...\n",
      "\n",
      "Installing dependencies from Pipfile.lock (98d9d9)...\n",
      "To activate this project's virtualenv, run pipenv shell.\n",
      "Alternatively, run a command inside the virtualenv with pipenv run.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.\n"
     ]
    }
   ],
   "source": [
    "!pipenv install scikit-learn==1.3.1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3a371fe-9df5-4a73-bf50-5fe2e21a1a80",
   "metadata": {},
   "source": [
    "first hash for scikit-learn : sha256\": \"e0d12a0331eb3926e2e7c7c37be9118ab3619b518475b3c3897cdb40da98d9d9\""
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9971cfeb-a166-48bc-8c0e-72c64605a1f9",
   "metadata": {},
   "source": [
    "### Question - 3"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d760d629-3b71-48b7-aa3c-1a19e8155ebb",
   "metadata": {},
   "source": [
    "PREFIX=https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2023/05-deployment/homework\n",
    "* wget $PREFIX/model1.bin\n",
    "* wget $PREFIX/dv.bin\n",
    "* Write a script for loading these models with pickle\n",
    "* Score this client:\n",
    "{\"job\": \"retired\", \"duration\": 445, \"poutcome\": \"success\"}\n",
    "* What's the probability that this client will get a credit?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f187e27f-e810-4aa6-a21b-ef962bc02eb3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "# Define the URL for the files\n",
    "url_prefix = \"https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2023/05-deployment/homework\"\n",
    "model_url = f\"{url_prefix}/model1.bin\"\n",
    "dv_url = f\"{url_prefix}/dv.bin\"\n",
    "\n",
    "# local file names to save the downloaded files\n",
    "model_filename = \"model1.bin\"\n",
    "dv_filename = \"dv.bin\"\n",
    "\n",
    "# Download the model1.bin file\n",
    "response = requests.get(model_url)\n",
    "with open(model_filename, 'wb') as file:\n",
    "    file.write(response.content)\n",
    "\n",
    "# Download the dv.bin file\n",
    "response = requests.get(dv_url)\n",
    "with open(dv_filename, 'wb') as file:\n",
    "    file.write(response.content)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f3c699fa-5c67-4fb0-99f4-c1c9481da51d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Probability of getting credit: 0.902\n"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "\n",
    "# Load the scikit-learn model\n",
    "with open('model1.bin', 'rb') as model_file:\n",
    "    scikit_model = pickle.load(model_file)\n",
    "\n",
    "# Load the label encoder (dv.bin) to transform input data\n",
    "with open('dv.bin', 'rb') as encoder_file:\n",
    "    dv = pickle.load(encoder_file)\n",
    "\n",
    "# Define the input data\n",
    "input_data = {\n",
    "    \"job\": \"retired\",\n",
    "    \"duration\": 445,\n",
    "    \"poutcome\": \"success\"\n",
    "}\n",
    "\n",
    "# Transform the input data using the label encoder\n",
    "input_data_transformed = dv.transform([input_data])\n",
    "\n",
    "# Make a probability prediction\n",
    "probability = scikit_model.predict_proba(input_data_transformed)\n",
    "\n",
    "# Get the probability of getting a credit (class 1)\n",
    "probability_of_getting_credit = probability[0][1]\n",
    "\n",
    "print(f\"Probability of getting credit: {probability_of_getting_credit:.3f}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "33ce3870-c533-4c18-96cc-e8d2c3bd84fe",
   "metadata": {},
   "source": [
    "### Question-4\n",
    "Now let's serve this model as a web service\n",
    "* Install Flask and gunicorn (or waitress, if you're on Windows)\n",
    "* Write Flask code for serving the model\n",
    "* Now score this client using requests:\n",
    "* url = \"YOUR_URL\"\n",
    "* client = {\"job\": \"unknown\", \"duration\": 270, \"poutcome\": \"failure\"}\n",
    "requests.post(url, json=client).json()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "460b0107-9332-4dee-bdbb-6ea2f0a87c17",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: Flask in c:\\users\\mamun\\onedrive\\desktop\\data_science_project\\ml zoomcamp\\myenv\\first_virtual_project\\myenv\\lib\\site-packages (3.0.0)\n",
      "Requirement already satisfied: gunicorn in c:\\users\\mamun\\onedrive\\desktop\\data_science_project\\ml zoomcamp\\myenv\\first_virtual_project\\myenv\\lib\\site-packages (21.2.0)\n",
      "Requirement already satisfied: Werkzeug>=3.0.0 in c:\\users\\mamun\\onedrive\\desktop\\data_science_project\\ml zoomcamp\\myenv\\first_virtual_project\\myenv\\lib\\site-packages (from Flask) (3.0.0)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\mamun\\onedrive\\desktop\\data_science_project\\ml zoomcamp\\myenv\\first_virtual_project\\myenv\\lib\\site-packages (from Flask) (3.1.2)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\users\\mamun\\onedrive\\desktop\\data_science_project\\ml zoomcamp\\myenv\\first_virtual_project\\myenv\\lib\\site-packages (from Flask) (2.1.2)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\users\\mamun\\onedrive\\desktop\\data_science_project\\ml zoomcamp\\myenv\\first_virtual_project\\myenv\\lib\\site-packages (from Flask) (8.1.7)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\users\\mamun\\onedrive\\desktop\\data_science_project\\ml zoomcamp\\myenv\\first_virtual_project\\myenv\\lib\\site-packages (from Flask) (1.6.3)\n",
      "Requirement already satisfied: packaging in c:\\users\\mamun\\onedrive\\desktop\\data_science_project\\ml zoomcamp\\myenv\\first_virtual_project\\myenv\\lib\\site-packages (from gunicorn) (23.2)\n",
      "Requirement already satisfied: colorama in c:\\users\\mamun\\onedrive\\desktop\\data_science_project\\ml zoomcamp\\myenv\\first_virtual_project\\myenv\\lib\\site-packages (from click>=8.1.3->Flask) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\mamun\\onedrive\\desktop\\data_science_project\\ml zoomcamp\\myenv\\first_virtual_project\\myenv\\lib\\site-packages (from Jinja2>=3.1.2->Flask) (2.1.3)\n"
     ]
    }
   ],
   "source": [
    "!pip install Flask gunicorn\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "789c3cdc-fe8e-443f-9614-7e9aee60bce3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "import pickle\n",
    "\n",
    "# Load the scikit-learn model and label encoder\n",
    "with open('model1.bin', 'rb') as model_file:\n",
    "    scikit_model = pickle.load(model_file)\n",
    "with open('dv.bin', 'rb') as encoder_file:\n",
    "    dv = pickle.load(encoder_file)\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    try:\n",
    "        data = request.json\n",
    "        input_data_transformed = dv.transform([data])\n",
    "        probability = scikit_model.predict_proba(input_data_transformed)\n",
    "        probability_of_getting_credit = probability[0][1]\n",
    "        return jsonify({'probability_of_getting_credit': probability_of_getting_credit})\n",
    "    except Exception as e:\n",
    "        return jsonify({'error': str(e)})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e8494055-5198-4227-81d3-5f47c27b56a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d887a357-f194-42c4-bca2-38761c010270",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
