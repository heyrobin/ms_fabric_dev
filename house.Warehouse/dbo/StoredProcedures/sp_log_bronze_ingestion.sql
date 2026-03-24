CREATE PROCEDURE dbo.sp_log_bronze_ingestion
(
    @table_name           VARCHAR(255),
    @pipeline_run_id      VARCHAR(255),
    @activity_name        VARCHAR(255),
    @status               VARCHAR(50),
    @rows_read            INT,
    @rows_written         INT,
    @error_message        VARCHAR(MAX),
    @execution_start_time DATETIME2(6),
    @execution_end_time   DATETIME2(6)
)
AS
BEGIN

    INSERT INTO dbo.bronze_ingestion_log
    (



        v_table_name,
        pipeline_run_id,
        activity_name,
        status,
        rows_read,
        rows_written,
        error_message,
        execution_start_time,
        execution_end_time
    )
    VALUES
    (
        @table_name,
        @pipeline_run_id,
        @activity_name,
        @status,
        @rows_read,
        @rows_written,
        @error_message,
        @execution_start_time,
        @execution_end_time
    );

END;