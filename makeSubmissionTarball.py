from hepdata_lib import Submission
from hepdata_lib import Submission, Variable, Table
from hepdata_lib import Uncertainty


submission = Submission()
submission.read_abstract("example_inputs/abstract.txt")
submission.add_link("Webpage with all figures and tables", "https://cms-results.web.cern.ch/cms-results/public-results/publications/HIN-23-006/")
submission.add_record_id(1234567, "inspire")
submission.add_link("arXiv", "http://arxiv.org/abs/arXiv:2504.XXXX")

from hepdata_lib import RootFileReader

#  KEY: TH1D	H1_clone__6;1	
#  KEY: TH1D	hDiffSys_0_0__13;1	
#  KEY: TH1D	H11_clone__20;1	
#  KEY: TH1D	hDiffSys_1_0__27;1	
#  KEY: TH1D	H21_clone__34;1	
#  KEY: TH1D	hDiffSys_2_0__41;1

reader_pp_pT1to2_deltaPhi= RootFileReader("deltaPhiPP.root")
pp_pT1to2_deltaPhi= reader_pp_pT1to2_deltaPhi.read_hist_1d("H1_clone__6")

x_pp_pT1to2_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_pp_pT1to2_deltaPhi.values = pp_pT1to2_deltaPhi["x_edges"]
x_pp_pT1to2_deltaPhi.values = [(round(elem,2), round(elem2,2)) for elem, elem2 in pp_pT1to2_deltaPhi["x_edges"]]

y_pp_pT1to2_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)
arr_pp_pT1to2_deltaPhi = pp_pT1to2_deltaPhi["y"]
arr_pp_pT1to2_deltaPhi[0:5] = arr_pp_pT1to2_deltaPhi[5:10][::-1]
arr_pp_pT1to2_deltaPhi[15:20] = arr_pp_pT1to2_deltaPhi[10:15][::-1]
y_pp_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_pp_pT1to2_deltaPhi]

stats_pp_pT1to2_deltaPhi= Uncertainty("Stat.", is_symmetric=True)
arr_pp_pT1to2_deltaPhi_dy = pp_pT1to2_deltaPhi["dy"]
arr_pp_pT1to2_deltaPhi_dy[0:5] = arr_pp_pT1to2_deltaPhi_dy[5:10][::-1]
arr_pp_pT1to2_deltaPhi_dy[15:20] = arr_pp_pT1to2_deltaPhi_dy[10:15][::-1]
stats_pp_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_pp_pT1to2_deltaPhi_dy]
y_pp_pT1to2_deltaPhi.add_uncertainty(stats_pp_pT1to2_deltaPhi)

systHist_pp_pT1to2_deltaPhi= reader_pp_pT1to2_deltaPhi.read_hist_1d("hDiffSys_0_0__13")
syst_pp_pT1to2_deltaPhi= Uncertainty("Syst.", is_symmetric=True)
arr_systHist_pp_pT1to2_deltaPhi = systHist_pp_pT1to2_deltaPhi["dy"]
arr_systHist_pp_pT1to2_deltaPhi[0:5] = arr_systHist_pp_pT1to2_deltaPhi[5:10][::-1]
arr_systHist_pp_pT1to2_deltaPhi[15:20] = arr_systHist_pp_pT1to2_deltaPhi[10:15][::-1]
syst_pp_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_pp_pT1to2_deltaPhi]
y_pp_pT1to2_deltaPhi.add_uncertainty(syst_pp_pT1to2_deltaPhi)

y_pp_pT1to2_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_pp_pT1to2_deltaPhi.add_qualifier("PTCH", "1 < $p_{T}^{ch}$ < 2 GeV")
y_pp_pT1to2_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_pp_pT1to2_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_pp_pT1to2_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_pp_pT1to2_deltaPhi.add_qualifier("RE", "pp --> Z + X")

table_pp_pT1to2_deltaPhi = Table("$\Delta\phi_{ch,Z}$ spectra in pp for $1 < p_T < 2$ GeV")
for var in [x_pp_pT1to2_deltaPhi,y_pp_pT1to2_deltaPhi]:
        table_pp_pT1to2_deltaPhi.add_variable(var)
table_pp_pT1to2_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $1 <p_T < 2$ GeV in pp collisions."
table_pp_pT1to2_deltaPhi.location = "Corresponds to upper left panel of Figure 1."
table_pp_pT1to2_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_pp_pT1to2_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_pp_pT1to2_deltaPhi.keywords["reactions"] = ["pp --> Z+X"]
table_pp_pT1to2_deltaPhi.keywords["cmenergies"] = ["5020"]


reader_pp_pT2to4_deltaPhi = RootFileReader("deltaPhiPP.root")
pp_pT2to4_deltaPhi = reader_pp_pT2to4_deltaPhi.read_hist_1d("H11_clone__20")

x_pp_pT2to4_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_pp_pT2to4_deltaPhi.values = pp_pT2to4_deltaPhi["x_edges"]
x_pp_pT2to4_deltaPhi.values = [(round(elem,2), round(elem2,2)) for elem, elem2 in pp_pT2to4_deltaPhi["x_edges"]]

y_pp_pT2to4_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)
arr_pp_pT2to4_deltaPhi = pp_pT2to4_deltaPhi["y"]
arr_pp_pT2to4_deltaPhi[0:5] = arr_pp_pT2to4_deltaPhi[5:10][::-1]
arr_pp_pT2to4_deltaPhi[15:20] = arr_pp_pT2to4_deltaPhi[10:15][::-1]
y_pp_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_pp_pT2to4_deltaPhi]

stats_pp_pT2to4_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_pp_pT2to4_deltaPhi_dy = pp_pT2to4_deltaPhi["dy"]
arr_pp_pT2to4_deltaPhi_dy[0:5] = arr_pp_pT2to4_deltaPhi_dy[5:10][::-1]
arr_pp_pT2to4_deltaPhi_dy[15:20] = arr_pp_pT2to4_deltaPhi_dy[10:15][::-1]
stats_pp_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_pp_pT2to4_deltaPhi_dy]
y_pp_pT2to4_deltaPhi.add_uncertainty(stats_pp_pT2to4_deltaPhi)

systHist_pp_pT2to4_deltaPhi = reader_pp_pT2to4_deltaPhi.read_hist_1d("hDiffSys_0_0__13")
syst_pp_pT2to4_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_pp_pT2to4_deltaPhi = systHist_pp_pT2to4_deltaPhi["dy"]
arr_systHist_pp_pT2to4_deltaPhi[0:5] = arr_systHist_pp_pT2to4_deltaPhi[5:10][::-1]
arr_systHist_pp_pT2to4_deltaPhi[15:20] = arr_systHist_pp_pT2to4_deltaPhi[10:15][::-1]
syst_pp_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_pp_pT2to4_deltaPhi]
y_pp_pT2to4_deltaPhi.add_uncertainty(syst_pp_pT2to4_deltaPhi)


y_pp_pT2to4_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_pp_pT2to4_deltaPhi.add_qualifier("PTCH", "2 < $p_{T}^{ch}$ < 4 GeV")
y_pp_pT2to4_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_pp_pT2to4_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_pp_pT2to4_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_pp_pT2to4_deltaPhi.add_qualifier("RE", "pp --> Z + X")

table_pp_pT2to4_deltaPhi = Table("$\Delta\phi_{ch,Z}$ spectra in pp for $2 < p_T < 4$ GeV")
for var in [x_pp_pT2to4_deltaPhi, y_pp_pT2to4_deltaPhi]:
    table_pp_pT2to4_deltaPhi.add_variable(var)

table_pp_pT2to4_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $2 <p_T < 4$ GeV in pp collisions."
table_pp_pT2to4_deltaPhi.location = "Corresponds to upper middle panel of Figure 1."
table_pp_pT2to4_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_pp_pT2to4_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_pp_pT2to4_deltaPhi.keywords["reactions"] = ["pp --> Z+X"]
table_pp_pT2to4_deltaPhi.keywords["cmenergies"] = ["5020"]

reader_pp_pT4to10_deltaPhi = RootFileReader("deltaPhiPP.root")
pp_pT4to10_deltaPhi = reader_pp_pT4to10_deltaPhi.read_hist_1d("H21_clone__34")

x_pp_pT4to10_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_pp_pT4to10_deltaPhi.values = pp_pT4to10_deltaPhi["x_edges"]
x_pp_pT4to10_deltaPhi.values = [(round(elem,2), round(elem2,2)) for elem, elem2 in pp_pT4to10_deltaPhi["x_edges"]]

y_pp_pT4to10_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)
arr_pp_pT4to10_deltaPhi = pp_pT4to10_deltaPhi["y"]
arr_pp_pT4to10_deltaPhi[0:5] = arr_pp_pT4to10_deltaPhi[5:10][::-1]
arr_pp_pT4to10_deltaPhi[15:20] = arr_pp_pT4to10_deltaPhi[10:15][::-1]
y_pp_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_pp_pT4to10_deltaPhi]

stats_pp_pT4to10_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_pp_pT4to10_deltaPhi_dy = pp_pT4to10_deltaPhi["dy"]
arr_pp_pT4to10_deltaPhi_dy[0:5] = arr_pp_pT4to10_deltaPhi_dy[5:10][::-1]
arr_pp_pT4to10_deltaPhi_dy[15:20] = arr_pp_pT4to10_deltaPhi_dy[10:15][::-1]
stats_pp_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_pp_pT4to10_deltaPhi_dy]
y_pp_pT4to10_deltaPhi.add_uncertainty(stats_pp_pT4to10_deltaPhi)

systHist_pp_pT4to10_deltaPhi = reader_pp_pT4to10_deltaPhi.read_hist_1d("hDiffSys_0_0__13")
syst_pp_pT4to10_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_pp_pT4to10_deltaPhi = systHist_pp_pT4to10_deltaPhi["dy"]
arr_systHist_pp_pT4to10_deltaPhi[0:5] = arr_systHist_pp_pT4to10_deltaPhi[5:10][::-1]
arr_systHist_pp_pT4to10_deltaPhi[15:20] = arr_systHist_pp_pT4to10_deltaPhi[10:15][::-1]
syst_pp_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_pp_pT4to10_deltaPhi]
y_pp_pT4to10_deltaPhi.add_uncertainty(syst_pp_pT4to10_deltaPhi)


y_pp_pT4to10_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_pp_pT4to10_deltaPhi.add_qualifier("PTCH", "4 < $p_{T}^{ch}$ < 10 GeV")
y_pp_pT4to10_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_pp_pT4to10_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_pp_pT4to10_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_pp_pT4to10_deltaPhi.add_qualifier("RE", "pp --> Z + X")

table_pp_pT4to10_deltaPhi = Table("$\Delta\phi_{ch,Z}$ spectra in pp for $4 < p_T < 10$ GeV")
for var in [x_pp_pT4to10_deltaPhi, y_pp_pT4to10_deltaPhi]:
    table_pp_pT4to10_deltaPhi.add_variable(var)

table_pp_pT4to10_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $4 <p_T < 10$ GeV in pp collisions."
table_pp_pT4to10_deltaPhi.location = "Corresponds to upper right panel of Figure 1."
table_pp_pT4to10_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_pp_pT4to10_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_pp_pT4to10_deltaPhi.keywords["reactions"] = ["pp --> Z+X"]
table_pp_pT4to10_deltaPhi.keywords["cmenergies"] = ["5020"]



#PbPb 0to30 centrality


reader_PbPb0to30_pT1to2_deltaPhi = RootFileReader("deltaPhiPbPb030pp.root")
PbPb0to30_pT1to2_deltaPhi = reader_PbPb0to30_pT1to2_deltaPhi.read_hist_1d("H1_clone__5")

x_PbPb0to30_pT1to2_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb0to30_pT1to2_deltaPhi.values = PbPb0to30_pT1to2_deltaPhi["x_edges"]
x_PbPb0to30_pT1to2_deltaPhi.values = [(round(elem,3), round(elem2,3)) for elem, elem2 in PbPb0to30_pT1to2_deltaPhi["x_edges"]]

y_PbPb0to30_pT1to2_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)
arr_PbPb0to30_pT1to2_deltaPhi = PbPb0to30_pT1to2_deltaPhi["y"]  # optional, if you want to preserve the original
arr_PbPb0to30_pT1to2_deltaPhi[0:5] = arr_PbPb0to30_pT1to2_deltaPhi[5:10][::-1]
arr_PbPb0to30_pT1to2_deltaPhi[15:20] = arr_PbPb0to30_pT1to2_deltaPhi[10:15][::-1]
y_PbPb0to30_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb0to30_pT1to2_deltaPhi]

stats_PbPb0to30_pT1to2_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_PbPb0to30_pT1to2_deltaPhi_dy = PbPb0to30_pT1to2_deltaPhi["dy"]
arr_PbPb0to30_pT1to2_deltaPhi_dy[0:5] = arr_PbPb0to30_pT1to2_deltaPhi_dy[5:10][::-1]
arr_PbPb0to30_pT1to2_deltaPhi_dy[15:20] = arr_PbPb0to30_pT1to2_deltaPhi_dy[10:15][::-1]
stats_PbPb0to30_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in  arr_PbPb0to30_pT1to2_deltaPhi_dy]
y_PbPb0to30_pT1to2_deltaPhi.add_uncertainty(stats_PbPb0to30_pT1to2_deltaPhi)


systHist_PbPb0to30_pT1to2_deltaPhi = reader_PbPb0to30_pT1to2_deltaPhi.read_hist_1d("HSys1__4")
syst_PbPb0to30_pT1to2_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_PbPb0to30_pT1to2_deltaPhi = systHist_PbPb0to30_pT1to2_deltaPhi["dy"]
arr_systHist_PbPb0to30_pT1to2_deltaPhi[0:5] = arr_systHist_PbPb0to30_pT1to2_deltaPhi[5:10][::-1]
arr_systHist_PbPb0to30_pT1to2_deltaPhi[15:20] = arr_systHist_PbPb0to30_pT1to2_deltaPhi[10:15][::-1]
syst_PbPb0to30_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_PbPb0to30_pT1to2_deltaPhi]
y_PbPb0to30_pT1to2_deltaPhi.add_uncertainty(syst_PbPb0to30_pT1to2_deltaPhi)

