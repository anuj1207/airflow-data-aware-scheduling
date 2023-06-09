import datetime

from airflow.decorators import dag
from airflow import Dataset
from data_aware_batch_ingestion_dag import batch_ingestion_dataset
from data_aware_stream_ingestion_dag import stream_ingestion_dataset
from airflow.providers.databricks.operators.databricks import (
   DatabricksSubmitRunDeferrableOperator,
)


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
