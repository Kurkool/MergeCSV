echo Start --- MergeCSVprocess ---
set matchingCol="Citizen ID"
"..\Merge_CSV\dist\Merge_CSV\Merge_CSV.exe" %matchingCol%

echo Start --- salesforceupsertprocess --

java -cp ..\dataloader_win\dataloader-51.0.1-uber.jar -Dsalesforce.config.dir=..\Merge_CSV com.salesforce.dataloader.process.ProcessRunner process.name=salesforceupsertprocess

IF ERRORLEVEL 0 echo success
IF NOT ERRORLEVEL 0 echo fail