y_PbPb0to30_pT1to2_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb0to30_pT1to2_deltaPhi.add_qualifier("PTCH", "1 < $p_{T}^{ch}$ < 2 GeV")
y_PbPb0to30_pT1to2_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb0to30_pT1to2_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb0to30_pT1to2_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb0to30_pT1to2_deltaPhi.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb0to30_pT1to2_deltaPhi.add_qualifier("CENTRALITY", "0--30")

table_PbPb0to30_pT1to2_deltaPhi = Table("$\Delta\phi_{ch,Z}$ in PbPb 0-30% for $1 < p_T < 2$ GeV")
for var in [x_PbPb0to30_pT1to2_deltaPhi, y_PbPb0to30_pT1to2_deltaPhi]:
    table_PbPb0to30_pT1to2_deltaPhi.add_variable(var)

table_PbPb0to30_pT1to2_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $1 <p_T < 2$ GeV in PbPb for centrality interval of 0-30% collisions."
table_PbPb0to30_pT1to2_deltaPhi.location = "Corresponds to upper left panel of Figure 1."
table_PbPb0to30_pT1to2_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_PbPb0to30_pT1to2_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb0to30_pT1to2_deltaPhi.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb0to30_pT1to2_deltaPhi.keywords["cmenergies"] = ["5020"]

reader_PbPb0to30_pT2to4_deltaPhi = RootFileReader("deltaPhiPbPb030pp.root")
PbPb0to30_pT2to4_deltaPhi = reader_PbPb0to30_pT2to4_deltaPhi.read_hist_1d("H5_clone__11")

x_PbPb0to30_pT2to4_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb0to30_pT2to4_deltaPhi.values = PbPb0to30_pT2to4_deltaPhi["x_edges"]
x_PbPb0to30_pT2to4_deltaPhi.values = [(round(elem,3), round(elem2,3)) for elem, elem2 in PbPb0to30_pT2to4_deltaPhi["x_edges"]]

y_PbPb0to30_pT2to4_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)
#y_PbPb0to30_pT2to4_deltaPhi.values = PbPb0to30_pT2to4_deltaPhi["y"]
arr_PbPb0to30_pT2to4_deltaPhi = PbPb0to30_pT2to4_deltaPhi["y"]
arr_PbPb0to30_pT2to4_deltaPhi[0:5] = arr_PbPb0to30_pT2to4_deltaPhi[5:10][::-1]
arr_PbPb0to30_pT2to4_deltaPhi[15:20] = arr_PbPb0to30_pT2to4_deltaPhi[10:15][::-1]
y_PbPb0to30_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb0to30_pT2to4_deltaPhi]

stats_PbPb0to30_pT2to4_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_PbPb0to30_pT2to4_deltaPhi_dy = PbPb0to30_pT2to4_deltaPhi["dy"]
arr_PbPb0to30_pT2to4_deltaPhi_dy[0:5] = arr_PbPb0to30_pT2to4_deltaPhi_dy[5:10][::-1]
arr_PbPb0to30_pT2to4_deltaPhi_dy[15:20] = arr_PbPb0to30_pT2to4_deltaPhi_dy[10:15][::-1]
stats_PbPb0to30_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb0to30_pT2to4_deltaPhi_dy]
y_PbPb0to30_pT2to4_deltaPhi.add_uncertainty(stats_PbPb0to30_pT2to4_deltaPhi)

systHist_PbPb0to30_pT2to4_deltaPhi = reader_PbPb0to30_pT2to4_deltaPhi.read_hist_1d("HSys1__4")
syst_PbPb0to30_pT2to4_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_PbPb0to30_pT2to4_deltaPhi = systHist_PbPb0to30_pT2to4_deltaPhi["dy"]
arr_systHist_PbPb0to30_pT2to4_deltaPhi[0:5] = arr_systHist_PbPb0to30_pT2to4_deltaPhi[5:10][::-1]
arr_systHist_PbPb0to30_pT2to4_deltaPhi[15:20] = arr_systHist_PbPb0to30_pT2to4_deltaPhi[10:15][::-1]
syst_PbPb0to30_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_PbPb0to30_pT2to4_deltaPhi]
y_PbPb0to30_pT2to4_deltaPhi.add_uncertainty(syst_PbPb0to30_pT2to4_deltaPhi)
y_PbPb0to30_pT2to4_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb0to30_pT2to4_deltaPhi.add_qualifier("PTCH", "2 < $p_{T}^{ch}$ < 4 GeV")
y_PbPb0to30_pT2to4_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb0to30_pT2to4_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb0to30_pT2to4_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb0to30_pT2to4_deltaPhi.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb0to30_pT2to4_deltaPhi.add_qualifier("CENTRALITY", "0--30")

table_PbPb0to30_pT2to4_deltaPhi = Table("$\Delta\phi_{ch,Z}$ in PbPb 0-30% for $2 < p_T < 4$ GeV")
for var in [x_PbPb0to30_pT2to4_deltaPhi, y_PbPb0to30_pT2to4_deltaPhi]:
    table_PbPb0to30_pT2to4_deltaPhi.add_variable(var)

table_PbPb0to30_pT2to4_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $2 <p_T < 4$ GeV in PbPb for centrality interval of 0-30% collisions."
table_PbPb0to30_pT2to4_deltaPhi.location = "Corresponds to upper middle panel of Figure 1."
table_PbPb0to30_pT2to4_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_PbPb0to30_pT2to4_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb0to30_pT2to4_deltaPhi.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb0to30_pT2to4_deltaPhi.keywords["cmenergies"] = ["5020"]

reader_PbPb0to30_pT4to10_deltaPhi = RootFileReader("deltaPhiPbPb030pp.root")
PbPb0to30_pT4to10_deltaPhi = reader_PbPb0to30_pT4to10_deltaPhi.read_hist_1d("H9_clone__17")

x_PbPb0to30_pT4to10_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb0to30_pT4to10_deltaPhi.values = PbPb0to30_pT4to10_deltaPhi["x_edges"]
x_PbPb0to30_pT4to10_deltaPhi.values = [(round(elem,3), round(elem2,3)) for elem, elem2 in PbPb0to30_pT4to10_deltaPhi["x_edges"]]

y_PbPb0to30_pT4to10_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)

arr_PbPb0to30_pT4to10_deltaPhi = PbPb0to30_pT4to10_deltaPhi["y"]
arr_PbPb0to30_pT4to10_deltaPhi[0:5] = arr_PbPb0to30_pT4to10_deltaPhi[5:10][::-1]
arr_PbPb0to30_pT4to10_deltaPhi[15:20] = arr_PbPb0to30_pT4to10_deltaPhi[10:15][::-1]
y_PbPb0to30_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb0to30_pT4to10_deltaPhi]

stats_PbPb0to30_pT4to10_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_PbPb0to30_pT4to10_deltaPhi_dy = PbPb0to30_pT4to10_deltaPhi["dy"]
arr_PbPb0to30_pT4to10_deltaPhi_dy[0:5] = arr_PbPb0to30_pT4to10_deltaPhi_dy[5:10][::-1]
arr_PbPb0to30_pT4to10_deltaPhi_dy[15:20] = arr_PbPb0to30_pT4to10_deltaPhi_dy[10:15][::-1]
stats_PbPb0to30_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb0to30_pT4to10_deltaPhi_dy]
y_PbPb0to30_pT4to10_deltaPhi.add_uncertainty(stats_PbPb0to30_pT4to10_deltaPhi)

systHist_PbPb0to30_pT4to10_deltaPhi = reader_PbPb0to30_pT4to10_deltaPhi.read_hist_1d("HSys1__4")
syst_PbPb0to30_pT4to10_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_PbPb0to30_pT4to10_deltaPhi = systHist_PbPb0to30_pT4to10_deltaPhi["dy"]
arr_systHist_PbPb0to30_pT4to10_deltaPhi[0:5] = arr_systHist_PbPb0to30_pT4to10_deltaPhi[5:10][::-1]
arr_systHist_PbPb0to30_pT4to10_deltaPhi[15:20] = arr_systHist_PbPb0to30_pT4to10_deltaPhi[10:15][::-1]
syst_PbPb0to30_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_PbPb0to30_pT4to10_deltaPhi]
y_PbPb0to30_pT4to10_deltaPhi.add_uncertainty(syst_PbPb0to30_pT4to10_deltaPhi)

y_PbPb0to30_pT4to10_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb0to30_pT4to10_deltaPhi.add_qualifier("PTCH", "4 < $p_{T}^{ch}$ < 10 GeV")
y_PbPb0to30_pT4to10_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb0to30_pT4to10_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb0to30_pT4to10_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb0to30_pT4to10_deltaPhi.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb0to30_pT4to10_deltaPhi.add_qualifier("CENTRALITY", "0--30")

table_PbPb0to30_pT4to10_deltaPhi = Table("$\Delta\phi_{ch,Z}$ in PbPb 0-30% for $4 < p_T < 10$ GeV")
for var in [x_PbPb0to30_pT4to10_deltaPhi, y_PbPb0to30_pT4to10_deltaPhi]:
    table_PbPb0to30_pT4to10_deltaPhi.add_variable(var)

table_PbPb0to30_pT4to10_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $4 <p_T < 10$ GeV in PbPb for centrality interval of 0-30% collisions."
table_PbPb0to30_pT4to10_deltaPhi.location = "Corresponds to upper right panel of Figure 1."
table_PbPb0to30_pT4to10_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_PbPb0to30_pT4to10_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb0to30_pT4to10_deltaPhi.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb0to30_pT4to10_deltaPhi.keywords["cmenergies"] = ["5020"]

#PbPb 30to50

#PbPb 30to50 centrality

reader_PbPb30to50_pT1to2_deltaPhi = RootFileReader("deltaPhiPbPb3050pp.root")
PbPb30to50_pT1to2_deltaPhi = reader_PbPb30to50_pT1to2_deltaPhi.read_hist_1d("H1_clone__5")

x_PbPb30to50_pT1to2_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb30to50_pT1to2_deltaPhi.values = PbPb30to50_pT1to2_deltaPhi["x_edges"]
x_PbPb30to50_pT1to2_deltaPhi.values = [(round(elem,3), round(elem2,3)) for elem, elem2 in PbPb30to50_pT1to2_deltaPhi["x_edges"]]

y_PbPb30to50_pT1to2_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)
#y_PbPb30to50_pT1to2_deltaPhi = Variable("$d<N_{ch}>/d(\\Delta\\phi_{ch,Z})$", is_independent=False, is_binned=False)
arr_PbPb30to50_pT1to2_deltaPhi = PbPb30to50_pT1to2_deltaPhi["y"]
arr_PbPb30to50_pT1to2_deltaPhi[0:5] = arr_PbPb30to50_pT1to2_deltaPhi[5:10][::-1]
arr_PbPb30to50_pT1to2_deltaPhi[15:20] = arr_PbPb30to50_pT1to2_deltaPhi[10:15][::-1]
y_PbPb30to50_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb30to50_pT1to2_deltaPhi]
stats_PbPb30to50_pT1to2_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_PbPb30to50_pT1to2_deltaPhi_dy = PbPb30to50_pT1to2_deltaPhi["dy"]
arr_PbPb30to50_pT1to2_deltaPhi_dy[0:5] = arr_PbPb30to50_pT1to2_deltaPhi_dy[5:10][::-1]
arr_PbPb30to50_pT1to2_deltaPhi_dy[15:20] = arr_PbPb30to50_pT1to2_deltaPhi_dy[10:15][::-1]
stats_PbPb30to50_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb30to50_pT1to2_deltaPhi_dy]
y_PbPb30to50_pT1to2_deltaPhi.add_uncertainty(stats_PbPb30to50_pT1to2_deltaPhi)

systHist_PbPb30to50_pT1to2_deltaPhi = reader_PbPb30to50_pT1to2_deltaPhi.read_hist_1d("HSys1__4")
syst_PbPb30to50_pT1to2_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_PbPb30to50_pT1to2_deltaPhi = systHist_PbPb30to50_pT1to2_deltaPhi["dy"]
arr_systHist_PbPb30to50_pT1to2_deltaPhi[0:5] = arr_systHist_PbPb30to50_pT1to2_deltaPhi[5:10][::-1]
arr_systHist_PbPb30to50_pT1to2_deltaPhi[15:20] = arr_systHist_PbPb30to50_pT1to2_deltaPhi[10:15][::-1]
syst_PbPb30to50_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_PbPb30to50_pT1to2_deltaPhi]
y_PbPb30to50_pT1to2_deltaPhi.add_uncertainty(syst_PbPb30to50_pT1to2_deltaPhi)


y_PbPb30to50_pT1to2_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb30to50_pT1to2_deltaPhi.add_qualifier("PTCH", "1 < $p_{T}^{ch}$ < 2 GeV")
y_PbPb30to50_pT1to2_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb30to50_pT1to2_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb30to50_pT1to2_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb30to50_pT1to2_deltaPhi.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb30to50_pT1to2_deltaPhi.add_qualifier("CENTRALITY", "30--50")

table_PbPb30to50_pT1to2_deltaPhi = Table("$\Delta\phi_{ch,Z}$ in PbPb 30-50% for $1 < p_T < 2$ GeV")
for var in [x_PbPb30to50_pT1to2_deltaPhi, y_PbPb30to50_pT1to2_deltaPhi]:
    table_PbPb30to50_pT1to2_deltaPhi.add_variable(var)

table_PbPb30to50_pT1to2_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $1 <p_T < 2$ GeV in PbPb for centrality interval of 30-50% collisions."
table_PbPb30to50_pT1to2_deltaPhi.location = "Corresponds to middle left panel of Figure 1."
table_PbPb30to50_pT1to2_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_PbPb30to50_pT1to2_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb30to50_pT1to2_deltaPhi.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb30to50_pT1to2_deltaPhi.keywords["cmenergies"] = ["5020"]

reader_PbPb30to50_pT2to4_deltaPhi = RootFileReader("deltaPhiPbPb3050pp.root")
PbPb30to50_pT2to4_deltaPhi = reader_PbPb30to50_pT2to4_deltaPhi.read_hist_1d("H5_clone__11")

