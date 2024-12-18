# Classic Machine Learning Algorithms

This repository contains implementations of fundamental classic machine learning algorithms in Python, organized for ease of learning and practical use. Each algorithm is accompanied by detailed explanations, clean code, and interactive Jupyter Notebooks demonstrating their functionality using real-world datasets. Whether you’re a beginner or an experienced practitioner, this repo serves as a comprehensive resource for understanding and applying classic ML techniques such as regression, classification, clustering, ensemble methods, and dimensionality reduction.

### Key Features:
	•	Modular and well-documented code.
	•	Interactive Jupyter Notebooks with visualizations.
	•	Small datasets for hands-on experimentation.
	•	Utility functions for metrics, plotting, and data loading.

Perfect for students, developers, and data enthusiasts to strengthen their foundation in machine learning. 🚀


### Highlights of the Repo:
	1.	Modularity: Each algorithm has a dedicated folder with self-contained code, explanations, and examples.
	2.	Documentation: Every folder has a README.md explaining the algorithm in detail (theory + code).
	3.	Reusability: Utility functions and example datasets make it easy to test and extend.
	4.	Jupyter Notebooks: Visual explanations and hands-on demonstrations for each algorithm.
	5.	Performance Comparison: A separate notebook to benchmark the algorithms.


 ### Repo Directory Structure

# Project Structure: Classic Machine Learning Algorithms

```plaintext
classic-ml-algorithms/
│
├── README.md                   # Project overview and usage instructions
├── LICENSE                     # License for open-source usage
├── requirements.txt            # Python dependencies for the project
├── .gitignore                  # Files and folders to exclude from version control
│
├── algorithms/                 # ML algorithms organized by type
│   ├── regression/             
│   │   ├── linear_regression/
│   │   │   ├── linear_regression.py       # Linear Regression implementation
│   │   │   ├── linear_regression.ipynb    # Notebook example for Linear Regression
│   │   │   ├── README.md                  # Documentation for Linear Regression
│   │   └── logistic_regression/
│   │       ├── logistic_regression.py
│   │       ├── logistic_regression.ipynb
│   │       ├── README.md
│   │
│   ├── classification/
│   │   ├── decision_tree/
│   │   │   ├── decision_tree.py
│   │   │   ├── decision_tree.ipynb
│   │   │   ├── README.md
│   │   ├── naive_bayes/
│   │       ├── naive_bayes.py
│   │       ├── naive_bayes.ipynb
│   │       ├── README.md
│   │
│   ├── clustering/
│   │   ├── kmeans/
│   │   │   ├── kmeans.py
│   │   │   ├── kmeans.ipynb
│   │   │   ├── README.md
│   │   └── hierarchical_clustering/
│   │       ├── hierarchical_clustering.py
│   │       ├── hierarchical_clustering.ipynb
│   │       ├── README.md
│   │
│   ├── dimensionality_reduction/
│   │   ├── pca/
│   │   │   ├── pca.py
│   │   │   ├── pca.ipynb
│   │   │   ├── README.md
│   │   └── lda/
│   │       ├── lda.py
│   │       ├── lda.ipynb
│   │       ├── README.md
│   │
│   ├── ensemble_methods/
│   │   ├── bagging/
│   │   │   ├── bagging.py
│   │   │   ├── README.md
│   │   ├── boosting/
│   │   │   ├── boosting.py
│   │   │   ├── README.md
│   │   └── random_forest/
│   │       ├── random_forest.py
│   │       ├── README.md
│   │
│   └── support_vector_machines/
│       ├── svm.py
│       ├── svm.ipynb
│       ├── README.md
│
├── datasets/                   # Small datasets for algorithm demonstration
│   ├── README.md               # Dataset descriptions
│   ├── iris.csv
│   ├── breast_cancer.csv
│   ├── wine.csv
│
├── utils/                      # Reusable utility functions
│   ├── metrics.py              # Custom evaluation metrics
│   ├── plot_utils.py           # Visualization helper functions
│   ├── data_loader.py          # Data loading and preprocessing functions
│
└── notebooks/                  # Interactive Jupyter Notebooks
    ├── overview_of_algorithms.ipynb     # Overview of all algorithms with examples
    ├── performance_comparison.ipynb     # Performance comparison of algorithms
    ├── README.md                        # Notebook descriptions


```

