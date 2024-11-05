import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# we define arcsinh as a function for transformation
def arcsinh_transform(x):
    return np.log(x + np.sqrt(x ** 2 + 1))


# we define a function arcsinh transformation function
def read_and_preprocess_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Drop the rows with missing values if any
    df.dropna(inplace=True)

    # Select relevant columns
    selected_columns = ['ch1-peak', 'ch9-peak']  # the headers in our csv file that required
    df = df[selected_columns]

    # Apply arcsinh transformation function
    df_transformed = df.apply(arcsinh_transform)

    # Standardize the transformed data
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_transformed)

    return df_scaled, df

# we define for clustering the data
def perform_clustering(df_scaled, num_clusters = 7):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(df_scaled)

    return labels

# we define to visualize the data on a histogram
def visualize_clusters(df, labels):
    # Visualize clusters
    plt.figure(figsize=(10, 6))
    plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=labels, cmap='viridis', alpha=0.5)

    # we define the captions here
    plt.xlabel('arcsinh(Close Price)')
    plt.ylabel('arcsinh(Volume)')
    plt.title('Stock Clusters')
    plt.colorbar(label='Cluster')
    plt.show()


def main():

    file_path = input("Enter the file path with csv ending or the full path: ")

    num_clusters = 7  # Number of clusters to create

    # Read the data with arcsinh transformation we defined. df = Data Frame
    df_scaled, df = read_and_preprocess_data(file_path)

    # Make the clustering using python clustering function
    labels = perform_clustering(df_scaled, num_clusters)

    # Visualize the clusters using python matplotlib library
    visualize_clusters(df, labels)


if __name__ == "__main__":
    main()


