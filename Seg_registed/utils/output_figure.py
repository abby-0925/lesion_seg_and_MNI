import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import os
import matplotlib


    
    
def plot_seg_result(b1_file, seg_file, output_dir=None):
    b1_data = nib.load(b1_file).get_fdata()
    seg_data = nib.load(seg_file).get_fdata()
    print(b1_data.shape, seg_data.shape)
    slice_number = b1_data.shape[-1]
    print(slice_number)
    
    # process b1 data
    b1_data = np.transpose(b1_data, (1,0,2))
    b1_data = np.flip(b1_data, 0)
    
    # process seg data
    seg_data = np.transpose(seg_data, (1,0,2))
    seg_data = np.flip(seg_data,0)
    
    matplotlib.use('AGG')
    fig = plt.figure(figsize=(3, slice_number))
    
    j = 1
    for i in range(1, slice_number):
        
        # plot b1 image
        ax = fig.add_subplot(slice_number, 3, j)
        plt.axis("off")
        plt.imshow(np.float32(b1_data[:,:,i-1]), cmap="gray")
        j+=1
        
        # plot seg image
        ax = fig.add_subplot(slice_number, 3, j)
        plt.axis("off")
        plt.imshow(np.float32(seg_data[:,:,i-1]), cmap="gray")
        j+=1
        
        # plot overlap seg image and b1 image
        ax = fig.add_subplot(slice_number, 3, j)
        plt.axis("off")
        plt.imshow(np.float32(b1_data[:,:,i-1]), cmap="gray")
        plt.imshow(np.float32(seg_data[:,:,i-1]), cmap="Reds", alpha=0.8)
        j+=1
        
    plt.subplots_adjust(wspace=0.0, hspace=0.2)    
    plt.savefig(output_dir, dpi=300)
    plt.close(fig)

if __name__ == "__main__":
    seg_path = "/data/workspace/Personal_Inference_SOP/data/LT3001_phaes2_supple/seg_nii/"
    b1_path = "/data/workspace/Personal_Inference_SOP/data/LT3001_phaes2_supple/Raw_DWI_b1000/"
    target_path = "/data/workspace/Personal_Inference_SOP/data/LT3001_phaes2_supple/QC_figure/"
    
    seg_list = sorted(os.listdir(seg_path))
    b1_list = sorted(os.listdir(b1_path))
    print(len(seg_list), len(b1_list))

    for idx in range(len(seg_list)):
        seg_file_name = seg_list[idx]
        b1_file_name = b1_list[idx]
        print(seg_list[idx], b1_list[idx])
        assert b1_file_name[:10] == seg_file_name[:10]
        
        b1_file_path = os.path.join(b1_path, b1_file_name)
        seg_file_path = os.path.join(seg_path, seg_file_name)
        output_file_name = os.path.join(target_path,b1_file_name.replace(".nii.gz",".png"))
        plot_seg_result(b1_file_path, seg_file_path, output_file_name)
