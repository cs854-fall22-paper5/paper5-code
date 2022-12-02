import random
import pandas as pd
from bs4 import BeautifulSoup


random.seed(42)
with open('webpage.html') as f:
    html_file = f.read()
soup = BeautifulSoup(html_file, 'html.parser')

focus = 'full-papers'  # Options: full-papers, short-papers
section = soup.find('h4', {'id': focus})
papers = []
for item in section.next_siblings:
    if item.name == 'p':
        papers.append(str(item.find('b').getText()).strip())
    elif item == '\n':
        continue
    else:
        break

sampled_papers = random.sample(papers, 40)
data = pd.DataFrame(sampled_papers, columns=['paper_name'])
data['contain_experiment?'] = None
data['did_statistical_analysis?'] = None
data['has_multiple_testing_problem?'] = None
data['has_proper_correction?'] = None
data.to_csv(f'{focus}.csv', index=False)
