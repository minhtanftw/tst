import sklearn
from sklearn.datasets import load_diabetes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

diabetes = load_diabetes()
column_name =diabetes.feature_names
df_diabetics = pd.DataFrame(diabetes.data, columns= column_name)
sns.boxplot(df_diabetics['bmi'])
plt.title('Boxplot of BMI')
plt.show()