x_PbPb30to50_pT2to4_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb30to50_pT2to4_deltaPhi.values = PbPb30to50_pT2to4_deltaPhi["x_edges"]
x_PbPb30to50_pT2to4_deltaPhi.values = [(round(elem,3), round(elem2,3)) for elem, elem2 in PbPb30to50_pT2to4_deltaPhi["x_edges"]]

y_PbPb30to50_pT2to4_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)
arr_PbPb30to50_pT2to4_deltaPhi = PbPb30to50_pT2to4_deltaPhi["y"]
arr_PbPb30to50_pT2to4_deltaPhi[0:5] = arr_PbPb30to50_pT2to4_deltaPhi[5:10][::-1]
arr_PbPb30to50_pT2to4_deltaPhi[15:20] = arr_PbPb30to50_pT2to4_deltaPhi[10:15][::-1]
y_PbPb30to50_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb30to50_pT2to4_deltaPhi]

stats_PbPb30to50_pT2to4_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_PbPb30to50_pT2to4_deltaPhi_dy = PbPb30to50_pT2to4_deltaPhi["dy"]
arr_PbPb30to50_pT2to4_deltaPhi_dy[0:5] = arr_PbPb30to50_pT2to4_deltaPhi_dy[5:10][::-1]
arr_PbPb30to50_pT2to4_deltaPhi_dy[15:20] = arr_PbPb30to50_pT2to4_deltaPhi_dy[10:15][::-1]
stats_PbPb30to50_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb30to50_pT2to4_deltaPhi_dy]
y_PbPb30to50_pT2to4_deltaPhi.add_uncertainty(stats_PbPb30to50_pT2to4_deltaPhi)

systHist_PbPb30to50_pT2to4_deltaPhi = reader_PbPb30to50_pT2to4_deltaPhi.read_hist_1d("HSys1__4")
syst_PbPb30to50_pT2to4_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_PbPb30to50_pT2to4_deltaPhi = systHist_PbPb30to50_pT2to4_deltaPhi["dy"]
arr_systHist_PbPb30to50_pT2to4_deltaPhi[0:5] = arr_systHist_PbPb30to50_pT2to4_deltaPhi[5:10][::-1]
arr_systHist_PbPb30to50_pT2to4_deltaPhi[15:20] = arr_systHist_PbPb30to50_pT2to4_deltaPhi[10:15][::-1]
syst_PbPb30to50_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_PbPb30to50_pT2to4_deltaPhi]
y_PbPb30to50_pT2to4_deltaPhi.add_uncertainty(syst_PbPb30to50_pT2to4_deltaPhi)


y_PbPb30to50_pT2to4_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb30to50_pT2to4_deltaPhi.add_qualifier("PTCH", "2 < $p_{T}^{ch}$ < 4 GeV")
y_PbPb30to50_pT2to4_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb30to50_pT2to4_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb30to50_pT2to4_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb30to50_pT2to4_deltaPhi.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb30to50_pT2to4_deltaPhi.add_qualifier("CENTRALITY", "30--50")


table_PbPb30to50_pT2to4_deltaPhi = Table("$\Delta\phi_{ch,Z}$ in PbPb 30-50% for $2 < p_T < 4$ GeV")
for var in [x_PbPb30to50_pT2to4_deltaPhi, y_PbPb30to50_pT2to4_deltaPhi]:
    table_PbPb30to50_pT2to4_deltaPhi.add_variable(var)

table_PbPb30to50_pT2to4_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $2 <p_T < 4$ GeV in PbPb for centrality interval of 30-50% collisions."
table_PbPb30to50_pT2to4_deltaPhi.location = "Corresponds to middle panel of Figure 1."
table_PbPb30to50_pT2to4_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_PbPb30to50_pT2to4_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb30to50_pT2to4_deltaPhi.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb30to50_pT2to4_deltaPhi.keywords["cmenergies"] = ["5020"]

reader_PbPb30to50_pT4to10_deltaPhi = RootFileReader("deltaPhiPbPb3050pp.root")
PbPb30to50_pT4to10_deltaPhi = reader_PbPb30to50_pT4to10_deltaPhi.read_hist_1d("H9_clone__17")

x_PbPb30to50_pT4to10_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb30to50_pT4to10_deltaPhi.values = PbPb30to50_pT4to10_deltaPhi["x_edges"]
x_PbPb30to50_pT4to10_deltaPhi.values = [(round(elem,2), round(elem2,2)) for elem, elem2 in PbPb30to50_pT4to10_deltaPhi["x_edges"]]

y_PbPb30to50_pT4to10_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)
# ---- PbPb30to50, pT4to10 ----
arr_PbPb30to50_pT4to10_deltaPhi = PbPb30to50_pT4to10_deltaPhi["y"]
arr_PbPb30to50_pT4to10_deltaPhi[0:5] = arr_PbPb30to50_pT4to10_deltaPhi[5:10][::-1]
arr_PbPb30to50_pT4to10_deltaPhi[15:20] = arr_PbPb30to50_pT4to10_deltaPhi[10:15][::-1]
y_PbPb30to50_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb30to50_pT4to10_deltaPhi]

stats_PbPb30to50_pT4to10_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_PbPb30to50_pT4to10_deltaPhi_dy = PbPb30to50_pT4to10_deltaPhi["dy"]
arr_PbPb30to50_pT4to10_deltaPhi_dy[0:5] = arr_PbPb30to50_pT4to10_deltaPhi_dy[5:10][::-1]
arr_PbPb30to50_pT4to10_deltaPhi_dy[15:20] = arr_PbPb30to50_pT4to10_deltaPhi_dy[10:15][::-1]
stats_PbPb30to50_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb30to50_pT4to10_deltaPhi_dy]
y_PbPb30to50_pT4to10_deltaPhi.add_uncertainty(stats_PbPb30to50_pT4to10_deltaPhi)

systHist_PbPb30to50_pT4to10_deltaPhi = reader_PbPb30to50_pT4to10_deltaPhi.read_hist_1d("HSys1__4")
syst_PbPb30to50_pT4to10_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_PbPb30to50_pT4to10_deltaPhi = systHist_PbPb30to50_pT4to10_deltaPhi["dy"]
arr_systHist_PbPb30to50_pT4to10_deltaPhi[0:5] = arr_systHist_PbPb30to50_pT4to10_deltaPhi[5:10][::-1]
arr_systHist_PbPb30to50_pT4to10_deltaPhi[15:20] = arr_systHist_PbPb30to50_pT4to10_deltaPhi[10:15][::-1]
syst_PbPb30to50_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_PbPb30to50_pT4to10_deltaPhi]
y_PbPb30to50_pT4to10_deltaPhi.add_uncertainty(syst_PbPb30to50_pT4to10_deltaPhi)


y_PbPb30to50_pT4to10_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb30to50_pT4to10_deltaPhi.add_qualifier("PTCH", "4 < $p_{T}^{ch}$ < 10 GeV")
y_PbPb30to50_pT4to10_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb30to50_pT4to10_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb30to50_pT4to10_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb30to50_pT4to10_deltaPhi.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb30to50_pT4to10_deltaPhi.add_qualifier("CENTRALITY", "30--50")

table_PbPb30to50_pT4to10_deltaPhi = Table("$\Delta\phi_{ch,Z}$ in PbPb 30-50% for $4 < p_T < 10$ GeV")
for var in [x_PbPb30to50_pT4to10_deltaPhi, y_PbPb30to50_pT4to10_deltaPhi]:
    table_PbPb30to50_pT4to10_deltaPhi.add_variable(var)

table_PbPb30to50_pT4to10_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $4 <p_T < 10$ GeV in PbPb for centrality interval of 30-50% collisions."
table_PbPb30to50_pT4to10_deltaPhi.location = "Corresponds to middle right panel of Figure 1."
table_PbPb30to50_pT4to10_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_PbPb30to50_pT4to10_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb30to50_pT4to10_deltaPhi.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb30to50_pT4to10_deltaPhi.keywords["cmenergies"] = ["5020"]

#PbPb 50to90 centrality
#PbPb 50to90 centrality

reader_PbPb50to90_pT1to2_deltaPhi = RootFileReader("deltaPhiPbPb5090pp.root")
PbPb50to90_pT1to2_deltaPhi = reader_PbPb50to90_pT1to2_deltaPhi.read_hist_1d("H1_clone__5")

x_PbPb50to90_pT1to2_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb50to90_pT1to2_deltaPhi.values = PbPb50to90_pT1to2_deltaPhi["x_edges"]
x_PbPb50to90_pT1to2_deltaPhi.values = [(round(elem,3), round(elem2,3)) for elem, elem2 in PbPb50to90_pT1to2_deltaPhi["x_edges"]]

y_PbPb50to90_pT1to2_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)

arr_PbPb50to90_pT1to2_deltaPhi = PbPb50to90_pT1to2_deltaPhi["y"]
arr_PbPb50to90_pT1to2_deltaPhi[0:5] = arr_PbPb50to90_pT1to2_deltaPhi[5:10][::-1]
arr_PbPb50to90_pT1to2_deltaPhi[15:20] = arr_PbPb50to90_pT1to2_deltaPhi[10:15][::-1]
y_PbPb50to90_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb50to90_pT1to2_deltaPhi]

stats_PbPb50to90_pT1to2_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_PbPb50to90_pT1to2_deltaPhi_dy = PbPb50to90_pT1to2_deltaPhi["dy"]
arr_PbPb50to90_pT1to2_deltaPhi_dy[0:5] = arr_PbPb50to90_pT1to2_deltaPhi_dy[5:10][::-1]
arr_PbPb50to90_pT1to2_deltaPhi_dy[15:20] = arr_PbPb50to90_pT1to2_deltaPhi_dy[10:15][::-1]
stats_PbPb50to90_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb50to90_pT1to2_deltaPhi_dy]
y_PbPb50to90_pT1to2_deltaPhi.add_uncertainty(stats_PbPb50to90_pT1to2_deltaPhi)

systHist_PbPb50to90_pT1to2_deltaPhi = reader_PbPb50to90_pT1to2_deltaPhi.read_hist_1d("HSys1__4")
syst_PbPb50to90_pT1to2_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_PbPb50to90_pT1to2_deltaPhi = systHist_PbPb50to90_pT1to2_deltaPhi["dy"]
arr_systHist_PbPb50to90_pT1to2_deltaPhi[0:5] = arr_systHist_PbPb50to90_pT1to2_deltaPhi[5:10][::-1]
arr_systHist_PbPb50to90_pT1to2_deltaPhi[15:20] = arr_systHist_PbPb50to90_pT1to2_deltaPhi[10:15][::-1]
syst_PbPb50to90_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_PbPb50to90_pT1to2_deltaPhi]
y_PbPb50to90_pT1to2_deltaPhi.add_uncertainty(syst_PbPb50to90_pT1to2_deltaPhi)


y_PbPb50to90_pT1to2_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb50to90_pT1to2_deltaPhi.add_qualifier("PTCH", "1 < $p_{T}^{ch}$ < 2 GeV")
y_PbPb50to90_pT1to2_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb50to90_pT1to2_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb50to90_pT1to2_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb50to90_pT1to2_deltaPhi.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb50to90_pT1to2_deltaPhi.add_qualifier("CENTRALITY", "50--90")

table_PbPb50to90_pT1to2_deltaPhi = Table("$\Delta\phi_{ch,Z}$ in PbPb 50-90% for $1 < p_T < 2$ GeV")
for var in [x_PbPb50to90_pT1to2_deltaPhi, y_PbPb50to90_pT1to2_deltaPhi]:
    table_PbPb50to90_pT1to2_deltaPhi.add_variable(var)

table_PbPb50to90_pT1to2_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $1 <p_T < 2$ GeV in PbPb for centrality interval of 50-90% collisions."
table_PbPb50to90_pT1to2_deltaPhi.location = "Corresponds to lower left panel of Figure 1."
table_PbPb50to90_pT1to2_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_PbPb50to90_pT1to2_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb50to90_pT1to2_deltaPhi.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb50to90_pT1to2_deltaPhi.keywords["cmenergies"] = ["5020"]

reader_PbPb50to90_pT2to4_deltaPhi = RootFileReader("deltaPhiPbPb5090pp.root")
PbPb50to90_pT2to4_deltaPhi = reader_PbPb50to90_pT2to4_deltaPhi.read_hist_1d("H5_clone__11")

x_PbPb50to90_pT2to4_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb50to90_pT2to4_deltaPhi.values = PbPb50to90_pT2to4_deltaPhi["x_edges"]
x_PbPb50to90_pT2to4_deltaPhi.values = [(round(elem,3), round(elem2,3)) for elem, elem2 in PbPb50to90_pT2to4_deltaPhi["x_edges"]]

y_PbPb50to90_pT2to4_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)

arr_PbPb50to90_pT2to4_deltaPhi = PbPb50to90_pT2to4_deltaPhi["y"]
arr_PbPb50to90_pT2to4_deltaPhi[0:5] = arr_PbPb50to90_pT2to4_deltaPhi[5:10][::-1]
arr_PbPb50to90_pT2to4_deltaPhi[15:20] = arr_PbPb50to90_pT2to4_deltaPhi[10:15][::-1]
y_PbPb50to90_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb50to90_pT2to4_deltaPhi]

stats_PbPb50to90_pT2to4_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_PbPb50to90_pT2to4_deltaPhi_dy = PbPb50to90_pT2to4_deltaPhi["dy"]
arr_PbPb50to90_pT2to4_deltaPhi_dy[0:5] = arr_PbPb50to90_pT2to4_deltaPhi_dy[5:10][::-1]
arr_PbPb50to90_pT2to4_deltaPhi_dy[15:20] = arr_PbPb50to90_pT2to4_deltaPhi_dy[10:15][::-1]
stats_PbPb50to90_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb50to90_pT2to4_deltaPhi_dy]
y_PbPb50to90_pT2to4_deltaPhi.add_uncertainty(stats_PbPb50to90_pT2to4_deltaPhi)

