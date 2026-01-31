import numpy as np

def alexnet_conv1(image: np.ndarray) -> np.ndarray:
    """AlexNet first conv layer: 11x11, stride 4, 96 filters (shape simulation)."""
    # YOUR CODE HERE
    # image - (m,n_h_prev,n_w_prev,n_c_prev) m-> no. of eg
    (m,n_h_prev,n_w_prev,n_c_prev) = image.shape
    # print(f"{m}, {n_h_prev} , {n_w_prev} , {n_c_prev}")
    # 96 filters are there
    filters = 96
    # all filters are of 11 x 11 x 3
    f = 11
    # stride
    stride = 4
    # padding
    pad = 2

    n_h = int(((n_h_prev - f + 2*pad)/stride)) + 1
    n_w = int(((n_w_prev - f + 2*pad)/stride)) + 1
    n_c = filters
    # output will be (m,n_h,n_w,n_c)
    z = np.zeros((m,n_h,n_w,n_c))
    return z
    # for each example 
    # for i in range(m):
    #     # for each filter
    #     for fil in range(filters):
    #         filt = np.random.randn(f,f,n_c)
    #         for h in range(n_h):
    #             vert_start = stride*h
    #             vert_end = vert_start + f
    #             for w in range(n_w):
    #                 hor_start = stride*h
    #                 hor_end = hor_start + f
    #                 for c in range(n_c_prev):
    #                     out = image[i,vert_start:vert_end,hor_start:hor_end,c] * filt[:,:,c]
    #                     z[i]



    pass