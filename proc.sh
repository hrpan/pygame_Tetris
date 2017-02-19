#/bin/bash
cycles=$1
for ((i=0;i<$cycles;i++)); do
	echo "Cycle: $i"
	python tetris.py
	python train.py
done
