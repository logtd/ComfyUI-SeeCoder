


seecoder_decoder_config = {
    'inchannels': {
        'res3': 384,
        'res4': 768,
        'res5': 1536
    },
    'trans_input_tags': ['res3', 'res4', 'res5'],
    'trans_dim': 768,
    'trans_dropout': 0.1,
    'trans_nheads': 8,
    'trans_feedforward_dim': 1024,
    'trans_num_layers': 6
}

seecoder_query_config = {
    'in_channels' : 768,
    'hidden_dim': 768,
    'num_queries': [4, 144],
    'nheads': 8,
    'num_layers': 9,
    'feedforward_dim': 2048,
    'pre_norm': False,
    'num_feature_levels': 3,
    'enforce_input_project': False,
    'with_fea2d_pos': False
}

# Not used
seecoder_query_pa_config = {
    **seecoder_query_config,
    'with_fea2d_pos': True
}

swin_config = {
    'embed_dim': 128,
    'depths': [ 2, 2, 18, 2 ],
    'num_heads': [ 4, 8, 16, 32 ],
    'window_size': 7,
    'ape': False,
    'drop_path_rate': 0.3,
    'patch_norm': True,
}

swin_large_config = {
    **swin_config,
    'embed_dim': 192,
    'depths': [ 2, 2, 18, 2 ],
    'num_heads': [ 6, 12, 24, 48 ],
    'window_size': 12,
    'ape': False,
    'drop_path_rate': 0.3,
    'patch_norm': True,
}