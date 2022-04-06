# Measuring DNS over TCP in the Era of Increasing DNS Response Sizes: A View from the Edge

Mike Kosek | Trinh Viet Doan | Simon Huber | Vaibhav Bajpai  
Technical University of Munich

TBA, 2022.

[Paper &rarr;] TBA

---

## Reproducibility

In order to enable the reproduction of our findings, we make the raw data of our measurements as well as the analysis scripts and supplementary files publicly available within this repository.

__Repository Overview__
* `analysis.ipynb` is a jupyter notebook containing all analyses detailed in the paper
* `public-resolvers-ipv4s.csv` is single column text file containing  a list of known public resolvers (used in related work)
* `pyasn.dat` is a 2 columns text file mapping RIPEAtlas probes IP address to the related ASN
* `sample.zip` an extract of the full measurements campaign (5 probes, ~6.3MB when unzipped)
* `measurements.zip` the full measurements campaign (XXX probes, ~2.7GB when unzipped)

Each measurements sample has the following schema
| field              | description |
|:------------------:|:------------|
|`msm_id`            | ADD DESCRIPTION |
|`probe_id`          | ADD DESCRIPTION |
|`time`              | ADD DESCRIPTION |
|`proto`             | ADD DESCRIPTION |
|`src_address`       | ADD DESCRIPTION |
|`dst_address`       | ADD DESCRIPTION |
|`dst_port`          | ADD DESCRIPTION |
|`result_rt`         | ADD DESCRIPTION |
|`err_msg`           | ADD DESCRIPTION |
|`edns_udp_size`     | ADD DESCRIPTION |
|`id_x`              | ADD DESCRIPTION |
|`latitude`          | ADD DESCRIPTION |
|`longitude`         | ADD DESCRIPTION |
|`country_code`      | ADD DESCRIPTION |
|`continent_code`    | ADD DESCRIPTION |
|`id_y`              | ADD DESCRIPTION |
|`description`       | ADD DESCRIPTION |
|`resolver`          | ADD DESCRIPTION |
|`resolver_name`     | ADD DESCRIPTION |
|`ip`                | ADD DESCRIPTION |
|`prb_id`            | ADD DESCRIPTION |
|`public_src_ip`     | ADD DESCRIPTION |


__Preparations__
```
conda create -n ccr2022 pip
conda activate ccr2022
python -m pip install jupyterlab pandas matplotlib seaborn IPy pyasn pyarrow
```

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
