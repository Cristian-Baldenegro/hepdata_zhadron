Files used to generate submission tarball for HepData record of HIN-23-006, see latest sandbox area here: https://www.hepdata.net/record/sandbox/1750777869

I used `CMSSW_14_1_3` release. After `cmsenv`, you just run:

`python3 makeSubmissionTarball.py`

This will generate a tarball `submission.tar.gz` with the relevant .yaml and .yoda files, which can be uploaded to HepData directly.

More information on Lxplus or CMSSW-related setup here: https://hepdata-lib.readthedocs.io/en/latest/setup.html

CMS HIN HepData requirements here:  https://twiki.cern.ch/twiki/bin/viewauth/CMS/HIN-HEPData

