import datetime

from airflow.decorators import dag
from airflow import Dataset
from airflow.providers.databricks.operators.databricks import (
   DatabricksSubmitRunDeferrableOperator,
)


batch_ingestion_dataset=Dataset("batch_ingestion_dataset")


@dag(
  dag_id="batch_ingestion_dag",
  start_date=datetime.datetime(2022, 12, 1),
  schedule="*/2 * * * *",
  catchup=False,
  max_active_runs=1,
  tags=["batch", "ingestion", "dependency"],
)
def batch_ingestion_dag_workflow():
    ingestion_task = DatabricksSubmitRunDeferrableOperator(
        task_id="ingestion_task",
        json="{...}",
        outlets=["batch_ingestion_dataset"],
    )


batch_ingestion_dag_workflow()
