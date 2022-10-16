import pandas as pd
workbook = pd.read_excel('file.xlsx')
workbook.head()

#creating new file

df = pd.DataFrame({ 'QuantumNumbers': workbook.QuantumNumbers, 'Frequency': workbook.Frequency, 'Eup': workbook.Eup, 'Vo': workbook.Vo, 'deltaVo': workbook.deltaVo,'FWHM_G': workbook.FWHM_G, 'deltaFWHM_G': workbook.deltaFWHM_G, 'Intensity': workbook.Intensity, 'FitFlux': workbook.FitFlux  })
df.set_index('QuantumNumbers', inplace=True)
df.to_excel('extracted_file.xlsx')
