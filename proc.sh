#/bin/bash
cycles=$1
rm data/*.npy
for ((i=0;i<$cycles;i++)); do
	echo "Cycle: $i"
	python tetris.py $i
	python train.py
done
