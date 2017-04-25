# FPO configuration profile
# See https://www.ibm.com/developerworks/community/wikis/form/anonymous/api/wiki/fa32927c-e904-49cc-a4cc-870bcc8e307c/page/c90999f2-60cd-4f6f-8430-29efb5f01c3b/attachment/71e2e956-e73c-44c4-b76f-00c8096dffd2/media/Spectrum%20Scale%20Shared%20Nothing%20Cluster%20Performance%20Tuning%20Guide_V0.7.pdf

%cluster:
  maxblocksize=16M
  restripeOnDiskFailure=yes
  unmountOnDiskFail=meta
  readReplicaPolicy=local
  nsdThreadsPerQueue=10
  nsdMinWorkerThreads=48
  nsdThreadsPerDisk=18
  nsdSmallThreadRatio=2
  workerThreads=128
  maxStatCache=512
  maxFilesToCache=64k
  ignorePrefetchLUNCount=yes
  prefetchaggressivenesswrite=0
  prefetchaggressivenessread=2
