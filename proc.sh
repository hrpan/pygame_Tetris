#/bin/bash
cycles=$1
rm data/*.npy
rm data/sample/*.npy
for ((i=0;i<$cycles;i++)); do
    echo "Cycle: $i"
    python tetris.py $i
    python train.py $i
    python extract.py $i
done
