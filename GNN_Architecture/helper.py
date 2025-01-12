
def get_model_size(given_model):
    param_size = 0
    for param in given_model.parameters():
        param_size += param.nelement() * param.element_size()

    buffer_size = 0
    for buffer in given_model.buffers():
        buffer_size += buffer.nelement() * buffer.element_size()

    size_all_mb = (param_size + buffer_size) / 1024**2
    print('model size: {:.3f}MB'.format(size_all_mb))
