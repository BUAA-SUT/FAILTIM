#! /bin/bash
echo script type: R

for v in $(seq 0 9)
do
for i in $(seq 0 99)
do
echo ">>>>>>>>running test${v}_${i}"
./print_tokens_v${v}.exe  < ./input/input${i} > ./output/output${v}_${i}
done

for i in $(seq 0 99) 
do
for j in $(seq 0 8)
do
echo ">>>>>>>>running test${v}_${i}_${j}"
./print_tokens_v${v}.exe  < ./input/input${i}_${j} > ./output/output${v}_${i}_${j}

done		
done

for i in $(seq 0 99)
do
for m in $(seq 0 8)
do
for n in $(seq 0 8)
do
echo ">>>>>>>>running test${v}_${i}_${m}_${n}"
./print_tokens_v${v}.exe  < ./input/input${i}_${m}_${n} > ./output/output${v}_${i}_${m}_${n}
done
done		
done


done

exec /bin/bash