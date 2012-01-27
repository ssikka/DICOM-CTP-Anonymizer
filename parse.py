#!/Library/Frameworks/EPD64.framework/Versions/Current/bin/python
import profileParser
import os
import sys

if __name__ == "__main__":


	profile = os.path.abspath('/Users/sikkas01/sharad_pydicom/project/CTPAnonimizationProfile.xml')

	parse = profileParser.ctpparser(profile)
	print parse._printParameters()
	dicom = os.path.abspath('/Users/sikkas01/sharad_pydicom/ssikka25-pydicom/source/dicom/testfiles/rtplan.dcm')
	
	targetDicom = '/Users/sikkas01/sharad_pydicom/project/anon_rtplan.dcm'
	parse.anonymizeDicom(dicom,targetDicom)
	#parse._printParameters()

	