systHist_PbPb50to90_pT2to4_deltaPhi = reader_PbPb50to90_pT2to4_deltaPhi.read_hist_1d("HSys1__4")
syst_PbPb50to90_pT2to4_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_PbPb50to90_pT2to4_deltaPhi = systHist_PbPb50to90_pT2to4_deltaPhi["dy"]
arr_systHist_PbPb50to90_pT2to4_deltaPhi[0:5] = arr_systHist_PbPb50to90_pT2to4_deltaPhi[5:10][::-1]
arr_systHist_PbPb50to90_pT2to4_deltaPhi[15:20] = arr_systHist_PbPb50to90_pT2to4_deltaPhi[10:15][::-1]
syst_PbPb50to90_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_PbPb50to90_pT2to4_deltaPhi]
y_PbPb50to90_pT2to4_deltaPhi.add_uncertainty(syst_PbPb50to90_pT2to4_deltaPhi)


y_PbPb50to90_pT2to4_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb50to90_pT2to4_deltaPhi.add_qualifier("PTCH", "2 < $p_{T}^{ch}$ < 4 GeV")
y_PbPb50to90_pT2to4_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb50to90_pT2to4_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb50to90_pT2to4_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb50to90_pT2to4_deltaPhi.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb50to90_pT2to4_deltaPhi.add_qualifier("CENTRALITY", "50--90")



table_PbPb50to90_pT2to4_deltaPhi = Table("$\Delta\phi_{ch,Z}$ in PbPb 50-90% for $2 < p_T < 4$ GeV")
for var in [x_PbPb50to90_pT2to4_deltaPhi, y_PbPb50to90_pT2to4_deltaPhi]:
    table_PbPb50to90_pT2to4_deltaPhi.add_variable(var)

table_PbPb50to90_pT2to4_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $2 <p_T < 4$ GeV in PbPb for centrality interval of 50-90% collisions."
table_PbPb50to90_pT2to4_deltaPhi.location = "Corresponds to lower middle panel of Figure 1."
table_PbPb50to90_pT2to4_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_PbPb50to90_pT2to4_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb50to90_pT2to4_deltaPhi.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb50to90_pT2to4_deltaPhi.keywords["cmenergies"] = ["5020"]

reader_PbPb50to90_pT4to10_deltaPhi = RootFileReader("deltaPhiPbPb5090pp.root")
PbPb50to90_pT4to10_deltaPhi = reader_PbPb50to90_pT4to10_deltaPhi.read_hist_1d("H9_clone__17")

x_PbPb50to90_pT4to10_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb50to90_pT4to10_deltaPhi.values = PbPb50to90_pT4to10_deltaPhi["x_edges"]
x_PbPb50to90_pT4to10_deltaPhi.values = [(round(elem,3), round(elem2,3)) for elem, elem2 in PbPb50to90_pT4to10_deltaPhi["x_edges"]]

y_PbPb50to90_pT4to10_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)

arr_PbPb50to90_pT4to10_deltaPhi = PbPb50to90_pT4to10_deltaPhi["y"]
arr_PbPb50to90_pT4to10_deltaPhi[0:5] = arr_PbPb50to90_pT4to10_deltaPhi[5:10][::-1]
arr_PbPb50to90_pT4to10_deltaPhi[15:20] = arr_PbPb50to90_pT4to10_deltaPhi[10:15][::-1]
y_PbPb50to90_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb50to90_pT4to10_deltaPhi]

stats_PbPb50to90_pT4to10_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_PbPb50to90_pT4to10_deltaPhi_dy = PbPb50to90_pT4to10_deltaPhi["dy"]
arr_PbPb50to90_pT4to10_deltaPhi_dy[0:5] = arr_PbPb50to90_pT4to10_deltaPhi_dy[5:10][::-1]
arr_PbPb50to90_pT4to10_deltaPhi_dy[15:20] = arr_PbPb50to90_pT4to10_deltaPhi_dy[10:15][::-1]
stats_PbPb50to90_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb50to90_pT4to10_deltaPhi_dy]
y_PbPb50to90_pT4to10_deltaPhi.add_uncertainty(stats_PbPb50to90_pT4to10_deltaPhi)

systHist_PbPb50to90_pT4to10_deltaPhi = reader_PbPb50to90_pT4to10_deltaPhi.read_hist_1d("HSys1__4")
syst_PbPb50to90_pT4to10_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_PbPb50to90_pT4to10_deltaPhi = systHist_PbPb50to90_pT4to10_deltaPhi["dy"]
arr_systHist_PbPb50to90_pT4to10_deltaPhi[0:5] = arr_systHist_PbPb50to90_pT4to10_deltaPhi[5:10][::-1]
arr_systHist_PbPb50to90_pT4to10_deltaPhi[15:20] = arr_systHist_PbPb50to90_pT4to10_deltaPhi[10:15][::-1]
syst_PbPb50to90_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_PbPb50to90_pT4to10_deltaPhi]
y_PbPb50to90_pT4to10_deltaPhi.add_uncertainty(syst_PbPb50to90_pT4to10_deltaPhi)

y_PbPb50to90_pT4to10_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb50to90_pT4to10_deltaPhi.add_qualifier("PTCH", "4 < $p_{T}^{ch}$ < 10 GeV")
y_PbPb50to90_pT4to10_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb50to90_pT4to10_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb50to90_pT4to10_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb50to90_pT4to10_deltaPhi.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb50to90_pT4to10_deltaPhi.add_qualifier("CENTRALITY", "50--90")

table_PbPb50to90_pT4to10_deltaPhi = Table("$\Delta\phi_{ch,Z}$ in PbPb 50-90% for $4 < p_T < 10$ GeV")
for var in [x_PbPb50to90_pT4to10_deltaPhi, y_PbPb50to90_pT4to10_deltaPhi]:
    table_PbPb50to90_pT4to10_deltaPhi.add_variable(var)

table_PbPb50to90_pT4to10_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $4 <p_T < 10$ GeV in PbPb for centrality interval of 50-90% collisions."
table_PbPb50to90_pT4to10_deltaPhi.location = "Corresponds to lower right panel of Figure 1."
table_PbPb50to90_pT4to10_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_PbPb50to90_pT1to2_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb50to90_pT4to10_deltaPhi.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb50to90_pT4to10_deltaPhi.keywords["cmenergies"] = ["5020"]

# PbPb 0to90 centrality

reader_PbPb0to90_pT1to2_deltaPhi = RootFileReader("deltaPhiPbPb090pp.root")
PbPb0to90_pT1to2_deltaPhi = reader_PbPb0to90_pT1to2_deltaPhi.read_hist_1d("H1_clone__5")

x_PbPb0to90_pT1to2_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb0to90_pT1to2_deltaPhi.values = PbPb0to90_pT1to2_deltaPhi["x_edges"]
x_PbPb0to90_pT1to2_deltaPhi.values = [(round(elem,3), round(elem2,3)) for elem, elem2 in PbPb0to90_pT1to2_deltaPhi["x_edges"]]

y_PbPb0to90_pT1to2_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)
# ---- PbPb0to90, pT1to2 ----
arr_PbPb0to90_pT1to2_deltaPhi = PbPb0to90_pT1to2_deltaPhi["y"]
arr_PbPb0to90_pT1to2_deltaPhi[0:5] = arr_PbPb0to90_pT1to2_deltaPhi[5:10][::-1]
arr_PbPb0to90_pT1to2_deltaPhi[15:20] = arr_PbPb0to90_pT1to2_deltaPhi[10:15][::-1]
y_PbPb0to90_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb0to90_pT1to2_deltaPhi]

stats_PbPb0to90_pT1to2_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_PbPb0to90_pT1to2_deltaPhi_dy = PbPb0to90_pT1to2_deltaPhi["dy"]
arr_PbPb0to90_pT1to2_deltaPhi_dy[0:5] = arr_PbPb0to90_pT1to2_deltaPhi_dy[5:10][::-1]
arr_PbPb0to90_pT1to2_deltaPhi_dy[15:20] = arr_PbPb0to90_pT1to2_deltaPhi_dy[10:15][::-1]
stats_PbPb0to90_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb0to90_pT1to2_deltaPhi_dy]
y_PbPb0to90_pT1to2_deltaPhi.add_uncertainty(stats_PbPb0to90_pT1to2_deltaPhi)

systHist_PbPb0to90_pT1to2_deltaPhi = reader_PbPb0to90_pT1to2_deltaPhi.read_hist_1d("HSys1__4")
syst_PbPb0to90_pT1to2_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_PbPb0to90_pT1to2_deltaPhi = systHist_PbPb0to90_pT1to2_deltaPhi["dy"]
arr_systHist_PbPb0to90_pT1to2_deltaPhi[0:5] = arr_systHist_PbPb0to90_pT1to2_deltaPhi[5:10][::-1]
arr_systHist_PbPb0to90_pT1to2_deltaPhi[15:20] = arr_systHist_PbPb0to90_pT1to2_deltaPhi[10:15][::-1]
syst_PbPb0to90_pT1to2_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_PbPb0to90_pT1to2_deltaPhi]
y_PbPb0to90_pT1to2_deltaPhi.add_uncertainty(syst_PbPb0to90_pT1to2_deltaPhi)

y_PbPb0to90_pT1to2_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb0to90_pT1to2_deltaPhi.add_qualifier("PTCH", "1 < $p_{T}^{ch}$ < 2 GeV")
y_PbPb0to90_pT1to2_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb0to90_pT1to2_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb0to90_pT1to2_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb0to90_pT1to2_deltaPhi.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb0to90_pT1to2_deltaPhi.add_qualifier("CENTRALITY", "0--90")

table_PbPb0to90_pT1to2_deltaPhi = Table("$\Delta\phi_{ch,Z}$ in PbPb 0-90% for $1 < p_T < 2$ GeV")
for var in [x_PbPb0to90_pT1to2_deltaPhi, y_PbPb0to90_pT1to2_deltaPhi]:
    table_PbPb0to90_pT1to2_deltaPhi.add_variable(var)

table_PbPb0to90_pT1to2_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $1 <p_T < 2$ GeV in PbPb for centrality interval of 0-90% collisions."
table_PbPb0to90_pT1to2_deltaPhi.location = "Supplementary material."
table_PbPb0to90_pT1to2_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_PbPb0to90_pT1to2_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb0to90_pT1to2_deltaPhi.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb0to90_pT1to2_deltaPhi.keywords["cmenergies"] = ["5020"]

reader_PbPb0to90_pT2to4_deltaPhi = RootFileReader("deltaPhiPbPb090pp.root")
PbPb0to90_pT2to4_deltaPhi = reader_PbPb0to90_pT2to4_deltaPhi.read_hist_1d("H5_clone__11")

x_PbPb0to90_pT2to4_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb0to90_pT2to4_deltaPhi.values = PbPb0to90_pT2to4_deltaPhi["x_edges"]
x_PbPb0to90_pT2to4_deltaPhi.values = [(round(elem,3), round(elem2,3)) for elem, elem2 in PbPb0to90_pT2to4_deltaPhi["x_edges"]]

y_PbPb0to90_pT2to4_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)
# ---- PbPb0to90, pT2to4 ----
arr_PbPb0to90_pT2to4_deltaPhi = PbPb0to90_pT2to4_deltaPhi["y"]
arr_PbPb0to90_pT2to4_deltaPhi[0:5] = arr_PbPb0to90_pT2to4_deltaPhi[5:10][::-1]
arr_PbPb0to90_pT2to4_deltaPhi[15:20] = arr_PbPb0to90_pT2to4_deltaPhi[10:15][::-1]
y_PbPb0to90_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb0to90_pT2to4_deltaPhi]

stats_PbPb0to90_pT2to4_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_PbPb0to90_pT2to4_deltaPhi_dy = PbPb0to90_pT2to4_deltaPhi["dy"]
arr_PbPb0to90_pT2to4_deltaPhi_dy[0:5] = arr_PbPb0to90_pT2to4_deltaPhi_dy[5:10][::-1]
arr_PbPb0to90_pT2to4_deltaPhi_dy[15:20] = arr_PbPb0to90_pT2to4_deltaPhi_dy[10:15][::-1]
stats_PbPb0to90_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb0to90_pT2to4_deltaPhi_dy]
y_PbPb0to90_pT2to4_deltaPhi.add_uncertainty(stats_PbPb0to90_pT2to4_deltaPhi)

systHist_PbPb0to90_pT2to4_deltaPhi = reader_PbPb0to90_pT2to4_deltaPhi.read_hist_1d("HSys1__4")
syst_PbPb0to90_pT2to4_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_PbPb0to90_pT2to4_deltaPhi = systHist_PbPb0to90_pT2to4_deltaPhi["dy"]
arr_systHist_PbPb0to90_pT2to4_deltaPhi[0:5] = arr_systHist_PbPb0to90_pT2to4_deltaPhi[5:10][::-1]
arr_systHist_PbPb0to90_pT2to4_deltaPhi[15:20] = arr_systHist_PbPb0to90_pT2to4_deltaPhi[10:15][::-1]
syst_PbPb0to90_pT2to4_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_PbPb0to90_pT2to4_deltaPhi]
y_PbPb0to90_pT2to4_deltaPhi.add_uncertainty(syst_PbPb0to90_pT2to4_deltaPhi)


y_PbPb0to90_pT2to4_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb0to90_pT2to4_deltaPhi.add_qualifier("PTCH", "2 < $p_{T}^{ch}$ < 4 GeV")
y_PbPb0to90_pT2to4_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb0to90_pT2to4_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb0to90_pT2to4_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb0to90_pT2to4_deltaPhi.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb0to90_pT2to4_deltaPhi.add_qualifier("CENTRALITY", "0--90")


table_PbPb0to90_pT2to4_deltaPhi = Table("$\Delta\phi_{ch,Z}$ in PbPb 0-90% for $2 < p_T < 4$ GeV")
for var in [x_PbPb0to90_pT2to4_deltaPhi, y_PbPb0to90_pT2to4_deltaPhi]:
    table_PbPb0to90_pT2to4_deltaPhi.add_variable(var)

table_PbPb0to90_pT2to4_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $2 <p_T < 4$ GeV in PbPb for centrality interval of 0-90% collisions."
table_PbPb0to90_pT2to4_deltaPhi.location = "Supplementary material."
table_PbPb0to90_pT2to4_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_PbPb0to90_pT2to4_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb0to90_pT2to4_deltaPhi.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb0to90_pT2to4_deltaPhi.keywords["cmenergies"] = ["5020"]

