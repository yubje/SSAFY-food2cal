-training

python flow --model cfg/my-tiny.cfg --load bin/yolov2-tiny-voc.weights --train --annotation train/Annotations --dataset train/Images --gpu 0.5 --epoch 10



- test

python flow --model cfg/my-tiny.cfg --load bin/yolov2-tiny-voc.weights --imgdir training --threshold 0.25