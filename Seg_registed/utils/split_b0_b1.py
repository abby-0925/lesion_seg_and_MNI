import os,shutil
import nibabel as nib
import numpy as np
paths= "/data/workspace/Personal_Inference_SOP/data/LT3001_phaes2_supple/Raw_nii/"
target_path = "/data/workspace/Personal_Inference_SOP/data/LT3001_phaes2_supple/Raw_DWI_b1000/"
for file in os.listdir(paths):
    img = nib.load(os.path.join(paths, file))
    data = img.get_fdata()
    affine = img.affine
    data_shape = data.shape
    if len(data_shape) == 3:
        shutil.copyfile(os.path.join(paths, file), os.path.join(target_path, file.replace('.nii.gz','-b1000.nii.gz')))
        print(data_shape, "Only B1000")
    else:
        print(data_shape, "shape")
        data1 = data[:,:,:,0]
        data2 = data[:,:,:,1]
        print(data1.shape, data2.shape)
        print(np.mean(data1), np.mean(data2))
        
        if np.mean(data1) < np.mean(data2):
            suffix_name1 = '-b1000'
            suffix_name2 = '-b0'
            file_name1 = file.replace('.nii.gz', suffix_name1 + '.nii.gz')
            nib.Nifti1Image(data1,affine).to_filename(os.path.join(target_path, file_name1))

        else:
            suffix_name1 = '-b0'
            suffix_name2 = '-b1000'
            file_name2 = file.replace('.nii.gz', suffix_name2 + '.nii.gz')
            nib.Nifti1Image(data2,affine).to_filename(os.path.join(target_path, file_name2))
        # file_name2 = file.replace('.nii.gz', suffix_name2 + '.nii.gz')
        # nib.Nifti1Image(data2,affine).to_filename(os.path.join(target_path, file_name2))

        
    
    