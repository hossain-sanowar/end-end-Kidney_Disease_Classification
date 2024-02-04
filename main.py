from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


#data ingestion pipeline
STAGE_NAME = "Data Ingestion stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started<<<<<<<<<<<<<")
        data_ingestion=DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed<<<<<<<<<<<\n\nx====================X")
    except Exception as e:
        logger.exception(e)
        raise e

#prepare base model pipeline       
STAGE_NAME = "Prepare base model"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started<<<<<<<<<<<<<")
        prepare_base_model=PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed<<<<<<<<<<<\n\nx====================X")
    except Exception as e:
        logger.exception(e)
        raise e
        
#Model training      
STAGE_NAME = "Model Training"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started<<<<<<<<<<<<<")
        model_training=ModelTrainingPipeline()
        model_training.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed<<<<<<<<<<<\n\nx====================X")
    except Exception as e:
        logger.exception(e)
        raise e
        
#Model Evaluation     

STAGE_NAME = "Model Evaluation"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started<<<<<<<<<<<<<")
        model_evaluation=EvaluationPipeline()
        model_evaluation.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed<<<<<<<<<<<\n\nx====================X")
    except Exception as e:
        logger.exception(e)
        raise e