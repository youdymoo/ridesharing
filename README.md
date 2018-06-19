```bash
./h3-bin/geoToH3 10 < ./data/index/tripData-space.txt >./data/index/tripData-index-complete.txt
python3 tripData.py --index
./h3-bin/h3ToGeo < ./data/index/tripData-index.txt >./data/center/tripData-center.txt
./h3-bin/h3ToGeo < ./data/index/tripData-index-complete.txt >./data/center/tripData-center-complete.txt
./h3-bin/hexRange 1 < ./data/index/tripData-index.txt > ./data/neighbor/tripData-neighbor.txt
python3 tripData.py --neighbor
```

