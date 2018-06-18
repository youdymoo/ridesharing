```bash
./h3-bin/geoToH3 10 < ./data/index/tripData-space.txt >./data/index/tripData-index-complete.txt
python3 tripData.py --index
./h3-bin/h3ToGeo < ./data/index/tripData-index-complete.txt >./data/index/tripData-center.txt
./hexRange 1
```

