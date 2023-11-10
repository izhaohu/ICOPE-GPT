import subprocess

conda_path = '/home/caregpt/anaconda3/envs/care3/bin/python3'  # 更新为你的conda路径
environment_name = 'care3'
script_path = '/home/caregpt/anaconda3/envs/care3/lib/python3.8/site-packages/paddleocr/ppstructure/predict_system.py'  # 更新为你的脚本路径
arg1 = '--image_dir=./input/老年长期照护与康复指导手册 - 缪荣明.pdf'
arg2 = '--recovery=True'
arg3 = '--rec_model_dir=inference/en_PP-OCRv3_rec_infer'
arg4 = '--rec_char_dict_path=../ppocr/utils/en_dict.txt'
arg5 = '--table_model_dir=inference/en_ppstructure_mobile_v2.0_SLANet_infer'
arg6 = '--table_char_dict_path=../ppocr/utils/dict/table_structure_dict.txt'
arg7 = '--layout_model_dir=inference/picodet_lcnet_x1_0_fgd_layout_infer'
arg8 = '--layout_dict_path=../ppocr/utils/dict/layout_dict/layout_publaynet_dict.txt'
arg9 = '--vis_font_path=../doc/fonts/simfang.ttf'
arg10 = '--recovery=True'
arg11 = '--output=./output/老年长期照护与康复指导手册ppstructure.docx'

subprocess.call([conda_path, script_path, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11])

# image_dir：测试文件，可以是图片、图片目录、pdf文件、pdf文件目录
# det_model_dir：OCR检测模型路径
# rec_model_dir：OCR识别模型路径
# rec_char_dict_path：OCR识别字典，如果更换为中文模型，需要更改为"../ppocr/utils/ppocr_keys_v1.txt"，如果您在自己的数据集上训练的模型，则更改为训练的字典的文件
# table_model_dir：表格识别模型路径
# table_char_dict_path：表格识别字典，如果更换为中文模型，不需要更换字典
# layout_model_dir：版面分析模型路径
# layout_dict_path：版面分析字典，如果更换为中文模型，需要更改为"../ppocr/utils/dict/layout_dict/layout_cdla_dict.txt"
# recovery：是否进行版面恢复，默认False
# output：版面恢复结果保存路径