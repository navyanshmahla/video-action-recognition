# Motionformer

This is one of the projects that I did as part of IE643: Deep Learning Course at IITB that aims to solve the problems of action recognition using trajectory attention in vision tranformers.

The skeleton code was taken from the official PyTorch implementation of MotioFormer. Changes were made accordingly to the dataset (we used less data i.e. less action features as well) and trained it on Nvidia A100 80GB GPU for this purpose. 

This paper has been very helpful in the implementation: [Keeping Your Eye on the Ball: Trajectory Attention in Video Transformers](https://arxiv.org/abs/2106.05392)

```BibTeX
@inproceedings{patrick2021keeping,
   title={Keeping Your Eye on the Ball: Trajectory Attention in Video Transformers}, 
   author={Mandela Patrick and Dylan Campbell and Yuki M. Asano and Ishan Misra Florian Metze and Christoph Feichtenhofer and Andrea Vedaldi and Jo\ão F. Henriques},
   year={2021},
   booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
}
```

