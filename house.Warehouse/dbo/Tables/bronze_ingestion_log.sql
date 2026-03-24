CREATE TABLE [dbo].[bronze_ingestion_log] (

	[v_table_name] varchar(255) NULL, 
	[pipeline_run_id] varchar(255) NULL, 
	[activity_name] varchar(255) NULL, 
	[status] varchar(50) NULL, 
	[rows_read] int NULL, 
	[rows_written] int NULL, 
	[error_message] varchar(max) NULL, 
	[execution_start_time] datetime2(6) NULL, 
	[execution_end_time] datetime2(6) NULL
);