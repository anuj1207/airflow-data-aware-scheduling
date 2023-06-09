import datetime

from airflow.decorators import dag
from airflow import Dataset
from airflow.providers.databricks.operators.databricks import (
   DatabricksSubmitRunDeferrableOperator,
)


#Suggestion: create the following datasets in a common place and import from there in here and depedency DAGs
stream_ingestion_dataset=Dataset("stream_ingestion_dataset")
batch_ingestion_dataset=Dataset("batch_ingestion_dataset")


@dag(
  dag_id="analyzer_app_dag",
  start_date=datetime.datetime(2022, 12, 1),
  schedule=[stream_ingestion_dataset, batch_ingestion_dataset],
  catchup=False,
  max_active_runs=1,
  tags=["analyzer", "dependent"],
)
def analyzer_app_dag_workflow():
    actual_task = DatabricksSubmitRunDeferrableOperator(
     ...
    )

analyzer_app_dag_workflow()
