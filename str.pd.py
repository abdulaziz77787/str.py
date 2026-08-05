
import pandas as pd
import numpy as np

data = {
    'Level': [100, 100, 100, 200, np.nan, np.nan, 200, 300, np.nan, 300, np.nan, np.nan, np.nan, np.nan, np.nan],
    'Course Name': [
        'Introduction to IT', 'Programming Fundamentals', 'Introduction to MIS',
        'Database Management', np.nan, 'Data Structures',
        'Systems Analysis and Design', 'Network Security', np.nan,
        'Algorithms', np.nan, np.nan, np.nan, np.nan, np.nan
    ],
    'Major': [
        'IT', 'CS', 'MIS',
        np.nan, np.nan, 'CS',
        'MIS', np.nan, np.nan,
        'CS', np.nan, np.nan, np.nan, np.nan, np.nan
    ]
}

df = pd.DataFrame(data)

print("--- DataFrame ---")
print(df)
print("\n" + "="*50 + "\n")

print("--- Describe Summary ---")
print(df.describe(include='all'))
print("\n" + "="*50 + "\n")

df['Level'] = df['Level'].astype('float64')
print("--- Data Types ---")
print(df.dtypes)
print("\n" + "="*50 + "\n")

print("--- First 4 Rows ---")
print(df.head(4))
print("\n" + "="*50 + "\n")

df_cleaned = df.dropna(how='all')
print("--- Data After Dropping Entirely Null Rows ---")
print(df_cleaned)
