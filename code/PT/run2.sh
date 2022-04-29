echo script type: R

for v in {5..5}
do
for i in {85..85} 
do
echo ">>>>>>>>running test${v}_${i}"
./print_tokens_v${v}_1.exe  < ./input/input${i} > ./output/output${v}_${i}_test
done
done

exec /bin/bash