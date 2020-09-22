- training

python flow --model cfg/my-tiny.cfg --load bin/yolov2-tiny-voc.weights --train --annotation train/Annotations --dataset train/Images --gpu 0.5 --epoch 10



- test

python flow --model cfg/my-tiny.cfg --load bin/yolov2-tiny-voc.weights --imgdir training --threshold 0.25



- save포인트와 load를 이용, 학습시킨 weights를 저장하고 불러올 수 있음

```
python flow --model cfg/my-tiny.cfg --load bin/yolov2-tiny-voc.weights --train --annotation train/Annotations --dataset train/Images --gpu 0.5 --epoch 300 --save 50 --keep 5
```

```python
python flow --model cfg/my-tiny.cfg --load -1 --imgdir training --threshold 0.25
```



- 학습된 모델 .pb 로 저장하기

(https://stackoverflow.com/questions/50618968/converting-checkpoints-generated-to-weights-darkflow)

The trained checkpoint files `yolov2-3c-5500.data` file is actually your weight file. If you want to convert to .pb file, use the below command

```python
flow --model cfg/Your_ConfigFile.cfg --load ckpt/Your_required_checkpoint-chkptNumber --savepb
```

flow --model cfg/my-tiny.cfg --load ckpt/my-tiny-5151 --savepb

flow --model cfg/my-tiny.cfg --load -1 --savepb



- .pb % .meta 파일을 이용한 예측 명령어

```python
python flow --pbLoad built_graph/my-tiny.pb --metaLoad built_graph/my-tiny.meta --threshold 0.25 --gpu 0.5 --imgdir training
```



- darkflow\darkflow\dark\darknet.py", line 47
  - def get_weight_src(self, FLAGS):

```python
from ..utils.process import cfg_yielder
from .darkop import create_darkop
from ..utils import loader
import warnings
import time
import os

class Darknet(object):

    _EXT = '.weights'

    def __init__(self, FLAGS):
        self.get_weight_src(FLAGS)
        self.modify = False

        print('Parsing {}'.format(self.src_cfg))
        src_parsed = self.parse_cfg(self.src_cfg, FLAGS)
        self.src_meta, self.src_layers = src_parsed
        
        if self.src_cfg == FLAGS.model:
            self.meta, self.layers = src_parsed
        else: 
        	print('Parsing {}'.format(FLAGS.model))
        	des_parsed = self.parse_cfg(FLAGS.model, FLAGS)
        	self.meta, self.layers = des_parsed

        self.load_weights()

    def get_weight_src(self, FLAGS):
        """
        analyse FLAGS.load to know where is the 
        source binary and what is its config.
        can be: None, FLAGS.model, or some other
        """
        self.src_bin = FLAGS.model + self._EXT
        self.src_bin = FLAGS.binary + self.src_bin
        self.src_bin = os.path.abspath(self.src_bin)
        exist = os.path.isfile(self.src_bin)

        if FLAGS.load == str(): FLAGS.load = int()
        if type(FLAGS.load) is int:
            self.src_cfg = FLAGS.model
            if FLAGS.load: self.src_bin = None
            elif not exist: self.src_bin = None
        else:
            assert os.path.isfile(FLAGS.load +".meta"), \
            '{} not found'.format(FLAGS.load)
            self.src_bin = FLAGS.load
            name = loader.model_name(FLAGS.load)
            cfg_path = os.path.join(FLAGS.config, name + '.cfg')
            if not os.path.isfile(cfg_path):
                warnings.warn(
                    '{} not found, use {} instead'.format(
                    cfg_path, FLAGS.model))
                cfg_path = FLAGS.model
            self.src_cfg = cfg_path
            FLAGS.load = int()


    def parse_cfg(self, model, FLAGS):
        """
        return a list of `layers` objects (darkop.py)
        given path to binaries/ and configs/
        """
        args = [model, FLAGS.binary]
        cfg_layers = cfg_yielder(*args)
        meta = dict(); layers = list()
        for i, info in enumerate(cfg_layers):
            if i == 0: meta = info; continue
            else: new = create_darkop(*info)
            layers.append(new)
        return meta, layers

    def load_weights(self):
        """
        Use `layers` and Loader to load .weights file
        """
        print('Loading {} ...'.format(self.src_bin))
        start = time.time()

        args = [self.src_bin, self.src_layers]
        wgts_loader = loader.create_loader(*args)
        for layer in self.layers: layer.load(wgts_loader)
        
        stop = time.time()
        print('Finished in {}s'.format(stop - start))
```

- .pb 파일 생성할 때 ".meta" 확장자가 붙지 않아 에러:
  - +".meta" 붙여줘 수정