reader_PbPb0to90_pT4to10_deltaPhi = RootFileReader("deltaPhiPbPb090pp.root")
PbPb0to90_pT4to10_deltaPhi = reader_PbPb0to90_pT4to10_deltaPhi.read_hist_1d("H9_clone__17")

x_PbPb0to90_pT4to10_deltaPhi = Variable("$\Delta\phi_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb0to90_pT4to10_deltaPhi.values = PbPb0to90_pT4to10_deltaPhi["x_edges"]
x_PbPb0to90_pT4to10_deltaPhi.values = [(round(elem,2), round(elem2,2)) for elem, elem2 in PbPb0to90_pT4to10_deltaPhi["x_edges"]]

y_PbPb0to90_pT4to10_deltaPhi = Variable("$d<N_{ch}>/d(\Delta\phi_{ch,Z})$", is_independent=False, is_binned=False)
arr_PbPb0to90_pT4to10_deltaPhi = PbPb0to90_pT4to10_deltaPhi["y"]
arr_PbPb0to90_pT4to10_deltaPhi[0:5] = arr_PbPb0to90_pT4to10_deltaPhi[5:10][::-1]
arr_PbPb0to90_pT4to10_deltaPhi[15:20] = arr_PbPb0to90_pT4to10_deltaPhi[10:15][::-1]
y_PbPb0to90_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb0to90_pT4to10_deltaPhi]

stats_PbPb0to90_pT4to10_deltaPhi = Uncertainty("Stat.", is_symmetric=True)
arr_PbPb0to90_pT4to10_deltaPhi_dy = PbPb0to90_pT4to10_deltaPhi["dy"]
arr_PbPb0to90_pT4to10_deltaPhi_dy[0:5] = arr_PbPb0to90_pT4to10_deltaPhi_dy[5:10][::-1]
arr_PbPb0to90_pT4to10_deltaPhi_dy[15:20] = arr_PbPb0to90_pT4to10_deltaPhi_dy[10:15][::-1]
stats_PbPb0to90_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_PbPb0to90_pT4to10_deltaPhi_dy]
y_PbPb0to90_pT4to10_deltaPhi.add_uncertainty(stats_PbPb0to90_pT4to10_deltaPhi)

systHist_PbPb0to90_pT4to10_deltaPhi = reader_PbPb0to90_pT4to10_deltaPhi.read_hist_1d("HSys1__4")
syst_PbPb0to90_pT4to10_deltaPhi = Uncertainty("Syst.", is_symmetric=True)
arr_systHist_PbPb0to90_pT4to10_deltaPhi = systHist_PbPb0to90_pT4to10_deltaPhi["dy"]
arr_systHist_PbPb0to90_pT4to10_deltaPhi[0:5] = arr_systHist_PbPb0to90_pT4to10_deltaPhi[5:10][::-1]
arr_systHist_PbPb0to90_pT4to10_deltaPhi[15:20] = arr_systHist_PbPb0to90_pT4to10_deltaPhi[10:15][::-1]
syst_PbPb0to90_pT4to10_deltaPhi.values = [format(round(elem,4), '.4f') for elem in arr_systHist_PbPb0to90_pT4to10_deltaPhi]
y_PbPb0to90_pT4to10_deltaPhi.add_uncertainty(syst_PbPb0to90_pT4to10_deltaPhi)

y_PbPb0to90_pT4to10_deltaPhi.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb0to90_pT4to10_deltaPhi.add_qualifier("PTCH", "4 < $p_{T}^{ch}$ < 10 GeV")
y_PbPb0to90_pT4to10_deltaPhi.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb0to90_pT4to10_deltaPhi.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb0to90_pT4to10_deltaPhi.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb0to90_pT4to10_deltaPhi.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb0to90_pT4to10_deltaPhi.add_qualifier("CENTRALITY", "0--90")

table_PbPb0to90_pT4to10_deltaPhi = Table("$\Delta\phi_{ch,Z}$ in PbPb 0-90% for $4 < p_T < 10$ GeV")
for var in [x_PbPb0to90_pT4to10_deltaPhi, y_PbPb0to90_pT4to10_deltaPhi]:
    table_PbPb0to90_pT4to10_deltaPhi.add_variable(var)

table_PbPb0to90_pT4to10_deltaPhi.description = "The $\Delta\phi_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $4 <p_T < 10$ GeV in PbPb for centrality interval of 0-90% collisions."
table_PbPb0to90_pT4to10_deltaPhi.location = "Supplementary material."
table_PbPb0to90_pT4to10_deltaPhi.keywords["observables"] = ["dNchdPhichZ spectra"]
table_PbPb0to90_pT4to10_deltaPhi.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb0to90_pT4to10_deltaPhi.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb0to90_pT4to10_deltaPhi.keywords["cmenergies"] = ["5020"]



reader_pp_pT1to2_deltaEta = RootFileReader("deltaEtaPP.root")
pp_pT1to2_deltaEta = reader_pp_pT1to2_deltaEta.read_hist_1d("H1_clone__6")

x_pp_pT1to2_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_pp_pT1to2_deltaEta.values = pp_pT1to2_deltaEta["x_edges"]
x_pp_pT1to2_deltaEta.values = [(round(elem,2), round(elem2,2)) for elem, elem2 in pp_pT1to2_deltaEta["x_edges"]]

y_pp_pT1to2_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_pp_pT1to2_deltaEta.values = pp_pT1to2_deltaEta["y"]
y_pp_pT1to2_deltaEta.values = [format(round(elem,4), '.4f') for elem in pp_pT1to2_deltaEta["y"]]

stats_pp_pT1to2_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_pp_pT1to2_deltaEta.values = pp_pT1to2_deltaEta["dy"]
stats_pp_pT1to2_deltaEta.values = [format(round(elem,4), '.4f') for elem in pp_pT1to2_deltaEta["dy"]]
y_pp_pT1to2_deltaEta.add_uncertainty(stats_pp_pT1to2_deltaEta)

systHist_pp_pT1to2_deltaEta = reader_pp_pT1to2_deltaEta.read_hist_1d("hDiffSys_0_0__13")
syst_pp_pT1to2_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_pp_pT1to2_deltaEta.values = systHist_pp_pT1to2_deltaEta["dy"]
syst_pp_pT1to2_deltaEta.values = [format(round(elem,4), '.4f') for elem in systHist_pp_pT1to2_deltaEta["dy"]]

y_pp_pT1to2_deltaEta.add_uncertainty(syst_pp_pT1to2_deltaEta)

y_pp_pT1to2_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_pp_pT1to2_deltaEta.add_qualifier("PTCH", "1 < $p_{T}^{ch}$ < 2 GeV")
y_pp_pT1to2_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_pp_pT1to2_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_pp_pT1to2_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_pp_pT1to2_deltaEta.add_qualifier("RE", "pp --> Z + X")

table_pp_pT1to2_deltaEta = Table("$\Delta y_{ch,Z}$ spectra in pp for $1 < p_T < 2$ GeV")
for var in [x_pp_pT1to2_deltaEta, y_pp_pT1to2_deltaEta]:
    table_pp_pT1to2_deltaEta.add_variable(var)
table_pp_pT1to2_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $1 <p_T < 2$ GeV in pp collisions."
table_pp_pT1to2_deltaEta.location = "Corresponds to upper left panel of Figure 2."
table_pp_pT1to2_deltaEta.keywords["observables"] = ["dNchdEtachZ spectra"]
table_pp_pT1to2_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_pp_pT1to2_deltaEta.keywords["reactions"] = ["pp --> Z+X"]
table_pp_pT1to2_deltaEta.keywords["cmenergies"] = ["5020"]

reader_pp_pT2to4_deltaEta = RootFileReader("deltaEtaPP.root")
pp_pT2to4_deltaEta = reader_pp_pT2to4_deltaEta.read_hist_1d("H11_clone__20")

x_pp_pT2to4_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_pp_pT2to4_deltaEta.values = pp_pT2to4_deltaEta["x_edges"]
x_pp_pT2to4_deltaEta.values = [(round(elem,2), round(elem2,2)) for elem, elem2 in pp_pT2to4_deltaEta["x_edges"]]

y_pp_pT2to4_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_pp_pT2to4_deltaEta.values = pp_pT2to4_deltaEta["y"]
y_pp_pT2to4_deltaEta.values = [format(round(elem,4), '.4f') for elem in pp_pT2to4_deltaEta["y"]]

stats_pp_pT2to4_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_pp_pT2to4_deltaEta.values = pp_pT2to4_deltaEta["dy"]
stats_pp_pT2to4_deltaEta.values = [format(round(elem,4), '.4f') for elem in pp_pT2to4_deltaEta["dy"]]
y_pp_pT2to4_deltaEta.add_uncertainty(stats_pp_pT2to4_deltaEta)

systHist_pp_pT2to4_deltaEta = reader_pp_pT2to4_deltaEta.read_hist_1d("hDiffSys_1_0__27")
syst_pp_pT2to4_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_pp_pT2to4_deltaEta.values = systHist_pp_pT2to4_deltaEta["dy"]
syst_pp_pT2to4_deltaEta.values = [format(round(elem,4), '.4f') for elem in systHist_pp_pT2to4_deltaEta["dy"]]

y_pp_pT2to4_deltaEta.add_uncertainty(syst_pp_pT2to4_deltaEta)

y_pp_pT2to4_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_pp_pT2to4_deltaEta.add_qualifier("PTCH", "2 < $p_{T}^{ch}$ < 4 GeV")
y_pp_pT2to4_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_pp_pT2to4_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_pp_pT2to4_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_pp_pT2to4_deltaEta.add_qualifier("RE", "pp --> Z + X")

table_pp_pT2to4_deltaEta = Table("$\Delta y_{ch,Z}$ spectra in pp for $2 < p_T < 4$ GeV")
for var in [x_pp_pT2to4_deltaEta, y_pp_pT2to4_deltaEta]:
    table_pp_pT2to4_deltaEta.add_variable(var)

table_pp_pT2to4_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $2 <p_T < 4$ GeV in pp collisions."
table_pp_pT2to4_deltaEta.location = "Corresponds to upper middle panel of Figure 2."
table_pp_pT2to4_deltaEta.keywords["observables"] = ["dNchdEtachZ spectra"]
table_pp_pT2to4_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_pp_pT2to4_deltaEta.keywords["reactions"] = ["pp --> Z+X"]
table_pp_pT2to4_deltaEta.keywords["cmenergies"] = ["5020"]

reader_pp_pT4to10_deltaEta = RootFileReader("deltaEtaPP.root")
pp_pT4to10_deltaEta = reader_pp_pT4to10_deltaEta.read_hist_1d("H21_clone__34")

x_pp_pT4to10_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_pp_pT4to10_deltaEta.values = pp_pT4to10_deltaEta["x_edges"]
x_pp_pT4to10_deltaEta.values = [(round(elem,2), round(elem2,2)) for elem, elem2 in pp_pT4to10_deltaEta["x_edges"]]

y_pp_pT4to10_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_pp_pT4to10_deltaEta.values = pp_pT4to10_deltaEta["y"]
y_pp_pT4to10_deltaEta.values = [format(round(elem,4), '.4f') for elem in pp_pT4to10_deltaEta["y"]]

stats_pp_pT4to10_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_pp_pT4to10_deltaEta.values = pp_pT4to10_deltaEta["dy"]
stats_pp_pT4to10_deltaEta.values = [format(round(elem,4), '.4f') for elem in pp_pT4to10_deltaEta["dy"]]
y_pp_pT4to10_deltaEta.add_uncertainty(stats_pp_pT4to10_deltaEta)

systHist_pp_pT4to10_deltaEta = reader_pp_pT4to10_deltaEta.read_hist_1d("hDiffSys_2_0__41")
syst_pp_pT4to10_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_pp_pT4to10_deltaEta.values = systHist_pT4to10_deltaEta["dy"]
syst_pp_pT4to10_deltaEta.values = [format(round(elem,4), '.4f') for elem in systHist_pp_pT4to10_deltaEta["dy"]]
y_pp_pT4to10_deltaEta.add_uncertainty(syst_pp_pT4to10_deltaEta)

y_pp_pT4to10_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_pp_pT4to10_deltaEta.add_qualifier("PTCH", "4 < $p_{T}^{ch}$ < 10 GeV")
y_pp_pT4to10_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_pp_pT4to10_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_pp_pT4to10_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_pp_pT4to10_deltaEta.add_qualifier("RE", "pp --> Z + X")



table_pp_pT4to10_deltaEta = Table("$\Delta y_{ch,Z}$ spectra in pp for $4 < p_T < 10$ GeV")
for var in [x_pp_pT4to10_deltaEta, y_pp_pT4to10_deltaEta]:
    table_pp_pT4to10_deltaEta.add_variable(var)

table_pp_pT4to10_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $4 <p_T < 10$ GeV in pp collisions."
table_pp_pT4to10_deltaEta.location = "Corresponds to upper right panel of Figure 2."
table_pp_pT4to10_deltaEta.keywords["observables"] = ["dNchdEtachZ spectra"]
table_pp_pT4to10_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_pp_pT4to10_deltaEta.keywords["reactions"] = ["pp --> Z+X"]
table_pp_pT4to10_deltaEta.keywords["cmenergies"] = ["5020"]


#PbPb 0-30%

reader_PbPb0to30_pT1to2_deltaEta = RootFileReader("deltaEtaPbPb030pp.root")
PbPb0to30_pT1to2_deltaEta = reader_PbPb0to30_pT1to2_deltaEta.read_hist_1d("H1_clone__5")

x_PbPb0to30_pT1to2_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
x_PbPb0to30_pT1to2_deltaEta.values = [(round(elem,1),round(elem2,1))  for elem, elem2 in PbPb0to30_pT1to2_deltaEta["x_edges"]]

#print (PbPb0to30_pT1to2_deltaEta["x_edges"])

y_PbPb0to30_pT1to2_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
y_PbPb0to30_pT1to2_deltaEta.values = [format(round(elem,4),'.4f')  for elem in PbPb0to30_pT1to2_deltaEta["y"]]


