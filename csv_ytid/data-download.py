import torchvision

dataset = torchvision.datasets.Kinetics(root="./", frames_per_clip=16, split = "test", download=True)

print("DONE!!")