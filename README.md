#  <img src="https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/1f008b11-bdcd-4a49-8611-13a9f269cdc0" alt="Twitter" width="30px" height="30px"/> Github Metadata Analytics 
<p align='justify'>
Choosing a technology or programming language is still one of the hardest decisions that have to be made internally in software engineering firms. In this school project, we consider a data science approach to distinguish different languages by considering features such as success, collaboration, activity, endangerment, FOSS, etc. as measured by variables such as stars, pull requests, commits, archrivals, licenses.
</p>


# 🧐  Points of Inquiry

In particular, we aim to address the following set of questions

<table border="0">
  <tr>
    <th colspan="2">Descriptive 🔍</th>
  </tr>
  <tr>
    <td colspan="2">1. What is the distribution of the average number of stars over different programming languages? What is the distribution of the average number of stars over time for the top 7 languages in stars?</td>
  </tr>
  <tr>
    <td colspan="2">2. What is the distribution of the most common primary language over time? And what is the distribution of the underlying margin compared to the next most frequent programming language?</td>
  </tr>
  <tr>
    <td colspan="2">3. What is the fraction of repositories without a license? What fraction of those with licenses also have a code of conduct?</td>
  </tr>
  <tr>
    <td colspan="2">4. What are the top three sets of programming languages used together over time? What are some strong association rules that can be drawn from these sets?</td>
  </tr>
  <tr>
    <td colspan="2">5. What is the average size of repositories over time for the top 3 programming languages in terms of pull requests?</td>
  </tr>
  <tr>
    <th colspan="2">Exploratory ⛵</th>
  </tr>
  <tr>
    <td colspan="2">6. What is the correlation between the number of watchers and number of pull requests for each programming language?</td>
  </tr>
  <tr>
    <td colspan="2">7. What databases tend to occur more often with different backend frameworks? What front-end frameworks tend to occur most often with the three most frequent backend frameworks?</td>
  </tr>
  <tr>
    <td colspan="2">8. Is there any association between the number of main branch commits, stars and pull requests, and the primary programming language used in a project?</td>
  </tr>
  <tr>
    <td colspan="2">9. What licenses are associated with what primary programming languages and project sizes?</td>
  </tr>
  <tr>
    <th colspan="2">Inferential 🌎</th>
  </tr>
  <tr>
    <td colspan="2">10. Does the popularity of Javascript generalize to prove that dynamically typed languages are more popular than statically typed ones?</td>
  </tr>
  <tr>
    <td colspan="2">11. If &lt;X&gt; is the language with the most archived repositories that don’t allow forking for the period before 2009 and after 2015, then does this generalize to the whole period (2009 to 2023) regardless whether forking is allowed or not?</td>
  </tr>
  <tr>
    <th colspan="2">Predictive 🔮</th>
  </tr>
  <tr>
    <td colspan="2">12. What is the expected number of pull requests over all Python repositories for the year 2023?</td>
  </tr>
  <tr>
    <td colspan="2">13. What programming language is expected to have the most repos archived in 2023?</td>
  </tr>
</table>

## 📂 Folder Structure
The following is the implied folder structure:
```
.
├── DataFiles
│   ├── dataset.csv
│   ├── test.csv
│   ├── train-val.csv
│   ├── train.csv
│   └── val.csv
├── DataPreparation
│   ├── DataPreperation.ipynb
│   ├── Preprocess.py
│   └── Visualize.py
├── Questions
│   ├── D - Language Commonality
│   │   ├── LanguageCommonality.ipynb
│   │   └── Logic.py
│   ├── D - Language Success
│   │   ├── LanguageSuccess.ipynb
│   │   └── Logic.py
│   ├── D - License Prevalence
│   │   ├── LicensePrevalence.ipynb
│   │   └── Logic.py
│   ├── D - Size & Contribution Effect
│   │   ├── Logic.py
│   │   └── SizeAndContributionEffect.ipynb
│   ├── E - Arbitrary Language Predictors
│   │   ├── ArbitraryLanguagePredictors.ipynb
│   │   └── Logic.py
│   ├── E - Contributions & Watchers
│   │   ├── Contributions & Watchers.ipynb
│   │   └── Logic.py
│   ├── E - Database & Frameworks Correspondence
│   │   ├── Databases&Frameworks.ipynb
│   │   └── Logic.py
│   ├── E - Language Associations
│   │   ├── Language Associations.ipynb
│   │   └── Logic.py
│   ├── E - Licenses, Language & Size
│   │   ├── Licenses, Language & Size.ipynb
│   │   └── Logic.py
│   ├── I - Generalizing Archival Trends
│   │   ├── Generalizing Archival Trends.ipynb
│   │   └── Logic.py
│   ├── I - Generalizing Dynamic Typed Languages
│   │   ├── Generalizing Dynamic Typed Languages.ipynb
│   │   └── Logic.py
│   ├── P - Expected Language Archivals
│   │   ├── ExpectedLanguageArchivals.ipynb
│   │   ├── Logic.py
│   │   └── langs.txt
│   └── P - Expected Python Contributions
│       ├── Expected Python Contributions.ipynb
│       └── Logic.py
├── README.md
├── LICENSE
├── Reports & Dashboard
├── DS Project.pdf
├── DS Proposal.pdf
├── script.py
└── utils.py
```