y_PbPb0to30_pT1to2_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb0to30_pT1to2_deltaEta.add_qualifier("PTCH", "1 < $p_{T}^{ch}$ < 2 GeV")
y_PbPb0to30_pT1to2_deltaEta.add_qualifier("ABS(YZ)","$|y_Z|$ < 2.4")
y_PbPb0to30_pT1to2_deltaEta.add_qualifier("ABS(ETACH)","$|\eta^{ch}|$ < 2.4")
y_PbPb0to30_pT1to2_deltaEta.add_qualifier("SQRT(S)/NUCLEON","5020 GeV")
y_PbPb0to30_pT1to2_deltaEta.add_qualifier("RE","Pb Pb --> Z + X")
y_PbPb0to30_pT1to2_deltaEta.add_qualifier("CENTRALITY","0--30")

stats_PbPb0to30_pT1to2_deltaEta = Uncertainty("Stat.", is_symmetric=True)
stats_PbPb0to30_pT1to2_deltaEta.values = [format(round(elem,4),'.4f')  for elem in  PbPb0to30_pT1to2_deltaEta["dy"]]
y_PbPb0to30_pT1to2_deltaEta.add_uncertainty(stats_PbPb0to30_pT1to2_deltaEta)

systHist_PbPb0to30_pT1to2_deltaEta = reader_PbPb0to30_pT1to2_deltaEta.read_hist_1d("HSys1__4")
syst_PbPb0to30_pT1to2_deltaEta = Uncertainty("Syst.", is_symmetric=True)
syst_PbPb0to30_pT1to2_deltaEta.values = [format(round(elem,4),'.4f')  for elem in  systHist_PbPb0to30_pT1to2_deltaEta["dy"]]
y_PbPb0to30_pT1to2_deltaEta.add_uncertainty(syst_PbPb0to30_pT1to2_deltaEta)

table_PbPb0to30_pT1to2_deltaEta = Table("$\Delta y_{ch,Z}$ in PbPb 0-30% for $1 < p_T < 2$ GeV")
for var in [x_PbPb0to30_pT1to2_deltaEta, y_PbPb0to30_pT1to2_deltaEta]:
    table_PbPb0to30_pT1to2_deltaEta.add_variable(var)

table_PbPb0to30_pT1to2_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $1 <p_T < 2$ GeV in PbPb for centrality interval of 0-30% collisions."
table_PbPb0to30_pT1to2_deltaEta.location = "Corresponds to upper left panel of Figure 2."
table_PbPb0to30_pT1to2_deltaEta.keywords["observables"] = ["dNchdYZ spectra"]
table_PbPb0to30_pT1to2_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb0to30_pT1to2_deltaEta.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb0to30_pT1to2_deltaEta.keywords["cmenergies"] = ["5020"]

reader_PbPb0to30_pT2to4_deltaEta = RootFileReader("deltaEtaPbPb030pp.root")
PbPb0to30_pT2to4_deltaEta = reader_PbPb0to30_pT2to4_deltaEta.read_hist_1d("H5_clone__11")

x_PbPb0to30_pT2to4_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb0to30_pT2to4_deltaEta.values = PbPb0to30_pT2to4_deltaEta["x_edges"]
x_PbPb0to30_pT2to4_deltaEta.values = [(round(elem,1),round(elem2,1))  for elem, elem2 in PbPb0to30_pT2to4_deltaEta["x_edges"]]


y_PbPb0to30_pT2to4_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_PbPb0to30_pT2to4_deltaEta.values = PbPb0to30_pT2to4_deltaEta["y"]
y_PbPb0to30_pT2to4_deltaEta.values = [format(round(elem,4),'.4f')  for elem in PbPb0to30_pT2to4_deltaEta["y"]]

y_PbPb0to30_pT2to4_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb0to30_pT2to4_deltaEta.add_qualifier("PTCH", "2 < $p_{T}^{ch}$ < 4 GeV")
y_PbPb0to30_pT2to4_deltaEta.add_qualifier("ABS(YZ)","$|y_Z|$ < 2.4")
y_PbPb0to30_pT2to4_deltaEta.add_qualifier("ABS(ETACH)","$|\eta^{ch}|$ < 2.4")
y_PbPb0to30_pT2to4_deltaEta.add_qualifier("SQRT(S)/NUCLEON","5020 GeV")
y_PbPb0to30_pT2to4_deltaEta.add_qualifier("RE","Pb Pb --> Z + X")
y_PbPb0to30_pT2to4_deltaEta.add_qualifier("CENTRALITY","0--30")



stats_PbPb0to30_pT2to4_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_PbPb0to30_pT2to4_deltaEta.values = PbPb0to30_pT2to4_deltaEta["dy"]
stats_PbPb0to30_pT2to4_deltaEta.values = [format(round(elem,4),'.4f')  for elem in  PbPb0to30_pT2to4_deltaEta["dy"]]
y_PbPb0to30_pT2to4_deltaEta.add_uncertainty(stats_PbPb0to30_pT2to4_deltaEta)

systHist_PbPb0to30_pT2to4_deltaEta = reader_PbPb0to30_pT2to4_deltaEta.read_hist_1d("HSys9__16")
syst_PbPb0to30_pT2to4_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_PbPb0to30_pT2to4_deltaEta.values = systHist_PbPb0to30_pT2to4_deltaEta["dy"]
syst_PbPb0to30_pT2to4_deltaEta.values = [format(round(elem,4),'.4f')  for elem in  systHist_PbPb0to30_pT2to4_deltaEta["dy"]]
y_PbPb0to30_pT2to4_deltaEta.add_uncertainty(syst_PbPb0to30_pT2to4_deltaEta)

table_PbPb0to30_pT2to4_deltaEta = Table("$\Delta y_{ch,Z}$ in PbPb 0-30% for $2 < p_T < 4$ GeV")
for var in [x_PbPb0to30_pT2to4_deltaEta, y_PbPb0to30_pT2to4_deltaEta]:
    table_PbPb0to30_pT2to4_deltaEta.add_variable(var)

table_PbPb0to30_pT2to4_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $2 <p_T < 4$ GeV in PbPb for centrality interval of 0-30% collisions."
table_PbPb0to30_pT2to4_deltaEta.location = "Corresponds to upper middle panel of Figure 2."
table_PbPb0to30_pT2to4_deltaEta.keywords["observables"] = ["dNchdYZ spectra"]
table_PbPb0to30_pT2to4_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb0to30_pT2to4_deltaEta.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb0to30_pT2to4_deltaEta.keywords["cmenergies"] = ["5020"]

reader_PbPb0to30_pT4to10_deltaEta = RootFileReader("deltaEtaPbPb030pp.root")
PbPb0to30_pT4to10_deltaEta = reader_PbPb0to30_pT4to10_deltaEta.read_hist_1d("H9_clone__17")

x_PbPb0to30_pT4to10_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb0to30_pT4to10_deltaEta.values = PbPb0to30_pT4to10_deltaEta["x_edges"]
x_PbPb0to30_pT4to10_deltaEta.values = [(round(elem,1),round(elem2,1))  for elem, elem2 in PbPb0to30_pT4to10_deltaEta["x_edges"]]

y_PbPb0to30_pT4to10_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_PbPb0to30_pT4to10_deltaEta.values = PbPb0to30_pT4to10_deltaEta["y"]

y_PbPb0to30_pT4to10_deltaEta.values = [format(round(elem,4),'.4f')  for elem in PbPb0to30_pT4to10_deltaEta["y"]]
#syst_PbPb0to30_pT4to10_deltaEta.values = [format(round(elem,4),'.4f')  for elem in systHist_PbPb0to30_pT4to10_deltaEta["dy"]]

y_PbPb0to30_pT4to10_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb0to30_pT4to10_deltaEta.add_qualifier("PTCH", "4 < $p_{T}^{ch}$ < 10 GeV")
y_PbPb0to30_pT4to10_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb0to30_pT4to10_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb0to30_pT4to10_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb0to30_pT4to10_deltaEta.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb0to30_pT4to10_deltaEta.add_qualifier("CENTRALITY", "0--30")


stats_PbPb0to30_pT4to10_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_PbPb0to30_pT4to10_deltaEta.values = PbPb0to30_pT4to10_deltaEta["dy"]
stats_PbPb0to30_pT4to10_deltaEta.values = [format(round(elem,4),'.4f')  for elem in PbPb0to30_pT4to10_deltaEta["dy"]]
y_PbPb0to30_pT4to10_deltaEta.add_uncertainty(stats_PbPb0to30_pT4to10_deltaEta)

systHist_PbPb0to30_pT4to10_deltaEta = reader_PbPb0to30_pT4to10_deltaEta.read_hist_1d("HSys5__10")
syst_PbPb0to30_pT4to10_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_PbPb0to30_pT4to10_deltaEta.values = systHist_PbPb0to30_pT4to10_deltaEta["dy"]
syst_PbPb0to30_pT4to10_deltaEta.values = [format(round(elem,4),'.4f')  for elem in systHist_PbPb0to30_pT4to10_deltaEta["dy"]]
y_PbPb0to30_pT4to10_deltaEta.add_uncertainty(syst_PbPb0to30_pT4to10_deltaEta)

table_PbPb0to30_pT4to10_deltaEta = Table("$\Delta y_{ch,Z}$ in PbPb 0-30% for $4 < p_T < 10$ GeV")
for var in [x_PbPb0to30_pT4to10_deltaEta, y_PbPb0to30_pT4to10_deltaEta]:
    table_PbPb0to30_pT4to10_deltaEta.add_variable(var)

table_PbPb0to30_pT4to10_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $4 <p_T < 10$ GeV in PbPb for centrality interval of 0-30% collisions."
table_PbPb0to30_pT4to10_deltaEta.location = "Corresponds to upper right panel of Figure 2."
table_PbPb0to30_pT4to10_deltaEta.keywords["observables"] = ["dNchdYZ spectra"]
table_PbPb0to30_pT4to10_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb0to30_pT4to10_deltaEta.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb0to30_pT4to10_deltaEta.keywords["cmenergies"] = ["5020"]

reader_PbPb30to50_pT1to2_deltaEta = RootFileReader("deltaEtaPbPb3050pp.root")
PbPb30to50_pT1to2_deltaEta = reader_PbPb30to50_pT1to2_deltaEta.read_hist_1d("H1_clone__5")

x_PbPb30to50_pT1to2_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb30to50_pT1to2_deltaEta.values = PbPb30to50_pT1to2_deltaEta["x_edges"]
# For pT1to2
x_PbPb30to50_pT1to2_deltaEta.values = [(round(elem,1),round(elem2,1)) for elem, elem2 in PbPb30to50_pT1to2_deltaEta["x_edges"]]

y_PbPb30to50_pT1to2_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_PbPb30to50_pT1to2_deltaEta.values = PbPb30to50_pT1to2_deltaEta["y"]
y_PbPb30to50_pT1to2_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb30to50_pT1to2_deltaEta["y"]]
y_PbPb30to50_pT1to2_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb30to50_pT1to2_deltaEta.add_qualifier("PTCH", "1 < $p_{T}^{ch}$ < 2 GeV")
y_PbPb30to50_pT1to2_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb30to50_pT1to2_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb30to50_pT1to2_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb30to50_pT1to2_deltaEta.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb30to50_pT1to2_deltaEta.add_qualifier("CENTRALITY", "30--50")


stats_PbPb30to50_pT1to2_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_PbPb30to50_pT1to2_deltaEta.values = PbPb30to50_pT1to2_deltaEta["dy"]
stats_PbPb30to50_pT1to2_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb30to50_pT1to2_deltaEta["dy"]]
y_PbPb30to50_pT1to2_deltaEta.add_uncertainty(stats_PbPb30to50_pT1to2_deltaEta)

systHist_PbPb30to50_pT1to2_deltaEta = reader_PbPb30to50_pT1to2_deltaEta.read_hist_1d("HSys1__4")
syst_PbPb30to50_pT1to2_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_PbPb30to50_pT1to2_deltaEta.values = systHist_PbPb30to50_pT1to2_deltaEta["dy"]
syst_PbPb30to50_pT1to2_deltaEta.values = [format(round(elem,4),'.4f') for elem in systHist_PbPb30to50_pT1to2_deltaEta["dy"]]
y_PbPb30to50_pT1to2_deltaEta.add_uncertainty(syst_PbPb30to50_pT1to2_deltaEta)

table_PbPb30to50_pT1to2_deltaEta = Table("$\Delta y_{ch,Z}$ in PbPb 30-50% for $1 < p_T < 2$ GeV")
for var in [x_PbPb30to50_pT1to2_deltaEta, y_PbPb30to50_pT1to2_deltaEta]:
    table_PbPb30to50_pT1to2_deltaEta.add_variable(var)

table_PbPb30to50_pT1to2_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $1 <p_T < 2$ GeV in PbPb for centrality interval of 30-50% collisions."
table_PbPb30to50_pT1to2_deltaEta.location = "Corresponds to middle left panel of Figure 2."
table_PbPb30to50_pT1to2_deltaEta.keywords["observables"] = ["dNchdYZ spectra"]
table_PbPb30to50_pT1to2_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb30to50_pT1to2_deltaEta.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb30to50_pT1to2_deltaEta.keywords["cmenergies"] = ["5020"]

reader_PbPb30to50_pT2to4_deltaEta = RootFileReader("deltaEtaPbPb3050pp.root")
PbPb30to50_pT2to4_deltaEta = reader_PbPb30to50_pT2to4_deltaEta.read_hist_1d("H5_clone__11")

x_PbPb30to50_pT2to4_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb30to50_pT2to4_deltaEta.values = PbPb30to50_pT2to4_deltaEta["x_edges"]
x_PbPb30to50_pT2to4_deltaEta.values = [(round(elem,1),round(elem2,1)) for elem, elem2 in PbPb30to50_pT2to4_deltaEta["x_edges"]]

y_PbPb30to50_pT2to4_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_PbPb30to50_pT2to4_deltaEta.values = PbPb30to50_pT2to4_deltaEta["y"]
y_PbPb30to50_pT2to4_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb30to50_pT2to4_deltaEta["y"]]

stats_PbPb30to50_pT2to4_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_PbPb30to50_pT2to4_deltaEta.values = PbPb30to50_pT2to4_deltaEta["dy"]
stats_PbPb30to50_pT2to4_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb30to50_pT2to4_deltaEta["dy"]]
y_PbPb30to50_pT2to4_deltaEta.add_uncertainty(stats_PbPb30to50_pT2to4_deltaEta)

