# This bash file is for creating Multiple sequence alignments from KALIGN
for my_fastas in *.fasta
do kalign $my_fastas $my_fastas.txt

echo 'YES'

done
