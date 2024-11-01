import os 

#PATTERN = "../../output/20241027/{}/no_control/{}/no_control/0.0001/chk{}/lightning_logs/version_87762"
#PATTERN = "../../output/20241025/{}/shcoeff2/{}/no_control/1e-4/chk{}/lightning_logs/version_0"
PATTERN = "../../output/20241025/{}/shcoeff2/{}/no_control/1e-4/chk{}/lightning_logs/version_0"
A = "val_coeff27_faceval10k_fuse_test_right"
B = "1.0"
C = "0"

MODES = ["val_face_test_left", "val_face_test_right"]
GUIDANCES = ["1.0","3.0","5.0","7.0"]
CHECKPOINTS = ["9","19","29","39","49"]

for mode in MODES:
    for guidance in GUIDANCES:
        for ckpt in CHECKPOINTS:
            main_dir = PATTERN.format(mode,guidance,ckpt) 
            # if not os.path.exists(main_dir):
            #     print("SKIP: ", main_dir)
            #     continue
            input_dir = main_dir + "/crop_image"
            output_dir = main_dir + "/face_light"
            os.system(f"python demos/demo_reconstruct.py -i /data/pakkapon/datasets/face/face_roll60_v5/images -s /tmp/output")
            exit()