## 📜 Standards
We have set the following set of working [standards](https://github.com/EssamWisam/Github-Metadata-Analytics/tree/main/MLDIR.md/) as we were undertaking the project. If you wish to contribute for any reason then please respect such standards.


## 🚀 Pipeline

<div align="center">
<img width="731" alt="image" src="https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/b3ac18c6-1a30-410d-9206-593168add1d6">
</div>

We harnessed the data science cycle for each of the questions. This includes an epicycle that applies in each stage. As in the standards, each notebook corresponding to a question was structured into the 5 stages of the cycle. We also logged our iterations for the epicycle in each stage using a table under that stage in the notebook.

To optimize the cycle over different questions, we also employed a single data preparation stage to include most of the common required processing over different questions.

## 🚁 Running the Project

```python
pip install requirements.txt
# To explore the cycle for any question, simply head to its notebook. 
```

In the rest of the README, we will explore the data preparation stage, the cycle for 2 or 3 questions and some dashboards!

## 🍳 Data Preparation

Our dataset was Kaggle's [Github Metadata dataset](https://www.kaggle.com/datasets/pelmers/github-repository-metadata-with-5-stars). An observation from the dataset is shown below
```json
{
  "owner": "pelmers",
  "name": "text-rewriter",
  "stars": 13,
  "forks": 5,
  "watchers": 4,
  "isFork": false,
  "isArchived": false,
  "languages": [ { "name": "JavaScript", "size": 21769 }, { "name": "HTML", "size": 2096 }, { "name": "CSS", "size": 2081 } ],
  "languageCount": 3,
  "topics": [ { "name": "chrome-extension", "stars": 43211 } ],
  "topicCount": 1,
  "diskUsageKb": 75,
  "pullRequests": 4,
  "issues": 12,
  "description": "Webextension to rewrite phrases in pages",
  "primaryLanguage": "JavaScript",
  "createdAt": "2015-03-14T22:35:11Z",
  "pushedAt": "2022-02-11T14:26:00Z",
  "defaultBranchCommitCount": 54,
  "license": null,
  "assignableUserCount": 1,
  "codeOfConduct": null,
  "forkingAllowed": true,
  "nameWithOwner": "pelmers/text-rewriter",
  "parent": null
}
```

Our data preparation module was used for all questions and supported the following:
- Reading specific splits of the data (train, test, val)
- Reading specific columns of the data (by name or type)
- Breaking down composite columns
- Deleting useless columns
- Handling missing values
- Handling outliers by multiple imputation
- Extracting time features

#### Basic Feature Analysis
<table style="width:50%; border-collapse: collapse; font-size: 16px; text-align:center; padding: 10px; border: 1px solid #fff; white-space: nowrap;"><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">Feature</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">Type</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">Uniques</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">Missing</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">Outliers</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">stars</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Numerical</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">2033</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">9.45%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">forks</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Numerical</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">1156</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">7.32%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">watchers</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Numerical</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">479</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">6.19%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">isArchived</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Binary</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">2</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">4.97%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">diskUsageKb</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Numerical</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">39921</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">13.19%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">pullRequests</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Numerical</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">1452</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">11.45%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">primaryLanguage</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Categorical</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">377</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">8.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">createdAt</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Date</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">209558</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">defaultBranchCommitCount</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Numerical</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">4415</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">8.77%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">license</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Categorical</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">44</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">47.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">assignableUserCount</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Numerical</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">783</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">15.36%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">codeOfConduct</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Categorical</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">8</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">96.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">languagesUsed</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Composite</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">37808</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">languagesSizes</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Composite</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">164696</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0%</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">isLicense</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Binary</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">2</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0.0%</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">0%</td></tr> </table>

After using domain knowledge to handle missing values and using multiple imputation with stochastic gradient descent, we obtain the following violin plots

![image](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/f987c3bf-aabd-437d-afb7-1ceb6654dcf1)

Myriad of other plots, statistics, insights for each and epicycle logging are present in the [demonstration notebook](https://github.com/EssamWisam/Github-Metadata-Analytics/blob/main/DataPreparation/DataPreperation.ipynb) which like all Github, should be viewed in dark mode.

Now let's have a cursory glance over some of the questions. Note that epicycle details and in-depth insights will rather be found in the corresponding notebook or the [report](https://github.com/EssamWisam/Github-Metadata-Analytics/blob/main/Report.pdf).

## 🔒 License Prevalence
### 🙋 Stating Questions
```
What is the fraction of repositories without a license?
What fraction of those with licenses also have a code of conduct?
```
### ⛵ Exploratory Data Analytics

#### The Available Licenses

![image](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/48382d8d-365e-4d03-922d-4c31d31dda81)

#### Top 10 Licenses

![image](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/5196ee0c-8684-4ccb-8884-7418f7a5d27d)

### 🗿 Model Building
![image](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/1d967188-9ed9-4f07-af55-92cb9c758268)

### 💡 Result Interpretation & Communicating Results

<table border="0">
  <tr>
    <th>License Prevalence</th>
  </tr>
  <tr>
    <td>&#10022; Although repos don't require a license by default, about one in every two repos has a license.</td>
  </tr>
  <tr>
    <td>&#10022; It means that about half of the repos are protected by the default strict copyright law. Without explicit permission, only viewing the code is legal.</td>
  </tr>
  <tr>
    <td>&#10022; This does not encourage FOSS development, one of the main goals of GitHub.</td>
  </tr>
  <tr>
    <th>Code of Conduct</th>
  </tr>
  <tr>
    <td>&#10022; The absolute majority of repos do not have a code of conduct; there is no option to add it at the time of repo creation.</td>
  </tr>
  <tr>
    <td>&#10022; Although, to organize collaboration and interaction in a community, a code of conduct is important; it's only used for a tiny fraction of repos.</td>
  </tr>
  <tr>
    <td>&#10022; Github may encourage using it by adding it as an option at the time of repo creation.</td>
  </tr>
</table>

## 🔮 Arbitrary Language Predictors
### 🙋 Stating Questions
```
 Is there any association between the number of main branch commits, stars and pull requests, and
 the primary programming language used in a project?
```
### ⛵ Exploratory Data Analytics

#### There seems to be no precise distinctive association

![image](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/f7c00501-6b8b-4d1e-92d0-a92a54bdf506)

#### Not even from a distribution prespective

![image](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/1084d816-7a1e-402a-bba8-07707a65f60f)

#### Let's rather look for a high-level association

![image](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/aedeab0f-2f36-4f61-852e-86dbb3deb716)


### 🗿 Model Building
Based on EDA for high-level association, we make the following claims:

I. Stars don’t really differ from language to language

II. TypeScript can be regarded as the most active language

III. C can be regarded as the least collaborative language

#### Check whether CLT holds before proceeding with hypothesis testing
![image](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/66f9aa35-604f-4e6f-b5ba-426b0ec59ef5)

#### Test Claim I

<table style="width:50%; border-collapse: collapse; font-size: 16px; text-align:center; padding: 10px; border: 1px solid #fff; white-space: nowrap;"><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">JavaScript</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">Python</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">Undetected</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">Java</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">C++</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">TypeScript</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">PHP</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">C</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">C#</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">HTML</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 15.5 > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 15.5 > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 15.5 > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 15.5 > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 15.5 > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 15.5 > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 15.5 > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 15.5 > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 15.5 > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 15.5 > 0</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 19.5 < 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 19.5 < 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 19.5 < 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 19.5 < 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 19.5 < 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 19.5 < 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 19.5 < 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 19.5 < 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 19.5 < 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ - 19.5 < 0</td></tr> </table>

#### Test Claim II

<table style="width:50%; border-collapse: collapse; font-size: 16px; text-align:center; padding: 10px; border: 1px solid #fff; white-space: nowrap;"><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">JavaScript</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">Python</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">Undetected</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">Java</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">C++</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">PHP</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">C</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">C#</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff; white-space: nowrap;">HTML</td></tr><tr><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ(TypeScript) - μ(JavaScript) > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ(TypeScript) - μ(Python) > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ(TypeScript) - μ(Undetected) > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ(TypeScript) - μ(Java) > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ(TypeScript) - μ(C++) > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ(TypeScript) - μ(PHP) > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ(TypeScript) - μ(C) > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ(TypeScript) - μ(C#) > 0</td><td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff; white-space: nowrap;">Accept:
 μ(TypeScript) - μ(HTML) > 0</td></tr> </table>

#### Test Claim III

|               JavaScript         | Python | Undetected | Java | C++ | TypeScript | PHP | C# | HTML |
|----------------------------------|--------|------------|------|-----|------------|-----|----|------|
| Accept: μ(C) - μ(JavaScript) < 0 | Accept: μ(C) - μ(Python) < 0 | Accept: μ(C) - μ(Undetected) > 0 | Accept: μ(C) - μ(Java) < 0 | Cannot Reject: μ(C) - μ(C++) > 0 | Accept: μ(C) - μ(TypeScript) < 0 | Accept: μ(C) - μ(PHP) < 0 | Accept: μ(C) - μ(C#) < 0 | Accept: μ(C) - μ(HTML) < 0 |


### 💡 Result Interpretation & Communicating Results

| Insights                                                                                               |
|-------------------------------------------------------------------------------------------------------|
| ✦ We cannot predict the language given stars, pull requests, and commits. In other words, no strong or precise association |
| ✦ Languages seem to be equally successful as their stars are not significantly different on average   |
| ✦ There is a high-level association for commits; for instance, TypeScript can be regarded as the most active language |
| ✦ There is a high-level association for pull requests; for instance, C (& C++) can be regarded as the least collaborative language |


## 🗃️ Expected Language Archivals
### 🙋 Stating Questions
```
What programming language is expected to have the most repos archived in 2023?
```
### ⛵ Exploratory Data Analytics

#### Archival Rate for Most Archived Language Every Year

![image](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/33334562-e533-40b1-9253-ac7068367ce5)

#### Monthly Arhivals for C

![image](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/1fa9a980-34c7-4250-9c93-95f8e88f42e2)

Does not seem to be leaving us soon.

### 🗿 Model Building

#### Training a Time-series Forecasting Model per Language 

![image](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/af16876e-7b8c-4dea-a324-a64d2f87149b)

#### Predicting for 2023 for each Language

![image](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/ce69da0e-8fcc-4eff-826f-c0d0e6706ab0)


### 💡 Result Interpretation & Communicating Results

| Insights                                                                                               |
|-------------------------------------------------------------------------------------------------------|
| ✦ Assembly is expected to be the most archived language in 2023. It makes sense as it's one of the oldest languages around |
| ✦ Different languages seem to follow trends of different complexity. The trend is mostly decreasing for modern popular languages but stochastic for older ones |
| ✦ C++ and C seem to be safer than expected, which can be justified by their use in embedded systems, operating systems, and libraries for other languages |
| ✦ Niche languages like HCL and Solidity don't seem to be at risk, but they probably took a big hit earlier |
| ✦ The endangerment of languages like Ruby and Lua is expected. Lua has recently been listed in a popular list of the worst languages, and Ruby stopped shining after the rise of Python and JavaScript |


#### This demos just 3 of the 13 questions; check the notebooks and the report for more!

## 📊 Some Dashboards

![Dashboard 1 (1)](https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/ce72feee-0a9c-426a-aceb-0f92b4becc5d)

<img width="1093" alt="image" src="https://github.com/EssamWisam/Github-Metadata-Analytics/assets/49572294/25ba0ee6-caec-44da-a0c1-50e32380062c">

## 👥 Collaborators
<!-- readme: contributors -start -->
<!-- readme: contributors -end -->



<h2 align="center"> 💖 Thank you. 💖 </h2>

