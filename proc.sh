#/bin/bash
cycles=$1
rm data/*.npy
for ((i=0;i<$cycles;i++)); do
	echo "Cycle: $((i+1))/$1"
	python tetris.py $i
	python train.py $i
done
