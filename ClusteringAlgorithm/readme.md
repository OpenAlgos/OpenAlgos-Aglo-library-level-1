# Interactive Cluster Predictor

This repository contains a simple interactive Python script that accepts 2D points belonging to different clusters, plots them, calculates the centroid (mean) of each cluster, and then predicts which cluster a new input point is closest to. The script leverages NumPy for numerical operations and Matplotlib for plotting.

---

## Features

- **Interactive Data Input:**  
  Users can input data points for various clusters. Each data point consists of two features (x and y coordinates) and a cluster label.
  
- **Dynamic Cluster Formation:**  
  New clusters are created based on unique labels provided by the user.
  
- **Visualization:**  
  The script plots the input data, the computed centroids for each cluster, and highlights a new prediction point along with a connecting line to its nearest centroid.
  
- **Prediction:**  
  Given a new input point (feature1, feature2), the script calculates the Euclidean distance to the centroid of each cluster and outputs the label of the closest cluster.

---

## Prerequisites

Ensure that you have the following Python libraries installed:

- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

You can install them via pip:

```bash
pip install numpy matplotlib
```

---

## Usage

1. **Clone the Repository**  
   Clone or download this repository to your local machine.

2. **Run the Script**  
   Open your terminal and execute the script using Python:

   ```bash
   python your_script_name.py
   ```

3. **Data Entry**  
   - On running the script, you will be prompted to enter data points in the following format:
     
     ```
     feature1 feature2 label
     ```
     
     For example:
     
     ```
     5 3 A
     2 7 B
     4 4 A
     ```
     
   - To stop data input, type:
     
     ```
     stp
     ```

4. **Visualization**  
   - The script will display a scatter plot of your points.
   - It will then calculate and display the centroids of each cluster, marking them with a different color (hotpink).

5. **Prediction**  
   - You will be asked to input a new point with two features (no label):
     
     ```
     feature1 feature2
     ```
     
   - The script will calculate the Euclidean distance from this point to each cluster centroid and output the label of the closest cluster.
   - A final plot will show the data points, centroids, the prediction point (in red), and a dotted line connecting the prediction point to the closest centroid.

---

## Code Walkthrough

- **Data Collection:**  
  The code collects data in an infinite loop until the user types `stp`. Each input consists of two features and a label.

- **Cluster Storage:**  
  A list is used to store points for each unique cluster. A separate list keeps track of the unique cluster labels.

- **Visualization:**  
  Points are plotted using Matplotlib. The clusters and centroids are visualized in successive plots.

- **Centroid Calculation:**  
  The mean of the x and y values for each cluster is computed to determine the centroid.

- **Prediction Logic:**  
  The Euclidean distance is calculated between the new input point and each centroid. The closest centroid determines the predicted cluster.

---

## Sample Input and Output

1. **Input Data:**

   ```
   5 3 A
   2 7 B
   4 4 A
   stp
   ```
   
2. **Prediction Input:**

   ```
   3 5
   ```

3. **Output:**

   - Visual plots showing clusters and centroids.
   - Printed text in the terminal similar to:

     ```
     The closest prediction would be A
     ```

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

Enjoy using the Interactive Cluster Predictor! If you have any questions or suggestions, feel free to open an issue or submit a pull request.