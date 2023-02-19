from keras.utils.data_utils import get_file

def download_and_cache_file(subject_id, experiment_suffix="Color116ms"):
    if subject_id == '1':
        url_format = "https://www.kaggle.com/datasets/rramele/p300samplingdataset?select=P300S01.mat"
    elif subject_id == '2':
        url_format = "https://www.kaggle.com/datasets/rramele/p300samplingdataset?select=P300S02.mat"
    elif subject_id == '3':
        url_format = "https://www.kaggle.com/datasets/rramele/p300samplingdataset?select=P300S03.mat"
    elif subject_id == '4':
        url_format = "https://www.kaggle.com/datasets/rramele/p300samplingdataset?select=P300S04.mat"
    elif subject_id == '5':
        url_format = "https://www.kaggle.com/datasets/rramele/p300samplingdataset?select=P300S05.mat"
    elif subject_id == '6':
        url_format = "https://www.kaggle.com/datasets/rramele/p300samplingdataset?select=P300S06.mat"
    elif subject_id == '7':
        url_format = "https://www.kaggle.com/datasets/rramele/p300samplingdataset?select=P300S07.mat"
    elif subject_id == '8':
        url_format = "https://www.kaggle.com/datasets/rramele/p300samplingdataset?select=P300S08.mat"
    else:
        raise Exception("subject not familiar")
    url = url_format.format(experiment_suffix, subject_id)

    file_name = url.split("/")[-1]
    return get_file(file_name, url, cache_subdir="p300_lstm")
