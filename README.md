# Measuring DNS over TCP in the Era of Increasing DNS Response Sizes: A View from the Edge

Mike Kosek | Trinh Viet Doan | Simon Huber | Vaibhav Bajpai  
Technical University of Munich

TBA, 2022.

[Paper &rarr;] TBA

---

## Reproducibility

In order to enable the reproduction of our findings, we make the raw data of our measurements as well as the analysis scripts and supplementary files publicly available within this repository.

0. Repository Overview
* The file ```analysis.ipynb``` is the script containing all analyses which are detailed in the paper
* The supplementary file ```public-resolvers-ipv4s.csv``` is used within the analysis script to check the identified probe resolvers against a list of known public resolvers used in related work
* The supplementary file ```pyasn.dat``` is used within the analysis script to map the IP addresses of the RIPEAtlas probes to ASNs

1. Dataset Overview
* A sample dataset is provided in ```sample.zip``` as an sqlite file based on all measurements of 5 probes. The extracted size is ~6.3MB
* The dataset is provided in ```measurements.zip``` as an sqlite file. The extracted size ~2.7GB
* Each row of the dataset contains one measurement result from one RIPEAtlas probe, where the probe is identified by the ```probe_id``` column
* The column ```public_src_ip``` contains the public IP address of the RIPEAtlas probe
* The measurement destination IP address is stated in the ```dst_address``` column
* The measurements were performed using DNS over TCP as well as DNS over UDP, which is stated in the ```proto``` column
* The column ```result_rt``` states the response time of the measurement
* If the measurement resulted in an error, ```err_msg``` is NOT NULL and contains the error reason
* The column ```edns_udp_size``` contains the edns(0) buffersize signaled by the recursive-resolver
* Geolocation information are provided in the ```latitude```, ```longitude```, ```country_code``` and ```continent_code``` columns

2. Preparations
* Clone this repository to a machine running ```Jupyter Notebook``` or ```JupyterLab```
* To minimize performance degradation through swapping, use a machine with at least 32GB of RAM
* Extract ```sample.zip``` if you would like to explore the sample dataset
* Extract ```measurements.zip``` if you would like to explore the full dataset

3. Analysis
* Open the Jupyter Notebook ```analysis.ipynb```
* By default, the full dataset (```measurements.db```) is used in the script If you prefer to run the sample data, replace ```measurements.db``` with ```sample.db``` in cell 2 of the script
* Run the Jupyter Notebook. Depending on machine capabilities, this can take from several minutes up to a few hours for the full dataset

---

## Contact

Please feel welcome to contact the authors for further details.

* Mike Kosek (kosek@in.tum.de) (corresponding author)
* Trinh Viet Doan (doan@in.tum.de)
* Simon Huber
* Vaibhav Bajpai (bajpai@cispa.de)
