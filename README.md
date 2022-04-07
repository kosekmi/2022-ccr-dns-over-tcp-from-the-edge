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
* `pyasn.dat` is a 2 columns text file mapping RIPEAtlas (RA) probes IP address to the related ASN
* `measurements.parquet` contains the full measurements campaign run via RA probes

Each measurements sample has the following schema
| field              | example value | description |
|:------------------:|:--------------|:------------|
|`msm_id`            | 29743869                 | Unique ID of the measurement |
|`probe_id`          | 21500                    | Unique ID of the RA probe |
|`time`              | 2021-04-19 14:58:56      | Execution time of the measurement |
|`proto`             | TCP                      | Transport protocol used for the measurement |
|`src_address`       | 192.168.111.130          | Source IP address of the RA probe |
|`dst_address`       | 208.67.222.222           | IP address of the targeted recursive DNS resolver |
|`dst_port`          | 53                       | Destination port of the measurement |
|`result_rt`         | 103.077                  | Response time of the measurement in ms|
|`err_msg`           | None                     | Error reason if a measurement resulted in an error |
|`edns_udp_size`     | 4096                     | EDNS(0) buffersize signaled by the recursive DNS resolver |
|`latitude`          | 50.4975                  | Latitude of the RA probe |
|`longitude`         | 13.6275                  | Longitude of the RA probe |
|`country_code`      | CZ                       | Country code of the RA probe |
|`continent_code`    | EU                       | Continent code of the RA probe |
|`resolver_name`     | OpenDNS                  | Name of the targeted Public DNS resolver, or `Probe Resolver` if not public |
|`public_src_ip`     | 213.129.132.83           | Public IP address of the RA probe |


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