systHist_PbPb30to50_pT2to4_deltaEta = reader_PbPb30to50_pT2to4_deltaEta.read_hist_1d("HSys9__16")
syst_PbPb30to50_pT2to4_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_PbPb30to50_pT2to4_deltaEta.values = systHist_PbPb30to50_pT2to4_deltaEta["dy"]
syst_PbPb30to50_pT2to4_deltaEta.values = [format(round(elem,4),'.4f') for elem in systHist_PbPb30to50_pT2to4_deltaEta["dy"]]
y_PbPb30to50_pT2to4_deltaEta.add_uncertainty(syst_PbPb30to50_pT2to4_deltaEta)
y_PbPb30to50_pT2to4_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb30to50_pT2to4_deltaEta.add_qualifier("PTCH", "2 < $p_{T}^{ch}$ < 4 GeV")
y_PbPb30to50_pT2to4_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb30to50_pT2to4_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb30to50_pT2to4_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb30to50_pT2to4_deltaEta.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb30to50_pT2to4_deltaEta.add_qualifier("CENTRALITY", "30--50")

table_PbPb30to50_pT2to4_deltaEta = Table("$\Delta y_{ch,Z}$ in PbPb 30-50% for $2 < p_T < 4$ GeV")
for var in [x_PbPb30to50_pT2to4_deltaEta, y_PbPb30to50_pT2to4_deltaEta]:
    table_PbPb30to50_pT2to4_deltaEta.add_variable(var)

table_PbPb30to50_pT2to4_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $2 <p_T < 4$ GeV in PbPb for centrality interval of 30-50% collisions."
table_PbPb30to50_pT2to4_deltaEta.location = "Corresponds to middle panel of Figure 2."
table_PbPb30to50_pT2to4_deltaEta.keywords["observables"] = ["dNchdYZ spectra"]
table_PbPb30to50_pT2to4_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb30to50_pT2to4_deltaEta.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb30to50_pT2to4_deltaEta.keywords["cmenergies"] = ["5020"]

reader_PbPb30to50_pT4to10_deltaEta = RootFileReader("deltaEtaPbPb3050pp.root")
PbPb30to50_pT4to10_deltaEta = reader_PbPb30to50_pT4to10_deltaEta.read_hist_1d("H9_clone__17")

x_PbPb30to50_pT4to10_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb30to50_pT4to10_deltaEta.values = PbPb30to50_pT4to10_deltaEta["x_edges"]
x_PbPb30to50_pT4to10_deltaEta.values = [(round(elem,1),round(elem2,1)) for elem, elem2 in PbPb30to50_pT4to10_deltaEta["x_edges"]]


y_PbPb30to50_pT4to10_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_PbPb30to50_pT4to10_deltaEta.values = PbPb30to50_pT4to10_deltaEta["y"]
y_PbPb30to50_pT4to10_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb30to50_pT4to10_deltaEta["y"]]

stats_PbPb30to50_pT4to10_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_PbPb30to50_pT4to10_deltaEta.values = PbPb30to50_pT4to10_deltaEta["dy"]
stats_PbPb30to50_pT4to10_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb30to50_pT4to10_deltaEta["dy"]]
y_PbPb30to50_pT4to10_deltaEta.add_uncertainty(stats_PbPb30to50_pT4to10_deltaEta)

systHist_PbPb30to50_pT4to10_deltaEta = reader_PbPb30to50_pT4to10_deltaEta.read_hist_1d("HSys5__10")
syst_PbPb30to50_pT4to10_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_PbPb30to50_pT4to10_deltaEta.values = systHist_PbPb30to50_pT4to10_deltaEta["dy"]
syst_PbPb30to50_pT4to10_deltaEta.values = [format(round(elem,4),'.4f') for elem in systHist_PbPb30to50_pT4to10_deltaEta["dy"]]
y_PbPb30to50_pT4to10_deltaEta.add_uncertainty(syst_PbPb30to50_pT4to10_deltaEta)

y_PbPb30to50_pT4to10_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb30to50_pT4to10_deltaEta.add_qualifier("PTCH", "4 < $p_{T}^{ch}$ < 10 GeV")
y_PbPb30to50_pT4to10_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb30to50_pT4to10_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb30to50_pT4to10_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb30to50_pT4to10_deltaEta.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb30to50_pT4to10_deltaEta.add_qualifier("CENTRALITY", "30--50")

table_PbPb30to50_pT4to10_deltaEta = Table("$\Delta y_{ch,Z}$ in PbPb 30-50% for $4 < p_T < 10$ GeV")
for var in [x_PbPb30to50_pT4to10_deltaEta, y_PbPb30to50_pT4to10_deltaEta]:
    table_PbPb30to50_pT4to10_deltaEta.add_variable(var)

table_PbPb30to50_pT4to10_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $4 <p_T < 10$ GeV in PbPb for centrality interval of 30-50% collisions."
table_PbPb30to50_pT4to10_deltaEta.location = "Corresponds to middle right panel of Figure 2."
table_PbPb30to50_pT4to10_deltaEta.keywords["observables"] = ["dNchdYZ spectra"]
table_PbPb30to50_pT4to10_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb30to50_pT4to10_deltaEta.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb30to50_pT4to10_deltaEta.keywords["cmenergies"] = ["5020"]

#PbPb 50to90 centrality

reader_PbPb50to90_pT1to2_deltaEta = RootFileReader("deltaEtaPbPb5090pp.root")
PbPb50to90_pT1to2_deltaEta = reader_PbPb50to90_pT1to2_deltaEta.read_hist_1d("H1_clone__5")

x_PbPb50to90_pT1to2_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb50to90_pT1to2_deltaEta.values = PbPb50to90_pT1to2_deltaEta["x_edges"]
x_PbPb50to90_pT1to2_deltaEta.values = [(round(elem,1),round(elem2,1)) for elem, elem2 in PbPb50to90_pT1to2_deltaEta["x_edges"]]

y_PbPb50to90_pT1to2_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_PbPb50to90_pT1to2_deltaEta.values = PbPb50to90_pT1to2_deltaEta["y"]
y_PbPb50to90_pT1to2_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb50to90_pT1to2_deltaEta["y"]]

stats_PbPb50to90_pT1to2_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_PbPb50to90_pT1to2_deltaEta.values = PbPb50to90_pT1to2_deltaEta["dy"]
stats_PbPb50to90_pT1to2_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb50to90_pT1to2_deltaEta["dy"]]
y_PbPb50to90_pT1to2_deltaEta.add_uncertainty(stats_PbPb50to90_pT1to2_deltaEta)

systHist_PbPb50to90_pT1to2_deltaEta = reader_PbPb50to90_pT1to2_deltaEta.read_hist_1d("HSys1__4")
syst_PbPb50to90_pT1to2_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_PbPb50to90_pT1to2_deltaEta.values = systHist_PbPb50to90_pT1to2_deltaEta["dy"]
syst_PbPb50to90_pT1to2_deltaEta.values = [format(round(elem,4),'.4f') for elem in systHist_PbPb50to90_pT1to2_deltaEta["dy"]]
y_PbPb50to90_pT1to2_deltaEta.add_uncertainty(syst_PbPb50to90_pT1to2_deltaEta)

y_PbPb50to90_pT1to2_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb50to90_pT1to2_deltaEta.add_qualifier("PTCH", "1 < $p_{T}^{ch}$ < 2 GeV")
y_PbPb50to90_pT1to2_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb50to90_pT1to2_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb50to90_pT1to2_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb50to90_pT1to2_deltaEta.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb50to90_pT1to2_deltaEta.add_qualifier("CENTRALITY", "50--90")


table_PbPb50to90_pT1to2_deltaEta = Table("$\Delta y_{ch,Z}$ in PbPb 50-90% for $1 < p_T < 2$ GeV")
for var in [x_PbPb50to90_pT1to2_deltaEta, y_PbPb50to90_pT1to2_deltaEta]:
    table_PbPb50to90_pT1to2_deltaEta.add_variable(var)

table_PbPb50to90_pT1to2_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $1 <p_T < 2$ GeV in PbPb for centrality interval of 50-90% collisions."
table_PbPb50to90_pT1to2_deltaEta.location = "Corresponds to lower left of Figure 2."
table_PbPb50to90_pT1to2_deltaEta.keywords["observables"] = ["dNchdYZ spectra"]
table_PbPb50to90_pT1to2_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb50to90_pT1to2_deltaEta.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb50to90_pT1to2_deltaEta.keywords["cmenergies"] = ["5020"]

reader_PbPb50to90_pT2to4_deltaEta = RootFileReader("deltaEtaPbPb5090pp.root")
PbPb50to90_pT2to4_deltaEta = reader_PbPb50to90_pT2to4_deltaEta.read_hist_1d("H5_clone__11")

x_PbPb50to90_pT2to4_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb50to90_pT2to4_deltaEta.values = PbPb50to90_pT2to4_deltaEta["x_edges"]
x_PbPb50to90_pT2to4_deltaEta.values = [(round(elem,1),round(elem2,1)) for elem, elem2 in PbPb50to90_pT2to4_deltaEta["x_edges"]]

y_PbPb50to90_pT2to4_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_PbPb50to90_pT2to4_deltaEta.values = PbPb50to90_pT2to4_deltaEta["y"]
y_PbPb50to90_pT2to4_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb50to90_pT2to4_deltaEta["y"]]

stats_PbPb50to90_pT2to4_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_PbPb50to90_pT2to4_deltaEta.values = PbPb50to90_pT2to4_deltaEta["dy"]
stats_PbPb50to90_pT2to4_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb50to90_pT2to4_deltaEta["dy"]]
y_PbPb50to90_pT2to4_deltaEta.add_uncertainty(stats_PbPb50to90_pT2to4_deltaEta)

systHist_PbPb50to90_pT2to4_deltaEta = reader_PbPb50to90_pT2to4_deltaEta.read_hist_1d("HSys9__16")
syst_PbPb50to90_pT2to4_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_PbPb50to90_pT2to4_deltaEta.values = systHist_PbPb50to90_pT2to4_deltaEta["dy"]
syst_PbPb50to90_pT2to4_deltaEta.values = [format(round(elem,4),'.4f') for elem in systHist_PbPb50to90_pT2to4_deltaEta["dy"]]
y_PbPb50to90_pT2to4_deltaEta.add_uncertainty(syst_PbPb50to90_pT2to4_deltaEta)

y_PbPb50to90_pT2to4_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb50to90_pT2to4_deltaEta.add_qualifier("PTCH", "2 < $p_{T}^{ch}$ < 4 GeV")
y_PbPb50to90_pT2to4_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb50to90_pT2to4_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb50to90_pT2to4_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb50to90_pT2to4_deltaEta.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb50to90_pT2to4_deltaEta.add_qualifier("CENTRALITY", "50--90")


table_PbPb50to90_pT2to4_deltaEta = Table("$\Delta y_{ch,Z}$ in PbPb 50-90% for $2 < p_T < 4$ GeV")
for var in [x_PbPb50to90_pT2to4_deltaEta, y_PbPb50to90_pT2to4_deltaEta]:
    table_PbPb50to90_pT2to4_deltaEta.add_variable(var)

table_PbPb50to90_pT2to4_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $2 <p_T < 4$ GeV in PbPb for centrality interval of 50-90% collisions."
table_PbPb50to90_pT2to4_deltaEta.location = "Corresponds to lower middle panel of Figure 2."
table_PbPb50to90_pT2to4_deltaEta.keywords["observables"] = ["dNchdYZ spectra"]
table_PbPb50to90_pT2to4_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb50to90_pT2to4_deltaEta.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb50to90_pT2to4_deltaEta.keywords["cmenergies"] = ["5020"]

reader_PbPb50to90_pT4to10_deltaEta = RootFileReader("deltaEtaPbPb5090pp.root")
PbPb50to90_pT4to10_deltaEta = reader_PbPb50to90_pT4to10_deltaEta.read_hist_1d("H9_clone__17")

x_PbPb50to90_pT4to10_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb50to90_pT4to10_deltaEta.values = PbPb50to90_pT4to10_deltaEta["x_edges"]
x_PbPb50to90_pT4to10_deltaEta.values = [(round(elem,1),round(elem2,1)) for elem, elem2 in PbPb50to90_pT4to10_deltaEta["x_edges"]]

y_PbPb50to90_pT4to10_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_PbPb50to90_pT4to10_deltaEta.values = PbPb50to90_pT4to10_deltaEta["y"]
y_PbPb50to90_pT4to10_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb50to90_pT4to10_deltaEta["y"]]

stats_PbPb50to90_pT4to10_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_PbPb50to90_pT4to10_deltaEta.values = PbPb50to90_pT4to10_deltaEta["dy"]
stats_PbPb50to90_pT4to10_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb50to90_pT4to10_deltaEta["dy"]]
y_PbPb50to90_pT4to10_deltaEta.add_uncertainty(stats_PbPb50to90_pT4to10_deltaEta)

systHist_PbPb50to90_pT4to10_deltaEta = reader_PbPb50to90_pT4to10_deltaEta.read_hist_1d("HSys5__10")
syst_PbPb50to90_pT4to10_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_PbPb50to90_pT4to10_deltaEta.values = systHist_PbPb50to90_pT4to10_deltaEta["dy"]
syst_PbPb50to90_pT4to10_deltaEta.values = [format(round(elem,4),'.4f') for elem in systHist_PbPb50to90_pT4to10_deltaEta["dy"]]
y_PbPb50to90_pT4to10_deltaEta.add_uncertainty(syst_PbPb50to90_pT4to10_deltaEta)

y_PbPb50to90_pT4to10_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb50to90_pT4to10_deltaEta.add_qualifier("PTCH", "4 < $p_{T}^{ch}$ < 10 GeV")
y_PbPb50to90_pT4to10_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb50to90_pT4to10_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb50to90_pT4to10_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb50to90_pT4to10_deltaEta.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb50to90_pT4to10_deltaEta.add_qualifier("CENTRALITY", "50--90")

