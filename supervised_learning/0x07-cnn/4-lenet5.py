#!/usr/bin/env python3
"""Lenet-5 cnn module"""

import tensorflow as tf


def lenet5(x, y):
    """
    Builds a modified version of the LeNet-5 architecture using tensorflow
        :param x: tf.placeholder of shape (m, 28, 28, 1)
        containing the input images for the network
        :param y: tf.placeholder of shape (m, 10)
        containing the one-hot labels for the network
        :returns Returns: a tensor for the softmax activated output
        a training operation that utilizes Adam optimization
        (with default hyperparameters)
        a tensor for the loss of the netowrk
        a tensor for the accuracy of the network
    """
    m, h_new, w_new, c_new = dA.shape
    _, h_prev, w_prev, c = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride

    dA_prev = np.zeros(A_prev.shape)

    for m in range(m):
        for h in range(h_new):
            for w in range(w_new):
                i = h * sh
                j = w * sw
                for c in range(c_new):
                    frame = A_prev[m, i: i + kh, j: j + kw, c]

                    if mode == 'max':
                        kernel = np.zeros(kernel_shape)
                        frame_max = np.amax(frame)
                        np.copyto(kernel, 1, where=(frame == frame_max))
                        dA_prev[m, i: i + kh, j: j + kw, c] +=\
                            kernel * dA[m, h, w, c]
                    elif mode == 'avg':
                        avg = dA[m, h, w, c] / kh / kw
                        kernel = np.ones(kernel_shape)
                        dA_prev[m, i: i + kh, j: j + kw, c] += avg * kernel

    return dA_prev
