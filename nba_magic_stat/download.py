import kaggle 

from nba_magic_stat import conf, logger


def download_data():
    dataset_name = conf.data.kaggle_dataset
    logger.debug(f"Downloading kaggle dataset {dataset_name}...")
    kaggle.api.dataset_download_files(dataset_name, path="./data/")
    #kaggle.api.dataset_download_file(dataset, file_name, path=None, force=False, quiet=True):