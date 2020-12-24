import pandas as pd
import re

# read
with open(r'data/aoc4.txt', 'r') as f:
    data = f.read()

data2 = data.split('\n')
# append emtpy item for use in loop
data2.append('')

# make list, split by blank records
d = []
y = ''
for x in data2:
    if x == '':
        d.append(y)
        y = ''
    else:
        y = str(x) + ' ' + str(y)

# to list
e = [list(x.replace('\n', '').split()) for x in d]
# make dictionairy
f = [dict([y.split(':') for y in x]) for x in e]

# make dataframe
df = pd.DataFrame(f)
total_number_records = df.shape[0]
# remove cid column
columns = list(df.columns)
columns.remove('cid')
df = df[columns]
# calculate result for question 4a
number_of_correct_passports = df.dropna().shape[0]

# %%
# 4b

df = df.dropna()
print('initial number of records is {}'.format(df.shape[0]))

def invalid_report(func):
    """
    decorator for validation functions.
    count number of incoming records
    execute validation function
    remove invalid records
    count number of outgoing records
    print result
    :param func: funcion
    :return: dataframe
    """
    def wrapper(*args):
        # set all to invalid
        df['valid'] = 0

        # count records
        start_records = df.shape[0]
        # execute function
        out = func(*args)
        # count invalid records
        invalid = out[out['valid'] == 0]['valid'].count()
        # drop invalid records
        out = out[out.valid == 1]
        # count records
        end_records = out.shape[0]
        print('start: {}, end: {}, invalid: {}'.format(start_records, end_records, invalid))

        return out

    return wrapper


@invalid_report
def year_validation(df, col, startyear, endyear):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    :param df:
    :param col:
    :param startyear:
    :param endyear:
    :return:
    """
    for label, row in df.iterrows():
        v = int(row[col])
        if startyear <= v <= endyear:
            df.loc[label, 'valid'] = 1

    return df

@invalid_report
def height_validation(df, col):
    """
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    :param df:
    :return:
    """
    for label, row in df.iterrows():
        if row[col][-2:] == 'cm':
            if 150 <= int(row[col][:-2]) <= 193:
                df.loc[label, 'valid'] = 1
        elif row[col][-2:] == 'in':
            if 59 <= int(row[col][:-2]) <= 76:
                df.loc[label, 'valid'] = 1

    return df

@invalid_report
def haircolor_validation(df, col):
    """
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    :param df:
    :return:
    """
    pattern = re.compile(r"^#([a-zA-Z0-9]{6})$")
    for label, row in df.iterrows():
        v = row[col]
        if pattern.search(v):
            df.loc[label, 'valid'] = 1

    return df

@invalid_report
def eyecolor_validation(df, col):
    """
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth
    :param df:
    :return:
    """
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for label, row in df.iterrows():
        v = row[col]
        if v in colors:
            df.loc[label, 'valid'] = 1

    return df

@invalid_report
def passportid_validation(df, col):
    """
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    :param df:
    :return: df
    """
    pattern = re.compile(r"^\d{9}$")
    for label, row in df.iterrows():
        v = str(row[col])
        if pattern.search(v):
            df.loc[label, 'valid'] = 1

    return df


df = year_validation(df, 'byr', 1920, 2002)
df = year_validation(df, 'iyr', 2010, 2020)
df = year_validation(df, 'eyr', 2020, 2030)
df = height_validation(df, 'hgt')
df = haircolor_validation(df, 'hcl')
df = eyecolor_validation(df, 'ecl')
df = passportid_validation(df, 'pid')

print('final number of records (and answer for the question) is {}'.format(df.shape[0]))


