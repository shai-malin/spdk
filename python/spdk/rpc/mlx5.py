#  SPDX-License-Identifier: BSD-3-Clause
#  Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES.
#  All rights reserved.

from spdk.rpc.helpers import deprecated_alias


def mlx5_scan_accel_module(client, qp_size=None, num_requests=None, enable_crypto=None, use_crypto_mb=None, split_mb_blocks=None):
    """Enable mlx5 accel module. Scans all mlx5 devices which can perform needed operations

    Args:
        qp_size: Qpair size. (optional)
        num_requests: size of a global requests pool per mlx5 device (optional)
        enable_crypto: enable crypto operations (optional)
    """
    params = {}

    if qp_size is not None:
        params['qp_size'] = qp_size
    if num_requests is not None:
        params['num_requests'] = num_requests
    if enable_crypto is not None:
        params['enable_crypto'] = enable_crypto
    if use_crypto_mb is not None:
        params['use_crypto_mb'] = use_crypto_mb
    if split_mb_blocks is not None:
        params['split_mb_blocks'] = split_mb_blocks
    return client.call('mlx5_scan_accel_module', params)