table_PbPb50to90_pT4to10_deltaEta = Table("$\Delta y_{ch,Z}$ in PbPb 50-90% for $4 < p_T < 10$ GeV")
for var in [x_PbPb50to90_pT4to10_deltaEta, y_PbPb50to90_pT4to10_deltaEta]:
    table_PbPb50to90_pT4to10_deltaEta.add_variable(var)

table_PbPb50to90_pT4to10_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $4 <p_T < 10$ GeV in PbPb for centrality interval of 50-90% collisions."
table_PbPb50to90_pT4to10_deltaEta.location = "Corresponds to lower right panel of Figure 2."
table_PbPb50to90_pT4to10_deltaEta.keywords["observables"] = ["dNchdYZ spectra"]
table_PbPb50to90_pT4to10_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb50to90_pT4to10_deltaEta.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb50to90_pT4to10_deltaEta.keywords["cmenergies"] = ["5020"]

# PbPb 0to90 centrality

reader_PbPb0to90_pT1to2_deltaEta = RootFileReader("deltaEtaPbPb090pp.root")
PbPb0to90_pT1to2_deltaEta = reader_PbPb0to90_pT1to2_deltaEta.read_hist_1d("H1_clone__5")

x_PbPb0to90_pT1to2_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb0to90_pT1to2_deltaEta.values = PbPb0to90_pT1to2_deltaEta["x_edges"]
x_PbPb0to90_pT1to2_deltaEta.values = [(round(elem,1),round(elem2,1)) for elem, elem2 in PbPb0to90_pT1to2_deltaEta["x_edges"]]
y_PbPb0to90_pT1to2_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
y_PbPb0to90_pT1to2_deltaEta.values = PbPb0to90_pT1to2_deltaEta["y"]
y_PbPb0to90_pT1to2_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb0to90_pT1to2_deltaEta["y"]]
stats_PbPb0to90_pT1to2_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_PbPb0to90_pT1to2_deltaEta.values = PbPb0to90_pT1to2_deltaEta["dy"]
stats_PbPb0to90_pT1to2_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb0to90_pT1to2_deltaEta["dy"]]
y_PbPb0to90_pT1to2_deltaEta.add_uncertainty(stats_PbPb0to90_pT1to2_deltaEta)

systHist_PbPb0to90_pT1to2_deltaEta = reader_PbPb0to90_pT1to2_deltaEta.read_hist_1d("HSys1__4")
syst_PbPb0to90_pT1to2_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_PbPb0to90_pT1to2_deltaEta.values = systHist_PbPb0to90_pT1to2_deltaEta["dy"]
syst_PbPb0to90_pT1to2_deltaEta.values = [format(round(elem,4),'.4f') for elem in systHist_PbPb0to90_pT1to2_deltaEta["dy"]]
y_PbPb0to90_pT1to2_deltaEta.add_uncertainty(syst_PbPb0to90_pT1to2_deltaEta)

y_PbPb0to90_pT1to2_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb0to90_pT1to2_deltaEta.add_qualifier("PTCH", "1 < $p_{T}^{ch}$ < 2 GeV")
y_PbPb0to90_pT1to2_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb0to90_pT1to2_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb0to90_pT1to2_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb0to90_pT1to2_deltaEta.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb0to90_pT1to2_deltaEta.add_qualifier("CENTRALITY", "0--90")

table_PbPb0to90_pT1to2_deltaEta = Table("$\Delta y_{ch,Z}$ in PbPb 0-90% for $1 < p_T < 2$ GeV")
for var in [x_PbPb0to90_pT1to2_deltaEta, y_PbPb0to90_pT1to2_deltaEta]:
    table_PbPb0to90_pT1to2_deltaEta.add_variable(var)

table_PbPb0to90_pT1to2_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $1 <p_T < 2$ GeV in PbPb for centrality interval of 0-90% collisions."
table_PbPb0to90_pT1to2_deltaEta.location = "Supplementary material."
table_PbPb0to90_pT1to2_deltaEta.keywords["observables"] = ["dNchdYZ spectra"]
table_PbPb0to90_pT1to2_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb0to90_pT1to2_deltaEta.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb0to90_pT1to2_deltaEta.keywords["cmenergies"] = ["5020"]

reader_PbPb0to90_pT2to4_deltaEta = RootFileReader("deltaEtaPbPb090pp.root")
PbPb0to90_pT2to4_deltaEta = reader_PbPb0to90_pT2to4_deltaEta.read_hist_1d("H5_clone__11")

x_PbPb0to90_pT2to4_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb0to90_pT2to4_deltaEta.values = PbPb0to90_pT2to4_deltaEta["x_edges"]
x_PbPb0to90_pT2to4_deltaEta.values = [(round(elem,1),round(elem2,1)) for elem, elem2 in PbPb0to90_pT2to4_deltaEta["x_edges"]]

y_PbPb0to90_pT2to4_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_PbPb0to90_pT2to4_deltaEta.values = PbPb0to90_pT2to4_deltaEta["y"]
y_PbPb0to90_pT2to4_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb0to90_pT2to4_deltaEta["y"]]

stats_PbPb0to90_pT2to4_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_PbPb0to90_pT2to4_deltaEta.values = PbPb0to90_pT2to4_deltaEta["dy"]
stats_PbPb0to90_pT2to4_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb0to90_pT2to4_deltaEta["dy"]]
y_PbPb0to90_pT2to4_deltaEta.add_uncertainty(stats_PbPb0to90_pT2to4_deltaEta)

systHist_PbPb0to90_pT2to4_deltaEta = reader_PbPb0to90_pT2to4_deltaEta.read_hist_1d("HSys9__16")
syst_PbPb0to90_pT2to4_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_PbPb0to90_pT2to4_deltaEta.values = systHist_PbPb0to90_pT2to4_deltaEta["dy"]
syst_PbPb0to90_pT2to4_deltaEta.values = [format(round(elem,4),'.4f') for elem in systHist_PbPb0to90_pT2to4_deltaEta["dy"]]
y_PbPb0to90_pT2to4_deltaEta.add_uncertainty(syst_PbPb0to90_pT2to4_deltaEta)
y_PbPb0to90_pT2to4_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb0to90_pT2to4_deltaEta.add_qualifier("PTCH", "2 < $p_{T}^{ch}$ < 4 GeV")
y_PbPb0to90_pT2to4_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb0to90_pT2to4_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb0to90_pT2to4_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb0to90_pT2to4_deltaEta.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb0to90_pT2to4_deltaEta.add_qualifier("CENTRALITY", "0--90")

table_PbPb0to90_pT2to4_deltaEta = Table("$\Delta y_{ch,Z}$ in PbPb 0-90% for $2 < p_T < 4$ GeV")
for var in [x_PbPb0to90_pT2to4_deltaEta, y_PbPb0to90_pT2to4_deltaEta]:
    table_PbPb0to90_pT2to4_deltaEta.add_variable(var)

table_PbPb0to90_pT2to4_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $2 <p_T < 4$ GeV in PbPb for centrality interval of 0-90% collisions."
table_PbPb0to90_pT2to4_deltaEta.location = "Supplementary material."
table_PbPb0to90_pT2to4_deltaEta.keywords["observables"] = ["dNchdYZ spectra"]
table_PbPb0to90_pT2to4_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb0to90_pT2to4_deltaEta.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb0to90_pT2to4_deltaEta.keywords["cmenergies"] = ["5020"]

reader_PbPb0to90_pT4to10_deltaEta = RootFileReader("deltaEtaPbPb090pp.root")
PbPb0to90_pT4to10_deltaEta = reader_PbPb0to90_pT4to10_deltaEta.read_hist_1d("H9_clone__17")

x_PbPb0to90_pT4to10_deltaEta = Variable("$\Delta y_{ch,Z}$", is_independent=True, is_binned=True)
#x_PbPb0to90_pT4to10_deltaEta.values = PbPb0to90_pT4to10_deltaEta["x_edges"]
x_PbPb0to90_pT4to10_deltaEta.values = [(round(elem,1),round(elem2,1)) for elem, elem2 in PbPb0to90_pT4to10_deltaEta["x_edges"]]
y_PbPb0to90_pT4to10_deltaEta = Variable("$d<N_{ch}>/d(\Delta y_{ch,Z})$", is_independent=False, is_binned=False)
#y_PbPb0to90_pT4to10_deltaEta.values = PbPb0to90_pT4to10_deltaEta["y"]
y_PbPb0to90_pT4to10_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb0to90_pT4to10_deltaEta["y"]]

stats_PbPb0to90_pT4to10_deltaEta = Uncertainty("Stat.", is_symmetric=True)
#stats_PbPb0to90_pT4to10_deltaEta.values = PbPb0to90_pT4to10_deltaEta["dy"]
stats_PbPb0to90_pT4to10_deltaEta.values = [format(round(elem,4),'.4f') for elem in PbPb0to90_pT4to10_deltaEta["dy"]]
y_PbPb0to90_pT4to10_deltaEta.add_uncertainty(stats_PbPb0to90_pT4to10_deltaEta)

systHist_PbPb0to90_pT4to10_deltaEta = reader_PbPb0to90_pT4to10_deltaEta.read_hist_1d("HSys5__10")
syst_PbPb0to90_pT4to10_deltaEta = Uncertainty("Syst.", is_symmetric=True)
#syst_PbPb0to90_pT4to10_deltaEta.values = systHist_PbPb0to90_pT4to10_deltaEta["dy"]
syst_PbPb0to90_pT4to10_deltaEta.values = [format(round(elem,4),'.4f') for elem in systHist_PbPb0to90_pT4to10_deltaEta["dy"]]
y_PbPb0to90_pT4to10_deltaEta.add_uncertainty(syst_PbPb0to90_pT4to10_deltaEta)

y_PbPb0to90_pT4to10_deltaEta.add_qualifier("PTZ", "40 < $p_{T}^{Z}$ < 350 GeV")
y_PbPb0to90_pT4to10_deltaEta.add_qualifier("PTCH", "4 < $p_{T}^{ch}$ < 10 GeV")
y_PbPb0to90_pT4to10_deltaEta.add_qualifier("ABS(YZ)", "$|y_Z|$ < 2.4")
y_PbPb0to90_pT4to10_deltaEta.add_qualifier("ABS(ETACH)", "$|\eta^{ch}|$ < 2.4")
y_PbPb0to90_pT4to10_deltaEta.add_qualifier("SQRT(S)/NUCLEON", "5020 GeV")
y_PbPb0to90_pT4to10_deltaEta.add_qualifier("RE", "Pb Pb --> Z + X")
y_PbPb0to90_pT4to10_deltaEta.add_qualifier("CENTRALITY", "0--90")

table_PbPb0to90_pT4to10_deltaEta = Table("$\Delta y_{ch,Z}$ in PbPb 0-90% for $4 < p_T < 10$ GeV")
for var in [x_PbPb0to90_pT4to10_deltaEta, y_PbPb0to90_pT4to10_deltaEta]:
    table_PbPb0to90_pT4to10_deltaEta.add_variable(var)

table_PbPb0to90_pT4to10_deltaEta.description = "The $\Delta y_{ch,Z}$ spectra for events with Z boson $p_{T}^Z > 40$ GeV and charged-hadrons with $4 <p_T < 10$ GeV in PbPb for centrality interval of 0-90% collisions."
table_PbPb0to90_pT4to10_deltaEta.location = "Supplementary material."
table_PbPb0to90_pT4to10_deltaEta.keywords["observables"] = ["dNchdYZ spectra"]
table_PbPb0to90_pT4to10_deltaEta.keywords["phrases"] = ["Inclusive Z", "Rapidity", "Azimuthal", "Differential"]
table_PbPb0to90_pT4to10_deltaEta.keywords["reactions"] = ["PbPb --> Z+X"]
table_PbPb0to90_pT4to10_deltaEta.keywords["cmenergies"] = ["5020"]


submission.add_table(table_pp_pT1to2_deltaPhi)
submission.add_table(table_pp_pT2to4_deltaPhi)
submission.add_table(table_pp_pT4to10_deltaPhi)
submission.add_table(table_PbPb0to30_pT1to2_deltaPhi)
submission.add_table(table_PbPb0to30_pT2to4_deltaPhi)
submission.add_table(table_PbPb0to30_pT4to10_deltaPhi)
submission.add_table(table_PbPb30to50_pT1to2_deltaPhi)
submission.add_table(table_PbPb30to50_pT2to4_deltaPhi)
submission.add_table(table_PbPb30to50_pT4to10_deltaPhi)
submission.add_table(table_PbPb50to90_pT1to2_deltaPhi)
submission.add_table(table_PbPb50to90_pT2to4_deltaPhi)
submission.add_table(table_PbPb50to90_pT4to10_deltaPhi)
submission.add_table(table_PbPb0to90_pT1to2_deltaPhi)
submission.add_table(table_PbPb0to90_pT2to4_deltaPhi)
submission.add_table(table_PbPb0to90_pT4to10_deltaPhi)


submission.add_table(table_pp_pT1to2_deltaEta)
submission.add_table(table_pp_pT2to4_deltaEta)
submission.add_table(table_pp_pT4to10_deltaEta)
submission.add_table(table_PbPb0to30_pT1to2_deltaEta)
submission.add_table(table_PbPb0to30_pT2to4_deltaEta)
submission.add_table(table_PbPb0to30_pT4to10_deltaEta)
submission.add_table(table_PbPb30to50_pT1to2_deltaEta)
submission.add_table(table_PbPb30to50_pT2to4_deltaEta)
submission.add_table(table_PbPb30to50_pT4to10_deltaEta)
submission.add_table(table_PbPb50to90_pT1to2_deltaEta)
submission.add_table(table_PbPb50to90_pT2to4_deltaEta)
submission.add_table(table_PbPb50to90_pT4to10_deltaEta)
submission.add_table(table_PbPb0to90_pT1to2_deltaEta)
submission.add_table(table_PbPb0to90_pT2to4_deltaEta)
submission.add_table(table_PbPb0to90_pT4to10_deltaEta)

submission.create_files('./outputHIN23006/')


#pp_pT1to2_HiCent0to30.keys()

#Stats_AK8 = Uncertainty("Stats", is_symmetric=True)

#for key in pp_pT1to2_HiCent0to30.keys():
#    print(key, type(pp_pT1to2_HiCent0to30[key]), type(pp_pT1to2_HiCent0to30[key][0]))
