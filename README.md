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
* `measurements.parquet` the full measurements campaign run via RipeAtlas probes

Each measurements sample has the following schema
| field              | example value | description |
|:------------------:|:--------------|:------------|
|`msm_id`            | 29743869                 | ADD DESCRIPTION |
|`probe_id`          | 21500                    | ADD DESCRIPTION |
|`time`              | 2021-04-19 14:58:56      | ADD DESCRIPTION |
|`proto`             | TCP                      | ADD DESCRIPTION |
|`src_address`       | 192.168.111.130          | ADD DESCRIPTION |
|`dst_address`       | 208.67.222.222           | ADD DESCRIPTION |
|`dst_port`          | 53                       | ADD DESCRIPTION |
|`result_rt`         | 103.077                  | ADD DESCRIPTION |
|`err_msg`           | None                     | ADD DESCRIPTION |
|`edns_udp_size`     | 4096                     | ADD DESCRIPTION |
|`id_x`              | 21500                    | ADD DESCRIPTION |
|`latitude`          | 50.4975                  | ADD DESCRIPTION |
|`longitude`         | 13.6275                  | ADD DESCRIPTION |
|`country_code`      | CZ                       | ADD DESCRIPTION |
|`continent_code`    | EU                       | ADD DESCRIPTION |
|`id_y`              | 29743869                 | ADD DESCRIPTION |
|`description`       | IPv4/4/q1-edns0-test7-2500-probes-200-domains/... | ADD DESCRIPTION |
|`resolver`          | 208.67.222.222           | ADD DESCRIPTION |
|`resolver_name`     | OpenDNS                  | ADD DESCRIPTION |
|`ip`                | 208.67.222.222           | ADD DESCRIPTION |
|`prb_id`            | 21500                    | ADD DESCRIPTION |
|`public_src_ip`     | 213.129.132.83           | ADD DESCRIPTION |


__Preparations__
```
conda create -n ccr2022 pip
conda activate ccr2022
python -m pip install jupyterlab pandas matplotlib seaborn IPy pyasn pyarrow
```

__Analysis__

All results are generated from the notebook `analysis.ipynb`

---

## Contact

Please feel welcome to contact the authors for further details.

* Mike Kosek (kosek@in.tum.de) (corresponding author)
* Trinh Viet Doan (doan@in.tum.de)
* Simon Huber
* Vaibhav Bajpai (bajpai@cispa.de)
