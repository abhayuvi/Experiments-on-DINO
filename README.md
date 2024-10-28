This Repository is made to experiment with DINO object Detection pretrained model [Link]( https://github.com/IDEA-Research/DINO?tab=readme-ov-file ).
Here, DINO object Detection pre-trained model is been fine-tuned on pedestrian dataset collected within the IIT Delhi Campus.

- As macos does not come with Nvidia 'CuDa' , so the code is written in the Google colab environment.

Instructions:-

- Get access to GPU .
  
- clone the repository and setup that on your environment.
  
- Install the dependencies and test the setup.
  
- this will require yaml version 0.31.0 , so install it through this command. '!pip install yapf==0.31.0'

- Download the pre-trained DINO-4scale model with the ResNet-50 (R50) from [DINO](https://drive.google.com/drive/folders/1qD5m1NmK0kjE5hh-G17XUX751WsEG-h_)

- Download the Pedestrain dataset from [Dataset](https://drive.google.com/drive/folders/1DCpmo919b7OrAng9clEbiMHjO3D0hyoa?usp=sharing)

- setup the dataset in COCODIR format , As:-

      COCODIR/
        ├── train2017/
        ├── val2017/
        └── annotations/
        	├── instances_train2017.json
        	└── instances_val2017.json


- After setting up the directory and repository , Evaluate the model on the validation set and visualize the Results.

- Train / Fine-Tune the model with the training set and Re-evaluate the model and note the changes .

- One will need to make changes in the config file (DINO/config/DINO_4scale.py) to fine-tune it .

- To leverage our pre-trained models for model fine-tuning, we suggest add two more commands in a bash:

      --pretrain_model_path /path/to/a/pretrianed/model. specify a pre-trained model.
      --finetune_ignore label_enc.weight class_embed. ignore some inconsistent parameters.



After completing every steps , i made a small report which states the model working , analysis , challenges faced... 
link:- [Google Drive Link]()


Experiments done:- 
- changed the weights of the pre-trained model.

  
- changed parameters like :
-     num_classes
-     dn_labebook_size
-     name_id

  
