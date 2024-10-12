# Discern-XR: Fine-Grain Identification of Metaverse Network Traffic

## Dataset Download and Setup

Please download the datasets from benow URL,

Dataset1: //URL//

Dataset2: https://www.kaggle.com/datasets/szhao2020/vr-gaming-network-traffic?resource=download

Dataset3: https://researchdata.cab.unipd.it/1179/

Recommended to place the code and datasets in a same reposiotry.
For datasets, create repositories named "Dataset1" for the Dataset1, "Dataset2" for Dataset2, and "Dataset3" for Dataset3 and place the respective datasets in the respective repositories.

Edit "Dataset1_path", "Dataset2_path", and "Dataset3_path" in "config.py" to add absolute path of the datasets.

Please execute main_aar.py as shown in the bewlo commands,

1) To run AAR for Dataset1
* python main_aar.py Dataset1
2) To run AAR for Dataset2
* python main_aar.py Dataset2
3) To run AAR for Dataset3 experiment 1 (consists of four classes as explained in config.py)
* python main_aar.py Daatset3 exp=1
4) To run AAR for Dataset3 experiment 1 (consists of two classes as explained in config.py)
* python main_aar.py Dataset3 exp=2

To plot the histograms of the pre processed .csv files, the commands are:

- python main_aar.py plot Dataset1
- python main_aar.py plot Dataset2
- python main_aar.py plot Dataset3 exp=1
- python main_aar.py plot Dataset3 exp=2

NOTE: ensure you execute the experiments before attempting to plot the histograms. As the pre processed .csv files are required
