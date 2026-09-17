## Lean Six Sigma with Python — Kruskal Wallis Test 👷
*How to replace Minitab with Python to perform the Kruskal-Wallis Test, evaluating the impact of training on warehouse operators’ productivity*

<p align="center">
  <img align="center" src="https://miro.medium.com/max/1280/1*uCzCpATHdoX2PRHeigsEHw.png">
</p>

Lean Six Sigma (LSS) is a method based on a stepwise approach to process improvements. This approach usually follows five steps. 
(Define, Measure, Analyse, Improve and Control) for improving existing process problems with unknown causes.

### Youtube Video
Find in the link below a short animated video to explain the concept behind this solution
<div align="center">
  <a href="https://www.youtube.com/watch?v=Voaq0l39LuE"><img src="https://github.com/samirsaci/lss-kruskal-wallis/blob/main/thumbnail.webp" alt="Explainer Video Link"></a>
</div>

### Article
In this [Article](https://www.samirsaci.com/lean-six-sigma-with-python-kruskal-wallis-test/), we will explore how Python can 
Replace Minitab (Software widely used by LSS experts) in the Analysis step to test hypotheses and 
understand what could improve the performance metrics of a specific process.

### Scenario
You are the Continuous Improvement Manager of a Distribution Centre (DC) for an iconic Luxury Maison focusing on Fashion, Fragrances and Watches.
The warehouse receives garments that require final assembling and value-added service (VAS) during the inbound process.
#### Objective
With support from the R&D team, you designed training for VAS operators to improve productivity and reduce quality issues.
#### Question
Does the training have a positive impact on operator productivity?
#### Hypothesis
The training has a positive effect on VAS operators' productivity.
#### Experiment
Randomly select operators and measure the time per batch (Time to finish a batch of 30 labels in seconds) to build a sample of 56 records.

## Code
In this repository, you will find all the code used to explain the concepts presented in the article.

### Files
- `Kruskal Wallis Test.ipynb` - Jupyter notebook with step-by-step analysis
- `kruskal_wallis_test.py` - Standalone Python script
- `data/` - Folder containing input data (df_sewing.xlsx)

### Getting Started
```bash
pip install -r requirements.txt
python kruskal_wallis_test.py
```

### Dependencies
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- pingouin
- bioinfokit
- statsmodels
- openpyxl

## Go further

- **The full write-up, with the reasoning behind the code:** [Lean Six Sigma with Python — Kruskal Wallis Test](https://www.samirsaci.com/lean-six-sigma-with-python-kruskal-wallis-test/?utm_source=github&utm_medium=readme&utm_campaign=lss-kruskal-wallis)
- **Test what you learned:** the [Supply Science App](https://supply-science.com/?utm_source=github&utm_medium=readme&utm_campaign=lss-kruskal-wallis) has lessons on lean six sigma and the statistics quizzes, free and in the browser.
- **100+ case studies with their source code:** [samirsaci.com](https://www.samirsaci.com/?utm_source=github&utm_medium=readme&utm_campaign=lss-kruskal-wallis)

## About me

Samir Saci, supply chain engineer and data scientist with ten years in operations across Asia and Europe. Founder of [LogiGreen](https://www.logi-green.com/), creator of [Supply Science](https://www.youtube.com/@SupplyScience).
For consulting on analytics and sustainable supply chain transformation: [LogiGreen](https://www.logi-green.com/). More about me: [samirsaci.com/about](https://www.samirsaci.com/about/) · [LinkedIn](https://www.linkedin.com/in/samir-saci/)

