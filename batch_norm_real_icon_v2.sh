#/bin/sh

set -x

input_prefix="./icons_real/"
output_prefix="icons_styled_"
extension="png"
style_list="
kandinsky
seated-nude
shipwreck
the_scream
woman-with-hat-matisse
"

for style in $style_list
do
    output_prefix_final="${output_prefix}result_${style}_"
    for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14
    do
        python my_run.py ${input_prefix}${i}.$extension ${style}.jpg ${output_prefix_final}${i}.$extension || exit $i
    done
    # gsutil mv ${output_prefix_final}*.$extension gs://q1-tensorflow
done

sudo poweroff
# gcloud compute instances stop instance-2 --zone=us-east1-b
