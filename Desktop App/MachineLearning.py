import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv('train.csv')


def log_transform(value):
    """
    This function does a log transformation for a specific value (negative or positive).
    :param value: The value to transform.


    :return: The transformed value
    """
    if value > 0:
        return np.log(value)
    elif value == 0:
        return 0
    return -np.log(-value)


def transform(data: pd.DataFrame,
              inplace=False,
              trim_long_calls=False,
              trim_poutcome=False,
              trim_age=False,
              log_transformation=True
              ):
    """
    This function cleans the data frame INPLACE or as a new dataframe.
    :param log_transformation: whether we want to apply log transformation to balance feature
    :param trim_age: whether we want to drop over aged clients
    :param data: The data frame to clean
    :param inplace: Whether to transform the dataframe in place or as a new dataframe
    :param  trim_long_calls: whether you want to drop calls longer than 1000 seconds
    :param trim_poutcome: Whether tor not you want to drop unknown previous campaign outcome
    :return: The transformed data frame as a new dataframe or None if clean happens in place
    """
    # Make a copy of the dataframe
    df = data if inplace else data.copy()
    # Drop the ID column
    df.drop(columns=['ID'], axis=1, inplace=True)
    # The subscribed (Target column) needs to be a 0/1 column
    df.subscribed = df.subscribed.replace({"yes": 1, "no": 0, "UNKNOWN": -1}).astype(int)
    # we want to handle outliers in the AGE column by cliping (any point > 70 will be 70) or drop them
    if trim_age:
        # Drop outliers
        df = df[df['age'] < 70]
    else:
        # Clip outliers
        df.age = np.where(df.age > 70,
                          70, df.age)
    # Handle the outliers in duration by clipping any rows above 1k to 1k or dropping them
    if trim_long_calls:
        df = df[df['duration'] < 1000]
    else:
        df.duration = np.where(df.duration > 1000,
                               1000, df.duration)
    # we want to handle outliers in the campaign column by cliping (any point > 10 will be 10)
    df.campaign = np.where(df.campaign > 10,
                           10, df.campaign)
    # Replace unknown jobs with others
    df.job = df.job.replace(to_replace="unknown", value="Others")
    # Replace unknown contacts with others
    df.contact = df.contact.replace(to_replace="unknown", value="Others")
    # handle missing values in the poutcome column
    if trim_poutcome:
        # If we want to leave this column we will have to drop any missing values
        df = df[df['poutcome'] != "unknown"]
        df = pd.get_dummies(df, columns=["poutcome"], prefix="P")
    else:
        # Drop that column entirely
        df.drop(columns=['poutcome'], axis=1, inplace=True)
    # Handle outliers in the prevoius column
    df.previous = np.where(df.previous > 10,
                           10, df.previous)
    # Drop pdays column
    df.drop(columns=['pdays'], axis=1, inplace=True)
    if log_transformation:
        # Log transformation for balance column
        df["log_balance"] = df.balance.apply(log_transform)
        df.drop(columns=['balance'], axis=1, inplace=True)

    # One Hot Encoding for categorical features
    df = pd.get_dummies(df, columns=["job"], prefix="J")
    df = pd.get_dummies(df, columns=["marital"], prefix="M")
    df = pd.get_dummies(df, columns=["education"], prefix="E")
    df = pd.get_dummies(df, columns=["default"], prefix="D")
    df = pd.get_dummies(df, columns=["housing"], prefix="H")
    df = pd.get_dummies(df, columns=["loan"], prefix="L")
    df = pd.get_dummies(df, columns=["month"], prefix="M")
    df = pd.get_dummies(df, columns=["contact"], prefix="C")

    # Return the transformed data frame as a new data frame
    return None if inplace else df


def predict(data):
    train_data = transform(train, trim_long_calls=True, log_transformation=True)
    data = transform(data, log_transformation=True)
    # Get the training features
    train_x = train_data.drop(["subscribed"], axis=1)
    # Get the training labels
    train_y = train_data[['subscribed']]
    # Train a Random Forrest model
    model = RandomForestClassifier(random_state=0)
    model.fit(train_x, train_y)
    data.drop(['subscribed'], axis=1, inplace=True)
    y_pred = model.predict(data)
    return y_pred

