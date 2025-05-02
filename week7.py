
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# load the dataset using pandas and handle possible errors
try:
    df = pd.read_csv("csv_files/cleaned_academic_levels.csv")
    # print(df)
    
    # check for missing values
    if df.isnull().values.any():
        print("warning: The datasets contains misisng values.")
except FileNotFoundError:
    print("Error: The file 'cleaned_academic_levels.csv' was not found")
except pd.errors.EmptyDataError:
    print("Error: The file is empty")
except pd.errors.ParserError:
    print("Error: There was an issue parsing the csv file")
except Exception as e:
    print(f"An unexpected error occured: {e}")
    

# display first few rows using .head() method
print(df.head())

# examine the stucture of the dataset and chek for missing values
print(df.info())


# fill the missing entries with values
df["Academic Level"] = df["Academic Level"].fillna("Unknown")
print(df.info())
    
    


# statistics of numerical column in the dataset
print(df.describe())

# get the mean, median and standard deviation of Age in the dataset
print("Mean Age:", df["Age"].mean())
print("Mean Age:", df["Age"].median())
print("Mean Age:", df["Age"].std())


#group gender by age and find the mean for each gender
grouped_gender_age = df.groupby("Gender")["Age"].mean()
print(grouped_gender_age)

# group academic level by age and find the mean for each academic level
grouped_level_age = df.groupby("Academic Level")["Age"].mean()
print(grouped_level_age)

# pattterns or findings
# there is a general increase in age with academic level, with 
# "diploma" being the youngest and "other" being the oldest

# Gender has minimal effect on age as both  male and females nearly had similar mean
# the "non_binary" and "other" categories show higher ages, this may indicate differnce
# in the non-tradition education or gender difference


# data visualization
# show average age across academic level
avg_age_academic = df.groupby("Academic Level")["Age"].mean().reset_index()
sns.barplot(
    x="Academic Level",
    y="Age",
    data=avg_age_academic,
    palette="pastel",
    hue="Academic Level",  
    legend=False            
)
plt.title("Average Age by Academic Level")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# distribution of age using histogram
plt.hist(df["Age"], bins=10, color="lightgreen", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()


# Line gragh of average age by country
country_avg_age = df.groupby("Country")["Age"].mean().sort_values()
country_avg_age.plot(kind="line", marker="o", linestyle="-", color="orange")
plt.title("Average Age Per Country")
plt.xlabel("Country")
plt.ylabel("Averag Age")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# map academic level to numbers and scatter plot against age
level_map = {
    'High School': 1,
    'Diploma': 2,
    'Undergraduate': 3,
    'Postgraduate': 4,
    'Other': 5
}
df['Academic_Level_Num'] = df['Academic Level'].map(level_map)

plt.scatter(df['Academic_Level_Num'], df['Age'], alpha=0.6, color='purple')
plt.title("Age vs. Academic Level (Numeric Mapping)")
plt.xlabel("Academic Level (Encoded)")
plt.ylabel("Age")
plt.xticks(list(level_map.values()), list(level_map.keys()), rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()