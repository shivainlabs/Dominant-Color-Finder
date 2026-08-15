# Dominant Color Finder

A Streamlit application that uses **K-Means clustering** to extract the
dominant colors from an uploaded image and generate a visual color
palette with HEX color codes.

## Live Demo

[Try the app on Streamlit](https://dominant-color-finder.streamlit.app/)

## Overview

The Dominant Color Finder treats every pixel in an image as an RGB data
point and applies K-Means clustering to group similar colors together.

The center of each cluster represents one dominant color in the image.
These cluster centers are converted into HEX color codes and displayed
as a color palette.

## Features

-   Upload common image formats such as JPG, JPEG, PNG, WEBP, BMP, and
    GIF.
-   Convert uploaded images to RGB.
-   Handle grayscale and RGBA images through RGB conversion.
-   Convert image data into a NumPy array.
-   Reshape image pixels into RGB feature vectors.
-   Use K-Means clustering to identify dominant colors.
-   Generate a visual color palette.
-   Display HEX values for the dominant colors.
-   Interactive Streamlit interface.

## How It Works

### 1. Upload an image

The application accepts an image through Streamlit's file uploader.

### 2. Convert the image to RGB

``` python
image = Image.open(uploaded_file).convert("RGB")
```

This ensures that every pixel has three channels:

``` text
[R, G, B]
```

It also allows grayscale and RGBA images to use the same processing
pipeline.

### 3. Convert the image to a NumPy array

``` python
image = np.array(image)
```

A PIL Image is converted into a numerical NumPy array so that it can be
processed by machine-learning algorithms.

For an RGB image, the shape is:

``` text
(height, width, 3)
```

### 4. Reshape the image

``` python
X = image.reshape(-1, 3)
```

Each pixel becomes one observation with three features:

``` text
R    G    B
---  ---  ---
120  80   30
250  250  250
40   90   120
...
```

The resulting shape is:

``` text
(number_of_pixels, 3)
```

### 5. Apply K-Means

``` python
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)
```

The application currently extracts five dominant colors.

The cluster centers represent the dominant colors:

``` python
dominant_colors = kmeans.cluster_centers_.astype(int)
```

### 6. Generate the palette

The cluster centers are passed to a custom palette function that creates
a visual palette and displays the HEX values of the dominant colors.

## Project Structure

``` text
dominant-color-finder/
│
├── app.py
├── palette.py
├── requirements.txt
├── README.md
│
└── deep-dive/
    ├── image-array.md
    └── palette.md
```

The `deep-dive` folder contains personal learning notes explaining the
reasoning behind the implementation, including questions, experiments,
and concepts discovered while building the project.

## Technologies Used

-   Python
-   Streamlit
-   NumPy
-   scikit-learn
-   Pillow
-   K-Means Clustering

## Running Locally

Clone the repository:

``` bash
git clone https://github.com/shivainlabs/Dominant-Color-Finder.git
cd dominant-color-finder
```

Install the dependencies:

``` bash
pip install -r requirements.txt
```

Run the Streamlit application:

``` bash
streamlit run app.py
```

## Requirements

``` text
streamlit
numpy
scikit-learn
Pillow
```

## Learning Goal

This project was built to understand how an image can be represented as
numerical data and how an unsupervised learning algorithm such as
K-Means can be applied to a practical computer-vision task.

The `deep-dive` notes document the reasoning behind the implementation
rather than only recording the final code.
