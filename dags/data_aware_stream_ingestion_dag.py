import datetime

from airflow.decorators import dag
from airflow import Dataset
from airflow.providers.databricks.operators.databricks import (
   DatabricksSubmitRunDeferrableOperator,
)


stream_ingestion_dataset=Dataset("stream_ingestion_dataset")


@dag(
  dag_id="stream_ingestion_dag",
  start_date=datetime.datetime(2022, 12, 1),
  schedule="*/2 * * * *",
  catchup=False,
  max_active_runs=1,
  tags=["stream", "ingestion", "dependency"],
)
def stream_ingestion_dag_workflow():

    ingestion_task = DatabricksSubmitRunDeferrableOperator(
        task_id="ingestion_task",
       json="{...}",
       outlets=["stream_ingestion_dataset"],
    )


stream_ingestion_dag_workflow()