This project structure is designed to showcase my machine learning engineering skills, emphasizing code reusability, readability, and demonstrability to make the project professional and well-organized.

Overall Purpose of the Structure
**Clear Organization:** Code, utility functions, datasets, notebooks, and documentation are neatly categorized for easy maintenance and navigation.
**Modular Code:** Utility functions (utils/) and core algorithm modules (algorithms/) prevent code duplication and demonstrate good coding practices.
**Learning and Demonstration:** Interactive Jupyter Notebooks (notebooks/) visually showcase algorithm functionality, results, and comparisons.
**Reusability:** Data loading, evaluation metrics, and visualization tools are abstracted into reusable modules.
**Standardization:** Files like requirements.txt and .gitignore ensure consistency and eliminate irrelevant files, aligning with industry standards.

Folder and Content Architecture
### 1. algorithms/
Content: Contains implementations of all machine learning algorithms, organized by categories (e.g., regression, classification, clustering).
Reason:
Enhances readability and maintainability by categorizing algorithms.
Highlights your understanding and mastery of ML algorithms.
Each algorithm includes a standalone implementation and a README.md for clarity and ease of use.
### 2. datasets/
Content: Includes small datasets like iris.csv or wine.csv used to demonstrate algorithms.
Reason:
Ensures the project is self-contained, eliminating the need for external downloads.
Demonstrates algorithm performance using standard datasets, ensuring reproducibility and simplicity.
### 3. utils/
Content: Contains utility scripts for metrics, visualization, and data loading, such as metrics.py, plot_utils.py, and data_loader.py.
Reason:
Improves modularity and reusability by centralizing common functions.
Avoids code duplication across multiple modules.
Adheres to engineering best practices, making the codebase cleaner and extensible.
### 4. notebooks/
Content: Includes interactive Jupyter Notebooks like overview_of_algorithms.ipynb and performance_comparison.ipynb.
Reason:
Demonstrability: Showcases algorithms with explanations, code, and visualizations for better understanding.
Comparative Analysis: Allows performance comparisons of multiple algorithms on the same dataset.
Learning-Oriented: Combines theory, code, and visual results, making it easy for others to follow.
Professional Showcase: Highlights your ability to communicate technical results effectively.
### 5. requirements.txt
Content: Lists the Python libraries and versions required for the project.
Reason:
Ensures consistency in the project environment.
Makes it easy for others to install dependencies and run the code.
Demonstrates professionalism and engineering standards.
### 6. .gitignore
Content: Specifies which files or folders should not be committed to the Git repository (e.g., temporary files, virtual environments, cache).
Reason:
Keeps the repository clean by excluding unnecessary files.
Demonstrates attention to detail and adherence to Git best practices.
### 7. README.md (Root and Submodules)
Content: Provides an overview of the project, its purpose, usage instructions, and explanations for each module.
Reason:
Helps others quickly understand the project structure and functionality.
Highlights your ability to document and communicate effectively, a critical skill for engineers.


### Why This Structure Is Needed
**Clear Organization:** Enhances project clarity and maintainability, reflecting strong coding habits.
**Modularity:** Promotes code reuse and extensibility through shared utility functions.
**Interactive Demonstration:** Jupyter Notebooks visually showcase results, making it easy to understand and explain the project.
**Standardized Environment:** Files like requirements.txt ensure the project runs consistently across systems.
**Comprehensive Documentation:** Well-written README.md files guide users through the project, reflecting professionalism.





## 🎉 Thanks for Exploring this Repo!  

Thank you for taking the time to explore this project. I hope it helps you understand and implement classic machine learning algorithms with ease.  

If you found this project useful, feel free to:  
- ⭐ **Star** this repository to show your support.  
- 🛠️ Fork and contribute to improve it further.  
- 💬 Reach out with any questions, feedback, or suggestions via [email](mengnanxu2333@gmail.com), [LinkedIn](www.linkedin.com/in/isobelxu) or Web message!  

Happy coding and learning! 🚀  

**--- Mengnan Xu**