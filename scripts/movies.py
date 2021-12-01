import pandas as pd

data = {
    'name': ['Toy Story', 'Akira', 'The Breakfast Club', 'The Artist', 'Modern Times', 'Fight Club', 'City of God'],
    'year': [1995, 1998, 1985, 2011, 1936, 1999, 2002],
    'length_min': [81, 125, 97, 100, 87, 139, 130],
    'genre': ['Animation', 'Animation', 'Drama', 'Romance', 'Comedy', 'Drama', 'Crime'],
    'average_rating': [8.3, 8.1, 7.9, 8, 8.6, 8.9, 8.7],
    'cost_millions': [30, 10.4, 1, 15, 1.5, 63, 3.3],
    'foreign': [False, False, False, False, False, False, True],
    'age_restriction': [0, 14, 14, 12, 10, 18, 18]
}

df = pd.DataFrame(data)
converted = df.to_csv('../data/movies.csv', index=False)

df = pd.read_csv(converted)
print(df)