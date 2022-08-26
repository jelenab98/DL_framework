import time
import torch
import torchvision


def measure_fps(model, n=1000, test_dims=(1024, 2048)):
    h, w = test_dims
    model.eval()
    model.cuda()
    with torch.no_grad():
        data = torch.randn(1, 3, h, w).cuda()
        for _ in range(50):                     # warmup
            logits = model.forward(data)
        torch.cuda.synchronize()
        t0 = time.perf_counter()
        for _ in range(n):
            logits = model.forward(data)
            # _, pred = logits.max(1)
            # out = pred.data.byte().cpu()
            torch.cuda.synchronize()
        t1 = time.perf_counter()
        fps = n / (t1 - t0)
    return fps


def measure_train_fps(model, n=100, test_dims=(1024, 2048)):
    h, w = test_dims
    model.cuda()
    data = torch.randn(1, 3, h, w).cuda()
    data_2 = torch.ones(1,).cuda().type(torch.cuda.LongTensor)

    for _ in range(50):                         # warmup
        logits = model.forward(data)

    torch.cuda.synchronize()
    t0 = time.perf_counter()
    for _ in range(n):
        logits = model.forward(data)
        loss = criterion(logits, data_2)
        loss.backward()
    torch.cuda.synchronize()
    t1 = time.perf_counter()
    fps = n / (t1 - t0)
    return fps


if __name__ == '__main__':
    model = torchvision.models.resnet50(pretrained=False, num_classes=10)
    criterion = torch.nn.CrossEntropyLoss()
    model.cuda()
    print(f"Inference fps: {measure_fps(model):.2f}")
    print(f"Train fps: {measure_train_fps(model)}")

