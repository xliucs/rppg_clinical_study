DEFAULT_CONFIG = {
    "prefix": "ppg_bp",
    "manual_seed": 6666,
    # "dataset_list_path": "/data/docker/machengqian/dataset/flicker_div_ffhq_data_patch_list.txt",
    "bp_csv_path": "/gscratch/ubicomp/cm74/clinical_data/BPData_230103.csv",
    "train_dataset_path": "/gscratch/ubicomp/cm74/bp/ppg_bp/uwppg_bp_train_fold_5.txt",
    "val_dataset_path": "/gscratch/ubicomp/cm74/bp/ppg_bp/uwppg_bp_val_fold_5.txt",
    "batch_size": 16,
    "num_workers": 16,
    "chunk_amount": 5,
    "chunk_length": 512,
    "filter_lpf": 0.7,
    "filter_hpf": 10,
    "frequency_sample": 60,
    "frequency_field": False,
    "derivative_input": False,
    "network": {
        "scale": 1,
        "pretrained": None,
    },
    "loss": "",
    "gpus": [0, 1],
    "learning_rate": 0.001,
    "scheduler_milestones": [50, 200, 500],
    "scheduler_gamma": 0.5,
    "steps_val": 20,
    "output_dir": "output/20230110_v1_fold5",
    "dist": True
}

TEST_CONFIG = {
    "prefix": "ppg_bp",
    "manual_seed": 6666,
    # "dataset_list_path": "/data/docker/machengqian/dataset/flicker_div_ffhq_data_patch_list.txt",
    "bp_csv_path": "/gscratch/ubicomp/cm74/clinical_data/BPData_230103.csv",
    "train_dataset_path": "/gscratch/ubicomp/cm74/bp/ppg_bp/uwppg_bp_train_72.txt",
    "val_dataset_path1": "/gscratch/ubicomp/cm74/bp/ppg_bp/uwppg_bp_palm_val_fold_1.txt",
    "val_dataset_path2": "/gscratch/ubicomp/cm74/bp/ppg_bp/uwppg_bp_palm_val_fold_2.txt",
    "val_dataset_path3": "/gscratch/ubicomp/cm74/bp/ppg_bp/uwppg_bp_palm_val_fold_3.txt",
    "val_dataset_path4": "/gscratch/ubicomp/cm74/bp/ppg_bp/uwppg_bp_palm_val_fold_4.txt",
    "val_dataset_path5": "/gscratch/ubicomp/cm74/bp/ppg_bp/uwppg_bp_palm_val_fold_5.txt",
    "num_workers": 16,
    "chunk_amount": 5,
    "chunk_length": 512,
    "filter_lpf": 0.7,
    "filter_hpf": 10,
    "frequency_sample": 60,
    "frequency_field": False,
    "derivative_input": False,
    "loss": "",
    "gpus": [0, 1],
    "learning_rate": 0.001,
    "scheduler_milestones": [50, 200, 500],
    "scheduler_gamma": 0.5,
    "steps_val": 20,
    "output_dir": "output/20230110_test_v2",
    "dist": True
}