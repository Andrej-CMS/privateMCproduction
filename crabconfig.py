from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "privateMCProduction"
config.General.workArea = 'crab_privateMCProduction'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'pythonLHEGENFilter2_cfg.py'
config.JobType.inputFiles = ["run_generic_tarball_cvmfs_modified.sh"]
config.JobType.disableAutomaticOutputCollection = False
config.JobType.outputFiles = ["eventLHEGEN-output_inLHE.root","eventLHEGEN-output.root"]

config.section_("Data")
config.Data.outputPrimaryDataset = 'privateMCProductionLHEGEN'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 5
config.Data.totalUnits = 5
config.Data.publication = False
config.Data.outputDatasetTag = 'eventLHEGEN'

config.section_("Site")
config.Site.storageSite = 'T2_DE_DESY'

config.section_("User")
config.User.voGroup = "dcms"
